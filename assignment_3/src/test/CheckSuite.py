import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = """func b() 
            begin
            end
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_no_entry_point_3(self):
        input = """func main() 
            begin
                return 1
            end
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_no_entry_point_4(self):
        input = """func main() 
            begin
                return
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_no_entry_point_5(self):
        input = """func bkool()
            begin
                return true
            end
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_redecl_var_1(self):
        input = """func main()
            begin
                number a
                string a
            end
            """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_redecl_var_2(self):
        input = """func main()
            begin
                number a
                number b
                string c
                bool b
            end
            """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_redecl_var_3(self):
        input = """ number a
            func main()
            begin
                string a
                return
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_redecl_var_4(self):
        input = """ number a
            func main()
            begin
                number a
                begin
                    string a
                end
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_redecl_var_5(self):
        input = """ number a
            number b
            func main()
            begin
                number a
            end
            number b
            """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    # FOR MULTIPLE FUNCTIONS
   
    def test_redecl_func_3(self):
        input = """func main()
        begin
            number main
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_redecl_func_4(self):
        input = """func main()
            begin
            end
            func foo (number a)
            begin
                bool a
            end
            """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_redecl_func_5(self):
        input = """func main() 
            begin
            end
            func foo(number a) 
            begin
            end
            string a
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_redecl_param_1(self):
        input = """func main() 
            begin
            end
            func foo (number a, string a)
            begin
            end
            """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_redecl_param_2(self):
        input = """func main() 
            begin
            end
            func foo (number foo)
            begin
            end
            """
        expect = """Redeclared Parameter: foo"""
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_redecl_param_3(self):
        input = """func main() 
            begin
            end
            func foo(number main)
            begin
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_redecl_param_4(self):
        input = """func main()
            begin
            end
            func foo (number a)
            begin
            end
            func a (number foo)
            begin
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_undecl_var_1(self):
        input = """func main()
        begin
            a <- 2
            return
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_undecl_var_2(self):
        input = """number a
        func main()
        begin
            a <- 2
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_undecl_var_3(self):
        input = """func main()
        begin
            var a <- 2
            var b <- a + 2
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_undecl_var_4(self):
        input = """func main()
        begin
            begin
                number a
            end
            a <- 2
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_undecl_var_5(self):
        input = """func main() 
                    begin 
                    end
            func foo(number a)
            begin
                a <- 2
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_undecl_func_1(self):
        input = """
        func check()
        begin
        end
        func main()
        begin
            foo()
        end
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_undecl_func_2(self):
        input = """func main()
        begin
            number a
            a <- foo() + 5
        end
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    
    def test_tmme_a1(self):
        input = """
        func main()
        begin
            number a[5]
            number b
            b <- a[5]
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_tmme_a2(self):
        input = """
        func main()
        begin
            number a
            number b
            b <- a[5]
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(5.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_tmme_a3(self):
        input = """
        func main()
        begin
            number a[5, 5]
            number b
            b <- a[1.0,"1"]
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), StringLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_tmme_b1_implicit(self):
        input = """
        func main()
        begin
            number a 
            string b
            ## a + b: Unknown a: number
            a <- a + b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_tmme_b2_implicit(self):
        input = """
        func main()
        begin
            number a
            number b
            ## number -> number:OK
            b <- a
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_tmme_b3_implicit(self):
        input = """
        func main()
        begin
            number a <- 1
            number b <- a + 2
            string c <- 2.3
        end
            """
        expect = """Type Cannot Be Inferred: VarDecl(Id(c), StringType, None, NumLit(2.3))"""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_tmme_b4_unary(self):
        input = """
        func main()
        begin
            string a
            a <- -a
        end
            """
        expect = """Type Mismatch In Expression: UnaryOp(-, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_tmme_b5_unary(self):
        input = """
        func main()
        begin
            number a
            a <- not a
        end
            """
        expect = """Type Mismatch In Expression: UnaryOp(not, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_tmme_b6_binary(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            a <- 1
            dynamic c
            c <- a + b
        end
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 438)) 
    
    def test_tmme_b7_binary(self):
        input = """
        func main()
        begin
            number a
            number b
            number c
            string d 
            string e 
            d <- d ... e ## valid
            b <- a % c ## valid
            a <- a == b ## invalid: a == b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_tmme_b8_binary(self):
        input = """
        func main()
        begin
            number a
            bool b
            bool c
            b <- (b and c) or c ## valid
            b <- a and b ## invalid: a and b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(and, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_4009(self):
        input = """
        func main()
        begin
            dynamic x 
            x  <- (x - 2) * (x + true)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 4009))
    
    def test_tmme_b9_binary(self):
        input = """
        func main()
        begin
            number a
            number b
            bool c
            bool d
            number e
            c <- b > e
            c <- e <= b
            d <- b == e ## invalid: b==e
        end
            """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(b), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
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
        expect = """Type Mismatch In Statement: Return()"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_tmme_c2_param_typ(self):
        input = """
        func foo(number a, number b)
        func main()
        begin
            number a <- 2
            string b <- "2.1"
            a <- foo(b,a) + 2
        end
        func foo(number a, number b)
        begin
            return a+b
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(b), Id(a)])"""
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_tmme_c3_param_len(self):
        input = """
        func foo(number a, number b, number c)
        func main()
        begin
            number a <- 2
            number b <- 2.1
            a <- foo(a,b) + 2
        end
        func foo(number a, number b, number c)
        begin
            return a+b+c
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_ial_1(self):
        input = """
        func main()
        begin
            number a[5]
            a <- [1,"2.0"]
        end
            """
        expect = """Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_ial_2(self):
        input = """
        number b1
        func main()
        begin
            bool a[5]
            bool b1 
            bool b2
            a <- [b1,b2]
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(b1), Id(b2)))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_ial_3(self):
        input = """
        string a[5]
        func main()
        begin
            number i1 <- 25
            number f2 <- 25.0
            a <- [i1,f2]
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(i1), Id(f2)))"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_ial_4(self):
        input = """
        func main()
        begin
            number a[5, 5]
            a <- [[1,2],[1,2,3],[1,2,"3"]]
        end
            """
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(3)))"""
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_ial_5(self):
        input = """
        func main()
        begin
            number a[5]
            string s
            a[3] <- 2.5
            a[2] <- 5
            a[1] <- s
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_tmms_condexpr_1(self):
        input = """
        func main()
        begin
            bool b
            number i
            if(b) 
            begin
            end
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_tmms_condexpr_2(self):
        input = """
        func main()
        begin
            bool b
            number i
            if (b)
            begin
            end
            elif (i)
            begin 
            end
        end
            """
        expect = """Type Mismatch In Statement: If((Id(b), Block([])), [(Id(i), Block([]))], None)"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_tmms_condexpr_3(self):
        input = """
        func main()
        begin
            bool b1
            bool b2
            number i1
            number i2
            if(i1 = i2)
            begin
            end
            if(i1)
            begin
            end
            if(b1)
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: If((Id(i1), Block([])), [], None)"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_tmms_condexpr_4(self):
        input = """
        func main()
        begin
            bool b1
            bool b2
            number i
            if (b1 and b2)
            begin
            end
            elif(b1 or b2)
            begin
            end
            elif (i)
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: If((BinaryOp(and, Id(b1), Id(b2)), Block([])), [(BinaryOp(or, Id(b1), Id(b2)), Block([])), (Id(i), Block([]))], None)"""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_tmms_forexpr_1(self):
        input = """
        func main()
        begin
            bool b
            var i <- 0
            for i until i<10 by i+1
            begin
            end
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_tmms_forexpr_2(self):
        input = """
        func main()
        begin
            bool b <- true
            number i
            for b until i<10 by i*2
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(b), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(*, Id(i), NumLit(2.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_tmms_forexpr_3(self):
        input = """
        func main()
        begin
            bool b <- true
            dynamic i <- 0
            for i until i<10 by i<10
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_tmms_forexpr_4(self):
        input = """
        func main()
        begin
            bool b
            number i
            for i until i+1 by i<10
            begin 
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(+, Id(i), NumLit(1.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_tmms_asm_1(self):
        input = """
        func main()
        begin
            bool b
            number i
            dynamic v
            v <- v
        end
            """
        expect = """Type Cannot Be Inferred: AssignStmt(Id(v), Id(v))"""
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_tmms_asm_2(self):
        input = """
        func main()
        begin
            bool b
            dynamic c
            number a[2, 3]
            a <- [[c, c, c], [c, c, c]]
        end
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_tmms_func_1(self):
        input = """
        func foo()
        begin
            return 0
        end
        func main()
        begin
            number i 
            number f
            f <- f+i
            foo() ## foo -> int (return - not auto anymore) != void (CallExpr) => INVALID !!
            f <- f+foo(i)
            i <- i+f
        end
            """
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [])"""
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_tmms_func_2(self):
        input = """
        func foo(number a,number b,number c)
        begin
            return 0.0
        end
        func bar()
        begin
        end
        func main()
        begin
            number i
            number f
            f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
            f <- foo(1,"2",3.0) ## invalid: param 2 mismatch
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(2), NumLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_tmms_func_3(self):
        input = """
        func foo(number a,number b,number c)
        begin
            return 0.0 
        end
        func main()
        begin
            number i
            number f
            f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
            f <- foo(1,2.0,3.0) 
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_tmms_func_4(self):
        input = """
        func foo(number a,number b,number c, number d)
        begin
            return 0
        end
        func main()
        begin
            number i
            number f
            f <- f+i
            begin
                f <- foo(i,f,f,i) ## infer: foo->number,a->number,b->number,c->number
            end
            f <- foo(1,2.0,3.0,1)
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_tmms_func_5(self):
        input = """
        func foo(number a,number b,number c, number d)
        begin
            a <- 5
            return a ## foo->number
        end
        func main()
        begin
            var f <- foo(1,2,3,4) ## f->number
            f <- f + "wrong"
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(+, Id(f), StringLit(wrong))"""
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_mil_1(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
                break
            end
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_mil_2(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
            end
            break
        end
            """
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_mil_3(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                break
            end
            continue
        end
            """
        expect = """Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_mil_4(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
                begin
                    break
                end
            end
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_mil_5(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i + 1
            begin
                continue
            end
            begin
                break
            end
        end
            """
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    # ALTERNATIVE TEST: parameter passed by value and by reference; if with elif stmt
    
    def test_ifs_normal_super(self): # check again
    
        input = """
        dynamic x
        func main() 
        begin
            var y <- x[0, 0] + 1
            writeNumber(y)
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    
    
    def test_var(self):
        input = """
        func main()
        begin
            var a <- 1
        end
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_infer_var(self):
        input = """
        func main()
        begin
            var a <- 10
            var b <- "100"
            var c <- a < 10
            writeNumber(a)
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_infer_func_1(self):
        
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            number a <- foo(1,2)
            writeNumber(foo(1,2))
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test_infer_func_2(self):
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            number a <- foo(1,2) + 1
            writeNumber(foo(1,2))
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_infer_func_3(self):
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            foo(1,2) ## error here because foo returns number type, not void
            number a <- foo(1,2) + 1
        end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_invalid_param_1(self):
        input = """
        func inc(number a) return a+1
            """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_invalid_param_2(self):
        input = """
            func inc(number a) 
            func main()
            begin
                string c <- "hello world" 
                var x <- inc(3)...c 
            end 
            func inc(number a) return a+1 
            """
        expect = """Type Mismatch In Statement: Return(BinaryOp(+, Id(a), NumLit(1.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_array_decl(self):
        input = """
        func foo(number a) return "vankha"
        func main()
        begin
            number a[3] <- [1,2]
        end
            """
        expect = """Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 487)) 
        
    def test_array_asm(self):
        input = """
        func foo(number a) return "vankha"
        func main()
        begin
            number a[2,3]
            a[1,2,3] <- 1
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test_out_param(self):
        input = """
        func foo(number x[2]) return
        func main()
        begin
            foo(1)
        end
            """
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_array_as_param(self):
        input = """
        func foo1() return 2
        func foo2() return 3
        func main()
        begin
            number a[2] <- [ foo1(), foo2()]
            writeNumber(foo1())
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_array_cell_nonatomic(self):
        input = """
        func main()
        begin
            number a[1,2,3]
            number x <- a[1]
        end
            """
        expect = """Type Cannot Be Inferred: VarDecl(Id(x), NumberType, None, ArrayCell(Id(a), [NumLit(1.0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_undeclare_func(self):
        input = """
        func x() return
        func main()
        begin
            super()
        end
            """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 492))
        
    def test_nonatomic_cell_init(self):
        input = """
        func x() return
        func main()
        begin
            number a[2, 3]
            number b <- a[0, 0]
            dynamic c <- a[0]
        end
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_func_id(self):
        input = """
        func foo() return 1
        var a <- foo
        func main()
        begin
        end
            """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test_array_id(self):
        input = """
        func foo()
        begin
        end
        func main()
        begin
            a[0] <- 5
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 495)) 
    

    
    def test_coercion_array_intfloat(self):
        input = """
        func main()
        begin
            number a[4] <- [1,2,3,4]
        end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498)) 
    
    def test_return_after(self):
        input = """
        func foo(string a, number b)
        begin
            if (b>0)
            begin
                return a ## -> string
            end
            return "a" ## -> string
            return 1 ## -> dont care
        end
        func main()
        begin
            writeString(foo("Hello",2))
        end
        
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
    
    # def test_func_pass(self):
    #     input = """
    #         func main()
    #         begin
    #             number arr <- 2
    #             main()
    #         end
    #         """
    #     expect = "Undeclared Function: main"
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
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        
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
    #     expect = ""
        
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

    # def test_ifs_normal_preventDefault(self):
    #     input = """
    #     func f()
    #     begin
    #         var j <- 1
    #         for j until j > 11 by 1
    #         begin
            
    #         end
    #         break
    #     end
        
    #     func main()
    #     begin
    #         f()
    #     end
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 471))
    
    # def test_ifs_block_stmt(self):
    #     input = """
    #     func findMax(number x[10], number n)
    #     begin
    #         if (n = 1) return x[0]
    #         number k <- findMax(x, n - 1)
    #         if (k >= x[n]) return k
    #         return x[n]
    #     end
    
    #     func main() 
    #     begin
    #         dynamic x <- [3, 4, 8, 1, 2, 7, 9, 8, 5, 6]
    #         writeNumber(findMax(x, 10))
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 472))
    
    # def test_ifs_inherit_parent(self):
    #     input = """
    #     func foo (number n, string n) begin
        
    #     end 
    #     func main() begin
        
    #     end
    #     """
    #     expect = "Redeclared Parameter: n"
    #     self.assertTrue(TestChecker.test(input, expect, 473))
        
    # def test_ifs_inherit_grandparent(self):
    #     input = """
    #     func foo(number a) begin
    #         writeNumber(a)
    #         number c <- 109
    #     end
        
    #     func main() begin
    #         foo(2018)
    #         goo(20, 1998)
    #     end
        
    #     func goo(number a, number b) begin            
    #         foo(3)
    #     end
    #      """
    #     expect = "Undeclared Function: goo"
    #     self.assertTrue(TestChecker.test(input, expect, 474))
    
    # def test_ifs_redecl_var(self):
    #     input = """
    #     func foo(number x) begin
    #         number a <- 7
    #     end
    #     func foo1(string x, bool x) begin
        
    #     end
    #     func main() begin
        
    #     end
    #     """
    #     expect = "Redeclared Parameter: x"
    #     self.assertTrue(TestChecker.test(input, expect, 475))
    
    # def test_ifs_redecl_param(self): ## Check again, output should be error on assignstmt
    #     input = """
    #     func foo(number a, number b)
    #     begin
    #         return a + b
    #     end
    #     string a <- "Hello"
    #     func main() begin
    #         a <- foo(1.1, 2)
    #     end
    #     """
    #     expect = "Type mismatch in expression: CallExpr(foo, [NumberLit(1.1), NumberLit(2)])"
    #     self.assertTrue(TestChecker.test(input, expect, 476))
    
    # def test_ifs_auto_inherit_empty(self): 
    #     input = """
    #     func main() 
    #     begin
    #         dynamic x
    #         dynamic y
    #         dynamic z
    #         number a[3, 3] <- [x, y, z]
    #         x <- [1, 2, 3]
    #         y <- [4, 5, 6]
    #         z <- [7, 8, 9]
    #         writeNumber(x[0] + z[0] + y[1])
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 477))
    
    # def test_ifs_auto_inherit_empty2(self): ## Bug here
    #     input = """
    #     func main() 
    #     begin
    #         dynamic x
    #         dynamic y
    #         dynamic z
    #         number a[3, 3] <- [x, y, [1, 2, 3]]
    #         x <- [1, 2, 3]
    #         y <- [4, 5, 6]
    #         z <- [7, 8, 9]
    #         writeNumber(x[0] + z[0] + y[1])
    #         dynamic t
    #         number b[1,3,4] <- [t]
    #         t <- [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 478))
    
    # def test_ifs_mixed_inherit(self):
    #     input = """
    #     func main()
    #     begin
    #         var x <- [[[1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
    #     self.assertTrue(TestChecker.test(input, expect, 479))
    
    # def test_4011(self):
    #     input = """
    #     func areDivisors(number num1, number num2) 
    #         return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
    #     func main()
    #     begin
    #         var num1 <- readNumber()
    #         var num2 <- readNumber()
    #         if (areDivisors(num1, num2)) writeString("Nope")
    #         else writeString("What?")
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4011))
    
    # def test_4012(self):
    #     input = """
    #     func main()
    #     begin
    #         number x <- readNumber()
    #         if (x <= 5) writeString("Number is smaller or equal 5")
    #         elif ((x < 5) and (x <= 10)) writeString("Number between 5 and 10")
    #         else writeString("Number greater than 10")
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4012))

    # def test_4013(self):
    #     input = """
    #     func f(number y)
    #     dynamic x <- f(3) + 1
    #     func main() 
    #     begin
    #         return
    #     end
    #     """
    #     expect = "No Function Definition: f"
    #     self.assertTrue(TestChecker.test(input, expect, 4013))
        
    # def test_4014(self): ## Bug here
    #     input = """
    #     func f(number y)
    #     func main() 
    #     begin
    #         number y <- f(4)
    #         writeNumber(x)
    #     end
        
    #     func f (number y)
    #     begin
    #         if (y >= 2) return f(y-1) + f(y-2)
    #         return 1
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 4014))
        
    # def test_426 (self):
    #     input = """
    #     bool x <- true
    #     func foo() begin
    #         return x
    #     end
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 426))
        
        
################# CHECK FUNCTION ###############
    # def test_redecl_var_6(self):
    #     input = """func main() 
    #         begin 
    #         end
    #         func c() 
    #         begin 
    #         end
    #         number c
    #         """
    #     expect = """Redeclared Variable: c"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # def test_redecl_func_1(self):
    #     input = """func main() begin
    #         end
    #         number c
    #         func c() begin
    #         end
    #         """
    #     expect = """Redeclared Function: c"""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    
    # def test_redecl_func_2(self):
    #     input = """func main() begin 
    #     end
    #         func c() begin 
    #         end
    #         func c() begin 
    #         end
    #         """
    #     expect = """Redeclared Function: c"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))
        
    # def test_infer_subscript(self):
    #     input = """
    #     func foo()
    #     func bar()
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
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a), [CallExpr(Id(foo), []), BinaryOp(+, NumLit(1.0), NumLit(4.0))])"
    #     self.assertTrue(TestChecker.test(input, expect, 497))
        
    # def test_undecl_mismatch_param(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #     end
    #     number a <- foo(1, 2)
    #     func foo() return 1
    #         """
    #     expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 496))
        
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


##################### 100 TC #############################

#     def test501(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 501))
        
#     def test502(self):
#         input = """
# func f(number x)

# func main()
# begin
#     number x <- f(2)
#     writeNumber(x)
# end

# func f(number x)
# begin
#     if (x <= 2) return f(x - 1) + f(x - 2)
#     return 1
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 502))

#     def test503(self):
#         input = """
# func main()
# begin
#     var x <- [[1, 2, 3], [4, 5, 6]]
#     var y <- x[0, 0] + 1
#     writeBool(y)
# end

# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 503))

#     def test504(self):
#         input = """
# dynamic x
# func main()
# begin
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end

# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 504))

#     def test505(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 505))

#     def test506(self):
#         input = """
# dynamic x <- f(2)
# func f(number x)

# func main()
# begin

# end
# """
#         expect = "Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 506))
    
#     def test507(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 507))

#     def test508(self):
#         input = """
# func f(number x)

# dynamic x <- f(2) + 1

# func main()
# begin
#     return
# end
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 508))

#     def test509(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 509))

#     def test510(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 510))

#     def test511(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 511))
    
#     def test512(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 512))

#     def test513(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 513))
    
#     def test514(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 514))

#     def test515(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 515))

#     def test516(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 516))


#     def test517(self):
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
#         self.assertTrue(TestChecker.test(input, expect, 517))
    
#     def test518(self):
#         input = """
# func main()
# begin
#     number x <- 2 + true
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 518))
    
#     def test519(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 519))


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

#     def test422(self):
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
#         expect = ""
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
#         expect = "Redeclared Parameter: x"
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

#     def test439(self): ## Redeclared Identifier: x
#         input = """
# func f(number x)
# begin
#     dynamic x <- (x - 2) * (x + true)
# end
# """
#         expect = "Redeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 439))
    
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
    
#     def test444(self): ## Tên biến được trùng với tên hàm
#         input = """
# func f()

# number f
# dynamic x
# func main()
#     return
# """
#         expect = "No Function Definition: f"
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

#     def test446(self): 
#         input = """
# func f(number x)
# begin
#     return f(x)
# end

# func main()
# begin
#     dynamic d <- f(10)
# end
# """
#         expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
#         self.assertTrue(TestChecker.test(input, expect, 446))
    
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


#     def test460(self): ## Tên biến có thể trùng với tên hàm
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
#     x <- ["Hello", ", my name is ", "Kien"]
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [ArrayLit(Id(a), Id(b), Id(c))])"
#         self.assertTrue(TestChecker.test(input, expect, 460))


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

#     def test463(self):
#         input = """
# number x <- 10
# func f(number x)
# begin
#     number x <- x + 20
#     writeNumber(x)
# end
# """
#         expect = "Redeclared Variable: x"
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
# func main()

# func main()

# func main()
# begin
#     if (1) writeBool(true)
#     else writeBool(false)
# end
# """
#         expect = "Redeclared Function: main"
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
    
#     def test488(self): # Confused
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

##################### ERROR TCs ##########################


#     def test452(self): ## Không lỗi vì trong forum (Khai báo array)
#         input = """
# func add(number x, number y)

# func main()
# begin
#     dynamic a
#     a[0] <- [1,2,3] 
# end

# func add(number x, number y)
#     return "Hello"
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 452))

#     def test483(self): ## Confused !!!
#         input = """
# dynamic a
# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [1, 9, 6]
#     writeNumber(a[0])
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(9.0), NumLit(6.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 483))
     
    
#     def test489(self): # Confused
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
#         expect = "Type Mismatch In Expression: CallExpr(Id(test), [NumLit(2018.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 489))
    
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


####################### TC array #####################

    # def test_001(self):
    #     input = """var a <- [[1,2],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    
    # def test_002(self):
    #     input = """
    #     string b
    #     var a <- [[1,2,4],[1,2,3],[b,b,b]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
        
    # def test_003(self):
    #     input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    # def test_004(self):
    #     input = """
    #     dynamic t
    #     var a <- [[1,2],[1,t],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    # def test_005(self):
    #     input = """
    #     dynamic ans
    #     dynamic temp <- "abc"
    #     var a <- [[1,2],[1,ans],[temp,ans]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(ans)), ArrayLit(Id(temp), Id(ans)))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    # def test_006(self):
    #     input = """
    #     dynamic ans
    #     number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    # def test_007(self):
    #     input = """number a[2,3] <- [[2,3],[2,3]]
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    # def test_008(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2,3] <- [[b,t,d],[c,e,f]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    # def test_009(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_010(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    
#     def test455(self):
#         input = """

#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic e
#     number arr[2, 2] <- [[a, b]]
#     ## number c[2, 2] <- arr

# """
#         expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
#         self.assertTrue(TestChecker.test(input, expect, 455))
        
        
#     def test485(self):
#         input = """
# dynamic a
# func main()
# begin
#     dynamic b
#     dynamic c
#     dynamic d
#     var e <- 1
#     var x <- [a, [[b]], [ [ [d, e] ] ] ]
#     ## c <- [-10, 2 / 3 % 0.75]
#     ## b <- [c]
#     ## a <- [b]
#     ## var arr <- [[1,2,3], [1,2,3], [7,8,9]]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 485))