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
                # print("Check here....", type)
                if symbol.name == name:
                    symbol.type = type
                    return type
                
    def isFunc(symbol):
        return symbol.param != None

class GetEnv(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        
    def visitProgram(self, ast, o):
        print("Round 1: program")
        global_scope = [[Symbol("readNumber",NumberType(), None, [], True),
                        Symbol("readBool",BoolType(), None, [], True),
                        Symbol("readString",StringType(), None, [], True),
                        Symbol("writeNumber",VoidType(), None,[Symbol("<Param>",NumberType())], True),
                        Symbol("writeString",VoidType(), None,[Symbol("<Param>",StringType())], True),
                        Symbol("writeBool",VoidType(), None,[Symbol("<Param>",BoolType())], True)
                        ]]
        for decl in ast.decl:
            self.visit(decl, global_scope)
        return global_scope     
    
    def visitVarDecl(self, ast, o):
        print("Round 1: vardecl")
        # o here is o1 of visitFuncDecl in GetEnv
        # just only for case of parameters:
        print(ast.name, ast.varType)
        if Utils.isFunc(o[0][0]) and o[0][0].type is None:
            # Check redeclared parameters
            for i in range(0, len(o[0])):
                if ast.name == o[0][i].name:
                    raise Redeclared(Parameter(), ast.name)
            o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, ast.varInit)]
            
    
    def visitFuncDecl(self, ast, o):
        print("Round 1: funcdecl")
        # Goal: o1 = [[Symbol(ast.name, None, None, []), param_symbol, param_symbol,...]] + o
        o1 = [[Symbol(ast.name.name, None, None, [])]] + o # o1 = [[local]] + [[scope], [scope]] = [[local], [scope], [scope]]
        for param in ast.param:
            self.visit(param, o1) # go to visitVarDecl in GetEnv
            
        list_params = []
        for i in range(1, len(ast.param) + 1):
            # o1[0][i] is the symbol which is added to the list (line 62)
            list_params += [Symbol(o1[0][i].name, o1[0][i].type, None, None)]

        o[0] += [Symbol(ast.name.name, None, None, list_params)]

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        
        self.no_body = []
    
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast, o):
        print("This is from visitId")
        for symbol_list in o:
            for symbol in symbol_list:
                # symbol.name here is Id() or str -> want to get name of Id() -> symbol.name.name
                # print(type(symbol.name))
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
        
        # Inference: Left or Right is None
        if left is None and right is not None:
            left = Utils.infer(o, ast.left.name, right)
        if left is not None and right is None:
            right = Utils.infer(o, ast.right.name, left)
            
        if (op in ['+','-','*','/', '%']):
            print("Check type from BinaryOp: ", type(left), type(right), ast.op)
            if type(left) is not NumberType or type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            if type(left) is NumberType and type(right) is NumberType:
                return NumberType()
        
        if op in ['and','or']:
            if not (type(left) is BoolType and type(right) is BoolType):
                raise TypeMismatchInExpression(ast)
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
        
        if op in ['...']:
            if type(left) is StringType and type(right) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['<', '>', '<=', '>=', '!=']:
            if not (type(left) is NumberType) and not (type(right) is NumberType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ['==']:
            if not (type(left) is StringType) and not (type(right) is StringType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
    def visitUnaryOp(self, ast, o):  # op: str, operand: Expr
        op = ast.op
        operand = self.visit(ast.operand, o)
        operandtype = type(operand)
        
        if op in ['-']:
            if not (operandtype is NumberType):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if op in ['not']:
            if operandtype is BoolType:
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
            if type(item_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
            elif type(item_type) is None: 
                Utils.infer(o, item.name, NumberType())
                
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
        print("This is from array literal")
        exprlist = ast.value
        arr_type_check = None
        
        for expr in exprlist:
            expr_type = self.visit(expr, o)
            # first time
            if arr_type_check is None:
                arr_type_check = expr_type
            else:
                #ArrayType: size: List[float] ; eleType: Type
                print("Check here in ArrayLiteral", type(expr_type), type(arr_type_check)) 
                if expr_type is None: # nếu phần tử được khai báo trước đó mà chưa có kiểu
                    Utils.infer(o, expr.name, arr_type_check)
                elif type(expr_type) is ArrayType or type(arr_type_check) is ArrayType:  # [[1,3], 3] -> error
                    if not hasattr(expr_type, "size") or not hasattr(arr_type_check, "size") or expr_type.size != arr_type_check.size:
                        raise TypeMismatchInExpression(ast)
                elif type(arr_type_check) != type(expr_type):
                    raise TypeMismatchInExpression(ast) ## need to fix because it must return at Vardecl.
                
        arr_dim = [len(ast.value)] + arr_type_check.size if type(arr_type_check) is ArrayType else [len(ast.value)]
        arr_type = arr_type_check.eleType if type(arr_type_check) is ArrayType else arr_type_check
        return ArrayType(arr_dim, arr_type)
    
    def visitCallExpr(self, ast, o): # name: Id, args: List[Expr]

        flag = False
        
        # for symbol_list in o:
        #     for symbol in symbol_list:
        #         print("Check here", symbol)
        #     print(".....")
        
        # find the body of this function being called
        
        for symbol_list in o[:-1]:
            for symbol in symbol_list:
                print("Check in call expr", symbol, symbol.is_body_having)
                if ast.name.name == symbol.name and Utils.isFunc(symbol):
                    flag = True
                    # print("Call expression", symbol.is_body_having)
                    # if type(symbol.type) is VoidType:
                    #     raise TypeCannotBeInferred(ast)
                    break
        
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
        # for symbollist in o:
        #     for symbol in symbollist:
        #         print("Check here .........", symbol)
        #     print('.///', len(o))
        if flag:
            # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)        
            for symbol in o[1]: #TypeCannotBeInfered error for calling again this function itself  
                # print("check here", symbol)
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    raise TypeCannotBeInferred(ast)
            for symbol in o[1:-1]: # kiểm tra ở non-local, tức là bỏ local và global
                for symbol in symbol_list:
                    if symbol.name == ast.name.name and Utils.isFunc(symbol):
                        if symbol.is_body_having == False:
                            raise NoDefinition(symbol.name)
                        break
        
        for symbol_list in o[1:-1]: # kiểm tra ở non-local, tức là bỏ local và global
            for symbol in symbol_list:
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    list_param = symbol.param
                    args = ast.args
                    
                    if len(list_param) > len(args):
                        raise TypeMismatchInExpression(ast)
                    elif len(args) < len(list_param):
                        raise TypeMismatchInExpression(ast)
                    else:
                        for i in range(0, len(list_param)):
                            param_type = list_param[i].type # param element here is symbol
                            args_type = self.visit(ast.args[i], o)
                            
                            # May be wrong because of passing by value
                            # atomic_types = [NumberType, BoolType, StringType]                        
                            # if not (type(args_type) in atomic_types):
                            #     args_type = param_type
                            # TYPE INFERRED: params -> args: Implicit keyword is not parameters
                            if type(args_type) is None:
                                ast.args[i].varType = param_type
                                continue 
                            # Passing by reference
                            if type(param_type) is ArrayType:
                                ast.args[i].varType = param_type
                                continue
                            # TYPE MISMATCH
                            if type(args_type) is not type(param_type):
                                return TypeMismatchInExpression(ast) ## for the case: y <- a + foo(x) of TypeCannotBeInferred in spec
                    return symbol.type
    def visitAssign(self, ast, o):
        print("This is from visitAssign")
        exp_type = self.visit(ast.rhs, o)
        lhs_type = self.visit(ast.lhs, o)
        print("Check type in assign", lhs_type, exp_type)
        
        if type(lhs_type) is VoidType or type(lhs_type) is ArrayType:
            raise TypeMismatchInStatement(ast)
        
        if lhs_type is None and exp_type is None:
            raise TypeCannotBeInferred(ast)
        
        if lhs_type is None:
            lhs_type = Utils.infer(o, ast.lhs.name, exp_type)
            return
        
        if exp_type is None:
            exp_type = Utils.infer(o, ast.rhs.name, lhs_type)
            return
                    
        if type(lhs_type) is type(exp_type):
            return exp_type
        
        if type(lhs_type) is not type(exp_type):
            raise TypeCannotBeInferred(ast)
        
    def visitIf(self, ast, o):
        condition_type = self.visit(ast.expr, o)
        if type(condition_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # Go to new scope -> need new o
        o1 = [[]] + o
        if ast.thenStmt:
            self.visit(ast.thenStmt, o1)
        o2 = [[]] + o
        if ast.elifStmt:
            self.visit(ast.elifStmt, o2)
        o3 = [[]] + o
        if ast.elseStmt:
            self.visit(ast.elifStmt, o3)

    def visitFor(self, ast, o): # name: Id, condExpr: Expr, updExpr: Expr, body: Stmt
        init_type = self.visit(ast.name, o)
        condition_type = self.visit(ast.condExpr, o)
        update_type = self.visit(ast.updExpr, o)
        if type(init_type) is not NumberType or type(condition_type) is not BoolType or type(update_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        # new scope
        o1 = [[Symbol("<Loop>", VoidType)]] + o
        self.visit(ast.body, o1)
        
    def visitBreak(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitContinue(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitReturn(self, ast, o):
        print("Return")
        # 'Cause the function does not have return type, we don't need to check type here. What we just need to do is that assign return_expr type to function type
        right_type = self.visit(ast.expr, o) if ast.expr else VoidType() # RHS
        for i in range(1, len(o)):
            if len(o[i]) > 0 and Utils.isFunc(o[i][0]):
                o[i][0].type = right_type
                # print("CHECK HERE", len(o), o[i][0])
                break
        
    def visitCallStmt(self, ast, o):
        flag = False    
            
        for symbol in o[-1]:
            if ast.name.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                break
        
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
        # for symbollist in o:
        #     for symbol in symbollist:
        #         print("Check here .........", symbol)
        #     print('.///', len(o))
        if flag:
            # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)        
            for symbol in o[1]: #TypeCannotBeInfered error for calling again this function itself  
                print("check here", symbol)
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    raise TypeCannotBeInferred(ast)
            for symbol_list in o[1:-1]:
                for symbol in symbol_list:
                    if symbol.name == ast.name.name and Utils.isFunc(symbol):
                        if symbol.is_body_having == False:
                            raise NoDefinition(symbol.name)
                        break
        
        for symbol_list in o[1:-1]:
            for symbol in symbol_list:
                if symbol.name == ast.name.name and Utils.isFunc(symbol):
                    list_param = symbol.param
                    args = ast.args
                    
                    if len(list_param) > len(args):
                        raise TypeMismatchInExpression(ast)
                    elif len(args) < len(list_param):
                        raise TypeMismatchInExpression(ast)
                    else:
                        for i in range(0, len(list_param)):
                            param_type = list_param[i].type # param element here is symbol
                            args_type = self.visit(ast.args[i], o)
                            
                            # May be wrong because of passing by value
                            # atomic_types = [NumberType, BoolType, StringType]                        
                            # if not (type(args_type) in atomic_types):
                            #     args_type = param_type
                            # TYPE INFERRED: params -> args: Implicit keyword is not parameters
                            if type(args_type) is None:
                                ast.args[i].varType = param_type
                                continue 
                            # Passing by reference
                            if type(param_type) is ArrayType: # args_type is None because ast.args[i] is declared 'dynamic' -> ast.args[i] is Id
                                ast.args[i].varType = param_type
                                continue
                            # TYPE MISMATCH
                            if type(args_type) is not type(param_type):
                                raise TypeMismatchInExpression(ast)
                    return symbol.type
                 
    def visitBlock(self, ast, o):
        print("From block ..............")
        o1 = [[]] + o
        # check if this block belongs to a function or not
        check_func = False
        for symbol in o1[1]:
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
                
                if type(stmt_decl) is Return:
                    check_return_stmt = True
                    
                if type(stmt_decl) is CallStmt:
                    # print("Check call stmt in visitBlock", o1[1][0])
                    # Write TypeCannotBeInfered error for calling again this function itself 
                    if stmt_decl.name.name == o1[1][0].name:
                        raise TypeCannotBeInferred(stmt_decl)
                    
                # first_stmt = False
            if not check_return_stmt: # there are no return statements, func type is VoidType
                o1[1][0].type = VoidType()
                
    def visitVarDecl(self, ast, o): # name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None 
        print("This is from visitVarDecl")
        flag = False
        # check redeclare
        for symbol in o[0]: # vì ở dưới hàm visitProgram chúng ta khai báo biến env = [[]] + global_scope nên mỗi biến được tạo ra sẽ được thêm vào env[0] (tức là o[0])
            if symbol.name == ast.name.name:
                raise Redeclared(Variable(), ast.name)
          
        # check duplicate with special function
        for symbol in o[-1][:6]:
            if symbol.name == ast.name.name and Utils.isFunc(symbol):
                raise Redeclared(Variable(), ast.name)
        
        if not ast.varInit: 
            # print("Check var without init", ast.name, ast.varType)
            o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, ast.varInit)]
            
        else:
            init = self.visit(ast.varInit, o)
            if ast.modifier == 'var' or ast.modifier == 'dynamic':
                o[0] += [Symbol(ast.name.name, init, ast.modifier, None)]
                # Utils.infer(o, ast.name, init)
            elif type(ast.varType) is ArrayType and type(init) is ArrayType:
                ast.varType.size = list(map(lambda x: int(x), ast.varType.size))       
                init.size = list(map(lambda x: int(x), init.size))   
                if ast.varType.size != init.size:
                    # print(11111)
                    raise TypeMismatchInExpression(ast)
                
                if type(ast.varType.eleType) is not type(init.eleType):
                    # print(3333)
                    raise TypeMismatchInExpression(ast)
                
                if hasattr(ast.varInit, 'value'): # ArrayLiteral -> init là: [1,2,3]
                    # print(2222)
                    for expr in ast.varInit.value:
                        expr_type = self.visit(expr, o) # if expr_type has modifier, need to define at visitExpr -> it means adding Symbol(name, None, 'var' / 'dynamic', None) at visitExpr
                        # print("Check here>>>>", type(expr_type))
                        if type(expr_type) is None: # biến này đã được khai báo trước đó
                            Utils.infer(o, expr_type.name, ast.varType.eleType)
                        elif type(expr_type) is not type(ast.varType.eleType):
                            raise TypeMismatchInExpression(ast)
                o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, None)]
            elif type(ast.varType) is ArrayType and (init.modifier == 'var' or init.modifier == 'dynamic'): 
                Utils.infer(o, init.name, ast.varType)
                o[0] += [Symbol(ast.name.name, ast.varType, init.modifier, None)]
            ## Mismatch
            elif (init is not None) and (ast.varType is not None) and type(init) is not type(ast.varType):
                raise TypeCannotBeInferred(ast)
            else:
                o[0] += [Symbol(ast.name.name, ast.varType, ast.modifier, None)]
            
    def visitFuncDecl(self, ast, o): # name: Id # param: List[VarDecl]  # body: Stmt = None  
        print("This is from visitFuncDecl")
        found = False
        
        for symbol in o[-1]: # Global
            # print("This is from function", symbol)
            if symbol.name == ast.name.name:
                raise Redeclared(Function(),ast.name.name)
        
        o1 = [[Symbol(ast.name.name, None, None, [])]] + o
        
        # Check if parameters are already defined
        for idx in range(len(ast.param)):
            if ast.param[idx].name.name == o[1][0].name: # Kiểm tra tham số có trùng với tên hàm ?
                raise Redeclared(Parameter(), ast.param[idx].name.name)
            
            for idx1 in range(idx):
                if ast.param[idx].name.name == ast.param[idx1].name.name:
                    raise Redeclared(Parameter(), ast.param[idx].name.name)
                
        # Visit params    
        for param in ast.param:
            self.visit(param, o1)
            
        check_having_body = False
        if ast.body:
            check_having_body = True
            self.visit(ast.body, o1) # after visiting body, we try to assign type of return stmt to o1[0][0].type (which is type of function)
        else:
            flag = False
            for decl in self.ast.decl:
                if type(decl) is FuncDecl and decl.name.name == ast.name.name:
                    for idx_param in range(len(decl.param)):
                        if decl.param[idx_param].type != ast.param[idx_param].varType:
                            raise Redeclared(Function(), ast.name)
                    
                    # Trùng tên và trùng cả tham số
                    if decl.body:
                        check_having_body = True
                        self.visit(decl.body, o1)      
                    else:
                        if flag is True: # tránh case: func g(), func g(), func g() begin end
                            raise Redeclared(Function(), ast.name)
                        flag = True
        # for symbollist in o1:
        #     for symbol in symbollist:
        #         print("Checking symbol", symbol)
        #     print(".......")
        list_params = []
        for i in range(1, len(ast.param) + 1):
            list_params += [Symbol(o1[0][i].name, o1[0][i].type, o1[0][i].modifier, None )]
        
        o[0] += [Symbol(ast.name.name, o1[0][0].type, None, list_params, check_having_body)]
        
    
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
        
        check_main_func = False
        for func in env[0]:
            # print(func.name == "main", type(func.type) is VoidType, func.param)
            if func.name == "main" and type(func.type) is VoidType and len(func.param)==0:
                check_main_func = True
                break
        
        if not check_main_func:
            raise NoEntryPoint()