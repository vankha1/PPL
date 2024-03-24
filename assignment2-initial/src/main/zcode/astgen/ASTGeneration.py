from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decllist())        

    # decl: vardecl | funcdecl;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        return self.visit(ctx.getChild(0))

    # vardecl: (vardecl_not_full | vardecl_full | vardecl_array) NEW_LINE+;
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        return self.visit(ctx.getChild(0))

    # vardecl_full: VAR ID ASSIGN exp;
    def visitVardecl_full(self, ctx: ZCodeParser.Vardecl_fullContext):
        return VarDecl(Id(ctx.ID().getText()), None, ctx.VAR().getText() ,self.visit(ctx.exp()))

    # vardecl_not_full: (atomic_types | DYNAMIC) ID (ASSIGN exp)?;
    def visitVardecl_not_full(self, ctx: ZCodeParser.Vardecl_not_fullContext):
        var_type = None
        id = Id(ctx.ID().getText())
        modifier = None
        expr = None
        if ctx.atomic_types():
            var_type = self.visit(ctx.atomic_types())
        if ctx.DYNAMIC():
            modifier = ctx.DYNAMIC().getText()
        if ctx.ASSIGN():
            expr = self.visit(ctx.exp())
        return VarDecl(id, var_type, modifier, expr)
    
    # vardecl_array: array_type (ASSIGN array_lit)?;
    def visitVardecl_array(self, ctx:ZCodeParser.Vardecl_arrayContext):
        name = Id(ctx.ID().getText())
        typ = ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomic_types()))
        array_lit = None
        if ctx.ASSIGN():
            array_lit = self.visit(ctx.array_lit())
        return VarDecl(name, typ , None, array_lit)

    # funcdecl: FUNC ID LP param_list RP NEW_LINE* (NEW_LINE | block_stmt | return_stmt);
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        id = Id(ctx.ID().getText())
        param_list = self.visit(ctx.param_list())
        func_body = None
        if ctx.block_stmt():
            func_body = self.visit(ctx.block_stmt())
        if ctx.return_stmt():
            func_body = self.visit(ctx.return_stmt())
        return FuncDecl(id, param_list, func_body)
    
    # func_prototype: FUNC ID LP param_list RP NEW_LINE*;
    # def visitFunc_prototype(self, ctx: ZCodeParser.Func_prototypeContext):
    #     return

    # # func_body: block_stmt | return_stmt;
    # def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
    #     return self.visit(ctx.getChild(0))
    
    # param_list: param_prime |;
    def visitParam_list(self, ctx: ZCodeParser.Param_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param_prime())
        return []

    # param_prime: paramdecl COMMA param_prime | paramdecl;
    def visitParam_prime(self, ctx: ZCodeParser.Param_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        return [self.visit(ctx.paramdecl())] + self.visit(ctx.param_prime())

    # paramdecl: atomic_types ID dimensions?;
    def visitParamdecl(self, ctx: ZCodeParser.ParamdeclContext):
        if ctx.dimensions():
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomic_types())), None, None)
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.atomic_types()), None, None)

    # stmt
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # assign_stmt: scalar_var EQUAL exp SEMI;
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.exp()))
   
    # if_stmt: IF sub_exp newline_list stmt (elif_stmt)* ( ELSE stmt)?;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        if_part = self.visit(ctx.sub_exp())
        then_part = self.visit(ctx.stmt())
        elif_part = []
        else_part = None
        if ctx.elif_stmt():
            elif_part = list(map(lambda x: self.visit(x), ctx.elif_stmt()))
        if ctx.else_stmt():
            else_part = self.visit(ctx.else_stmt())
        return If(if_part, then_part, elif_part, else_part)
    
    # elif_stmt: ELIF sub_exp newline_list stmt;
    def visitElif_stmt(self, ctx: ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.sub_exp()), self.visit(ctx.stmt()))
    
    def visitElse_stmt(self, ctx: ZCodeParser.Else_stmtContext):
        return self.visit(ctx.stmt())

    # for_stmt: FOR ID UNTIL exp BY exp newline_list stmt;
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        init = Id(ctx.ID().getText())
        condition = self.visit(ctx.exp(0))
        update = self.visit(ctx.exp(1))
        stmt = self.visit(ctx.stmt())
        
        return For(init, condition, update, stmt)

    # break_stmt: BREAK NEW_LINE+;
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE NEW_LINE+;
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()

    # return_stmt: RETURN (exp)? NEW_LINE+;
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        exp = None
        if ctx.exp():
            exp = self.visit(ctx.exp())
        return Return(exp)
    
    # call_stmt: ID LP expr_list RP NEW_LINE+ | spec_func NEW_LINE+;
    def visitCall_stmt(self, ctx: ZCodeParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))

    # block_stmt: BEGIN NEW_LINE+ blocked_list END NEW_LINE+;
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.blocked_list()))

    # blocked_list: stmt_plus_vardecl blocked_list |;
    def visitBlocked_list(self, ctx: ZCodeParser.Blocked_listContext): 
        if ctx.stmt_plus_vardecl():
            if isinstance(self.visit(ctx.stmt_plus_vardecl()), list):
                return self.visit(ctx.stmt_plus_vardecl()) + self.visit(ctx.blocked_list())
            else:
                return [self.visit(ctx.stmt_plus_vardecl())] + self.visit(ctx.blocked_list())
        else:
            return []
                

    # stmt_plus_vardecl: (stmt | vardecl);
    def visitStmt_plus_vardecl(self, ctx: ZCodeParser.Stmt_plus_vardeclContext):
        return self.visit(ctx.getChild(0))

    # lhs: ID index_operator?;
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.index_operator():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operator()))
        return Id(ctx.ID().getText())

    # expr_list: exprprime |;
    def visitExpr_list(self, ctx: ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exprprime())
        return []
    
    # exp_prime: exp COMMA exp_prime | exp;
    def visitExprprime(self, ctx: ZCodeParser.ExprprimeContext):
        if ctx.COMMA():
            exp = [self.visit(ctx.exp())]
            return exp + self.visit(ctx.exprprime())
        return [self.visit(ctx.exp())]
    
    # exp0: exp1 CONCAT exp1 | exp1;
    def visitExp0(self, ctx: ZCodeParser.Exp0Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.getChild(0))
    
    # exp1:
    #   exp2 (
    #   	EQUAL
    #   	| NOT_SAME
    #   	| SAME
    #   	| LESS_THAN
    #   	| LESS_THAN_EQUAL
    #   	| GREATER_THAN
    #   	| GREATER_THAN_EQUAL
    #   ) exp2
    #   | exp2;
    def visitExp1(self, ctx:  ZCodeParser.Exp1Context):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.getChild(0))
    
    # exp2: exp2 (AND | OR) exp3 | exp3;
    def visitExp2(self, ctx:  ZCodeParser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        return self.visit(ctx.exp3())
    
    # exp3: exp3 (ADD | SUB) exp4 | exp4;
    def visitExp3(self, ctx:  ZCodeParser.Exp3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        if ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        return self.visit(ctx.exp4())
    
    # exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
    def visitExp4(self, ctx:  ZCodeParser.Exp4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        if ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        return self.visit(ctx.exp5())
    
    # exp5: NOT exp5 | exp6;
    def visitExp5(self, ctx:  ZCodeParser.Exp5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())
    
    # exp6: SUB exp6 | exp7;
    def visitExp6(self, ctx:  ZCodeParser.Exp6Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())

    # exp7: ID | constant | func_call | sub_exp | index_expr ;
    def visitExp7(self, ctx:  ZCodeParser.Exp7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.constant():
            return self.visit(ctx.constant())
        elif ctx.func_call():
            if ctx.index_operator():
                return ArrayCell(self.visit(ctx.func_call()), self.visit(ctx.index_operator()))
            return self.visit(ctx.func_call())
        elif ctx.index_expr():
            return self.visit(ctx.index_expr())
        return self.visit(ctx.sub_exp())

    # func_call: ID LP expr_list RP;
    def visitFunc_call(self, ctx:  ZCodeParser.Func_callContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))

    # constant: NUMBER_LIT | BOOL_LIT | STRING_LIT | array_lit;
    def visitConstant(self, ctx:  ZCodeParser.ConstantContext):
        if (ctx.NUMBER_LIT()):
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif (ctx.BOOL_LIT()):
            return BooleanLiteral(ctx.BOOL_LIT().getText() == 'true')
        elif (ctx.STRING_LIT()):
            return StringLiteral(ctx.STRING_LIT().getText())
        return self.visit(ctx.array_lit())
    
    # sub_exp: LP exp RP;
    def visitSub_exp(self, ctx: ZCodeParser.Sub_expContext):
        return self.visit(ctx.exp())
    
    def visitIndex_expr(self, ctx: ZCodeParser.Index_exprContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operator()))
    
    # index_operator: LS exprprime RS;
    def visitIndex_operator(self, ctx:  ZCodeParser.Index_operatorContext):
        return self.visit(ctx.getChild(1))

    # array_lit: LS non_empty_expr_list RS;
    def visitArray_lit(self, ctx: ZCodeParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.non_empty_expr_list()))
    
    # non_empty_expr_list: exp COMMA non_empty_expr_list | exp;
    def visitNon_empty_expr_list(self, ctx: ZCodeParser.Non_empty_expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.non_empty_expr_list())

    # array_type: atomic_types ID dimensions;
    def visitArray_type(self, ctx: ZCodeParser.Array_typeContext):
        dimensions = self.visit(ctx.dimensions())
        atomic_types = self.visit(ctx.atomic_types())
        return ArrayType(dimensions, atomic_types)

    # dimensions: LS number_lits RS;
    def visitDimensions(self, ctx: ZCodeParser.DimensionsContext):
        return self.visit(ctx.number_lits())

   
    # number_lits: NUMBER_LIT COMMA number_lits | NUMBER_LIT;
    def visitNumber_lits(self, ctx: ZCodeParser.Number_litsContext):
        if (ctx.getChildCount() == 1):
            return [float(ctx.NUMBER_LIT().getText())]
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.number_lits())
    
    # number_lit: FLOAT_LIT | INT_LIT;
    # def visitNumber_lit(self, ctx: ZCodeParser.Number_litContext):
    #     return NumberLiteral(float(ctx.FLOAT_LIT().getText()))

    # atomic_types: BOOL | NUMBER | STRING;
    def visitAtomic_types(self, ctx: ZCodeParser.Atomic_typesContext):
        if (ctx.NUMBER()):
            return NumberType()
        elif (ctx.BOOL()):
            return BoolType()
        elif (ctx.STRING()):
            return StringType()