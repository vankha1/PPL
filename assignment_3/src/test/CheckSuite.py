import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    # def test_no_entry_point(self):
    #     input = """number a
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    
    # def test_no_entry_point_2(self):
    #     input = """func b() 
    #         begin
    #         end
    #     """
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    
    # def test_no_entry_point_3(self):
    #     input = """func main() 
    #         begin
    #             return 1
    #         end
    #     """
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    
    # def test_no_entry_point_4(self):
    #     input = """func main() 
    #         begin
    #             return
    #         end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    
    # def test_no_entry_point_5(self):
    #     input = """func bkool()
    #         begin
    #             return true
    #         end
    #     """
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    
    # def test_redecl_var_1(self):
    #     input = """func main()
    #         begin
    #             number a
    #             string a
    #         end
    #         """
    #     expect = """Redeclared Variable: Id(a)"""
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    
    # def test_redecl_var_2(self):
    #     input = """func main()
    #         begin
    #             number a
    #             number b
    #             string c
    #             bool b
    #         end
    #         """
    #     expect = """Redeclared Variable: Id(b)"""
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    
    # def test_redecl_var_3(self):
    #     input = """ number a
    #         func main()
    #         begin
    #             string a
    #             return
    #         end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    
    # def test_redecl_var_4(self):
    #     input = """ number a
    #         func main()
    #         begin
    #             number a
    #             begin
    #                 string a
    #             end
    #         end
    #         """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    
    # def test_redecl_var_5(self):
    #     input = """ number a
    #         number b
    #         func main()
    #         begin
    #             number a
    #         end
    #             number b
    #         """
    #     expect = """Redeclared Variable: Id(b)"""
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_redecl_var_6(self):
    #     input = """func main() 
    #         begin 
    #         end
    #         func c() 
    #         begin 
    #         end
    #         number c
    #         """
    #     expect = """Redeclared Variable: Id(c)"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # def test_redecl_func_1(self):
    #     input = """func main() begin
    #         end
    #          number c
    #         func c() begin
    #         end
    #         """
    #     expect = """Redeclared Function: Id(c)"""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    
    # def test_redecl_func_2(self):
    #     input = """func main() begin 
    #     end
    #         func c() begin 
    #         end
    #         func c() begin 
    #         end
    #         """
    #     expect = """Redeclared Function: Id(c)"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))
   
    # def test_redecl_func_3(self):
    #     input = """func main()
    #     begin
    #         number main
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 413))
    
    # def test_redecl_func_4(self):
    #     input = """func main()
    #         begin
    #         end
    #         func foo (number a)
    #         begin
    #             bool a
    #         end
    #         """
    #     expect = """Redeclared Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 414))
    
    # def test_redecl_func_5(self):
    #     input = """func main() 
    #         begin
    #         end
    #         func foo(number a) 
    #         begin
    #         end
    #         string a
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    
    # def test_redecl_param_1(self):
    #     input = """func main() 
    #         begin
    #         end
    #         func foo (number a, string a)
    #         begin
    #         end
    #         """
    #     expect = """Redeclared Parameter: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 416))
    
    # def test_redecl_param_2(self):
    #     input = """func main() 
    #         begin
    #         end
    #         func foo (number foo)
    #         begin
    #         end
    #         """
    #     expect = """Redeclared Parameter: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 417))
    
    # def test_redecl_param_3(self):
    #     input = """func main() 
    #         begin
    #         end
    #         func foo(number main)
    #         begin
    #         end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 418))
    
    # def test_redecl_param_4(self):
    #     input = """func main()
    #         begin
    #         end
    #         func foo (number a)
    #         begin
    #         end
    #         func a (number foo)
    #         begin
    #         end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 419))
    
    # def test_undecl_var_1(self):
    #     input = """func main()
    #     begin
    #         a <- 2
    #         return
    #     end
    #         """
    #     expect = """Undeclared Identifier: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 420))
    
    # def test_undecl_var_2(self):
    #     input = """number a
    #     func main()
    #     begin
    #         a <- 2
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 421))
    
    # def test_undecl_var_3(self):
    #     input = """func main()
    #     begin
    #         var a <- 2
    #         var b <- a + 2
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 422))
    
    # def test_undecl_var_4(self):
    #     input = """func main()
    #     begin
    #         begin
    #             number a
    #         end
    #         a <- 2
    #     end
    #         """
    #     expect = """Undeclared Identifier: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 423))
    
    # def test_undecl_var_5(self):
    #     input = """func main() 
    #                 begin 
    #                 end
    #         func foo(number a)
    #         begin
    #             a <- 2
    #         end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 424))
    
    # def test_undecl_func_1(self):
    #     input = """
    #     func check()
    #     begin
    #     end
    #     func main()
    #     begin
    #         foo()
    #     end
    #         """
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 425))
    
    # def test_undecl_func_2(self):
    #     input = """func main()
    #     begin
    #         number a
    #         a <- foo() + 5
    #     end
    #         """
    #     expect = """Undeclared Function: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 426))
    
    # def test_undecl_func_3(self):
    #     """forward invocation"""
    #     input = """
    #     func foo()
    #     begin
    #         return 1
    #     end
        
    #     func check()
    #     begin
    #         return 2
    #     end
        
    #     func main()
    #     begin
    #         number a
    #         begin
    #             a <- foo() + 5
    #         end
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 427))
    
    # def test_undecl_func_4(self):
    #     """backward invocation"""
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         number a
    #         a <- foo() + 5
    #     end
    #     func foo()
    #     begin
    #        return 1
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 428))
    
    # def test_undecl_func_5(self):
    #     """backward inheritance"""
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         number a
    #         a <- foo() + 5
    #     end
        
    #     func foo()
    #     begin
    #         barrr()
    #         return 1
    #     end
        
    #     func bar()
    #     begin
    #         return 2
    #     end
    #         """
    #     expect = """Undeclared Function: barrr"""
    #     self.assertTrue(TestChecker.test(input, expect, 429))
    
    # def test_tmme_a1(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[5]
    #         number b
    #         b <- a[5]
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 430))
    
    # def test_tmme_a2(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         number b
    #         b <- a[5]
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(5.0)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 431))
    
    # def test_tmme_a3(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[5, 5]
    #         number b
    #         b <- a[1.0,"1"]
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), StringLit(1)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 432))
    
    # def test_tmme_b1_implicit(self):
    #     input = """
    #     func main()
    #     begin
    #         number a 
    #         string b
    #         ## a + b: Unknown a: number
    #         a <- a + b
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"""
    #     self.assertTrue(TestChecker.test(input, expect, 433))
    
    # def test_tmme_b2_implicit(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         number b
    #         ## number -> number:OK
    #         b <- a
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 434))
    
    # def test_tmme_b3_implicit(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 1
    #         number b <- a + 2
    #         string c <- 2.3
    #     end
    #         """
    #     expect = """Type Cannot Be Inferred: VarDecl(Id(c), StringType, None, NumLit(2.3))"""
    #     self.assertTrue(TestChecker.test(input, expect, 435))
    
    # def test_tmme_b4_unary(self):
    #     input = """
    #     func main()
    #     begin
    #         string a
    #         a <- -a
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: UnaryOp(-, Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 436))
    
    # def test_tmme_b5_unary(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         a <- not a
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: UnaryOp(not, Id(a))"""
    #     self.assertTrue(TestChecker.test(input, expect, 437))
    
    # def test_tmme_b6_binary(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         a <- 1
    #         dynamic c
    #         c <- a + b
    #     end
    #         """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 438)) 
    
    # def test_tmme_b7_binary(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         number b
    #         number c
    #         string d 
    #         string e 
    #         d <- d ... e ## valid
    #         b <- a % c ## valid
    #         a <- a == b ## invalid: a == b
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
    #     self.assertTrue(TestChecker.test(input, expect, 439))
    
    # def test_tmme_b8_binary(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         bool b
    #         bool c
    #         b <- (b and c) or c ## valid
    #         b <- a and b ## invalid: a and b
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: BinaryOp(and, Id(a), Id(b))"""
    #     self.assertTrue(TestChecker.test(input, expect, 440))
        
    # def test_4009(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic x 
    #         x  <- (x - 2) * (x + true)
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 4009))
    
    # def test_tmme_b9_binary(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         number b
    #         bool c
    #         bool d
    #         number e
    #         c <- b > e
    #         c <- e <= b
    #         d <- b == e ## invalid: b==e
    #     end
    #         """
    #     expect = "Type Mismatch In Expression: BinaryOp(==, Id(b), Id(e))"
    #     self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_tmme_c1_void_CallExpr(self):
        input = """
        func foo()
        func main()
        begin
            number a <- 2
            a <- foo() + 2
        end
        func foo()
        begin
            return
        end
            """
        expect = """Type mismatch in expression: CallExpr(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    # def test_tmme_c2_param_typ(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 2
    #         string b <- "2.1"
    #         a <- foo(b,a) + 2
    #     end
    #     func foo(number a, string b)
    #     begin
    #         return a+b
    #     end
    #         """
    #     expect = """Type mismatch in expression: CallExpr(foo, [Id(b), Id(a)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 443))
    
    # def test_tmme_c3_param_len(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 2
    #         number b <- 2.1
    #         a <- foo(a,b) + 2
    #     end
    #     func foo(number a, number b, number c)
    #     begin
    #         return a+b+c
    #     end
    #         """
    #     expect = """Type mismatch in expression: CallExpr(foo, [Id(a), Id(b)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 444))
    
    # def test_ial_1(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[5]
    #         a <- [1,"2.0"]
    #     end
    #         """
    #     expect = """Illegal array literal: ArrayLit([NumberLiteral(1), StringLiteral(2.0)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 445))
    
    # def test_ial_2(self):
    #     input = """
    #     number b1
    #     func main()
    #     begin
    #         bool a[5]
    #         bool b1 
    #         bool b2
    #         a <- [b1,b2]
    #     end
    #         """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 446))
        
    # def test_ial_3(self):
    #     input = """
    #     string a[5]
    #     func main()
    #     begin
    #         number i1 <- 25
    #         number f2 <- 25.0
    #         a <- [i1,f2]
    #     end
    #         """
    #     expect = """Illegal array literal: ArrayLit([Id(i1), Id(f2)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 447))
    
    # def test_ial_4(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[5, 5]
    #         a <- [[1,2],[1,2,3],[1,2,"3"]]
    #     end
    #         """
    #     expect = """Illegal array literal: ArrayLit([ArrayLit([NumberLiteral(1), NumberLiteral(2)]), ArrayLit([NumberLiteral(1), NumberLiteral(2), NumberLiteral(3)]), ArrayLit([NumberLiteral(1), NumberLiteral(2), StringLit(3)])])"""
    #     self.assertTrue(TestChecker.test(input, expect, 448))
        
    # def test_ial_5(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[5]
    #         string s
    #         a[3] <- 2.5
    #         a[2] <- 5
    #         a[1] <- s
    #     end
    #         """
    #     expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [numberLit(1)]), Id(s))"""
    #     self.assertTrue(TestChecker.test(input, expect, 449))
        
    # def test_tmms_condexpr_1(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b
    #         number i
    #         if(b){}
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 450))
    
    # # def test_tmms_condexpr_2(self):
    # #     input = """
    # #     func main()
    # #         bool b
    # #         i: number
    # #         while(i){}
    # #         if(b){}
    # #         do{}while(b)
    # #     }
    # #         """
    # #     expect = """Type mismatch in statement: WhileStmt(Id(i), BlockStmt([]))"""
    # #     self.assertTrue(TestChecker.test(input, expect, 451))
    
    # def test_tmms_condexpr_3(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b1
    #         bool b2
    #         number i1
    #         number i2
    #         if(i1 = i2) begin end
    #         if(i1) begin end
    #         if(b1) begin end
    #     end
    #         """
    #     expect = """Type mismatch in statement: If(Id(i1), Block([]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 452))
    
    # def test_tmms_condexpr_4(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b1
    #         bool b2
    #         number i
    #         if (b1 and b2) begin end
    #         if(b1 or b2) begin end
    #         if (i) begin end
    #     end
    #         """
    #     expect = """Type mismatch in statement: If(Id(i), BlockStmt([]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 453))
    
    # def test_tmms_forexpr_1(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b
    #         var i <- 0
    #         for i until i<10 by i+1
    #         begin
    #         end
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 454))
    
    # def test_tmms_forexpr_2(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b <- true
    #         number i
    #         for b until i<10 by i*2
    #         begin
    #         end
    #     end
    #         """
    #     expect = """Type mismatch in statement: ForStmt(Id(b), BinExpr(<, Id(i), NumberLiteral(10)), BinExpr(*, Id(i), NumberLiteral(2)), Block([]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 455))
    
    # def test_tmms_forexpr_3(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b <- true
    #         dynamic i <- 0
    #         for i until i<10 by i<10
    #         begin
    #         end
    #     end
    #         """
    #     expect = """Type mismatch in statement: ForStmt(Id(i), BinExpr(<, Id(i), NumberLiteral(10)), BinExpr(<, Id(i), NumberLiteral(10)), BlockStmt([]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 456))
    
    # def test_tmms_forexpr_4(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b
    #         number i
    #         for i until i+1 by i<10
    #         begin 
    #         end
    #     end
    #         """
    #     expect = """Type mismatch in statement: ForStmt(Id(i), BinExpr(+, Id(i), NumberLiteral(1)), BinExpr(<, Id(i), NumberLiteral(10)), BlockStmt([]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 457))
    
    # def test_tmms_asm_1(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b
    #         number i
    #         var v
    #         v <- v
    #     end
    #         """
    #     expect = """Type mismatch in statement: AssignStmt(Id(v), Id(v))"""
    #     self.assertTrue(TestChecker.test(input, expect, 458))
    
    # def test_tmms_asm_2(self):
    #     input = """
    #     func main()
    #     begin
    #         bool b
    #         number a[5]
    #         a <- [1,2,3,4,5]
    #     end
    #         """
    #     expect = """Type mismatch in statement: AssignStmt(Id(a), ArrayLit([NumberLiteral(1), NumberLiteral(2), NumberLiteral(3), NumberLiteral(4), NumberLiteral(5)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 459))
    
    # def test_tmms_func_1(self):
    #     input = """
    #     func foo()
    #     begin
    #         return 0
    #     end
    #     func main()
    #     begin
    #         number i 
    #         number f
    #         f <- f+i
    #         foo() ## foo -> int (return - not auto anymore) != void (CallExpr) => INVALID !!
    #         f <- f+foo(i)
    #         i <- i+f
    #     end
    #         """
    #     expect = """Type mismatch in expression: CallExpr(foo, [Id(i)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 460))
        
    # def test_tmms_func_2(self):
    #     input = """
    #     func foo(number a,number b,number c)
    #     begin
    #         return 0.0 ## foo->float
    #     end
    #     func bar() begin end
    #     func main()
    #     begin
    #         number i
    #         number f
    #         f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
    #         f <- foo(1,"2",3.0) ## invalid: param 2 mismatch
    #     end
    #         """
    #     expect = """Type mismatch in expression: CallExpr(foo, [NumberLiteral(1), StringLit(2), NumberLiteral(3.0)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 461))
    
    # def test_tmms_func_3(self):
    #     input = """
    #     func foo(number a,number b,number c)
    #     begin
    #         return 0.0 ## foo->float
    #     end
    #     func main()
    #     begin
    #         number i
    #         number f
    #         f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
    #         f <- foo(1,2.0,3.0) ## invalid: foo is not void
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 462))
    
    # def test_tmms_func_4(self):
    #     input = """
    #     func foo(number a,number b,number c, number d)
    #     begin
    #         return 0
    #     end
    #     func main()
    #     begin
    #         number i
    #         number f
    #         f <- f+i
    #         begin
    #             f <- foo(i,f,f,i) ## infer: foo->number,a->number,b->number,c->number
    #         end
    #         foo(1,2.0,3.0,1)
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 463))
    
    # def test_tmms_func_5(self):
    #     input = """
    #     func foo(number a,number b,number c, number d)
    #     begin
    #         a <- 5
    #         return a ## foo->number
    #     end
    #     func main()
    #     begin
    #         var f <- foo(1,2,3,4) ## f->number
    #         f <- f + "wrong"
    #     end
    #         """
    #     expect = """Type mismatch in expression: BinExpr(+, Id(f), StringLit(wrong))"""
    #     self.assertTrue(TestChecker.test(input, expect, 464))
        
    # def test_mil_1(self):
    #     input = """
    #     func main()
    #     begin
    #         number i <- 0
    #         for i until i < 10 by i
    #         begin
    #             continue
    #             break
    #         end
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 465))
    
    # def test_mil_2(self):
    #     input = """
    #     func main()
    #     begin
    #         number i <- 0
    #         for i until i < 10 by i
    #         begin
    #             continue
    #         end
    #         break
    #     end
    #         """
    #     expect = """Must in loop: Break()"""
    #     self.assertTrue(TestChecker.test(input, expect, 466))
    
    # def test_mil_3(self):
    #     input = """
    #     func main()
    #     begin
    #         number i <- 0
    #         for i until i < 10 by i
    #         begin
    #             break
    #         end
    #         continue
    #     end
    #         """
    #     expect = """Must in loop: ContinueStmt()"""
    #     self.assertTrue(TestChecker.test(input, expect, 467))
    
    # def test_mil_4(self):
    #     input = """
    #     func main()
    #     begin
    #         number i <- 0
    #         for i until i < 10 by i
    #         begin
    #             continue
    #             begin
    #                 break
    #             end
    #         end
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 468))
    
    # def test_mil_5(self):
    #     input = """
    #     func main()
    #     begin
    #         number i <- 0
    #         for i until i < 10 by i + 1
    #         begin
    #             continue
    #         end
    #         begin
    #             break
    #         end
    #     end
    #         """
    #     expect = """Must in loop: BreakStmt()"""
    #     self.assertTrue(TestChecker.test(input, expect, 469))
    
    # # ALTERNATIVE TEST: parameter passed by value and by reference; if with elif stmt
    
    # # def test_ifs_normal_super(self):
    
    # #     input = """
    # #     func foo(inherit a: number){}
    # #     mid: function void(){}
    # #     main: function void() inherit foo{
    # #         super(1)
    # #     }
    # #         """
    # #     expect = ""
    # #     self.assertTrue(TestChecker.test(input, expect, 470))
    
    # # def test_ifs_normal_preventDefault(self):
    # #     input = """
    # #     foo: function void(a: number){}
    # #     mid: function void(){}
    # #     main: function void() inherit foo{
    # #         preventDefault()
    # #     }
    # #         """
    # #     expect = ""
    # #     self.assertTrue(TestChecker.test(input, expect, 471))
    
    # # def test_ifs_block_stmt(self):
    # #     input = """
    # #     foo: function void(a: number){}
    # #     mid: function void(){}
    # #     main: function void() inherit foo{
    # #         {
    # #             super(1)
    # #         }
    # #         preventDefault()
    # #     }
    # #         """
    # #     expect = """Invalid statement in function: main"""
    # #     self.assertTrue(TestChecker.test(input, expect, 472))
    
    # # def test_ifs_inherit_parent(self):
    # #     input = """
    # #     foo: function void(inherit a: number,b: auto, inherit c: number){}
    # #     mid: function void(){}
    # #     main: function void() inherit foo{
    # #         super(1,2,3)
    # #         a = a+1
    # #         c = c+1
    # #         b = b+1
    # #     }
    # #         """
    # #     expect = """Undeclared Identifier: b"""
    # #     self.assertTrue(TestChecker.test(input, expect, 473))
        
    # # def test_ifs_inherit_grandparent(self):
    # #     input = """
    # #     func main()}
    # #     goo: function void(c: number) inherit bar{
    # #         super(2)
    # #         c = b + a
    # #     }
    # #     bar: function void(inherit b: number) inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number){}
    # #         """
    # #     expect = """Undeclared Identifier: a"""
    # #     self.assertTrue(TestChecker.test(input, expect, 474))
    
    # # def test_ifs_redecl_var(self):
    # #     input = """
    # #     func main()}
    # #     goo: function void(c: number) inherit bar{
    # #         super(2)
    # #         a: number
    # #         c = a + b
    # #     }
    # #     bar: function void(inherit b: number) inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number){}
    # #         """
    # #     expect = ""
    # #     self.assertTrue(TestChecker.test(input, expect, 475))
    
    # # def test_ifs_redecl_param(self):
    # #     input = """
    # #     func main()}
    # #     goo: function void(b: number) inherit bar{
    # #         super(2)
    # #         c = a + b
    # #     }
    # #     bar: function void(inherit b: number) inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number){}
    # #         """
    # #     expect = """Invalid Parameter: b"""
    # #     self.assertTrue(TestChecker.test(input, expect, 476))
    
    # # def test_ifs_auto_inherit_empty(self):
    # #     input = """
    # #     func main()}
    # #     go: function void(b: number) inherit bar{
    # #         b = a
    # #     }
    # #     bar: function void() inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number){}
    # #         """
    # #     expect = "Undeclared Identifier: a"
    # #     self.assertTrue(TestChecker.test(input, expect, 477))
    
    # # def test_ifs_block_inherit_empty(self):
    # #     input = """
    # #     func main()}
    # #     go: function void(b: number) inherit bar{
    # #         preventDefault()
    # #         b = a
    # #     }
    # #     bar: function void() inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number){}
    # #         """
    # #     expect = """Undeclared Identifier: a"""
    # #     self.assertTrue(TestChecker.test(input, expect, 478))
    
    # # def test_ifs_mixed_inherit(self):
    # #     input = """
    # #     func main()}
    # #     go: function void(b: number) inherit bar{
    # #         b = a
    # #     }
    # #     bar: function void() inherit foo{
    # #         super(1)
    # #     }
    # #     foo: function void(inherit a: number) inherit zar{
    # #         preventDefault()
    # #     }
    # #     zar: function void(inherit b: number){}
    # #         """
    # #     expect = "Undeclared Identifier: a"
    # #     self.assertTrue(TestChecker.test(input, expect, 479))
    
    # def test_invalid_var(self):
    #     input = """
    #     func main()
    #     begin
    #         var a
    #     end
    #         """
    #     expect = """Invalid Variable: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 480))
    
    # def test_infer_var(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- 10
    #         var b <- "100"
    #         var c <- a<10
    #         writeNumber(a)
    #         writeString(b)
    #         writeBool(c)
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 481))
    
    # def test_infer_func_1(self):
        
    #     input = """
    #     func foo(number a, number b) return 1.2
    #     func main()
    #     begin
    #         number a <- foo(1,2)
    #         writeNumber(foo(1,2))
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 482))
        
    # def test_infer_func_2(self):
    #     input = """
    #     func foo(number a, number b) return 1.2
    #     func main()
    #     begin
    #         number a <- foo(1,2) + 1
    #         writeNumber(foo(1,2))
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 483))
    
    # def test_infer_func_3(self):
    #     input = """
    #     func foo(number a, number b) return 1.2
    #     func main()
    #     begin
    #         foo(1,2) ## error here because foo returns number type, not void
    #         number a <- foo(1,2) + 1
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 484))
    
    # # def test_invalid_param_1(self):
    # #     input = """
    # #     foo: function auto(a: number){}
    # #     main: function void(a: number) inherit foo{
    # #         super(1)
    # #     }
    # #         """
    # #     expect = """No entry point"""
    # #     self.assertTrue(TestChecker.test(input, expect, 485))
    
    # # def test_invalid_param_2(self):
    # #     input = """
    # #     foo: function auto(inherit a: number){}
    # #     main: function void(a: number) inherit foo{
    # #         super(1)
    # #     }
    # #         """
    # #     expect = """Invalid Parameter: a"""
    # #     self.assertTrue(TestChecker.test(input, expect, 486))
    
    # ## TESTS from BKeL
    # def test_array_decl(self):
    #     input = """
    #     func foo(number a) return "vankha"
    #     func main()
    #     begin
    #         number a[3] <- [1,2]
    #     end
    #         """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], NumberType), ArrayLit([NumberLiteral(1), NumberLiteral(2)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 487)) 
        
    # def test_array_asm(self):
    #     input = """
    #     func foo(number a) return "vankha"
    #     func main()
    #     begin
    #         number a[2,3]
    #         a[1,2,3] <- 1
    #     end
    #         """
    #     expect = """Type mismatch in expression: ArrayCell(a, [NumberLiteral(1), NumberLiteral(2), NumberLiteral(3)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 488))
        
    # def test_out_param(self):
    #     input = """
    #     foo: func(number x[2]) return
    #     func main()
    #     begin
    #         foo(1)
    #     end
    #         """
    #     expect = """Type mismatch in statement: CallExpr(foo, NumberLiteral(2))"""
    #     self.assertTrue(TestChecker.test(input, expect, 489))
    
    # def test_array_as_param(self):
    #     input = """
    #     func foo1() return 2
    #     func foo2() return 3
    #     func main()
    #     begin
    #         number a[2] <- [ foo1(), foo2()]
    #         writeNumber(foo1())
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 490))
    
    # def test_array_cell_nonatomic(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[1,2,3]
    #         number x <- a[1]
    #     end
    #         """
    #     expect = """Type mismatch in Variable Declaration: ArrayCell(a, [NumberLiteral(1)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 491))
    
    # def test_super_in_empty_parent(self):
    #     input = """
    #     func x() return
    #     func main()
    #     begin
    #         super()
    #     end
    #         """
    #     expect = """Invalid statement in function: super"""
    #     self.assertTrue(TestChecker.test(input, expect, 492))
        
    # def test_nonatomic_cell_init(self):
    #     input = """
    #     func x() return
    #     func main()
    #     begin
    #         number a[2, 3]
    #         number b[3]  <- a[0]
    #         number c[5] <- a[0]
    #     end
    #         """
    #     expect = """Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], numberType), ArrayCell(a, [numberLit(0)]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 493))
    
    # def test_func_id(self):
    #     input = """
    #     func foo() return 1
    #     var a <- foo
    #     func main()
    #     begin
    #     end
    #         """
    #     expect = """Undeclared Identifier: foo"""
    #     self.assertTrue(TestChecker.test(input, expect, 494))
        
    # def test_array_id(self):
    #     input = """
    #     func foo() begin end
    #     func main()
    #     begin
    #         a[0] = 5
    #     end
    #         """
    #     expect = """Undeclared Identifier: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 495)) 
        
    # def test_undecl_mismatch_param(self):
    #     input = """
    #     func main()
    #     begin
            
    #     end
    #     var a <- foo(1, 2)
    #     func foo() return 1
    #         """
    #     expect = """Type mismatch in expression: CallExpr(foo, [numberLit(1), numberLit(2)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 496))
    
    # def test_infer_subscript(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[3,4]
    #         a[foo(), 1+4] <- 222
    #         a[1,2] <- bar()
    #         writeNumber(foo())
    #         writeNumber(bar())
    #     end
    #     func foo() return 1
    #     func bar() return 2
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 497))
    
    # def test_coercion_array_intfloat(self):
    #     input = """
    #     func main()
    #     begin
    #         number a[4] <- [1,2,3,4]
    #     end
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 498)) 
    
    # def test_return_after(self):
    #     input = """
    #     func foo(string a, number b)
    #     begin
    #         if (b>0)
    #         begin
    #             return a ## -> string
    #         end
    #         return "a" ## -> string
    #         return 1 ## -> dont care
    #     end
    #     func main()
    #     begin
    #         writeString(foo(1,2))
    #     end
        
    #         """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))
    
    # def test_func_pass(self):
    #     input = """
    #         func main()
    #         begin
    #             number arr <- 2
    #             main()
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(CallStmt(Id("main"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 4000))
    
    # def test_4001(self):
    #     input = """
    #         number a[3] <- [2,3,4]
    #         func main()
    #         begin
    #             a[3] <- "error here"
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('a'), [NumberLiteral(3.0)]), StringLiteral("error here"))))
    #     #Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a),[NumLit(3.0)]),StringLit(error here))
    #     self.assertTrue(TestChecker.test(input, expect, 4001))
        
    # def test_4002(self):
    #     input = """
    #         func foo(number x)
    #         begin
    #             return
    #         end
            
    #         func main()
    #         begin
    #             number x <- 2
    #             dynamic y
    #             y <- foo(x)
    #         end
            
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(Id("y"), CallExpr(Id("foo"), [Id("x")]))))
        
    #     self.assertTrue(TestChecker.test(input, expect, 4002))
        
    # def test_4003(self):
    #     input = """
    #         func main()
    #         begin
    #             dynamic c
    #             dynamic d
    #             d <- c
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(Id("d"), Id("c"))))
        
    #     self.assertTrue(TestChecker.test(input, expect, 4003))
    
    # def test_4004(self):
    #     input = """
    #         func foo(number x)
    #         begin
    #             return x
    #         end
        
    #         func main()
    #         begin
    #             dynamic x <-2 
    #             dynamic a
    #             var y <- 2
    #             x <- y + foo(a)
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(Id("x"), BinaryOp("+", Id("y"), CallExpr(Id("foo"), [Id("a")])))))
        
    #     self.assertTrue(TestChecker.test(input, expect, 4004))
    
    # def test_4004(self):
    #     input = """
    #         dynamic y
    #         func main()
    #         begin
    #             var x <- 2
    #             if (true) 
    #             begin
    #                 var a <- y
    #                 if (true)
    #                 begin
    #                     x <- y
    #                 end
    #             end
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(Id("x"), Id("y"))))
        
    #     self.assertTrue(TestChecker.test(input, expect, 4004))
    
    # def test_4005(self):
    #     input = """
    #         func main()
    #         begin
    #             number x[3] <- [2,3,"4"]
    #         end
    #         """
    #     expect = str(TypeCannotBeInferred(Assign(Id("x"), Id("y"))))
        
    #     self.assertTrue(TestChecker.test(input, expect, 4005))
    
    # def test_4006(self):
    #     input = """
    #         func f()
    #     begin
    #         var i <- 0
    #         for i until i > 10 by i
    #         begin
            
    #         end
    #         continue
    #     end
    #     func main()
    #     begin
    #         number x <- 2 + true
    #         writeNumber(x)
    #     end
    #         """
    #     expect = "Continue Not In Loop"
        
    #     self.assertTrue(TestChecker.test(input, expect, 4006))
        
    # def test_4007(self):
    #     input = """
    #     func main()
    #     begin
    #         number x <- 2 + true
    #         writeNumber(x)
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4007))
    
    # def test_4008(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic x <- (x - 2) * (x + true)
    #     end
    #     """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input, expect, 4008))
    
    
    
    # def test_4010(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic x 
    #         x  <- (x - 2) * (x + true)
    #     end
    #     """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input, expect, 4010))
    
    
