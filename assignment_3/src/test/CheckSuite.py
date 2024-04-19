import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    
    ## NO ENTRY POINT, NO ERROR WITH MAIN FUNC

         
#     def test_no_entry_point(self):
#         input = """number a
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 400))
    
#     def test_no_entry_point_2(self):
#         input = """func b() 
#             begin
#             end
#         """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 401))
    
#     def test_no_entry_point_3(self):
#         input = """func main() 
#             begin
#                 return 1
#             end
#         """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 402))
    
#     def test_no_entry_point_4(self):
#         input = """func main() 
#             begin
#                 return
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 403))
    
#     def test_no_entry_point_5(self):
#         input = """func bkool()
#             begin
#                 return true
#             end
#         """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 404))
        
#     def test_invalid_param_1(self):
#         input = """
#         func inc(number a) return a+1
#             """
#         expect = """No Entry Point"""
#         self.assertTrue(TestChecker.test(input, expect, 485))
        
#     ## REDECLARED VARIABLES
    
#     def test_redecl_var_1(self):
#         input = """func main()
#             begin
#                 number a
#                 string a
#             end
#             """
#         expect = """Redeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 405))
    
#     def test_redecl_var_2(self):
#         input = """func main()
#             begin
#                 number a
#                 number b
#                 string c
#                 bool b
#             end
#             """
#         expect = """Redeclared Variable: b"""
#         self.assertTrue(TestChecker.test(input, expect, 406))
    
#     def test_redecl_var_3(self):
#         input = """ number a
#             func main()
#             begin
#                 string a
#                 return
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))
    
#     def test_redecl_var_4(self):
#         input = """ number a
#             func main()
#             begin
#                 number a
#                 begin
#                     string a
#                 end
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 408))
    
#     def test_redecl_var_5(self):
#         input = """ number a
#             number b
#             func main()
#             begin
#                 number a
#             end
#             number b
#             """
#         expect = """Redeclared Variable: b"""
#         self.assertTrue(TestChecker.test(input, expect, 409))
        
#     def test_redecl_func_4(self):
#         input = """func main()
#             begin
#             end
#             func foo (number a)
#             begin
#                 bool a
#             end
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 414))
        
#     def test_redecl_func_5(self):
#         input = """func main() 
#             begin
#             end
#             func foo(number a) 
#             begin
#             end
#             string a
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))
        
#     ## BREAK/CONTINUE NOT IN LOOP
        
#     def test_ifs_normal_preventDefault(self):
#         input = """
#         func f()
#         begin
#             var j <- 1
#             for j until j > 11 by 1
#             begin
            
#             end
#             break
#         end
        
#         func main()
#         begin
#             f()
#         end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 410))
        
#     def test_mil_1(self):
#         input = """
#         func main()
#         begin
#             number i <- 0
#             for i until i < 10 by i
#             begin
#                 continue
#                 break
#             end
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 465))
    
#     def test_mil_2(self):
#         input = """
#         func main()
#         begin
#             number i <- 0
#             for i until i < 10 by i
#             begin
#                 continue
#             end
#             break
#         end
#             """
#         expect = """Break Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 466))
    
#     def test_mil_3(self):
#         input = """
#         func main()
#         begin
#             number i <- 0
#             for i until i < 10 by i
#             begin
#                 break
#             end
#             continue
#         end
#             """
#         expect = """Continue Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 467))
    
#     def test_mil_4(self):
#         input = """
#         func main()
#         begin
#             number i <- 0
#             for i until i < 10 by i
#             begin
#                 continue
#                 begin
#                     break
#                 end
#             end
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 468))
    
#     def test_mil_5(self):
#         input = """
#         func main()
#         begin
#             number i <- 0
#             for i until i < 10 by i + 1
#             begin
#                 continue
#             end
#             begin
#                 break
#             end
#         end
#             """
#         expect = """Break Not In Loop"""
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test_476(self):
#         input = """
#             func f()
#         begin
#             var i <- 0
#             for i until i > 10 by i
#             begin
            
#             end
#             continue
#         end
#         func main()
#         begin
#             number x <- 2 + true
#             writeNumber(x)
#         end
#             """
#         expect = "Continue Not In Loop"
        
#         self.assertTrue(TestChecker.test(input, expect, 476))
        
#     ## PASS ARRAY AS ARGUMENT
    
#     def test_ifs_block_stmt(self):
#         input = """
#         func findMax(number x[10], number n)
#         begin
#             if (n = 1) return x[0]
#             number k <- findMax(x, n - 1)
#             if (k >= x[n]) return k
#             return x[n]
#         end
    
#         func main() 
#         begin
#             dynamic x <- [3, 4, 8, 1, 2, 7, 9, 8, 5, 6]
#             writeNumber(findMax(x, 10))
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 411))
        
#     ## REDECLARED PARAMETERS
    
#     def test_ifs_inherit_parent(self):
#         input = """
#         func foo (number n, string n) begin
        
#         end 
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Parameter: n"
#         self.assertTrue(TestChecker.test(input, expect, 412))
        
#     def test_redecl_param_1(self):
#         input = """func main() 
#             begin
#             end
#             func foo (number a, string a)
#             begin
#             end
#             """
#         expect = """Redeclared Parameter: a"""
#         self.assertTrue(TestChecker.test(input, expect, 416))
        
#     def test_redecl_param_2(self):
#         input = """func main() 
#             begin
#             end
#             func foo (number foo) ## No error variable name can be same as func name
#             begin
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 417))
    
#     def test_redecl_param_3(self):
#         input = """func main() 
#             begin
#             end
#             func foo(number main)
#             begin
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 418))
    
#     def test_redecl_param_4(self):
#         input = """func main()
#             begin
#             end
#             func foo (number a)
#             begin
#             end
#             func a (number foo)
#             begin
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 419))


#     def test_ifs_redecl_var(self):
#         input = """
#         func foo(number x) begin
#             number a <- 7
#         end
#         func foo1(string x, bool x) begin
        
#         end
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 497))    
#     ## FOR MULTIPLE FUNCTIONS
   
#     def test_redecl_func_3(self):
#         input = """func main()
#         begin
#             number main
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))
    
    
#     ## UNDECLARED IDENTIFIERS
    
#     def test_undecl_var_1(self):
#         input = """func main()
#         begin
#             a <- 2
#             return
#         end
#             """
#         expect = """Undeclared Identifier: a"""
#         self.assertTrue(TestChecker.test(input, expect, 420))
    
#     def test_undecl_var_2(self):
#         input = """number a
#         func main()
#         begin
#             a <- 2
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 421))
    
#     def test_undecl_var_3(self):
#         input = """func main()
#         begin
#             var a <- 2
#             var b <- a + 2
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))
    
#     def test_undecl_var_4(self):
#         input = """func main()
#         begin
#             begin
#                 number a
#             end
#             a <- 2
#         end
#             """
#         expect = """Undeclared Identifier: a"""
#         self.assertTrue(TestChecker.test(input, expect, 423))
    
#     def test_undecl_var_5(self):
#         input = """
#             func main() 
#             begin 
#             end
#             func foo(number a)
#             begin
#                 a <- 2
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))
        
#     def test_478(self):
#         input = """
#         func main()
#         begin
#             dynamic x <- (x - 2) * (x + true)
#         end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 478))
    
#     def test_func_id(self):
#         input = """
#         func foo() return 1
#         var a <- foo
#         func main()
#         begin
#         end
#             """
#         expect = """Undeclared Identifier: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 494))
        
#     def test_array_id(self):
#         input = """
#         func foo()
#         begin
#         end
#         func main()
#         begin
#             a[0] <- 5
#         end
#             """
#         expect = """Undeclared Identifier: a"""
#         self.assertTrue(TestChecker.test(input, expect, 495)) 
            
#     ## UNDECLARED FUNCTIONS
    
#     def test_undecl_func_1(self):
#         input = """
#         func check()
#         begin
#         end
#         func main()
#         begin
#             foo()
#         end
#             """
#         expect = """Undeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 425))
    
#     def test_undecl_func_2(self):
#         input = """func main()
#         begin
#             number a
#             a <- foo() + 5
#         end
#             """
#         expect = """Undeclared Function: foo"""
#         self.assertTrue(TestChecker.test(input, expect, 426))
        
    
#     def test_func_pass(self):
#         input = """
#             func main()
#             begin
#                 number arr <- 2
#                 main()
#             end
#             """
#         expect = "Undeclared Function: main"
#         self.assertTrue(TestChecker.test(input, expect, 427))
        

#     def test_undeclare_func(self):
#         input = """
#         func x() return
#         func main()
#         begin
#             super()
#         end
#             """
#         expect = """Undeclared Function: super"""
#         self.assertTrue(TestChecker.test(input, expect, 492))


#     def test_ifs_inherit_grandparent(self):
#         input = """
#         func foo(number a) begin
#             writeNumber(a)
#             number c <- 109
#         end
        
#         func main() begin
#             foo(2018)
#             goo(20, 1998)
#         end
        
#         func goo(number a, number b) begin            
#             foo(3)
#         end
#          """
#         expect = "Undeclared Function: goo"
#         self.assertTrue(TestChecker.test(input, expect, 496))        
#     ## TYPE MISMATCH STMT: ASSIGN-STMT
    
#     def test_4001(self):
#         input = """
#             number a[3] <- [2,3,4]
#             func main()
#             begin
#                 a[3] <- "error here"
#             end
#             """
#         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(3.0)]), StringLit(error here))"
#         self.assertTrue(TestChecker.test(input, expect, 428))
        
#     def test_ial_2(self):
#         input = """
#         number b1
#         func main()
#         begin
#             bool a[5]
#             bool b1 
#             bool b2
#             a <- [b1,b2]
#         end
#             """
#         expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(b1), Id(b2)))"""
#         self.assertTrue(TestChecker.test(input, expect, 446))
        
#     def test_ial_3(self):
#         input = """
#         string a[5]
#         func main()
#         begin
#             number i1 <- 25
#             number f2 <- 25.0
#             a <- [i1,f2]
#         end
#             """
#         expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(i1), Id(f2)))"""
#         self.assertTrue(TestChecker.test(input, expect, 447))
        
#     def test_ial_5(self):
#         input = """
#         func main()
#         begin
#             number a[5]
#             string s
#             a[3] <- 2.5
#             a[2] <- 5
#             a[1] <- s
#         end
#             """
#         expect = """Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), Id(s))"""
#         self.assertTrue(TestChecker.test(input, expect, 449))
        
#     def test_tmms_asm_1(self):
#         input = """
#         func main()
#         begin
#             bool b
#             number i
#             dynamic v
#             v <- v
#         end
#             """
#         expect = """Type Cannot Be Inferred: AssignStmt(Id(v), Id(v))"""
#         self.assertTrue(TestChecker.test(input, expect, 458))
        
#     def test_471(self):
#         input = """
#             func main()
#             begin
#                 dynamic c
#                 dynamic d
#                 d <- c
#             end
#             """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(d), Id(c))"
        
#         self.assertTrue(TestChecker.test(input, expect, 471))
        
#     ## TYPE MISMATCH EXPRESSION: CALL-EXPR
        
#     def test_4002(self):
#         """Call function with the void type (wrong)"""
        
#         input = """
#             func foo(number x)
#             begin
#                 return
#             end
            
#             func main()
#             begin
#                 number x <- 2
#                 dynamic y
#                 y <- foo(x)
#             end
            
#             """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        
#         self.assertTrue(TestChecker.test(input, expect, 429))
        
#     def test_tmme_c2_param_typ(self):
#         """Pass wrong type as arguments"""
        
#         input = """
#         func foo(number a, number b)
#         func main()
#         begin
#             number a <- 2
#             string b <- "2.1"
#             a <- foo(b,a) + 2
#         end
#         func foo(number a, number b)
#         begin
#             return a+b
#         end
#             """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(b), Id(a)])"""
#         self.assertTrue(TestChecker.test(input, expect, 443))
        
#     def test_tmme_c3_param_len(self):
#         """Pass not enough parameters"""
        
#         input = """
#         func foo(number a, number b, number c)
#         func main()
#         begin
#             number a <- 2
#             number b <- 2.1
#             a <- foo(a,b) + 2
#         end
#         func foo(number a, number b, number c)
#         begin
#             return a+b+c
#         end
#             """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b)])"""
#         self.assertTrue(TestChecker.test(input, expect, 444))
        
#     def test_tmms_func_2(self):
#         input = """
#         func foo(number a,number b,number c)
#         begin
#             return 0.0
#         end
        
#         func bar()
#         begin
#         end
        
#         func main()
#         begin
#             number i
#             number f
#             f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
#             f <- foo(1,"2",3.0) ## invalid: param 2 mismatch
#         end
#             """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(2), NumLit(3.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 461))
    
#     ## TYPE MISMATCH EXPR: ARRAY-CELL
    
#     def test_tmme_a1(self):
#         input = """
#         func main()
#         begin
#             number a[5]
#             number b
#             b <- a[5]
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 430))
    
#     def test_tmme_a2(self):
#         input = """
#         func main()
#         begin
#             number a
#             number b
#             b <- a[5]
#         end
#             """
#         expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(5.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 431))
    
#     def test_tmme_a3(self):
#         input = """
#         func main()
#         begin
#             number a[5, 5]
#             number b
#             b <- a[1.0,"1"]
#         end
#             """
#         expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), StringLit(1)])"""
#         self.assertTrue(TestChecker.test(input, expect, 432))
    
#     def test_array_asm(self):
#         input = """
#         func foo(number a) return "vankha"
#         func main()
#         begin
#             number a[2,3]
#             a[1,2,3] <- 1
#         end
#             """
#         expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 488))
        
           
#     ## TYPE MISMATCH EXPR: BINARY-OP
    
#     def test_tmme_b1_implicit(self):
#         input = """
#         func main()
#         begin
#             number a 
#             string b
#             ## a + b: Unknown a: number
#             a <- a + b
#         end
#             """
#         expect = """Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 433))
    
#     def test_tmme_b2_implicit(self):
#         input = """
#         func main()
#         begin
#             number a
#             number b
#             ## number -> number:OK
#             b <- a
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 434))
    
#     def test_tmme_b6_binary(self):
#         input = """
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             a <- 1
#             dynamic c
#             c <- a + b
#         end
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 438)) 
        
#     def test_tmme_b7_binary(self):
#         input = """
#         func main()
#         begin
#             number a
#             number b
#             number c
#             string d 
#             string e 
#             d <- d ... e ## valid
#             b <- a % c ## valid
#             a <- a == b ## invalid: a == b
#         end
#             """
#         expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 439))
    
#     def test_tmme_b8_binary(self):
#         input = """
#         func main()
#         begin
#             number a
#             bool b
#             bool c
#             b <- (b and c) or c ## valid
#             b <- a and b ## invalid: a and b
#         end
#             """
#         expect = """Type Mismatch In Expression: BinaryOp(and, Id(a), Id(b))"""
#         self.assertTrue(TestChecker.test(input, expect, 440))
    
#     def test_tmme_b9_binary(self):
#         input = """
#         func main()
#         begin
#             number a
#             number b
#             bool c
#             bool d
#             number e
#             c <- b > e
#             c <- e <= b
#             d <- b == e ## invalid: b==e
#         end
#             """
#         expect = "Type Mismatch In Expression: BinaryOp(==, Id(b), Id(e))"
#         self.assertTrue(TestChecker.test(input, expect, 441))
        
#     def test_472(self):
#         input = """
#         func main()
#         begin
#             dynamic x 
#             x  <- (x - 2) * (x + true)
#         end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 472))    

#     def test_477(self):
#         input = """
#         func main()
#         begin
#             number x <- 2 + true
#             writeNumber(x)
#         end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 477))
        
#     def test_479(self):
#         input = """
#         dynamic a
#         func main()
#         begin
#             var i <- a ... 2.75
#         end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
#         self.assertTrue(TestChecker.test(input, expect, 479))
        
#     ## TYPE CANNOT BE INFERRED: VARDECL
    
#     def test_tmme_b3_implicit(self):
#         input = """
#         func main()
#         begin
#             number a <- 1
#             number b <- a + 2
#             string c <- 2.3
#         end
#             """
#         expect = """Type Mismatch In Statement: VarDecl(Id(c), StringType, None, NumLit(2.3))"""
#         self.assertTrue(TestChecker.test(input, expect, 435))
        
#     def test_ifs_normal_super(self): # check again
    
#         input = """
#         dynamic x
#         func main() 
#         begin
#             var y <- x[0, 0] + 1
#             writeNumber(y)
#         end
#             """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 470))
        
        
#     def test_474(self):
#         input = """
#             dynamic y
#             func main()
#             begin
#                 var x <- 2
#                 if (true) 
#                 begin
#                     var a <- y
#                     if (true)
#                     begin
#                         x <- y
#                     end
#                 end
#             end
#             """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(y))"
        
#         self.assertTrue(TestChecker.test(input, expect, 474))       


#     def test_array_cell_nonatomic(self):
#         input = """
#         func main()
#         begin
#             number a[1,2,3]
#             number x <- a[1]
#         end
#             """
#         expect = """Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, ArrayCell(Id(a), [NumLit(1.0)]))"""
#         self.assertTrue(TestChecker.test(input, expect, 491))        
#     ## TYPE MISMATCH EXPR: UNARY-OP
    
#     def test_tmme_b4_unary(self):
#         input = """
#         func main()
#         begin
#             string a
#             a <- -a
#         end
#             """
#         expect = """Type Mismatch In Expression: UnaryOp(-, Id(a))"""
#         self.assertTrue(TestChecker.test(input, expect, 436))
    
#     def test_tmme_b5_unary(self):
#         input = """
#         func main()
#         begin
#             number a
#             a <- not a
#         end
#             """
#         expect = """Type Mismatch In Expression: UnaryOp(not, Id(a))"""
#         self.assertTrue(TestChecker.test(input, expect, 437))
        
        
#     ## TYPE MISMATCH STMT: RETURN-STMT
    

    
#     def test_invalid_param_2(self):
#         input = """
#             func inc(number a) 
#             func main()
#             begin
#                 string c <- "hello world" 
#                 var x <- inc(3)...c 
#             end 
#             func inc(number a) return a+1 
#             """
#         expect = """Type Mismatch In Statement: Return(BinaryOp(+, Id(a), NumLit(1.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 486))
        
#     def test_return_after(self):
#         input = """
#         func foo(string a, number b)
#         begin
#             if (b>0)
#             begin
#                 return a ## -> string
#             end
#             return "a" ## -> string
#             return 1 ## -> dont care
#         end
#         func main()
#         begin
#             writeString(foo("Hello",2))
#         end
        
#             """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 499))   
        
                 
#     ## TYPE MISMATCH EXPRESSION: ARRAYLITERAL
    
#     def test_ial_1(self):
#         """Wrong type in array literal"""
        
#         input = """
#         func main()
#         begin
#             number a[5]
#             a <- [1,"2.0"]
#         end
#             """
#         expect = """Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(2.0))"""
#         self.assertTrue(TestChecker.test(input, expect, 445))
    
#     def test_ial_4(self):
#         """Wrong type in array literal"""
        
#         input = """
#         func main()
#         begin
#             number a[5, 5]
#             a <- [[1,2],[1,2,3],[1,2,"3"]]
#         end
#             """
#         expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(3)))"""
#         self.assertTrue(TestChecker.test(input, expect, 448))
        
#     def test_tmms_asm_2(self):
#         input = """
#         func main()
#         begin
#             bool b
#             dynamic c
#             number a[2, 3]
#             a <- [[c, c, c], [c, c, c]]
#         end
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 459))
        
#     def test_475(self):
#         input = """
#             func main()
#             begin
#                 number x[3] <- [2,3,"4"]
#             end
#             """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(2.0), NumLit(3.0), StringLit(4))"
        
#         self.assertTrue(TestChecker.test(input, expect, 475))
        
#     def test_array_as_param(self):
#         input = """
#         func foo1() return 2
#         func foo2() return 3
#         func main()
#         begin
#             number a[2] <- [ foo1(), foo2()]
#             writeNumber(foo1())
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 490))              
#     ## TYPE MISMATCH STMT: IF-STMT
        
#     def test_tmms_condexpr_1(self):
#         input = """
#         func main()
#         begin
#             bool b
#             number i
#             if(b) 
#             begin
#             end
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 450))
    
#     def test_tmms_condexpr_2(self):
#         input = """
#         func main()
#         begin
#             bool b
#             number i
#             if (b)
#             begin
#             end
#             elif (i)
#             begin 
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: If((Id(b), Block([])), [(Id(i), Block([]))], None)"""
#         self.assertTrue(TestChecker.test(input, expect, 451))
    
#     def test_tmms_condexpr_3(self):
#         input = """
#         func main()
#         begin
#             bool b1
#             bool b2
#             number i1
#             number i2
#             if(i1 = i2)
#             begin
#             end
            
#             if(i1)
#             begin
#             end
#             if(b1)
#             begin
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: If((Id(i1), Block([])), [], None)"""
#         self.assertTrue(TestChecker.test(input, expect, 452))
    
#     def test_tmms_condexpr_4(self):
#         input = """
#         func main()
#         begin
#             bool b1
#             bool b2
#             number i
#             if (b1 and b2)
#             begin
#             end
#             elif(b1 or b2)
#             begin
#             end
#             elif (i)
#             begin
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: If((BinaryOp(and, Id(b1), Id(b2)), Block([])), [(BinaryOp(or, Id(b1), Id(b2)), Block([])), (Id(i), Block([]))], None)"""
#         self.assertTrue(TestChecker.test(input, expect, 453))
        
        
#     ## TYPE MISMATCH STMT: FOR-STMT
    
#     def test_tmms_forexpr_1(self):
#         input = """
#         func main()
#         begin
#             bool b
#             var i <- 0
#             for i until i<10 by i+1
#             begin
#             end
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 454))
    
#     def test_tmms_forexpr_2(self):
#         input = """
#         func main()
#         begin
#             bool b <- true
#             number i
#             for b until i<10 by i*2
#             begin
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: For(Id(b), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(*, Id(i), NumLit(2.0)), Block([]))"""
#         self.assertTrue(TestChecker.test(input, expect, 455))
    
#     def test_tmms_forexpr_3(self):
#         input = """
#         func main()
#         begin
#             bool b <- true
#             dynamic i <- 0
#             for i until i<10 by i<10
#             begin
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
#         self.assertTrue(TestChecker.test(input, expect, 456))
    
#     def test_tmms_forexpr_4(self):
#         input = """
#         func main()
#         begin
#             bool b
#             number i
#             for i until i+1 by i<10
#             begin 
#             end
#         end
#             """
#         expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(+, Id(i), NumLit(1.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
#         self.assertTrue(TestChecker.test(input, expect, 457))
        
    
#     ## TYPE MISMTACH STMT: CALL-STMT
    
#     def test_tmms_func_1(self):
#         input = """
#         func foo()
#         begin
#             return 0
#         end
#         func main()
#         begin
#             number i 
#             number f
#             f <- f+i
#             foo() ## foo -> int (return - not auto anymore) != void (CallExpr) => INVALID !!
#             f <- f+foo(i)
#             i <- i+f
#         end
#             """
#         expect = """Type Mismatch In Statement: CallStmt(Id(foo), [])"""
#         self.assertTrue(TestChecker.test(input, expect, 460))
    
#     def test_tmms_func_3(self):
#         input = """
#         func foo(number a,number b,number c)
#         begin
#             return 0.0 
#         end
#         func main()
#         begin
#             number i
#             number f
#             f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
#             f <- foo(1,2.0,3.0) 
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 462))
    
#     def test_tmms_func_4(self):
#         input = """
#         func foo(number a,number b,number c, number d)
#         begin
#             return 0
#         end
#         func main()
#         begin
#             number i
#             number f
#             f <- f+i
#             begin
#                 f <- foo(i,f,f,i) ## infer: foo->number,a->number,b->number,c->number
#             end
#             f <- foo(1,2.0,3.0,1)
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 463))
    
#     def test_tmms_func_5(self):
#         input = """
#         func foo(number a,number b,number c, number d)
#         begin
#             a <- 5
#             return a ## foo->number
#         end
#         func main()
#         begin
#             var f <- foo(1,2,3,4) ## f->number
#             f <- f + "wrong"
#         end
#             """
#         expect = """Type Mismatch In Expression: BinaryOp(+, Id(f), StringLit(wrong))"""
#         self.assertTrue(TestChecker.test(input, expect, 464))
        
#     def test_infer_func_3(self):
#         input = """
#         func foo(number a, number b) return 1.2
#         func main()
#         begin
#             foo(1,2) ## error here because foo returns number type, not void
#             number a <- foo(1,2) + 1
#         end
#             """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0), NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 484))
        
        
#     def test_out_param(self):
#         input = """
#         func foo(number x[2]) return
#         func main()
#         begin
#             foo(1)
#         end
#             """
#         expect = """Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 489))
        
#     ## INFER TYPE PARAMETER
        
#     def test_473(self):
#         input = """
#             func foo(number x)
#             begin
#                 return x
#             end
        
#             func main()
#             begin
#                 dynamic x <-2 
#                 dynamic a
#                 var y <- 2
#                 x <- y + foo(a)
#             end
#             """
#         expect = ""
        
#         self.assertTrue(TestChecker.test(input, expect, 473))
    
    

#     ## INFER VARDECL
#     def test_var(self):
#         input = """
#         func main()
#         begin
#             var a <- 1
#         end
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 480))
    
#     def test_infer_var(self):
#         input = """
#         func main()
#         begin
#             var a <- 10
#             var b <- "100"
#             var c <- a < 10
#             writeNumber(a)
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 481))
    
#     def test_infer_func_1(self):
        
#         input = """
#         func foo(number a, number b) return 1.2
#         func main()
#         begin
#             number a <- foo(1,2)
#             writeNumber(foo(1,2))
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 482))
        
#     def test_infer_func_2(self):
#         input = """
#         func foo(number a, number b) return 1.2
#         func main()
#         begin
#             number a <- foo(1,2) + 1
#             writeNumber(foo(1,2))
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 483))
    

#     ## TYPE MISMATCH STMT: VARDECL
#     def test_array_decl(self):
#         input = """
#         func foo(number a) return "vankha"
#         func main()
#         begin
#             number a[3] <- [1,2]
#         end
#             """
#         expect = """Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0)))"""
#         self.assertTrue(TestChecker.test(input, expect, 487)) 
        
#     def test_nonatomic_cell_init(self):
#         input = """
#         func x() return
#         func main()
#         begin
#             number a[2, 3]
#             number b <- a[0, 0]
#             dynamic c <- a[0]
#         end
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 493))

#     def test_coercion_array_intfloat(self):
#         input = """
#         func main()
#         begin
#             number a[4] <- [1,2,3,4]
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 498)) 
        
#     def test__499(self):
#         input = """
#         func main()
#         begin
#             number a[7] <- [1,2,3,4,5,6,7]
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499)) 

#     ################### Check function redeclared/no definition ##########
    
#     def test_no_definition(self):
#         input = """
#             func f(number a) return 1
#             func f(number x)
            
#             func main()
#             begin
#                 number a <- f(2) + 1
#             end
#         """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 500))
        
#     def test_no_definition_2(self):
#         input = """
#             func f(number x)
#             func f(number a) return 1
            
#             func main()
#             begin
#                 number a <- f(2) + 1
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 501)) 
        
#     def test_no_definition_3(self):
#         input = """
#             func f(number x)
            
#             func main()
#             begin
#                 number a <- f(2) + 1
#             end
#         """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 502)) 
    
#     def test_no_definition_4(self):
#         input = """
#             func f(number x)
#             func f(number x)
#             func f(number x)
#             func f(number x) return 1
            
#             func main()
#             begin
#                 number a <- f(2) + 1
#             end
#         """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 503)) 
    
#     def test_no_definition_4(self):
#         input = """
#             func f(number x)
#             func f(number x) return 1
#             func f(number x)
#             func f(number x)
            
#             func main()
#             begin
#                 number a <- f(2) + 1
#             end
#         """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 504)) 
    
    
#     def test_tmme_c1_void_CallExpr(self):
#         """Return() in void function -> infer call expr"""
#         input = """
#         func foo()
#         func main()
#         begin
#             number a <- 2
#             a <- foo() + 2
#         end
#         func foo()
#         begin
#             return
#         end
#             """
#         expect = """Type Mismatch In Statement: Return()"""
#         self.assertTrue(TestChecker.test(input, expect, 442))    
    
#     def test_redecl_var_6(self):
#         input = """func main() 
#             begin 
#             end
#             func c() 
#             begin 
#             end
#             number c
#             """
#         expect = """"""
#         self.assertTrue(TestChecker.test(input, expect, 505))
    
#     def test_redecl_func_2(self):
#         input = """func main() begin 
#         end
#             func c() begin 
#             end
#             func c() begin 
#             end
#             """
#         expect = """Redeclared Function: c"""
#         self.assertTrue(TestChecker.test(input, expect, 506))
        
#     def test_infer_subscript(self):
#         input = """
#         func foo()
#         func bar()
#         func main()
#         begin
#             number a[3,4]
#             a[foo(), 1+4] <- 222
#             a[1,2] <- bar()
#             writeNumber(foo())
#             writeNumber(bar())
#         end
#         func foo() return 1
#         func bar() return 2
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 507))
        
#     def test_undecl_mismatch_param(self):
#         input = """
#         func foo()
#         func main()
#         begin
#         end
#         number a <- foo(1, 2)
#         func foo() return 1
#             """
#         expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0)])"""
#         self.assertTrue(TestChecker.test(input, expect, 508))
        
#     def test_undecl_func_3(self):
#         """forward invocation"""
#         input = """
#         func foo()
#         begin
#             return 1
#         end
        
#         func check()
#         begin
#             return 2
#         end
        
#         func main()
#         begin
#             number a
#             begin
#                 a <- foo() + 5
#             end
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 509))
    
#     def test_undecl_func_4(self):
#         """backward invocation"""
#         input = """
#         func foo()
#         func main()
#         begin
#             number a
#             a <- foo() + 5
#         end
#         func foo()
#         begin
#            return 1
#         end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 510))
    
#     def test_undecl_func_5(self):
#         input = """
#         func foo()
#         func main()
#         begin
#             number a
#             a <- foo() + 5
#         end
        
#         func foo()
#         begin
#             barrr()
#             return 1
#         end
        
#         func bar()
#         begin
#             return 2
#         end
#             """
#         expect = """Undeclared Function: barrr"""
#         self.assertTrue(TestChecker.test(input, expect, 511))

#     def test443(self): 
#         input = """
# number x
# number y
# func f()

# func main()
#     return
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 443))

#     def test_param_array(self):
#         input = """
#         number x
#         number y
#         func f(number a[10], number x)
#         func f(number a[5], number x)
#             return x
        
#         func main()
#             return
#         """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 512))


#     def test583(self): ## Confused !!!
#         input = """
# dynamic a
# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [1, 9, 6]
#     writeNumber(a[0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(NumLit(10.0), NumLit(20.0), NumLit(30.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 583))

        
#     def test_429(self):    
#         input = """
#             func a() begin
#                 number a <- 1
#             end
#             func main() begin
#                 a()
#                 b()
#             end
#         """
#         expect = "Undeclared Function: b"
#         self.assertTrue(TestChecker.test(input, expect, 429))
    
#     def test019(self):
#         input="""
       
#         number d
#         var c <-[c,c,c,c,d]   ## visit bien truoc roi moi visit init value
#         """
#         expect="Type Mismatch In Statement: VarDecl(Id(c), None, var, ArrayLit(Id(c), Id(c), Id(c), Id(c), Id(d)))"
#         self.assertTrue(TestChecker.test(input,expect,419))
               
#     def test022(self):
#         input="""
#         func a(number a,number b, number b)
#         func main()
#         return 0
#         """
#         expect="No Function Definition: a"
#         self.assertTrue(TestChecker.test(input,expect,422))
    
    
#     def test91(self): # type mismatch in expression
#         input = """
#             func main()
#             begin
#             var a <- 1 + 1 * 1 / 1 = "1"
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(=, BinaryOp(+, NumLit(1.0), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(1.0)), NumLit(1.0))), StringLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 196))

#     def test46(self): # type mismatch in expression
#         input = """
#             func main()
#             begin
#             var a <- "abc" ... "aa"
#             dynamic b <- a == false
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 146))
    
            
#     def test126(self): # type mismatch in statement
#         input = """
#             func a()
#             func main()
#             begin
#             dynamic a <- a() = 5
#             var b <- (a() + 1 > 6) or (a and true)
#             end
#             func a() return false
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 236))
    
# ################# ERROR ######################
        
#     def test71(self): # type mismatch in statement
#         input = """
#             func f(number x)
#             begin
#             if (x > 5) return x % 2
#             elif (x <= 5) return x - 1
#             end
#             func main()
#             begin
#             number x
#             if (f(2)) x <- 0
#             end
#         """
#         expect = "Type Mismatch In Statement: If((CallExpr(Id(f), [NumLit(2.0)]), AssignStmt(Id(x), NumLit(0.0))), [], None)"
#         self.assertTrue(TestChecker.test(input, expect, 173))
        
#     def test122(self): # type mismatch in statement
#         input = """
#             func b122()
#             func a122()
#             begin
#             return 1
#             return b122()
#             end
#             func b122() return true
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 232))
        
#     def test112(self): # type mismatch in statement
#         input = """
#             func foo(number i)
#             begin
#                 if (i = 1) return 2
#                 else
#                 begin
#                     dynamic x
#                     return x
#                 end
#             end
#             func main()
#             begin
#                 bool b <- foo(2)
#             end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), BoolType, None, CallExpr(Id(foo), [NumLit(2.0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 220))
        
#     def test109(self): # type mismatch in statement (note)
#         input = """
#             func f()
#             func main()
#             begin
#             number x <- f()
#             end
#             func f() begin ## NumberType
#             end
#         """
#         expect = "Type Mismatch In Statement: Block([])"
#         self.assertTrue(TestChecker.test(input, expect, 217))
        
#     def test135(self): #
#         """ Array Literals: RHS in Assign Statement """
#         input = """
#         func foo(number x[4])
#         func main()
#             begin
#                 dynamic x
#                 number arr135[2,3,4] 
#                 arr135 <- [foo(x),[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
#             end
#         func createArr(number n)
#             begin
#                 return [[n + n % n, n - n, -n, n * n],[n + 12.5, n % n - n, n, n],[n + - n, - n - - n, n, n]]
#             end
#         func foo(number n[4])
#             return createArr(n[0])
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 245))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10132
#     def test_f110(self): 
#         input = """
#           func main()
#             begin
#                 dynamic num
#                 bool arr <- num and (num > num)
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
#         self.assertTrue(TestChecker.test(input, expect, 218))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10964    
#     def test_f111(self): 
#         input = """
#             dynamic a
#             dynamic x <- a == (a+2)
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 219))
   
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10964      
#     def test_f112(self): 
#         input = """
#             dynamic a
#             string x <- [a]
#             func main() return
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
#         self.assertTrue(TestChecker.test(input, expect, 220))

#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10636
#     def test_f113(self):
#         input = """func main() return
#             number a[2,2] <- [[1,2], [5, "abc"]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(5.0), StringLit(abc))"
#         self.assertTrue(TestChecker.test(input, expect, 221))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10496
#     def test_f114(self):
#         input = """
#         func main()
#             begin
#             end
#         func aaa(number a, bool b)
#         begin
#             number b
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 222))
    
    
    
##########################################################    
#     def test401(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- [[1, 2, 3], [4, 5, 6]]
#     return x[0, 0]
# end

# func main()
# begin
#     number x <- f()
# end

# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))
    
#     def test402(self):
#         input = """
# func f(number x)

# func main()
# begin
#     number x <- f(2)
#     writeNumber(x)
# end

# func f(number x)
# begin
#     if (x >= 2) return f(x - 1) + f(x - 2)
#     return 1
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))
    
#     def test403(self):
#         input = """
# func main()
# begin
#     var x <- [[1, 2, 3], [4, 5, 6]]
#     var y <- x[0, 0] + 1
#     writeBool(y)
# end

# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 403))
    
#     def test404(self):
#         input = """
# dynamic x
# func main()
# begin
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end

# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))
    
#     def test405(self):
#         input = """
# dynamic x
# func main()
# begin
#     x <- [1, 2, 3, 4, 5, 6]
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end

# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 405))
    
#     def test406(self):
#         input = """
# dynamic x <- f(2)
# func f(number x)

# func main()
# begin

# end
# """
#         expect = "Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 406))
    
#     def test407(self):
#         input = """
# func f(number x)

# dynamic x <- f(2) + 1

# func f(number y)
# begin
#     if (y <= 1) return 1
#     return y * f(y - 1)
# end

# func main()
# begin
#     return 2
# end
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 407))
    
#     def test408(self):
#         input = """
# func f(number x)

# dynamic x <- f(2) + 1

# func main()
# begin
#     return
# end
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 408))
    
#     def test409(self): 
#         input = """
# func f(number x[2, 3])
#     return x[2]

# func main()
# begin
#     number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#     writeNumber(f()[2])
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
#         self.assertTrue(TestChecker.test(input, expect, 409))
    
#     def test410(self):
#         input = """
# func f(number x[2, 3])
#     return x

# func main()
# begin
#     number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#     writeNumber(f(x)[0, 1])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 410))
    
#     def test411(self):
#         input = """
# func f(number x[2, 3])
#     return x

# func main()
# begin
#     dynamic x <- [[1, 2, 3], [4, 5, 6]]
#     var y <- x[0, 0]
#     writeString(y)
# end
# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 411))
    
#     def test412(self):
#         input = """
# func f(number x[2, 3], number i, number j)
#     return x[i, j]

# func main()
# begin
#     dynamic x <- [[1, 2, 3], [4, 5, 6]]
#     var i <- 0
#     for i until i >= 2 by 1
#         for j until j >= 3 by 1
#             writeNumber(f(x, i, j))
# end
# """
#         expect = "Undeclared Identifier: j"
#         self.assertTrue(TestChecker.test(input, expect, 412))
    
#     def test413(self):
#         input = """
# func main()
# begin
#     number x <- readNumber()
#     if (x <= 10) writeString("Number is less than or equal to 10")
#     elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
#     else writeString("Invalid number!")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))
    
#     def test414(self):
#         input = """
# func isPrime(number x)

# func main()
# begin
#     number x <- readNumber()
#     if (isPrime(x)) writeString("x is a prime number")
#     else writeString("x is not a prime number")
# end

# func isPrime(number x)
# begin
#     if (x <= 1) return false
#     var i <- 2
#     for i until i > x / 2 by 1
#     begin
#         if (x % i = 0) return false
#     end
#     return true
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 414))
    
#     def test415(self):
#         input = """
# func areDivisors(number num1, number num2)
#     return ((num1 % num2 = 0) or (num2 % num1 = 0))

# func main()
# begin
#     var num1 <- readNumber()
#     var num2 <- readNumber()
#     if (areDivisors(num1, num2)) writeString("Yes")
#     else writeString("No")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))
    
#     def test416(self):
#         input = """
# func f()
# begin
#     var i <- 0
#     for i until i > 10 by 1
#     begin

#     end
#     continue
# end

# func main()
# begin
#     f()
# end
# """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 416))
    
#     def test417(self):
#         input = """
# func findMax(number x[10], number n)
# begin
#     if (n = 1) return x[0]
#     number k <- findMax(x, n - 1)
#     if (k >= x[n]) return k
#     return x[n]
# end

# func main()
# begin
#     dynamic x <- [3, 4, 0, 1, 2, 7, 9, 8, 5, 6]
#     writeNumber(findMax(x, 10))
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 417))
    
#     def test418(self):
#         input = """
# func main()
# begin
#     number x <- 2 + true
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 418))
    
#     def test419(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 419))
    
#     def test420(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3, 3] <- [a, b, c]
#     a <- [1, 2, 3]
#     b <- [4, 5, 6]
#     c <- [7, 8, 9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 420))
    
#     def test421(self):
#         input = """
# func f(number x[3])
# begin
#     return
# end
    
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     f([a, b, c])
#     a <- 3
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test422(self): # VAR
#         input = """
# func f(number x[2, 3])
    
# func main()
# begin
#     dynamic a
#     number x[2, 3] <- f(a)
#     a[0] <- [1, 2, 3]
# end

# func f(number x[2, 3])
#     return x
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 422))
    
#     def test423(self):
#         input = """
# func f(number x)
# begin
#     if (x = 0) return 0
#     elif (x = 1) return 1
#     else return f(x - 1) + f(x - 2)
# end
    
# func main()
# begin
#     dynamic a
#     number x <- f(a)
#     a[0] <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 423))
    
#     def test424(self):
#         input = """
# func max(number x, number y)
# begin
#     if (x <= y) return y
#     return x
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     number z <- readNumber()
#     writeNumber(max(max(x, y), z))
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))
    
#     def test425(self):
#         input = """
# func pow(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(pow(x, y))
# end

# func pow(number a, number b)
# begin
#     if (b = 0) return 1
#     number k <- pow(a, b / 2)
#     if (b % 2 = 0) return k * k
#     return a * k * k
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 425))
    
#     def test426(self):
#         input = """
# func add(number x, number x)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(add(x, y))
# end

# func add(number a, number b)
# begin
#     return a + b
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 426))
    
#     def test427(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(pow(x, y))
# end

# func add(number a, number b)
# begin
#     return a + b
# end
# """
#         expect = "Undeclared Function: pow"
#         self.assertTrue(TestChecker.test(input, expect, 427))
    
#     def test428(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     var i <- 0
#     for i until i > 10 by 0
#     begin
#         i <- add(i, 1)
#         writeNumber(i)
#     end
# end

# func add(number a, number b)
# begin
#     number x <- a + b
#     return x
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 428))
    
#     def test429(self):
#         input = """
# func f(number x)

# func main()
# begin
#     number x <- 10
#     number y <- f(x)
#     writeNumber(y)
# end

# func f(string x)
# begin
#     return x == "Hello"
# end
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 429))
    
#     def test430(self):
#         input = """
# func main()
# begin
#     var i <- 0
#     for i until i < 0 by 1
#     begin
#         string x <- readString()
#         if (x == "Hello") 
#         begin
#             x <- x ... ", world!"
#             writeString(x)
#         end
#         else writeString("Try again")
#     end
#     break
# end
# """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 430))
    
#     def test431(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     var i <- 0
#     for i until i >= n by 1
#         writeNumber(arr[i])
# end

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 431))
    
#     def test432(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     var i <- 0
#     for i until i >= n by 1
#         writeNumber(arr[i])
# end

# func main()
# begin
#     dynamic n
#     f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
#     n <- 10
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 432))
    
#     def test433(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[2, 2] <- [a, [b, 2]]
#     a <- 2
#     b <- 3
#     c <- true
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 433))
    
#     def test434(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3, 2] <- [a, b, [c, 0]]
#     a <- [1]
#     b <- [3, 4]
#     c <- 0
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 434))
    
#     def test435(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [readNumber(), a, b, c]
#     a <- 3
#     b <- x[0]
#     c <- a + b
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 435))
    
#     def test436(self):
#         input = """
# func main()
# begin
#     dynamic x <- readBool()
#     dynamic y <- not readBool()
#     if (x and y) writeNumber(1)
#     else writeNumber(0)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 436))
    
#     def test437(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if (x) writeString("x is infer to true value")
#     else writeString("x is infer to false value")
#     x <- 1 + true
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 437))
    
#     def test438(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if (x) writeString("x is infer to true value")
#     else writeString("x is infer to false value")
#     x <- not (true and not false) and not (false and not true)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 438))
    
    
#     def test440(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- (x - 2) * (x + true)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 440))
    
#     def test441(self):
#         input = """
# number a <- 1 + "Hello"
# func main()
#     return
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 441))
    
#     def test442(self):
#         input = """
# func f()

# func main()
# begin
#     number x <- g(1, 2, 3)
# end
# """
#         expect = "Undeclared Function: g"
#         self.assertTrue(TestChecker.test(input, expect, 442))
    
#     def test443(self):
#         input = """
# number x
# number y
# func f()

# func main()
#     return
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 443))
    
#     def test444(self):
#         input = """
# func f() begin

# end

# number f
# dynamic x
# func main()
#     return
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 444))
    
#     def test445(self):
#         input = """
# func f()
# begin

# end
# dynamic a
# number b
# bool c
# string d
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 445))
    
# #     def test446(self): # COMMENT BECAUSE TESTCASE WON'T HAVE RECURSIVE FUNCTIONS
# #         input = """
# # func f(number x)
# # begin
# #     return f(x)
# # end

# # func main()
# # begin
# #     dynamic d <- f(10)
# # end
# # """
# #         expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
# #         self.assertTrue(TestChecker.test(input, expect, 446))
    
#     def test447(self):
#         input = """
# func f(number x)
# begin
#     return 1
# end

# func main()
# begin
#     f(2018)
# end
# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2018.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 447))
    
#     def test448(self):
#         input = """
# func main()
# begin
#     continue
# end
# """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 448))
    
#     def test449(self):
#         input = """
# func main()
# begin
#     break
# end
# """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 449))
    
#     def test450(self):
#         input = """
# number x
# number y
# func add()
#     return x + y

# func main()
# begin
#     x <- readNumber()
#     y <- readNumber()
#     writeNumber(add())
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 450))
    
#     def test451(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     dynamic a <- add(x, y) + 1
# end

# func add(number x, number y)
#     return "Hello"
# """
#         expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 451))
    
#     def test452(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     dynamic a
#     a[0] <- [1, 2, 3]
# end

# func add(number x, number y)
#     return "Hello"
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 452))
    
#     def test453(self):
#         input = """
# func main()
# begin
#     number arr[3, 2] <- [[1, 2], [3, 4], [5, 6]]
#     number b[2] <- arr[1]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 453))
    
#     def test454(self):
#         input = """
# func f(number arr[10], number x)

# func main()
# begin
#     dynamic n
#     var i <- 0
#     number arr[10]
#     for i until true by 1
#     begin
#         n <- readNumber()
#         if ((n > 10) or (n <= 0)) writeString("Try again")
#         else break
#     end
    
#     for i until i >= n by 1
#         arr[i] <- readNumber()
    
#     f(arr, n)
# end

# func f(number a[5], number n)
#     return
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 454))

#     def test455(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     number arr[2, 2] <- [[a, b]]
#     number c[2, 2] <- arr
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
#         self.assertTrue(TestChecker.test(input, expect, 455))

#     def test456(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     var arr <- [[a], [b], [c], [1]]
#     arr <- [[1], [2], [3], [4]]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 456))
    
#     def test457(self):
#         input = """
# func main()
# begin
#     dynamic x <- "Hello"
#     if (x == "Hello") writeString(x)
#     else writeString("Something weird!")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 457))
    
#     def test458(self):
#         input = """
# func main()
# begin
#     dynamic x <- [1, 2, 3]
#     dynamic a <- x
#     writeNumber(a[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 458))

#     def test459(self):
#         input = """
# func foo(number a)

# func main()
# begin
#     number a <- foo(1)
#     return
# end

# func foo(number a)
# begin
#     return
# end
# """
#         expect = "Type Mismatch In Statement: Return()"
#         self.assertTrue(TestChecker.test(input, expect, 459))
    
#     def test460a(self): # VAR
#         input = """
# var f <- 10
# func f()
#     return

# func main()
# begin
#     dynamic a
#     dynamic b
#     number c
#     dynamic x <- f([a, b, c])
#     x <- ["Hello", ", my name is ", "Hy"]
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [ArrayLit(Id(a), Id(b), Id(c))])"
#         self.assertTrue(TestChecker.test(input, expect, 460))
    
#     def test460b(self):
#         input = """
# var f <- 10
# func f()
#     return

# func main()
# begin
#     dynamic a
#     dynamic b
#     number c
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 501))
    
#     def test461(self):
#         input = """
# func f(number a[3], number b[3])
#     return

# func main()
# begin
#     f([1, 3, 2], [1, "Hello", 2])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test462(self):
#         input = """
# dynamic a <- [[3, 9, 2, 10, -1], [0, -10, 5, 3, 11], [10, 9, -27, 36, 4]]
# func sort(number a[5])
# begin
#     var i <- 0
#     var j <- 0
#     for i until i > 4 by 1
#         for j until j > 4 by 1
#             if (a[i] > a[j])
#             begin
#                 var temp <- a[i]
#                 a[i] <- a[j]
#                 a[j] <- temp
#             end
# end

# func main()
# begin
#     var i <- 0
#     for i until i > 2 by 1
#         sort(a[i])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 462))
    
#     def test463(self): # VAR
#         input = """
# number x <- 10
# func f(number x)
# begin
#     number x <- x + 20
#     writeNumber(x)
# end
# func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 463))
    
#     def test464(self):
#         input = """
# func f(number n)

# number a[2, 3] <- [[f(1), f(2), f(3)], [f(4), f(5), f(6)]]
# func main()
# begin
#     var i <- 0
#     dynamic j <- 0
#     for i until i > 1 by 1
#         for j until j > 2 by 1
#             writeNumber(a[i, j])
# end

# func f(number a)
#     return a
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 464))
    
#     def test465(self):
#         input = """
# func f(number x[2, 3])
#     return x[0]

# func main()
# begin
#     dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 465))
    
#     def test466(self):
#         input = """
# func f(number n)

# func main()
# begin
#     var i <- f(2, 3)
# end

# func f(number a)
#     return a
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 466))
    
#     def test467(self):
#         input = """
# func f(number x, number y)

# func main()
# begin
#     var i <- f(2)
# end

# func f(number a)
#     return a
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 467))
    
#     def test468(self): 
#         input = """
# dynamic a
# func main()
# begin
#     var i <- a ... 2.75
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
#         self.assertTrue(TestChecker.test(input, expect, 468))
    
#     def test469(self): 
#         input = """
# dynamic a
# func main()
# begin
#     var i <- a[2] ... 2.75
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75)))"
#         self.assertTrue(TestChecker.test(input, expect, 469))
    
#     def test470(self):
#         input = """
# func main()
# begin
#     if (1) writeBool(true)
#     else writeBool(false)
# end
# """
#         expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
#         self.assertTrue(TestChecker.test(input, expect, 470))
    
#     def test471(self):
#         input = """
# func test()

# func test()

# func main()
# begin
#     if (1) writeBool(true)
#     else writeBool(false)
# end
# """
#         expect = "Redeclared Function: test"
#         self.assertTrue(TestChecker.test(input, expect, 471))
    
#     def test472(self):
#         input = """
# number a
# bool b
# string c
# dynamic d
# func main()
# begin
#     if (b) d <- 1 + a
#     else d <- a - 1.75
#     c <- "Hello, world!"
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 472))
    
#     def test473(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     if ((n < 0) or (n >= 10)) return -999
#     number i <- 0
#     for i until i >= n by 1
#         if (arr[i] < 10) return i
    
#     return not (n < 20)
# end

# func main()
# begin
#     f([1, 9, 6, 5, 3, 8, 10, 28, 0, -10], 10)
# end
# """
#         expect = "Type Mismatch In Statement: Return(UnaryOp(not, BinaryOp(<, Id(n), NumLit(20.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 473))
    
#     def test474(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     var arr <- [[a, 1], [b, true], [c, "Hello"]]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
#         self.assertTrue(TestChecker.test(input, expect, 474))
    
#     def test475(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     dynamic z
#     dynamic arr <- [[1, x], [2, y], [3, z]]
#     x <- 20
#     y <- 30
#     z <- "Hi"
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
#         self.assertTrue(TestChecker.test(input, expect, 475))
    
#     def test476(self):
#         input = """
# func main()
# begin
#     var x <- [10, 20, 40]
#     var y <- [true, false, true]
#     number a[2, 3] <- [x, y]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
#         self.assertTrue(TestChecker.test(input, expect, 476))
    
#     def test477(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 3] <- [x, y]
#     x <- [10, 20, 40]
#     y <- [true, false, true]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(y), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True)))"
#         self.assertTrue(TestChecker.test(input, expect, 477))
    
#     def test478(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 3] <- [x, y]
#     y <- [y[1] + y[2], y[2] - y[0], y[0] + y[1] < y[2]]
#     x <- [1, 9, 6]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(BinaryOp(+, ArrayCell(Id(y), [NumLit(1.0)]), ArrayCell(Id(y), [NumLit(2.0)])), BinaryOp(-, ArrayCell(Id(y), [NumLit(2.0)]), ArrayCell(Id(y), [NumLit(0.0)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(y), [NumLit(0.0)]), ArrayCell(Id(y), [NumLit(1.0)])), ArrayCell(Id(y), [NumLit(2.0)])))"
#         self.assertTrue(TestChecker.test(input, expect, 478))
    
#     def test479(self):
#         input = """
# func f(number x, bool y, string z)
#     return not y

# func main()
# begin
#     dynamic x
#     dynamic y
#     dynamic z
#     bool t <- f(x, y, z)
#     writeBool(y and not t)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test480(self):
#         input = """
# func main()
# begin
#     var x <- [[1, 2], [3, 4, 5]]
#     writeNumber(x[0, 2])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test481(self):
#         input = """
# func test(number x)
# begin
#     var y <- test
#     test(2018)
# end
# """
#         expect = "Undeclared Identifier: test"
#         self.assertTrue(TestChecker.test(input, expect, 481))
    
#     def test482(self):
#         input = """
# func test(number x)
# begin
#     var a <- x
#     var b <- -a
#     var c <- a + b
#     writeNumber(a + b + c)
# end

# func main()
# begin
#     test(2018)
#     return -1
# end
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 482))

#     def test483a(self):
#         input = """
# dynamic a
# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [1, 9, 6]
#     writeNumber(a[0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(NumLit(10.0), NumLit(20.0), NumLit(30.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 483))
 
#     def test483b(self):
#         input = """
# dynamic a
# func foo() begin
#     number a[2, 3] <- [a, [10, 20, 30]]
# end

# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [[1, 9, 6], [2,4,6]]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(NumLit(10.0), NumLit(20.0), NumLit(30.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 542))

#     def test484(self):
#         input = """
# dynamic a
# func main()
# begin
#     var x <- [a, [1, 2, 3]]
#     a <- [1, 9, 6]
#     x <- [[3, 9, 6], [1, 3, 2]]
#     writeNumber(x[0, 0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 484))
    
#     def test485(self):
#         input = """
# dynamic a
# func main()
# begin
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic e 
#     var x <- [a, [b], [[c]], [[[d, e]]]]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c))), ArrayLit(ArrayLit(ArrayLit(Id(d), Id(e))))))"
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test486(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     var x <- [a, b, c, [[1, 2, 3, 4], [5, 6, 7, 8]]]
#     c[0] <- d
#     d <- [0, 3, 1]
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(d), ArrayLit(NumLit(0.0), NumLit(3.0), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 486))
    
#     def test487(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c <- a ... ", world!"
#     a <- b
#     b <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 487))

#     def test488(self):
#         input = """
# func main()
# begin
#     number x
#     begin
#         number x <- (10 + x) * 2
#     end
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 488))
    
#     def test489(self): # VAR
#         input = """
# func test(number x)

# func main()
# begin
#     number test
#     begin
#         number x <- test(2018) + 1
#     end
# end
# """
#         expect = "No Function Definition: test"
#         self.assertTrue(TestChecker.test(input, expect, 489))
    
#     def test490(self):
#         input = """
# dynamic x
# func f(number x)
#     return x + 1

# func main()
# begin
#     x <- f(20, 30, 40) + 1
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(20.0), NumLit(30.0), NumLit(40.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 490))

#     def test491(self):
#         input = """
# func main()
# begin
#     number a[1, 2, 3, 4]
#     var b <- a[0]
#     number c[2, 3, 4]
#     b <- c
#     number d[1, 3, 4]
#     b <- d
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(d))"
#         self.assertTrue(TestChecker.test(input, expect, 491))
    
#     def test492(self):
#         input = """
# func f(number x, number y)
# begin
#     if (y == 0) return x
#     return f(y, x % y)
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     dynamic res <- f(x, y)
#     writeString(res)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(==, Id(y), NumLit(0.0))"
#         self.assertTrue(TestChecker.test(input, expect, 492))
    
#     def test493(self):
#         input = """
# func f(number x, number y)
# begin
#     if (y = 0) return x
#     return f(y, x % y)
# end

# func main()
# begin
#     number x[10]
#     number y[10]
#     var i <- 0
#     for i until i >= 10 by 1
#         x[i] <- readNumber()
    
#     for i until i >= 10 by "Hello"
#         y[i] <- readNumber()
    
# end
# """
#         expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), StringLit(Hello), AssignStmt(ArrayCell(Id(y), [Id(i)]), CallExpr(Id(readNumber), [])))"
#         self.assertTrue(TestChecker.test(input, expect, 493))
    
#     def test494(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [a, b, c]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 494))
    
#     def test495(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x
#     x <- [a, b, [c]]
# end
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
#         self.assertTrue(TestChecker.test(input, expect, 495))
    
#     def test496(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- (a ... b) ... c
#     writeString(x)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 496))
    
#     def test497(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [a, [b, c], [2, 3]]
#     writeNumber(a[0] + a[1] + b + c)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 497))
    
#     def test498(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic x <- [a, [b, c], [2, d]]
#     d <- x[0, 0] + x[0, 1]
#     writeNumber(a[0] + a[1] + b + c + d)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 498))
    
#     def test499(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic x <- [a, [b, c], [d + 20, d ... "Hello"]]
#     d <- x[0, 0] + x[0, 1]
#     writeNumber(a[0] + a[1] + b + c + d)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(..., Id(d), StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 499))
    
#     def test500(self):
#         input = """
# func main()
# begin
#     number arr[2, 2] <- [1, 2, 3, 4]
# end
# """
#         expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 500))
        
#     ############ More testcases from forum ##############
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=7948
#     def test501(self):
#         input = """
#         func f(number x)
# func g() begin
#     return 2
# end
# func f(number y) begin
#     return y
# end
# func main() begin
#     return
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 502))
        
#     def test502(self):
#         input = """
#     func a()
#         return true
#     func main()
#     begin
#         dynamic b <- a
#         dynamic c <- b() 
#     end     
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 503))
    
#     def test503(self):
#         input = """
#         func inc(number a) 
# func main() begin
#     string c <- "hello world" 
#     var x <- inc(3)...c 
# end 
# func inc(number a) return a+1 
#         """
#         expect = "Type Mismatch In Statement: Return(BinaryOp(+, Id(a), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 519))
        
#     def test504(self):
#         input = """
#         func foo()
# begin
#     number x
#     if (x = 1)
#         return true
#     else
#         return 1
# end
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 504))
        
#     def test505(self):
#         input = """
#         func main() begin
#  if (false) var x <- 1
# x <- 1
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 505))
    
#     # This test wrong at AST gen stage
#     def test506(self):
#         input = """
#     func writeNumber(number x) begin
#         return
#     end
#     func main() begin
#     writeNumber(4)
# end
#         """
#         expect = "Redeclared Function: writeNumber"
#         self.assertTrue(TestChecker.test(input, expect, 506))
    
#     def test507(self):
#         input = """
#     func foo(number u) begin
#         return 5
#     end
#         func main() begin
#     number a
#     dynamic x
#     var y <- a + foo(x)
#     x <- 5
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 507))
        
#     def test508(self):
#         input = """
#         func main() begin
#  dynamic x
#  if (x) begin
#     number y <- 1
# end
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 508))
        
#     def test509(self):
#         input = """
#         func main() begin
#  dynamic x
#  for x until true by 1 begin
#     x <- x + 1
# end
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 509))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8428
#     def test510(self):
#         input = """func f(number x, number x)
# func f(number x, number y) begin
#  return x + y
# end
#     func main() begin
#         return
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 510))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8404
#     def test511(self):
#         input = """func main() begin
#         dynamic x
#         x <- (x = 1) or ("abc" == "abc")
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
#         self.assertTrue(TestChecker.test(input, expect, 511))
        
#     def test512(self):
#         input = """func f() return 1
# func main() begin
#  var x <- f
# end
# """
#         expect = "Undeclared Identifier: f"
#         self.assertTrue(TestChecker.test(input, expect, 512))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9576
#     def test513(self):
#         input = """func main() begin
#         var c <- c
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 513))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9576
#     def test514(self):
#         input = """func main() begin
#         dynamic c <- c
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 514))
    
#     def test515(self):
#         input = """func main() begin
#         number a[4] <- [1, true, false, "a"]
#         end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), BooleanLit(False), StringLit(a))"
#         self.assertTrue(TestChecker.test(input, expect, 515))
        
#     def test516(self):
#         input = """func main()
#         """
#         expect = "No Function Definition: main"
#         self.assertTrue(TestChecker.test(input, expect, 516))
        
#     def test517(self):
#         input = """ func x()
#         func main() return
#         """
#         expect = "No Function Definition: x"
#         self.assertTrue(TestChecker.test(input, expect, 517))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9824
#     def test518(self):
#         input = """dynamic a
# func foo() return a
# func main()
# begin
#       number num <- foo()
# end
# """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 518))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5815
#     def test520(self):
#         input = """
# func main()
# begin
#       dynamic a
#       a <- [1, 2, true, false]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 520))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5591
#     def test521(self): 
#         input = """
#         func main() begin
#             number x[1.2]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 521))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5591
#     def test522(self):
#         input = """
#         func f(bool x) begin
#         if (x)
#             return 1
#         end
#         func main() begin
            
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 522))
    
#     def test523(self):
#         input = """
#         func f() begin
#   var input <- readString()
#   return input
# end
#     var x <- f()
#     func main() begin
    
#     end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 523))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8632
#     def test524(self):
#         input = """
#         func hello(number x)
#         begin
#             dynamic a
#             string b[4]
#             dynamic c <- b[a]
#             ## type a is Number
#             bool d <- c == ""
#             bool e <- not a
#         end
#         func main()
#         begin
#             hello(1)
#         end
        
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 524))
        
#     def test525(self):
#         input = """
#         ## Function scope: parameter a
#         func hello(number a)
#         begin
#             ## Block scope: local variables a
#             dynamic a
#         end
#         func main()
#         begin
#             hello(1)
#         end
        
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 525))


#     def test526(self):
#         input = """
#         func hello(number a)
#         begin
#         end
        
#         func main()
#         begin
#             dynamic b
#             hello(b)
#             ## b is Number, because the parameter of hello() is number
#             number c <- b + 1
#         end
        
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 526))


#     def test527(self):
#         input = """
#         func hello(number a)
#         begin
#         end
        
#         func main()
#         begin
#             dynamic a 
#             dynamic b <- [[1,2,3], a]
#             ## a is type number[3]
#             number c <- a[0]
#             number d <- a
#         end
        
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(d), NumberType, None, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 527))
        
#     def test528(self):
#         input = """func main() begin
#         dynamic a
#         dynamic b
#         number x[2,1] <- [[a], [1]]
#         number y[2,2] <- [[1, 2], b]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 528))
        
#     def test529(self):
#         input = """func foo() begin
#             dynamic a
#             return 3
#             return true
#         end
#         func main() begin
        
#         end
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 529))
        
#     def test530(self):
#         input = """func foo() begin
#             dynamic a
#             bool b
#             if (2 = 5) return b
#             else return a
#         end
#         func main() begin
        
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 530))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9664
#     def test531(self): # VAR
#         input = """func foo() 
#         begin
#             dynamic a
#             return a
#         end
#         func main() begin
#             number b <- foo()
#         end
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 531))
        
#     def test532(self):
#         input = """
#         func foo (number i)
#         begin
#             if (i>=0)
#                 return 69 
#         end
#         func main ()
#         begin
#             var i <- foo(10)
#             writeNumber(i)
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 532))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9900
#     def test533(self):
#         input = """func foo(number a, number b)
# func main()
# begin
# 	return 1 + foo(1, "str")
# end
# func foo(number a, number b)
# begin
# 	return 0
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(str)])"
#         self.assertTrue(TestChecker.test(input, expect, 533))
        
#     def test534(self):
#         input = """func foo(number a)
#         func foo(number a, number b) return 0
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 534))
        
#     def test535(self):
#         input = """func foo(number a, number b)
#         func foo(number b) return 0
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 535))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9968
#     # def test536(self):
#     #     input = """func a()
#     #     func main() begin
#     #         number a
#     #         a()
#     #     end
#     #     """
#     #     expect = ""
#     #     self.assertTrue(TestChecker.test(input, expect, 536))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10008
#     # def test537(self):
#     #     input = """
#     #     func foo(number a) return a
#     #     func foo(number a)
#     #     func main() begin
        
#     #     end
#     #     """
#     #     expect = ""
#     #     self.assertTrue(TestChecker.test(input, expect, 537))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10012
# #     def test538(self):
# #         input = """func main()
# # begin 
# #     dynamic a
# #     number x[3,3] <- a[1] 
# # end
# # """
# #         expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayCell(Id(a), [NumLit(1.0)]))"
# #         self.assertTrue(TestChecker.test(input, expect, 538))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10252
#     def test539(self):
#         input = """func main()
# begin
#     number arr[2,2] <- [[1,2],[1,2]]
#     var x <- arr[0,3]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 539))
       
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10132 
#     def test540(self): 
#         input = """
#         func main()
#             begin
#                 dynamic num
#                 bool arr <- num and (num > num)
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
#         self.assertTrue(TestChecker.test(input, expect, 540))
    
#     def test541(self):
#         input = """func foo(number a,number b) begin
#     number a
# end
# func main() return
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 541))
        
#     def test543(self):
#         input = """func foo(number a, number b)
# func foo1()
# begin
# 	return 1 + foo(1, 2)
# end
# func main() begin

# end
# func foo(number a, number b)
# begin
# 	return 0
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 543))
        
#     def test544(self):
#         input = """func main()
#         """
#         expect = "No Function Definition: main"
#         self.assertTrue(TestChecker.test(input, expect, 544))
        
#     def test545(self):
#         input = """
#         func foo() begin
#      dynamic d
#      return d
# end
# func main() return
# """
#         expect = "Type Cannot Be Inferred: Return(Id(d))"
#         self.assertTrue(TestChecker.test(input, expect, 545))
        
#     def test546(self):
#         input = """
#         func main() begin
#             dynamic x
#             dynamic y
#             dynamic z
#             z <- [x, y, 2]
#             dynamic x1
#             dynamic y1
#             number a[2] <- [x1, y1]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 546))
     
#     def test547(self):   
#         input = """string b <- "Hello"
#             var a <- 2.3
#             func foo(number a) begin
#                 return a + 1 - -a
#             end
#             func main ()
#             begin
#                 number x <- 2
#                 var y <- "Bobo"
#                 var z <- 3.4
#                 writeNumber(foo(x))
#             end
#             """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 547))
    
#     def test548(self):
#         input = """
#         func main() begin
#             var x <- [[1, true], [1, 2]]
#         end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 548))
    
#     def test549(self):
#         input = """func main()
# begin
# dynamic a
# var x <- a[0]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 549))
        
#     def test550(self):
#         input = """func foo(number a)
# func foo(string a, bool b) return a
# func main()
# begin 
# end
# """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 550))
        
#     def test551(self):
#         input = """func foo(number a,number b) begin
# number a
# end
# func main() return
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 551))
    
# #     def test552(self):
# #         input = """func foo(number a,number b) begin
# # number a
# # end
# # func main() begin
# #     dynamic a
# #     number b <- a[0]
# # end
# # """
# #         expect = "Type Cannot Be Inferred: VarDecl(Id(b), NumberType, None, ArrayCell(Id(a), [NumLit(0.0)]))"
# #         self.assertTrue(TestChecker.test(input, expect, 552))
    
#     def test553(self):
#         input = """ func func1()
#         func main()
#         begin
#         number a <- func1()
#         end
#         func func2()
#         func func1()
#         begin
#         var b <- func2()
#         return b
#         end
#         func func2() return 1
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, CallExpr(Id(func2), []))"
#         self.assertTrue(TestChecker.test(input, expect, 553))
        
#     def test554(self):
#         input = """func main() begin
#         dynamic b
#         var a <- b + 1
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 554))
        
#     def test555(self):
#         input = """func f()begin
# number c[3,2] <- [[6,7],[4,5],[4,5]]
# return c[2,0]
# end
# func main() begin
# number a <- f() 
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 555))
        
#     def test556(self):
#         input = """func main()
#             func foo()
#             begin
#             number a <- main()
#             end
#             func main() return 
#             """
#         expect = "Type Mismatch In Statement: Return()"
#         self.assertTrue(TestChecker.test(input, expect, 556))
        
#     def test557(self):
#         input = """dynamic a
# dynamic x <- a == (a+2)
# func main() return
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 557))
        
#     def test558(self):
#         input = """func foo( number a, number b[1,2])
# func foo( number a, number b[1,2])
# func main() return
# func foo( number a, number b[1,2])
#      return 1
#      """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 558))
        
#     def test559(self):
#         input = """func main() begin
#             var i <- 1
#             for i until i > 3 by 1
#                 var x <- 1
#             var y <- x
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 559))
        
#     def test560(self):
#         input = """func main() begin
#             if (true) 
#                 var x <- 1
#             var y <- x
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 560))
        
# #     def test561(self):
# #         input = """dynamic a <- [1,2,3]
# # func main() begin
# # number i
# # a[4] <- [2,3]
# # a[i] <- [1,2]
# # end
# #         """
# #         expect = ""
# #         self.assertTrue(TestChecker.test(input, expect, 561))
        
#     def test562(self):
#         input = """func foo()
# begin
#       number a <- 3
# end
# func foo()
# """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 562))
        
#     def test563(self):
#         input = """func foo(number x, string y)
# func foo(number x, number x) 
# begin

# end
# func main() begin

# end
# """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 563))

        

# # -----------------------------------------------------------   
#         #invalid_arrayliteral
        
#     def test_001(self):
#         input = """var a <- [[1,2],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 401))
#     def test_002(self):
#         input = """
#         string b
#         var a <- [[1,2,4],[1,2,3],[b,b,b]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 402))
#     def test_003(self):
#         input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 403))
#     def test_004(self):
#         input = """
#         dynamic t
#         var a <- [[1,2],[1,t],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))
#     def test_005(self):
#         input = """
#         dynamic ans
#         dynamic temp <- "abc"
#         var a <- [[1,2],[1,ans],[temp,ans]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(temp), Id(ans))"
#         self.assertTrue(TestChecker.test(input, expect, 405))
#     def test_006(self):
#         input = """
#         dynamic ans
#         number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 406))
#     def test_007(self):
#         input = """number a[2,3] <- [[2,3],[2,3]]
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 407))
#     def test_008(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2,3] <- [[b,t,d],[c,e,f]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 408))
#     def test_009(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 409))
#     def test_010(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 410))
#     def test011(self):
#         input = """
#     dynamic a
#     dynamic b
#     dynamic c
#     number arr[1, 2,2] <- [[a, b]]
#     ## number c[2, 2] <- arr
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 411))
#     def test012(self):
#         input = """
# dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     var e <- 1
#     var x <- [a, [b], [[c]], [[[d, e]]] ]
#     ##c <- [-10, 2 / 3 % 0.75]
#     ##b <- [c]
#     ##a <- [b]
# """
#         expect = "No Entry Point"
        
#         self.assertTrue(TestChecker.test(input, expect, 412))
#     def test013(self):
#         input = """
# dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic e
#     var x <- [a, [b], [[c]], [[[d, e]]] ]
#     ##c <- [-10, 2 / 3 % 0.75]
#     ##b <- [c]
#     ##a <- [b]
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c))), ArrayLit(ArrayLit(ArrayLit(Id(d), Id(e))))))"
#         self.assertTrue(TestChecker.test(input, expect, 413)) 
#     def test014(self):
#         input = """
#         func b()
#         dynamic b
#         number a[2,3]<- [[b(),b,b],[b,b,b()]]
#         func b()
#         return true
#         """
#         result="Type Mismatch In Statement: Return(BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input,result,414))
#     def test015(self):
#         input ="""
#         func main()
#         begin
#         number a <- [a,a,a,a,a]
#         end
#         """
#         expect="Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(a), Id(a), Id(a), Id(a), Id(a)))"
#         self.assertTrue(TestChecker.test(input,expect,415))
#     def test016(self):
#         input ="""
#         func a()
#         number a
#         func main()
#         begin
#             number a[5] <- [a(),2,3,4,5]
#         end
#         func a()
#             return
#     """
#         expect="Type Mismatch In Statement: Return()"
#         self.assertTrue(TestChecker.test(input,expect,416))
#     def test017(self):
#         input="""
#         dynamic a
#         var c <-[a,[a],[[a,a,a]]]
#         """
#         expect="Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(Id(a)), ArrayLit(ArrayLit(Id(a), Id(a), Id(a))))"
#         self.assertTrue(TestChecker.test(input,expect,417))
#     def test018(self):
#         input="""
#         dynamic a
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         var g <-[a,[b],[[c,d,e]]]
#         """
#         expect="Type Cannot Be Inferred: VarDecl(Id(g), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c), Id(d), Id(e)))))"
#         self.assertTrue(TestChecker.test(input,expect,418))
#     def test019(self):
#         input="""
       
        
       
#         number d
#         var c <-[c,c,c,c,d]   ## visit bien truoc roi moi visit init value
#         """
#         expect="Type Mismatch In Statement: VarDecl(Id(c), None, var, ArrayLit(Id(c), Id(c), Id(c), Id(c), Id(d)))"
#         self.assertTrue(TestChecker.test(input,expect,419))
#     def test020(self):
#         input="""
#         dynamic a
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         string g[6,99,100,101] <-[a,b,c,d,e,f]
#         """
#         expect="No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,420))
#     ###test func_para
#     def test021(self):
#         input="""
#         func a1(number a,number b, number c)
#         func main()
#         begin
#             number a <- 1
#             a1(1,2,3)
#         end
#         func a(number a,number b, number c)
#         begin
#             a<-a1(a,b,c)
#             return "lo ve du"
#         end
#         """
#         expect="Type Mismatch In Expression: CallExpr(Id(a1), [Id(a), Id(b), Id(c)])"
#         self.assertTrue(TestChecker.test(input,expect,421))
        
#     def test022(self):
#         input="""
#         func a(number a,number b, number b)
#         func main()
#         return 0
#         """
#         expect="No Function Definition: a"
#         self.assertTrue(TestChecker.test(input,expect,422))
#     def test023(self):
#         input="""
#         func test()
#         func main()
#         begin
#             number a[2,3]<- test()
#         end
#         func test()
#         begin
#             begin
#                 begin
#                     begin
#                         return 1
#                     end
#                 end
#             end
#         end
#         """
#         expect="Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input,expect,423))
#     def test024(self):
#         input="""
#         func test(number a[2,3])

#         func main()
#         begin
#             number a[2,3]<- test(test(a))
#         end
#         """
#         expect="No Function Definition: test"
#         self.assertTrue(TestChecker.test(input,expect,424))
#     def test025(self):
#         input="""
#         func test(number a, string b)
#         func main()
#             begin
#             dynamic a
#             dynamic b
#                 a <-test(test(a,b),test(a,b))
#             end
        
#         """
#         expect="Type Mismatch In Expression: CallExpr(Id(test), [CallExpr(Id(test), [Id(a), Id(b)]), CallExpr(Id(test), [Id(a), Id(b)])])"
#         self.assertTrue(TestChecker.test(input,expect,425))
 
#     def test027(self):
#         input="""
#         func hehe()
#         func main()
#         begin
#             number a[2,3]
#             a[hehe(),hehe()]<-hehe()
#             a[hehe()]<-[hehe(),hehe(),hehe()]
            
#         end
#         func hehe()
#         begin
#             begin
#             end
#         end
#         """
#         expect="Type Mismatch In Statement: Block([Block([])])"
#         self.assertTrue(TestChecker.test(input,expect,427))
#     def test028(self):
#         input="""
#         func hehe(number a, number b)
#         func main()
#         begin
#             number a[2,3]
#             a[hehe(1,2),hehe(1,2)]<-hehe(1,2)
#             a[hehe(1,2)]<-[hehe(1,2),hehe(1,2),hehe(1,2)]
            
#         end
#         func hehe1(number a, number b)
#         func hehe(number hehe1,number hehe)
#         begin
#             hehe<-hehe1(hehe,hehe)
#             hehe1<-hehe1(hehe1,hehe1(hehe1,hehe1))+hehe(hehe1,hehe1(hehe1,hehe))
        
#         end
#         """
#         expect="Type Mismatch In Statement: Block([AssignStmt(Id(hehe), CallExpr(Id(hehe1), [Id(hehe), Id(hehe)])), AssignStmt(Id(hehe1), BinaryOp(+, CallExpr(Id(hehe1), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe1)])]), CallExpr(Id(hehe), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe)])])))])"
#         self.assertTrue(TestChecker.test(input,expect,428))
#     def test029(self):
#         input="""
#         func hehe()
#         func hehe1()
#         func main()
#         begin
#             number a[2,3]
#             a[hehe(),hehe()]<-hehe()
#             a[hehe()]<-[hehe(),hehe(),hehe()]
            
#         end
#         func hehe()
#         begin
#             return 1
#         end
#         """
#         expect="No Function Definition: hehe1"
#         self.assertTrue(TestChecker.test(input,expect,429))
#     def test030(self):
#         input="""
#         func hehe()
#         func hehe1()
#         func main()
#         begin
#             number a[2,3]
#             a[hehe(),hehe()]<-hehe()
#             a[hehe()]<-[hehe(),hehe(),hehe()]
            
#         end
#         func hehe(number hehe1, string hehe, number hehe2)
#         begin
#             hehe<- hehe...hehe
#             return hehe1
#         end
#         """
#         expect="Redeclared Function: hehe"
#         self.assertTrue(TestChecker.test(input,expect,430))
#     # test func_decl:10
#     def test031(self):
#         input="""
#         func hehe()
#         func hehe1(number a, number b)
#         func main()
#         return 0
#         func hehe1(number c, number d)
#         begin
#         end
        
#         """
#         expect="No Function Definition: hehe"
#         self.assertTrue(TestChecker.test(input,expect,431))
#     def test032(self):
#         input="""
       
#         func hehe1(number a, number b)
#         begin
#             number c[2,3]
#             begin 
#                 number a <- 1
#             end
#             number a <- a
#         end
#         func main()
#             return 0
        
#         """
#         expect="No Entry Point"
#         self.assertTrue(TestChecker.test(input,expect,432))
#     def test033(self):
#         input="""
#         func hehe1(number a, number b, number c[1,2,3])
#         begin
#             dynamic t
#             dynamic hehe1 <- [c,t]
#             return hehe1
#         end
        
#         func main()
#         begin
#             dynamic a
#             hehe1(1,1,a)
#         end
        
#         """
#         expect="Type Mismatch In Statement: CallStmt(Id(hehe1), [NumLit(1.0), NumLit(1.0), Id(a)])"
#         self.assertTrue(TestChecker.test(input,expect,433))
#     def test034(self):
#         input="""
#         func hehe()
#         func hehe(number a)
#         func main()
#         return 0
#         """
#         expect="Redeclared Function: hehe"
#         self.assertTrue(TestChecker.test(input,expect,434))
#     def test035(self):
#         input="""
#         func hehe(number a)
#         func hehe1(number a)
#         return true
        
#         func main()
#         return 3
#         func hehe(number t)
#         return t
#         func hehe1(number t)
#         return t
#         """
#         expect="Redeclared Function: hehe1"
#         self.assertTrue(TestChecker.test(input,expect,435))
#     def test036(self):
#         input="""
#         func test1()
#         func test2()
#         func test3()
#         func test(number test1, string test2, bool test3)
#         begin
#             return (test1 > test1()) and (test2 == test2()) or (test3 and test3())
#         end
#         func main()
#         begin
#             return test(1,"abc",true)
#         end

#         """
#         expect="No Function Definition: test1"
#         self.assertTrue(TestChecker.test(input,expect,436))
#     def test037(self):
#         input="""
#         func test()
#         return true
#         func main()
#         begin
#             string t[2,3]
#             dynamic a <- t[test(),test()]
#         end
#         """
#         expect="Type Mismatch In Expression: ArrayCell(Id(t), [CallExpr(Id(test), []), CallExpr(Id(test), [])])"
#         self.assertTrue(TestChecker.test(input,expect,437))
#     def test038(self):
#         input="""
#         func happy()
#         return 2
#         func happy()
#         return 1
#         func main()
#         return 0
#         """
#         expect="Redeclared Function: happy"
#         self.assertTrue(TestChecker.test(input,expect,438))
#     def test039(self):
#         input="""
#         func happy(string a, string b)
#         begin
#             a <- "Vi ngay em dep nhat"
#             b <- "La ngay anh mat em"
#             return a ... b
#         end
#         func main()
#         begin
#             dynamic a <- "Hen em kiep sau"
#             dynamic b <- "Kiep nay thoi tim den nhau"
#             happy()
#         end
#         return 0
#         """
#         expect="Type Mismatch In Statement: CallStmt(Id(happy), [])"
#         self.assertTrue(TestChecker.test(input,expect,439))
#     def test040(self):
#         input="""
#         func happy()
#         number a <- happy()
#         func happy()
#         return 1
        

#         func main()
#         begin
#             string a <- "Tu nay duyen kiep bo lai phia sau, troi nhu muon khoc ngay minh mat nhau"
#             a <- happy()
            
#         end
#         """
#         expect="Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(happy), []))"
#         self.assertTrue(TestChecker.test(input,expect,440))
#     # test Expression: 20
#     def test041(self):
#         input="""
#         func main(number a, number b)
#         begin
#             dynamic d
#             dynamic c
#             bool e <- (d...c == c ) and (a > b) or (a < b)
#         end
#         func main()
#         """
#         expect="Type Mismatch In Expression: BinaryOp(..., Id(d), BinaryOp(==, Id(c), Id(c)))"
#         self.assertTrue(TestChecker.test(input,expect,441))
#     def test042(self):
#         input="""
#         func main()
#         begin
#             number a <- 1
#             number b <- 2
#             bool c <- a > b
#             bool d <- a < b
#             bool e <- a == b
#             bool f <- a != b
#             bool g <- a >= b
#             bool h <- a <= b
#         end
#         """
#         expect="Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input,expect,442))
#     def test043(self):
#         input="""
#         func test(number a, number b)
#         begin
#             dynamic c <- a + b > a - b and ((c ... "tam biet e nhe") == "hehe")
#         end
#         """
#         expect="Type Mismatch In Expression: BinaryOp(and, BinaryOp(-, Id(a), Id(b)), BinaryOp(==, BinaryOp(..., Id(c), StringLit(tam biet e nhe)), StringLit(hehe)))"
#         self.assertTrue(TestChecker.test(input,expect,443))
#     def test044(self):
#         input="""
#         func hehe()
#         func test(number a, number b)
#         begin
#             number t[2,3]<- hehe()
#         end
#         func hehe()
#         begin
#         number a [2,4]
#         return a 
#         end
#         """
#         expect="Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,444))
#     def test045(self):
#         input="""
#         func test(number a, number b)
#         begin
#             dynamic c <- a + b > a - b and ((c ... "tam biet e nhe") == "hehe")
#         end
#         """
#         expect="Type Mismatch In Expression: BinaryOp(and, BinaryOp(-, Id(a), Id(b)), BinaryOp(==, BinaryOp(..., Id(c), StringLit(tam biet e nhe)), StringLit(hehe)))"
#         self.assertTrue(TestChecker.test(input,expect,445))


#     def test048(self):
#         input="""
#         func test()
#         func main()
#         begin
#             dynamic a
#             for a until a < test() by test()
#                 begin
#                 end
#         end
#         func test()
#         begin
#             dynamic a
#             a <- [1,2,3]
#             return a
#         end
#         """
#         expect="Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,448))
#     def test049(self):
#         input="""
#         func test(number a[2,3], number  a[2,3])
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             test([[a,a,a],[1,2,3]], [[b,b,b],[b,b,b]])
#         end
#         func test(number a[2,3], number b[2,3])
#         begin
#             return a
#         end
#         """
#         expect = "Type Mismatch In Statement: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,449))

#     def test051(self):
#         input="""
#         func test()
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             number c <-  (a - 3) > (not test() or a)
#         end
#         """
#         expect= "Type Mismatch In Expression: BinaryOp(or, UnaryOp(not, CallExpr(Id(test), [])), Id(a))"
#     def test052(self):
#         input="""
#         func test()
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             number c <-  (a - 3) > (not test() or a)
#         end
#         """
#         expect= "Type Mismatch In Expression: BinaryOp(or, UnaryOp(not, CallExpr(Id(test), [])), Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,452))


#     def test055(self):
#         input="""
#         func test1(number a)
#         func test2(number a)
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             number c <-test1(test1(test1(test1([a])))) + test2(b)
#         end
#         """
#         expect="Type Cannot Be Inferred: VarDecl(Id(c), NumberType, None, BinaryOp(+, CallExpr(Id(test1), [CallExpr(Id(test1), [CallExpr(Id(test1), [CallExpr(Id(test1), [ArrayLit(Id(a))])])])]), CallExpr(Id(test2), [Id(b)])))"
#         self.assertTrue(TestChecker.test(input,expect,455))

#     def test057(self):
#         input="""
#         dynamic c
#         func test()
#         begin 
#             number a <- c
#         end
#         func main()
#         begin
#             dynamic c
#             c <- "hello"
#             begin
#                 dynamic c
#                 c <- 1
#             end
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,457))
#     def test058(self):
#         input="""
#         dynamic c
#         func test()
#         begin
#             number a <- c
#         end
#         func main()
#         begin
#             dynamic c
#             c <- "hello"
#             begin
#                 c <- 1
#             end
#         end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(c), NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input,expect,458))

    
#     ##test break,cont: 10
    

#     def test062(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#             begin
#                 break 
#                 break
#                 break
#             end
#         end
#         """
#         expect=""
#         self.assertTrue(TestChecker.test(input,expect,462))
#     def test063(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#             begin
#                 continue
#                 continue
#                 continue
#             end
#         end
#         """
#         expect=""
#         self.assertTrue(TestChecker.test(input,expect,463))
#     def test064(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#             begin
#                 for a until a < 10 by 1
#                 begin
#                     break
#                     break
#                     break
#                 end
#                 continue 
#                 continue 
#                 continue
#             end
#             break
#         end
#         """
#         expect="Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,464))
#     def test065(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#             begin
#                 for a until a < 10 by 1
#                 begin
#                     break
#                     break
#                     break
#                 end
#                 if (a = 5) break
#                 elif (a=6) continue
#                 else break
#             end
#         end
#         """
#         expect=""
#         self.assertTrue(TestChecker.test(input,expect,465))
#     def test066(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#             begin
#                 for a until a < 10 by 1
#                 begin
#                     break
#                     break
#                     break
#                 end
#                 if (a = 5) break
#                 elif (a=6) continue
#                 else break
#                 break
#                 break
#             end
#         end
#         """
#         expect=""
#         self.assertTrue(TestChecker.test(input,expect,466))
#     def test067(self):
#         input ="""
#         func main()
#         begin
#             break
#         end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,467))
#     def test068(self):
#         input="""
#         func main()
#         begin
#             continue
#         end
#         """
#         expect="Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,468))
#     def test069(self):
#         input="""
#         func main()
#         begin
#             begin
#                 break
#             end
#         end
#         """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input,expect,469))
#     ###test if,for,CallStmt: 10
#     def test070(self):
#         input="""
#         dynamic a
#         func main()
#         begin
#             if (a) a<-1
#         end
#         """
#         expect="Type Mismatch In Statement: AssignStmt(Id(a), NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input,expect,470))
#     # def test071(self):
#     #     input="""
#     #     func test()
#     #     begin
#     #         dynamic a
#     #         if (1=2) return 1
#     #         else return a
#     #     end
#     #     func main()
#     #     begin
#     #         test()
#     #     end
#     #     """
#     #     expect="Type Cannot Be Inferred: Return(Id(a))"
#     #     self.assertTrue(TestChecker.test(input,expect,471))

#     def test073(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by a[2]
#             begin
#                 if (a == 5) return 1
#                 else
#                     return 2
#             end
#         end
#         """
#         expect="Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input,expect,473))
#     def test074(self):
#         input="""
#         func main()
#         begin
#             dynamic b
#             dynamic a
#             for a until a < 10 by b[2]
#             begin
#                 if (a == 5) return 1
#                 else
#                     return 2
#             end
#         end
#         """
#         expect = "Type Cannot Be Inferred: For(Id(a), BinaryOp(<, Id(a), NumLit(10.0)), ArrayCell(Id(b), [NumLit(2.0)]), Block([If((BinaryOp(==, Id(a), NumLit(5.0)), Return(NumLit(1.0))), [], Return(NumLit(2.0)))]))"
#         self.assertTrue(TestChecker.test(input,expect,474))
#     def test075(self):
#         input="""
#         func test()
#         begin
#             dynamic a
#             for a until a < 10 by 1
#                 return 1
#             return a
#         end
#         func main()
#         begin
#             bool a<- test()
#         end
#         """
#         expect="Type Mismatch In Statement: VarDecl(Id(a), BoolType, None, CallExpr(Id(test), []))"
#         self.assertTrue(TestChecker.test(input,expect,475))
#     def test076(self):
#         input="""
#         func test()
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by test()
#                 return 1
#             return a
#         end
#         func test()
#         return true
#         """
#         expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input,expect,476))
#     def test077(self):
#         input="""
#         func main()
#         begin
#             test()
#         end
#         """
#         expect="Undeclared Function: test"
#         self.assertTrue(TestChecker.test(input,expect,477))
#     def test078(self):
#         input="""
#         func test()
#         func main()
#         begin
#             test()
#             number a <- test()+2
#         end
#         func test()
#         return 2
#         """
#         expect="Type Mismatch In Expression: CallExpr(Id(test), [])"
#         self.assertTrue(TestChecker.test(input,expect,478))
#     def test079(self):
#         input="""
#         func test()
#         func main()
#         begin
#             dynamic a
#             for a until a < 10 by test()
#                 begin
#                     test()
#                 end
#         end
#         func test()
#         return 2
#         """
#         expect="Type Mismatch In Statement: CallStmt(Id(test), [])"
#         self.assertTrue(TestChecker.test(input,expect,479))



#     def test080(self):
#         input="""
#         func test(number a)
#         func main()
#         begin
#             dynamic b
#             for b until b < 10 by 1
#             begin
#                 return
#             end
#             dynamic a
#             a <- test(1)+ test(a[1])
#         end
#         func test(number a)
#         return 1
#         """
#         expect="Type Cannot Be Inferred: AssignStmt(Id(a), BinaryOp(+, CallExpr(Id(test), [NumLit(1.0)]), CallExpr(Id(test), [ArrayCell(Id(a), [NumLit(1.0)])])))"
#         self.assertTrue(TestChecker.test(input,expect,480))
    
#     def test072(self):
#         input="""
#         func test()
#         begin
#             dynamic a
#             if (1=2) return a
#             else return 1
#         end
#         func main()
#         begin
#             test()
#         end
#         """
#         expect="Type Mismatch In Statement: CallStmt(Id(test), [])"
#         self.assertTrue(TestChecker.test(input,expect,472))
        
#     def test061(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             for a until a < 10 by 1
#             begin
#                 if (true) continue
#                 else
#                     break
#             end
#         end
#         """
#         expect=""
#         self.assertTrue(TestChecker.test(input,expect,461))
        
#     def test059(self):
#         input="""
#         func main()
#         begin
#             dynamic x
#             number a[2,2]<-[x,[x,x]]
#         end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
#         self.assertTrue(TestChecker.test(input,expect,459))
        
#     def test056(self):
#         input="""
#         func test1(number a)
#         func test2(number b)
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             dynamic c
#             c[2] <-test1(test1(test1(test1(a)))) + test2(b) + 1 
#         end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(c), [NumLit(2.0)]), BinaryOp(+, BinaryOp(+, CallExpr(Id(test1), [CallExpr(Id(test1), [CallExpr(Id(test1), [CallExpr(Id(test1), [Id(a)])])])]), CallExpr(Id(test2), [Id(b)])), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input,expect,456))
    
#     def test054(self):
#         input="""
#         func test1(number a)
#         func test2(number a)
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             number c <- test1([a]) + test2(b)
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), NumberType, None, BinaryOp(+, CallExpr(Id(test1), [ArrayLit(Id(a))]), CallExpr(Id(test2), [Id(b)])))"
#         self.assertTrue(TestChecker.test(input,expect,454))
        
#     # def test050(self):
#     #     input="""
#     #     func test(number a[2,3], number  b[2,3])
#     #     func main()
#     #     begin
#     #         dynamic a
#     #         dynamic b
#     #         test(test([[a,a,a],[1,2,3]],[[1,2,3],[1,2,3]]), [[b,b,b],[b,b,b]])
#     #     end
#     #     func test(number a[2,3], number b[2,3])
#     #     begin
#     #         return b
#     #     end
#     #     """
#     #     expect = "Type Mismatch In Expression: CallExpr(Id(test), [ArrayLit(ArrayLit(Id(a), Id(a), Id(a)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])"
#     #     self.assertTrue(TestChecker.test(input,expect,450))
        
#     def test047(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             var c <- a == a + 2
#         end
            
#         """
#         expect="Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input,expect,447))
        
#     def test046(self):
#         input="""
#         dynamic a
#         dynamic c
#         var b <- [a,[a,a]]
        
#         ##  [a,[a,a],[[a,a,a]]] [c,[a,a]] [a,[a,a]]  [[c,c,c],[a,a]]
#         """
#         expect="Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(Id(a), Id(a)))"
#         self.assertTrue(TestChecker.test(input,expect,446))

#     def test026(self):
#         input="""
#         func hehe()
#         func main()
#         begin
#             number a[2,3]
#             a[hehe(),hehe()]<-hehe()
#             a[hehe()]<-[hehe(),hehe(),hehe()]
#             a[hehe()]<-[hehe(),hehe(),hehe(),hehe()]
#         end
#         """
#         expect="Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [CallExpr(Id(hehe), [])]), ArrayLit(CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), [])))"
#         self.assertTrue(TestChecker.test(input,expect,426))

#     def test96(self): 
#         input = """
#             func main()
#             begin
#                 dynamic a
#                 dynamic b
#                 var c <- [a, [a, a]]
#             end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(Id(a), Id(a)))"
#         self.assertTrue(TestChecker.test(input, expect, 203))

#     def test555(self):
#         input = """

#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic e
#     number arr[2, 2] <- [[a, b]]
#     ## number c[2, 2] <- arr

# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
#         self.assertTrue(TestChecker.test(input, expect, 555))
        
#     def test053(self):
#         input="""
#         func main()
#         begin
#             dynamic a
#             dynamic b
#             number c[2,3]<-[[a,a,a],[b,b]]
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(a), Id(a)), ArrayLit(Id(b), Id(b))))"
#         self.assertTrue(TestChecker.test(input,expect,453))

    def test_array1(self):
        input="""
            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                a <- [[c,c,c], [b,b]]
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(c), Id(c), Id(c)), ArrayLit(Id(b), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 1000))
    def test_array2(self):
        input="""
            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                a <- [b, [c,b]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(b), ArrayLit(Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 1002))
    def test_array3(self):
        input="""
            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                a <- [[b,b,b], [c,b]]
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(b), Id(b), Id(b)), ArrayLit(Id(b), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 1003))
    def test_array4(self):
        input="""
            func main()
            begin
                dynamic b
                dynamic c
                number a[3,2,2]
                a <- [c, [b,b], [[1,2],[1,2]]]
                c <- [[2,3],[2,3]]
                b <- [4,5]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1004))
        
    def test_array5(self):
        input="""
            func foo(number a[2,3],number a[2,3])
            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                foo(a,[b,[b,b]])
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(b), ArrayLit(Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 1005))

    def test_array6(self):
        input="""
            func foo(number a[2,3],number x[2,3])
            begin
                dynamic a
                if (1 = 2) return 1
                elif (1 = 2) return a
                else return a
            end 
            func main()
            begin
                dynamic b
                dynamic c
                number a[2,3]
                number x <- foo(a, c)
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 1006))
    
   