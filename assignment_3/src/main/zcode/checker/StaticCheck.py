from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


''' 
    o = [local,Scope(N-1),Scope(0),global]
    Scope(i) = [Symbol1,Symbol2,...,SymbolN]
    Symbol:
        name: str
        typ: Type
        modifier: None
        param: [Symbol]: Name
'''

class Symbol:
    def __init__(self, name, type, modifier = None, param = None, is_body_having = False):
        self.name = name
        self.type = type
        self.modifier = modifier
        self.param = param
        self.is_body_having = is_body_having
        
    def __str__(self):
        return "Symbol" + "(" + str(self.name) + ", " + str(self.type) + (", " + str(self.modifier) if self.modifier != None else "") + (", " + str(self.param) if self.param != None else "") + ")"    
        
class Utils:
    def infer(env, name, type):
        for symbol_list in env:
            for symbol in symbol_list:
                # print("Check in Utils.infer", symbol)
                if symbol.name == name and Utils.isFunc(symbol) is False:
                    symbol.type = type
                    return type
                
    def resolveType(expr, typ, param):
        if type(expr) is Id:
            for symbol_list in param:
                for symbol in symbol_list:
                    # print("Check in Utils.infer", symbol, expr, typ)
                    if Utils.isFunc(symbol) is False and symbol.name == expr.name:
                        symbol.type = typ
                        return typ
        
        if type(expr) is CallExpr:
            for symbol_list in param:
                for symbol in symbol_list:
                    if Utils.isFunc(symbol) and symbol.name == expr.name.name:
                        symbol.type = typ
                        return typ
                    
        if type(expr) is ArrayLiteral:
            if typ is None or type(typ) is not ArrayType:
                return 
            if len(expr.value) != typ.size[0]:
                return False
            for val in expr.value:
                expr_type = Utils.resolveType(val, typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType), param)
                if expr_type is False:
                    return False
            return typ  
    
    def isFunc(symbol):
        return symbol.param != None
class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        self.func_no_body = []
        self.arraylit_ast = []
        self.return_type = None
        self.has_return = False
        self.return_list = []
    
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast, o):
        print("This is from visitId", ast.name)
        for symbol_list in o:
            for symbol in symbol_list:
                # print(symbol)
                if ast.name == symbol.name and not Utils.isFunc(symbol):
                    return symbol.type
        raise Undeclared(Identifier(),ast.name)

    def visitNumberType(self, ast, o):
        return NumberType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitArrayType(self, ast, o): # number a[6]
        return ArrayType(ast.size, ast.eleType)
    
    def visitBinaryOp(self, ast, o):
        op = ast.op
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        # print("Check type from BinaryOp: ", ast.left, ast.right, ast.op)
        
        # Inference: Left or Right is None
        if left is None and right is not None:
            if type(ast.left) in [CallExpr]:
                left = Utils.resolveType(ast.left, right, o)
            elif type(ast.left) in [Id]: 
                left = Utils.resolveType(ast.left, right, o)
            else:
                return None
        if left is not None and right is None:
            if type(ast.right) in [CallExpr]:
                right = Utils.resolveType(ast.right, left, o)
            elif type(ast.right) in [Id]: 
                right = Utils.resolveType(ast.right, left, o)
            else:
                return None
            
        print("Check type from BinaryOp: ", type(left), type(right), ast.op)
        if op in ['+','-','*','/', '%']:
            if left is None and right is None:
                left = Utils.resolveType(ast.left, NumberType(), o)
                right = Utils.resolveType(ast.right, NumberType(), o)
            if type(left) is not NumberType or type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            if type(left) is NumberType and type(right) is NumberType:
                return NumberType()
        
        if op in ['and','or']:
            if left is None and right is None:
                left = Utils.resolveType(ast.left, BoolType(), o)
                right = Utils.resolveType(ast.right, BoolType(), o)
            if not (type(left) is BoolType and type(right) is BoolType):
                raise TypeMismatchInExpression(ast)
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
        
        if op in ['...']:
            if left is None and right is None:
                left = Utils.resolveType(ast.left, StringType(), o)
                right = Utils.resolveType(ast.right, StringType(), o)
            if type(left) is StringType and type(right) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['=', '<', '>', '<=', '>=', '!=']:
            if left is None and right is None:
                left = Utils.resolveType(ast.left, NumberType(), o)
                right = Utils.resolveType(ast.right, NumberType(), o)
            if not (type(left) is NumberType) or not (type(right) is NumberType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ['==']:
            if left is None and right is None:
                left = Utils.resolveType(ast.left, StringType(), o)
                right = Utils.resolveType(ast.right, StringType(), o)
            if not (type(left) is StringType) or not (type(right) is StringType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
    def visitUnaryOp(self, ast, o):  # op: str, operand: Expr
        op = ast.op
        operand = self.visit(ast.operand, o)
        
        if op in ['-']:
            if operand is None:
                operand = Utils.resolveType(ast.operand, NumberType(), o)
            if not (type(operand) is NumberType):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if op in ['not']:
            if operand is None:
                operand = Utils.resolveType(ast.operand, BoolType(), o)
            if type(operand) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
    
    def visitArrayCell(self, ast, o): # arr: Expr, idx: List[Expr] -> a[1, 2, 3]
        name_type = self.visit(ast.arr, o)
        print("Check in array cell", name_type)
        if name_type is None:
            return None
        
        # The name should be in ArrayType
        if type(name_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        # All cell vals must be of NumberType
        for item in ast.idx:
            item_type = self.visit(item, o)
            if item_type is None: 
                # if type(item) is Id:
                #     item_type = Utils.infer(o, item.name, NumberType())
                # elif type(item) is CallExpr:
                #     item_type = Utils.infer(o, item.name.name, NumberType())
                if type(item) in [Id, CallExpr]:
                    item_type = Utils.resolveType(item, NumberType(), o)
                    
            if type(item_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
                
        # Check dimensions and cell in ArrayType and ArrayCell with name_type is ArrayType
        if len(name_type.size) == len(ast.idx):
            return name_type.eleType
        elif len(name_type.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        else:
            return ArrayType(name_type.size[len(ast.idx):], name_type.eleType)
    
    def visitNumberLiteral(self, ast, o):
        return NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return BoolType()
    
    def visitStringLiteral(self, ast, o):
        return StringType()
    
    def visitArrayLiteral(self, ast, o):# value: List[Expr] -> [1,2] -> ArrayLit([1.0, 2.0], NumberType)
        # if ast not in self.arraylit_ast:
        
        self.arraylit_ast += [ast]
        
        print("This is from array literal")
        exprlist = ast.value
        arr_type_check = None
        
        for value in exprlist:
            arr_type_check = self.visit(value, o)
            # print("Check array type", arr_type_check)
            if arr_type_check is not None:
                break

        print('Array literal######', arr_type_check)
        if arr_type_check is not None:
            for expr in exprlist:
                expr_type = self.visit(expr, o) 
                # ArrayType: size: List[float] ; eleType: Type
                # print("Check here in ArrayLiteral",expr_type, arr_type_check) 
                if expr_type is None: 
                    print("check", expr)
                    # if type(expr) is Id:
                    #     expr_type = Utils.infer(o, expr.name, arr_type_check)
                    # elif type(expr) is CallExpr:
                    #     expr_type = Utils.infer(o, expr.name.name, arr_type_check)
                    if type(expr) in [ArrayLiteral, Id, CallExpr]:
                        expr_type = Utils.resolveType(expr, arr_type_check, o)
                    else:
                        return None
                    
                # print("######", arr_type_check, expr_type)
                
                if type(arr_type_check) is not type(expr_type):
                    # print("Come here 3")
                    raise TypeMismatchInExpression(self.arraylit_ast[0])
                    
                if type(expr_type) is ArrayType:  # [[1,3], 3] -> error
                    ## [[a], [b], [c], [1]]
                    if expr_type.size[:len(arr_type_check.size)] != arr_type_check.size:
                        # print("Come here 4")
                        raise TypeMismatchInExpression(self.arraylit_ast[0])
                
                    if len(expr_type.size) > len(arr_type_check.size) and expr_type.size[:len(arr_type_check.size)] == arr_type_check.size:
                        arr_type_check.size = expr_type.size
                        
                    if expr_type.eleType is not None and arr_type_check.eleType is None:
                        arr_type_check.eleType = expr_type.eleType
                        
                        
                    elif expr_type.eleType is None:
                        # print("..............")
                        # print("Changed type", expr, expr_type, arr_type_check)
                        if expr_type.eleType is None and arr_type_check.eleType is None:
                            continue
                        # if type(expr) is Id:
                        #     expr_type.eleType = Utils.infer(o, expr.name, arr_type_check.eleType) 
                        # elif type(expr) is CallExpr:
                        #     expr_type.eleType= Utils.infer(o, expr.name.name, arr_type_check.eleType)
                        if type(expr) in [ArrayLiteral, Id, CallExpr]:
                            expr_type.eleType = Utils.resolveType(expr, arr_type_check.eleType, o)
                        else:
                            return None
                        
                    if expr_type.eleType is not None and arr_type_check.eleType is not None and type(expr_type.eleType) is not type(arr_type_check.eleType):
                        # print("Come here 1")
                        raise TypeMismatchInExpression(self.arraylit_ast[0])
                    
                    elif expr_type.eleType is not None and arr_type_check.eleType is not None and expr_type.size != arr_type_check.size:
                        # print("Come here 2")
                        raise TypeMismatchInExpression(self.arraylit_ast[0])
                # print("::::::::::::::", arr_type_check, expr_type)
                
            self.arraylit_ast = self.arraylit_ast[:-1]
            arr_dim = [len(ast.value)] + arr_type_check.size if type(arr_type_check) is ArrayType else [len(ast.value)]
            arr_type = arr_type_check.eleType if type(arr_type_check) is ArrayType else arr_type_check
            return ArrayType(arr_dim, arr_type)
        
    def visitCallExpr(self, ast, o): # name: Id, args: List[Expr]
        flag = False
        
        # for symbol_list in o:
        #     for symbol in symbol_list:
        #         print("Check here", symbol)
        #     print(".....")
        
        # find built-in function
        for symbol in o[-1]:
            if ast.name.name == symbol.name:
                if type(symbol.type) is VoidType:
                    raise TypeMismatchInExpression(ast)
                else:
                    return symbol.type
        
        # find this function call
        for symbol_list in o[:-1]:
            for symbol in symbol_list:
                # print("Check in call expr", symbol, symbol.is_body_having)
                if ast.name.name == symbol.name and Utils.isFunc(symbol):
                    flag = True
                    # print("Call expression", symbol.is_body_having, type(symbol.type) is VoidType)
                    if type(symbol.type) is VoidType:
                        raise TypeMismatchInExpression(ast)
                    break
        
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
        
        # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)  
            
        # for symbol in o[:-1]: # kiểm tra ở non-local, global
        #     for symbol in symbol_list:
        #         if symbol.name == ast.name.name and Utils.isFunc(symbol):
        #             if symbol.is_body_having == False:
        #                 raise NoDefinition(symbol.name)
        #             break
        
        for symbol_list in o: # kiểm tra ở non-local, global, check recursion with o[2]
            for symbol in symbol_list:
                # print("check here", symbol)
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    list_param = symbol.param
                    args = ast.args
                    # print(len(list_param), len(args))
                    if len(list_param) > len(args):
                        raise TypeMismatchInExpression(ast)
                    elif len(list_param) < len(args):
                        raise TypeMismatchInExpression(ast)
                    else:
                        for i in range(0, len(list_param)):
                            param_type = list_param[i].type # param element here is symbol
                            args_type = self.visit(ast.args[i], o)
                            
                            atomic_types = [NumberType, BoolType, StringType] 
                            # TYPE INFERRED: params -> args: Implicit keyword is not parameters
                            if args_type is None and type(param_type) in atomic_types:
                                args_type = Utils.resolveType(ast.args[i], param_type, o)
                                continue 
                            
                            if type(param_type) is ArrayType:
                                ast.args[i].varType = param_type
                                continue
                            # TYPE MISMATCH
                            if type(args_type) is not type(param_type):
                                # print("Type mismatch", args_type)
                                raise TypeMismatchInExpression(ast) ## for the case: y <- a + foo(x) of TypeCannotBeInferred in spec
                    return symbol.type
            
    def visitAssign(self, ast, o):
        print("This is from visitAssign")
        exp_type = self.visit(ast.rhs, o)
        lhs_type = self.visit(ast.lhs, o)
        print("Check type in assign", lhs_type, exp_type)
        
        if lhs_type is None and exp_type is None:
            raise TypeCannotBeInferred(ast)
        
        if lhs_type is None:
            # if type(ast.lhs) is Id:
            #     lhs_type = Utils.infer(o, ast.lhs.name, exp_type)
            # elif type(ast.lhs) is CallExpr:
            #     lhs_type = Utils.infer(o, ast.lhs.name.name, exp_type)
            
            if type(ast.lhs) in [Id, CallExpr]:
                lhs_type = Utils.resolveType(ast.lhs, exp_type, o)
            else:
                return None
        
        if exp_type is None:
            # if type(ast.rhs) is Id:
            #     exp_type = Utils.infer(o, ast.rhs.name, lhs_type)
            # elif type(ast.rhs) is CallExpr:
            #     exp_type = Utils.infer(o, ast.rhs.name.name, lhs_type)
            
            if type(ast.rhs) in [Id, CallExpr]:
                exp_type = Utils.resolveType(ast.rhs, lhs_type, o)
            else:
                return None
        
        if type(lhs_type) is VoidType:
            raise TypeMismatchInStatement(ast)
        
        if type(lhs_type) is not type(exp_type):
            raise TypeMismatchInStatement(ast)
        
        # If come here, lhs_type = rhs_type != None
        if type(lhs_type) is ArrayType: # it means type(exp_type) is also ArrayType
            if lhs_type.size[:len(exp_type.size)] != exp_type.size:
                raise TypeMismatchInStatement(ast)
            else:
                if exp_type.eleType is None:
                    if type(ast.rhs) in [Id, CallExpr, ArrayLiteral]:
                        exp_ele_type = Utils.resolveType(ast.rhs, lhs_type, o)
                        print(exp_ele_type)
                        exp_type.eleType = lhs_type.eleType
                    else:
                        TypeCannotBeInferred(ast)
                
                if type(lhs_type.eleType) is not type(exp_type.eleType) or lhs_type.size != exp_type.size:
                    raise TypeMismatchInStatement(ast)
              
        if type(lhs_type) is type(exp_type):
            return exp_type
        
        self.arraylit_ast = []
        
    def visitIf(self, ast, o): # expr: Expr, thenStmt: Stmt, elifStmt: List[Tuple[Expr, Stmt]], elseStmt: Stmt = None
        condition_type = self.visit(ast.expr, o)
        print("Check type in visitIf: ", condition_type)
        if condition_type is None:
            # if type(ast.expr) is Id:
            #     condition_type = Utils.infer(o, ast.expr.name, BoolType())
            # elif type(ast.expr) is CallExpr:
            #     condition_type = Utils.infer(o, ast.expr.name.name, BoolType())
                
            if type(ast.expr) in [Id, CallExpr]:
                condition_type = Utils.resolveType(ast.expr, BoolType(), o)
            else:
                raise TypeCannotBeInferred(ast)
        
        if type(condition_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # Go to new scope -> need new o
        o1 = [[]] + o
        if ast.thenStmt:
            self.visit(ast.thenStmt, o1)
            self.has_return = False
            
        o2 = [[]] + o
        if ast.elifStmt:
            for elif_expr, elif_stmt in ast.elifStmt:
                elif_type = self.visit(elif_expr, o2)
                if elif_type is None:
                    if type(elif_expr) in [Id, CallExpr]:
                        elif_type = Utils.resolveType(elif_expr, BoolType(), o2)
                    else:
                        raise TypeCannotBeInferred(ast)
                    
                if type(elif_type) is not BoolType:
                    raise TypeMismatchInStatement(ast)
                
                self.visit(elif_stmt, o2)
                self.has_return = False
                
        o3 = [[]] + o
        if ast.elseStmt:
            self.visit(ast.elseStmt, o3)
            
        self.arraylit_ast = []

    def visitFor(self, ast, o): # name: Id, condExpr: Expr, updExpr: Expr, body: Stmt
        init_type = self.visit(ast.name, o)
        if init_type is None:
            # if type(ast.name) is Id:
            #     init_type = Utils.infer(o, ast.name.name, NumberType())
            # elif type(ast.name) is CallExpr:
            #     init_type = Utils.infer(o, ast.name.name.name, NumberType())
            if type(ast.name) in [Id, CallExpr]:
                init_type = Utils.resolveType(ast.name, NumberType(), o)
            else:
                raise TypeCannotBeInferred(ast)
        if type(init_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
         
        condition_type = self.visit(ast.condExpr, o)
        if condition_type is None:
            # if type(ast.condExpr) is Id:
            #     condition_type = Utils.infer(o, ast.condExpr.name, BoolType())
            # elif type(ast.condExpr) is CallExpr:
            #     condition_type = Utils.infer(o, ast.condExpr.name.name, BoolType())
                
            if type(ast.condExpr) in [Id, CallExpr]:
                condition_type = Utils.resolveType(ast.condExpr, BoolType(), o)
            else:
                raise TypeCannotBeInferred(ast)
        if type(condition_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        update_type = self.visit(ast.updExpr, o)
        if update_type is None:
            # if type(ast.updExpr) is Id:
            #     update_type = Utils.infer(o, ast.updExpr.name, NumberType())
            # elif type(ast.updExpr) is CallExpr:
            #     update_type = Utils.infer(o, ast.updExpr.name.name, NumberType())
                
            if type(ast.updExpr) in [Id, CallExpr]:
                update_type = Utils.resolveType(ast.updExpr, NumberType(), o)
            else:
                raise TypeCannotBeInferred(ast)
        if type(update_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        # new scope
        o1 = [[Symbol("<Loop>", VoidType)]] + o
        self.visit(ast.body, o1)
        
        self.arraylit_ast = []
        
    def visitBreak(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
        self.arraylit_ast = []
        
    def visitContinue(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
        self.arraylit_ast = []
        
    def visitReturn(self, ast, o):
        if self.has_return:
            return
        print("Return")
        self.has_return = True
        right_type = self.visit(ast.expr, o) if ast.expr else VoidType() # RHS
        print("Check return type in visitReturn", right_type)
        
        for i in range(0, len(o)):
            if len(o[i]) > 0 and Utils.isFunc(o[i][0]):
                # print("Check return type in visitReturn", right_type, o[i][0].type, o[i][0].name)
                if o[i][0].type is None:
                    if right_type is None:
                        self.return_list += [ast]
                    else:
                        self.return_type = right_type
                        o[i][0].type = right_type
                        
                        if self.return_list != []:
                            while self.return_list != []:
                                if type(self.return_list[0].expr) in [ArrayLiteral, Id, CallExpr]:
                                    res = Utils.resolveType(self.return_list[0].expr, o[i][0].type, o)
                                    if res is False:
                                        raise TypeMismatchInStatement(self.return_list[0])
                                else:
                                    raise TypeCannotBeInferred(self.return_list[0])
                                
                                self.return_list = self.return_list[1:]
                else:
                    if type(o[i][0].type) is VoidType and type(right_type) is not VoidType:
                        raise TypeMismatchInStatement(ast)
                    
                    ## Infers the type of the return expression
                    if right_type is None: 
                        if type(ast.expr) is ArrayLiteral:
                            right_type = Utils.resolveType(ast.expr, o[i][0].type, o)
                            if right_type is False:
                                raise TypeMismatchInStatement(ast)
                        else:
                            right_type = Utils.resolveType(ast.expr, o[i][0].type, o)
                    
                    else:    
                        if type(o[i][0].type) is not type(right_type):
                            raise TypeMismatchInStatement(ast)
                        
                        else: ## o[i][0].type == right_type
                            if type(o[i][0].type) is ArrayType:
                                if o[i][0].type.size[:len(right_type.size)] != right_type.size:
                                    raise TypeMismatchInStatement(ast)
                                
                                if right_type.eleType is None:
                                    # if type(ast.expr) is Id:
                                    #     right_type.eleType = Utils.infer(o, ast.expr.name, o[i][0].type.eleType)
                                    # elif type(ast.expr) is CallExpr:
                                    #     right_type.eleType = Utils.infer(o, ast.expr.name.name, o[i][0].type.eleType)
                                    if type(ast.expr) in [ArrayLiteral, Id, CallExpr]:
                                        right_type.eleType = Utils.resolveType(ast.expr, o[i][0].type.eleType, o)
                                        if right_type.eleType is False:
                                            raise TypeMismatchInStatement(ast)
                            
                                if type(right_type.eleType) is not type(o[i][0].type.eleType) or o[i][0].type.size != right_type.size:
                                    raise TypeMismatchInStatement(ast)
                                
                            self.return_type = right_type
                break
            
        self.arraylit_ast = []
        
    def visitCallStmt(self, ast, o):
        print("This is from CallStmt")
        flag = False    
        
        # for symbollist in o:
        #     for symbol in symbollist:
        #         print("Check symbol in call stmt", symbol)
        #     print('.............', len(o))    
            
        for symbol in o[-2] + o[-1]:
            # print("Check symbol in call stmt", symbol)
            if ast.name.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                if symbol.type is not None and type(symbol.type) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                break
        
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
        
            # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)        
            # for symbol in o[1]: #TypeCannotBeInfered error for calling again this function itself  
            #     print("Check symbol in Call Stmt", symbol)
            #     if symbol.name == ast.name.name and Utils.isFunc(symbol):
            #         raise TypeCannotBeInferred(ast)
                
        # for symbol_list in o[1:-1]:
        #     for symbol in symbol_list:
        #         if symbol.name == ast.name.name and Utils.isFunc(symbol):
        #             if symbol.is_body_having == False:
        #                 raise NoDefinition(symbol.name)
        #             break

        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    list_param = symbol.param
                    args = ast.args
                    
                    if len(list_param) > len(args):
                        raise TypeMismatchInStatement(ast)
                    elif len(args) > len(list_param):
                        raise TypeMismatchInStatement(ast)
                    else:
                        for i in range(0, len(list_param)):
                            param_type = list_param[i].type # param element here is symbol
                            args_type = self.visit(ast.args[i], o)
                            
                            # print("Check parameter and arguments", param_type, args_type)
                            
                            atomic_types = [NumberType, BoolType, StringType] 
                            
                            # TYPE INFERRED: params -> args: Implicit keyword is not parameters
                            # Passing by value
                            if args_type is None and type(param_type) in atomic_types:
                                continue 
                            # Passing by reference
                            if args_type is None and type(param_type) is ArrayType: # args_type is None because ast.args[i] is declared 'dynamic' -> ast.args[i] is Id
                                ast.args[i].varType = param_type
                                continue
                            # TYPE MISMATCH
                            if type(args_type) is not type(param_type):
                                raise TypeMismatchInStatement(ast)
                            
                    if symbol.type is None:
                        symbol.type = VoidType()
                    return symbol.type
                
        self.arraylit_ast = []
                 
    def visitBlock(self, ast, o):
        print("From block ..............")
        o1 = [[]] + o
        # check if this block belongs to a function or not
        check_func = False
        for symbol in o1[1]:
            # print("Check symbol in block >>>>>>", symbol)
            if Utils.isFunc(symbol):
                check_func = True
                
        if not check_func: # just a block (not a block of function), so visit stmt and decl in this block
            for stmt_decl in ast.stmt:
                self.visit(stmt_decl, o1)
        else:
            # o1: [[block],[func_name,func_param1,...],...]
            function_scope = o1[1]
            check_return_stmt = False
            # first_stmt = True
            
            for stmt_decl in ast.stmt:
                if hasattr(stmt_decl, "name"): # Vardecl
                    for func_component in function_scope[1:]: # Kiểm tra tham số có trùng với khai báo biến trong hàm hay không ??
                        if stmt_decl.name.name == func_component.name: 
                            raise Redeclared(Variable(), stmt_decl.name.name)
                        
                # Check if encountering return statement or not
                if check_return_stmt is True and type(stmt_decl) is Return: continue
                
                self.visit(stmt_decl,o1)
                # for symbol in o1[1]:
                #     print("Check symbol in block >>>>>>", symbol, self.has_return)
                if type(stmt_decl) is Return or self.has_return:
                    check_return_stmt = True
                    
                if type(stmt_decl) is CallStmt:
                    # Write TypeCannotBeInfered error for calling again this function itself 
                    if stmt_decl.name.name == o1[1][0].name:
                        raise TypeCannotBeInferred(stmt_decl)
            
            # if (type(o1[1][0].type) in [NumberType, BoolType, StringType, ArrayType]): -> have return 
            # if (type(o1[1][0].type) is VoidType):
                # have return with no expr
                # no return stmt -> check_return_stmt = False
                
            # if o1[1][0] is None: 
                # 
            
            ## Chưa được suy diễn
            if not check_return_stmt and self.return_type is None: # there are no return statements, func type is VoidType
                self.return_type = VoidType()
            
            ## Đã được suy diễn kiểu, giờ kiểm tra kiểu đó với kiểu thực của hàm với trường hợp không có câu lệnh return trong block
            if not check_return_stmt and self.return_type is not None:
                if o1[1][0].type is None:
                    o1[1][0].type = self.return_type
                # Đã được suy diễn nhưng giờ mới chạy hàm thật sự -> Cần kiểm tra kiểu đã suy diễn với kiểu thật
                if type(self.return_type) is not type(o1[1][0].type):
                    raise TypeMismatchInStatement(ast)
                # Đã chạy hàm thực sự
        
        self.has_return = False   
        self.arraylit_ast = []   
    
                
    def visitVarDecl(self, ast, o): # name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None 
        print("This is from visitVarDecl")
        flag = False
        # Tên biến được trùng với tên hàm
        
        # check redeclare
        for symbol in o[0]: # vì ở dưới hàm visitProgram chúng ta khai báo biến env = [[]] + global_scope nên mỗi biến được tạo ra sẽ được thêm vào env[0] (tức là o[0])
            if symbol.name == ast.name.name and Utils.isFunc(symbol) is False:
                raise Redeclared(Variable(), ast.name.name)
          
        # check duplicate with special function
        for symbol in o[-1][:6]:
            if symbol.name == ast.name.name and Utils.isFunc(symbol):
                raise Redeclared(Variable(), ast.name.name)
        
        if not ast.varInit: 
            # print("Check var without init", ast.name, ast.varType)
            o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, None)]
            
        else:
            o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, None)]
            init = self.visit(ast.varInit, o)
            # for symbol in o[0]:
            #     print("check here :::: ", symbol)
            print("Check init type in Vardecl", init, o[0][-1].type, ast.varType)
            if o[0][-1].type is None and init is not None:
                o[0][-1] = Symbol(ast.name.name, init, ast.modifier, None)
                
            elif o[0][-1].type is None and init is None:
                raise TypeCannotBeInferred(ast)
            
            elif type(ast.varType) is ArrayType and type(init) is ArrayType:
                ast.varType.size = list(map(lambda x: float(x), ast.varType.size))  
                init.size = list(map(lambda x: float(x), init.size))  
                # print("Check here", ast.varType.size, init.size, init.eleType, ast.varInit, ast.varType)
                    
                if init.eleType is None:
                    # number a[2, 3] <- [x, y, z] => init.eleType is None
                    init = Utils.resolveType(ast.varInit, ast.varType, o)
                    
                if ast.varType.size != init.size:
                    # print(1111)
                    raise TypeMismatchInStatement(ast)
                
                elif type(ast.varType.eleType) is not type(init.eleType):
                    # print(3333)
                    raise TypeMismatchInStatement(ast)
                
                elif hasattr(ast.varInit, 'value'): # varInit is ArrayLiteral -> init là: [1,2,3]
                    # print(2222)
                    expr_type = Utils.resolveType(ast.varInit, ast.varType, o)
                    print("Check infer type arraylit in Vardecl", expr_type)
                          
                o[0][-1] = Symbol(ast.name.name, ast.varType, ast.modifier, None)
                
            elif ast.varType is not None and init is None: 
                # if type(ast.varInit) is Id:
                #     Utils.infer(o, ast.varInit.name, ast.varType)
                # elif type(ast.varInit) is CallExpr:
                #     Utils.infer(o, ast.varInit.name.name, ast.varType)
                
                if type(ast.varInit) in [ArrayLiteral, Id, CallExpr]:
                    res = Utils.resolveType(ast.varInit, ast.varType, o)
                    if res is False:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeCannotBeInferred(ast)
                o[0][-1] = Symbol(ast.name.name, ast.varType, ast.modifier, None)
                
            ## Mismatch
            elif (init is not None) and (o[0][-1].type is not None) and type(init) is not type(o[0][-1].type):
                raise TypeMismatchInStatement(ast)
            else:
                o[0][-1] = Symbol(ast.name.name, o[0][-1].type, ast.modifier, None)
                
        self.arraylit_ast = []
            
    def visitFuncDecl(self, ast, o): # name: Id # param: List[VarDecl]  # body: Stmt = None  
        print("This is from visitFuncDecl")
        # Tên biến được trùng với tên hàm
        
        for symbol in o[-1]: # Global
            # print("This is from function", symbol)
            if symbol.name == ast.name.name:
                raise Redeclared(Function(),ast.name.name)
        
        # for symbol in o[-2]: # Variable in Non-local 
        #     # print("This is from function", symbol)
        #     if symbol.name == ast.name.name and Utils.isFunc(symbol):
        #         raise Redeclared(Function(),ast.name.name)
        
        o1 = [[Symbol(ast.name.name, None, None, [])]] + o
        
        # Check if parameters are already defined
        if ast.body:
            for idx in range(len(ast.param)):
                # if ast.param[idx].name.name == ast.name.name: # Kiểm tra tham số có trùng với tên hàm ?
                #     raise Redeclared(Parameter(), ast.param[idx].name.name)
                
                for idx1 in range(idx):
                    if ast.param[idx].name.name == ast.param[idx1].name.name:
                        raise Redeclared(Parameter(), ast.param[idx].name.name)
                
        # Visit params    
        list_params = []
        for param in ast.param:
            sym = Symbol(param.name.name, param.varType, param.modifier, None)
            list_params += [sym]
            o1[0] += [sym] 
            # self.visit(param, o1)
        # for symbol_lst in o:
        #     for symbol in symbol_lst:
        #         print("Check symbol in FuncDecl", symbol)
        
        # for i in range(1, len(ast.param) + 1):
        #     list_params += [Symbol(o1[0][i].name, o1[0][i].type, o1[0][i].modifier, None )]
        
        o1[0][0].param = list_params
        
        check_having_body = False
        if ast.body:
            check_having_body = True
            found_symbol = None 
            found_no_body = False  
            for func in self.func_no_body:
                if func.name.name == ast.name.name:
                    if len(func.param) != len(ast.param):
                        raise Redeclared(Function(), ast.name.name)
                    
                    for idx_param in range(len(ast.param)):
                        if type(func.param[idx_param].varType) is not type(ast.param[idx_param].varType) or (type(func.param[idx_param].varType) is ArrayType and func.param[idx_param].varType.size != ast.param[idx_param].varType.size):
                            raise Redeclared(Function(), ast.name.name)
                    found_no_body = True # in case of having multiple functions with the same name but no body
                    self.func_no_body.remove(func)
                        
            # Tìm hàm mà đã được suy diễn kiểu nhưng chưa có body
            if found_no_body:          
                for symbol in o[0]:
                    if symbol.name == ast.name.name and Utils.isFunc(symbol):
                        if len(symbol.param) != len(ast.param):
                            print("Check here")
                            raise Redeclared(Function(), ast.name.name)
                        
                        for idx_param in range(len(ast.param)):
                            if type(symbol.param[idx_param].type) is not type(ast.param[idx_param].varType) or (type(symbol.param[idx_param].type) is ArrayType and symbol.param[idx_param].type.size != ast.param[idx_param].varType.size):
                                print("Check here 2")
                                raise Redeclared(Function(), ast.name.name) 
                        found_symbol = symbol
                    
            # for symbollist in o1:
            #     for symbol in symbollist:
            #         print("Checking symbol", symbol)
            #     print(".......")
            
            if found_symbol is None:
                for symbol in o[-2]: # Variable in Non-local 
                    print("This is from function", symbol)
                    if symbol.name == ast.name.name and Utils.isFunc(symbol):
                        raise Redeclared(Function(),ast.name.name)
            else:
                o1[0][0].type = found_symbol.type
                o1[0][0].param = found_symbol.param
                o[0].remove(found_symbol)
                
            self.visit(ast.body, o1) # after visiting body, we try to assign type of return stmt to o1[0][0].type (which is type of function)
            if len(self.return_list) != 0:
                raise TypeCannotBeInferred(self.return_list[0])
        else:
            self.func_no_body += [ast]
            for symbol in o[0]:
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    raise Redeclared(Function(), ast.name.name)
                        
            # for decl in self.ast.decl:
            #     if type(decl) is FuncDecl and decl.name.name == ast.name.name:
            #         for idx_param in range(len(decl.param)):
            #             # print('Check param', decl.param[idx_param].varType, ast.param[idx_param].varType)
            #             if type(decl.param[idx_param].varType) is not type(ast.param[idx_param].varType):
            #                 raise Redeclared(Function(), ast.name.name)
                        
            #             if type(decl.param[idx_param].varType) is ArrayType and decl.param[idx_param].varType.size != ast.param[idx_param].varType.size:
            #                 raise Redeclared(Function(), ast.name.name)
                        
            #         # Đến đây thì đã là trùng tên và trùng cả tham số
            #         if decl.body:
            #             check_having_body = True
            #             # self.visit(decl.body, o1)      
            #         else:
            #             if flag is True: # tránh case: func g(), func g(), func g() begin end
            #                 raise Redeclared(Function(), ast.name.name)
            #             flag = True
        o[0] += [Symbol(ast.name.name, o1[0][0].type, None, list_params, check_having_body)]
        self.return_type = None
        self.has_return = False
        self.return_list = []
        
    def visitProgram(self, ast, o):
        global_scope = [[Symbol("readNumber",NumberType(), None, [], True),
                        Symbol("readBool",BoolType(), None, [], True),
                        Symbol("readString",StringType(), None, [], True),
                        Symbol("writeNumber",VoidType(), None,[Symbol("<Param>",NumberType())], True),
                        Symbol("writeString",VoidType(), None,[Symbol("<Param>",StringType())], True),
                        Symbol("writeBool",VoidType(), None,[Symbol("<Param>",BoolType())], True)
                        ]]
        
        # Round 2 - Visit inside body
        env = [[]] + global_scope
        
        for decl in ast.decl:
            self.visit(decl, env)
        
        if self.func_no_body != []:
            raise NoDefinition(self.func_no_body[0].name.name)
        
        # for symbol_list in env:
        #     for symbol in symbol_list:
        #         print("Symbol in program", symbol)
                
        check_main_func = False
        for func in env[0]:
            # print(func.name == "main", type(func.type) is VoidType, func.param)
            if func.name == "main" and type(func.type) is VoidType and len(func.param)==0:
                check_main_func = True
                break
        
        if not check_main_func:
            raise NoEntryPoint()