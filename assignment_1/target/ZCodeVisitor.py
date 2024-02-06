# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl_full.
    def visitVardecl_full(self, ctx:ZCodeParser.Vardecl_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl_not_full.
    def visitVardecl_not_full(self, ctx:ZCodeParser.Vardecl_not_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl_array.
    def visitVardecl_array(self, ctx:ZCodeParser.Vardecl_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramdecl.
    def visitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_prime.
    def visitParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#spec_func.
    def visitSpec_func(self, ctx:ZCodeParser.Spec_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write_string.
    def visitWrite_string(self, ctx:ZCodeParser.Write_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_string.
    def visitRead_string(self, ctx:ZCodeParser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write.
    def visitWrite(self, ctx:ZCodeParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_bool.
    def visitRead_bool(self, ctx:ZCodeParser.Read_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#write_number.
    def visitWrite_number(self, ctx:ZCodeParser.Write_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#read_number.
    def visitRead_number(self, ctx:ZCodeParser.Read_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blocked_list.
    def visitBlocked_list(self, ctx:ZCodeParser.Blocked_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_plus_vardecl.
    def visitStmt_plus_vardecl(self, ctx:ZCodeParser.Stmt_plus_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp.
    def visitExp(self, ctx:ZCodeParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprprime.
    def visitExprprime(self, ctx:ZCodeParser.ExprprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp0.
    def visitExp0(self, ctx:ZCodeParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp1.
    def visitExp1(self, ctx:ZCodeParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp2.
    def visitExp2(self, ctx:ZCodeParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp3.
    def visitExp3(self, ctx:ZCodeParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp4.
    def visitExp4(self, ctx:ZCodeParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp5.
    def visitExp5(self, ctx:ZCodeParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp6.
    def visitExp6(self, ctx:ZCodeParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exp7.
    def visitExp7(self, ctx:ZCodeParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#constant.
    def visitConstant(self, ctx:ZCodeParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sub_exp.
    def visitSub_exp(self, ctx:ZCodeParser.Sub_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#non_empty_expr_list.
    def visitNon_empty_expr_list(self, ctx:ZCodeParser.Non_empty_expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimensions.
    def visitDimensions(self, ctx:ZCodeParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_lits.
    def visitNumber_lits(self, ctx:ZCodeParser.Number_litsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#atomic_types.
    def visitAtomic_types(self, ctx:ZCodeParser.Atomic_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_lit.
    def visitNumber_lit(self, ctx:ZCodeParser.Number_litContext):
        return self.visitChildren(ctx)



del ZCodeParser