import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
        300-309: Types & Literals
        310-324: Declarations
        325-344: Expressions
        345-374: Statements
        375-399: Mixed Cases
    """

    ##### TYPES & LITERALS #####
    def test300_single_atomic_types(self):
        input = """
            number x
            string y
            bool z
        """
        expect = """Program([VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), StringType, None, None), VarDecl(Id(z), BoolType, None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test301_inferred_types(self):
        input = """
            var x <- 2
            dynamic y
        """
        expect = """Program([VarDecl(Id(x), None, var, NumLit(2.0)), VarDecl(Id(y), None, dynamic, None)])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test302_array_types(self):
        input = """number x[5]
        """
        expect = """Program([\
VarDecl(Id(x), ArrayType([5.0], NumberType), None, None)\
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test303_atomic_types_with_init(self):
        input = """
            number x <- 5
            number y <- 5.5e5
            string z <- "55"
            bool t <- true
        """
        expect = """Program([\
VarDecl(Id(x), NumberType, None, NumLit(5.0)), \
VarDecl(Id(y), NumberType, None, NumLit(550000.0)), \
VarDecl(Id(z), StringType, None, StringLit(55)), \
VarDecl(Id(t), BoolType, None, BooleanLit(True))\
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test304_array_types_with_init(self):
        input = """number x[5] <- [1,2,3,4,5]
        """
        expect = """Program([\
VarDecl(Id(x), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)))\
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test305_inferred_types_with_init(self):
        input = """
            var x <- "vankha"
            dynamic y
        """
        expect = """Program([\
VarDecl(Id(x), None, var, StringLit(vankha)), \
VarDecl(Id(y), None, dynamic, None)\
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test306_assign_with_basic_literal(self):
        input = """
            func main()
            begin
                a <- 1
                b <- 1.1
                c <- "c"
                d <- false
            end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([AssignStmt(Id(a), NumLit(1.0)), \
AssignStmt(Id(b), NumLit(1.1)), \
AssignStmt(Id(c), StringLit(c)), \
AssignStmt(Id(d), BooleanLit(False))\
]))])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test307_assign_with_array_literal(self):
        input = """func main()
            begin
            a <- [1,2,3,4]
            b <- [1]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))), \
AssignStmt(Id(b), ArrayLit(NumLit(1.0)))\
]))])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test308_assign_with_multiD_array_literal(self):
        input = """func main()
            begin
            a <- [1,[2,[3,4]]]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), ArrayLit(NumLit(1.0), ArrayLit(NumLit(2.0), ArrayLit(NumLit(3.0), NumLit(4.0)))))\
]))])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test309_assign_with_mixed_array_literal(self):
        input = """func main()
            begin
            a <- ["1",2,false,abc,abcd()]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), ArrayLit(StringLit(1), NumLit(2.0), BooleanLit(False), Id(abc), CallExpr(Id(abcd), [])))\
]))])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    ##### DECLARATIONS #####
    def test310_short_vardecl(self):
        input = """number x
        """
        expect = str(Program([VarDecl(Id("x"), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test311_full_vardecl(self):
        input = """var x <- 1
                    number y <- 2
                    number z <- 3
        """
        expect = """Program([\
VarDecl(Id(x), None, var, NumLit(1.0)), \
VarDecl(Id(y), NumberType, None, NumLit(2.0)), \
VarDecl(Id(z), NumberType, None, NumLit(3.0))\
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test312_vardecls(self):
        input = """number x <- 1
                    number y <- 2
                    number z <- 3
                string a
                string b
        """
        expect = """Program([VarDecl(Id(x), NumberType, None, NumLit(1.0)), VarDecl(Id(y), NumberType, None, NumLit(2.0)), VarDecl(Id(z), NumberType, None, NumLit(3.0)), VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test313_full_vardecl_simple_expr(self):
        input = """number x <- a
                number y <- b
                number z <- c
        """
        expect = """Program([VarDecl(Id(x), NumberType, None, Id(a)), VarDecl(Id(y), NumberType, None, Id(b)), VarDecl(Id(z), NumberType, None, Id(c))])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test314_full_vardecl_complex_expr(self):
        input = """number x <- hello()
                    number y <- a+5
                    number z <- not b
                """
        expect = """Program([VarDecl(Id(x), NumberType, None, CallExpr(Id(hello), [])), VarDecl(Id(y), NumberType, None, BinaryOp(+, Id(a), NumLit(5.0))), VarDecl(Id(z), NumberType, None, UnaryOp(not, Id(b)))])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test315_empty_funcdecl(self):
        input = """func main() begin 
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test316_simple_empty_params_funcdecl(self):
        input = """func main (number a,string b,bool c,number d) begin 
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[VarDecl(Id(a), NumberType, None, None), \
VarDecl(Id(b), StringType, None, None), \
VarDecl(Id(c), BoolType, None, None), \
VarDecl(Id(d), NumberType, None, None)], \
Block([]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test317_inherit_empty_funcdecl(self):
        input = """func main(number a, string b) begin 
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None)], Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test318_normal_funcdecl(self):
        input = """func main()
            begin
                a <- a+1
                writeNumber(a)
            end
            """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0))), \
CallStmt(Id(writeNumber), [Id(a)])]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test319_inherit_out_funcdecl(self):
        input = """func main(number c) begin 
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[VarDecl(Id(c), NumberType, None, None)], \
Block([]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test320_mixed_decl1(self):
        input = """number x <- 1
        func main()
            begin
                x <- x+1
            end
        """
        expect = """Program([\
VarDecl(Id(x), NumberType, None, NumLit(1.0)), \
FuncDecl(Id(main), \
[], \
Block([AssignStmt(Id(x), BinaryOp(+, Id(x), NumLit(1.0)))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test321_mixed_decl2(self):
        input = """number x
        func main()
            begin
                number x <- 2.0
            end
        """
        expect = """Program([\
VarDecl(Id(x), NumberType, None, None), \
FuncDecl(Id(main), \
[], \
Block([VarDecl(Id(x), NumberType, None, NumLit(2.0))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test322_mixed_decl3(self):
        input = """
        func getTotal(number x, number y)
        begin
            return x+y
        end
        func main()
        begin
            number x <- getTotal(1,2)
        end
        """
        expect = """Program([\
FuncDecl(Id(getTotal), \
[VarDecl(Id(x), NumberType, None, None), \
VarDecl(Id(y), NumberType, None, None)], \
Block([Return(BinaryOp(+, Id(x), Id(y)))])), \
FuncDecl(Id(main), \
[], \
Block([\
VarDecl(Id(x), NumberType, None, CallExpr(Id(getTotal), [NumLit(1.0), NumLit(2.0)]))\
]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test323_mixed_decl4(self):
        input = """number x[2] <- [1,2]
        func main()
        begin
            x <- [1,2,3]
        end
        """
        expect = """Program([\
VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0))), \
FuncDecl(Id(main), \
[], \
Block([AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test324_mixed_decl5(self):
        input = """number x[2] <- [1,2]
        func main()
        begin
            print(x)
            return
        end
        """
        expect = """Program([\
VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0))), \
FuncDecl(Id(main), \
[], \
Block([CallStmt(Id(print), [Id(x)]), \
Return()]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    ##### EXPRESSIONS #####
    def test325_empty_call_expr(self):
        input = """
        func main()
        begin
            hello()
            good_boy()
            are_you_ok()
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
CallStmt(Id(hello), []), \
CallStmt(Id(good_boy), []), \
CallStmt(Id(are_you_ok), [])]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test326_index_1D_ops(self):
        input = """
        func main()
        begin
            a[0] <- 5
            b[1] <- "string"
            c[3] <- 0.5e6
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(5.0)), \
AssignStmt(ArrayCell(Id(b), [NumLit(1.0)]), StringLit(string)), \
AssignStmt(ArrayCell(Id(c), [NumLit(3.0)]), NumLit(500000.0))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test327_index_ND_ops(self):
        input = """
        func main()
        begin
            b[0,1] <- "string"
            c[1,2,3] <- 0.5e6
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(ArrayCell(Id(b), [NumLit(0.0), NumLit(1.0)]), StringLit(string)), \
AssignStmt(ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), NumLit(500000.0))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test328_param_lit_call_expr(self):
        input = """
        func main()
        begin
            hello(1)
            good_boy("Sang","Kha")
            are_you_ok(true)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
CallStmt(Id(hello), [NumLit(1.0)]), \
CallStmt(Id(good_boy), [StringLit(Sang), StringLit(Kha)]), \
CallStmt(Id(are_you_ok), [BooleanLit(True)])]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test329_param_id_call_expr(self):
        input = """
        func main()
        begin
            hello(a)
            good_boy(b,e)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
CallStmt(Id(hello), [Id(a)]), \
CallStmt(Id(good_boy), [Id(b), Id(e)])]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test330_nested_func_call(self):
        input = """
        func main()
        begin
            foo(foo(2),5,foo())
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
CallStmt(Id(foo), [CallExpr(Id(foo), [NumLit(2.0)]), NumLit(5.0), CallExpr(Id(foo), [])])]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test331_unary_operator(self):
        input = """
        func main()
        begin
            a <- -4
            a <- --4
            a <- not true
            a <- b[5]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), UnaryOp(-, NumLit(4.0))), \
AssignStmt(Id(a), UnaryOp(-, UnaryOp(-, NumLit(4.0)))), \
AssignStmt(Id(a), UnaryOp(not, BooleanLit(True))), \
AssignStmt(Id(a), ArrayCell(Id(b), [NumLit(5.0)]))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test332_nested_array(self):
        input = """
        func main()
        begin
            a <- [1,2,3,[4,5,6]]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0))))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test333_multivar_array(self):
        input = """
        func main()
        begin
            b <- a[1,2,3]
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(b), ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test334_binary_operator(self):
        input = """
        func main()
        begin
            a <- 1*b
            a <- true and false
            a <- a==b
            a <- a!=b
            a <- (a...b)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), BinaryOp(*, NumLit(1.0), Id(b))), \
AssignStmt(Id(a), BinaryOp(and, BooleanLit(True), BooleanLit(False))), \
AssignStmt(Id(a), BinaryOp(==, Id(a), Id(b))), \
AssignStmt(Id(a), BinaryOp(!=, Id(a), Id(b))), \
AssignStmt(Id(a), BinaryOp(..., Id(a), Id(b)))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test335_complex_binary_operator(self):
        input = """
        func main()
        begin
            a <- a*b*c + a/b/c
            a <- a + b%c + d
            a <- a and b or a
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), Id(c)), BinaryOp(/, BinaryOp(/, Id(a), Id(b)), Id(c)))), \
AssignStmt(Id(a), BinaryOp(+, BinaryOp(+, Id(a), BinaryOp(%, Id(b), Id(c))), Id(d))), \
AssignStmt(Id(a), BinaryOp(or, BinaryOp(and, Id(a), Id(b)), Id(a)))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test336_complex_binary_operator_with_paren1(self):
        input = """
        func main()
        begin
            a <- a*b*(c+a)/b/c
            a <- a + (b%c + d)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
AssignStmt(Id(a), BinaryOp(/, BinaryOp(/, BinaryOp(*, BinaryOp(*, Id(a), Id(b)), BinaryOp(+, Id(c), Id(a))), Id(b)), Id(c))), \
AssignStmt(Id(a), BinaryOp(+, Id(a), BinaryOp(+, BinaryOp(%, Id(b), Id(c)), Id(d))))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test337_complex_binary_operator_with_paren2(self):
        input = """
        func main()
        begin
            a <- (a and b) or (a>=b and b)
            a <- (a + (-b - c*(d+e)))*5
            a <- a...((b...c)...d)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(or, BinaryOp(and, Id(a), Id(b)), BinaryOp(>=, Id(a), BinaryOp(and, Id(b), Id(b))))), AssignStmt(Id(a), BinaryOp(*, BinaryOp(+, Id(a), BinaryOp(-, UnaryOp(-, Id(b)), BinaryOp(*, Id(c), BinaryOp(+, Id(d), Id(e))))), NumLit(5.0))), AssignStmt(Id(a), BinaryOp(..., Id(a), BinaryOp(..., BinaryOp(..., Id(b), Id(c)), Id(d))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test338_numeric_left_to_right(self):
        input = """
        func main()
        begin
            a <- b*c/d%e
            a <- b+c-d+e
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(%, BinaryOp(/, BinaryOp(*, Id(b), Id(c)), Id(d)), Id(e))), AssignStmt(Id(a), BinaryOp(+, BinaryOp(-, BinaryOp(+, Id(b), Id(c)), Id(d)), Id(e)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test339_logic_left_to_right(self):
        input = """
        func main()
        begin
            a <- b and c or d
            a <- b or c and d
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(or, BinaryOp(and, Id(b), Id(c)), Id(d))), AssignStmt(Id(a), BinaryOp(and, BinaryOp(or, Id(b), Id(c)), Id(d)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test340_relational_nonassoc(self):
        input = """
        func main()
        begin
            a <- b and c
            a <- b!=c
            a <- b>=c
            a <- b<=c
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(and, Id(b), Id(c))), AssignStmt(Id(a), BinaryOp(!=, Id(b), Id(c))), AssignStmt(Id(a), BinaryOp(>=, Id(b), Id(c))), AssignStmt(Id(a), BinaryOp(<=, Id(b), Id(c)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test341_string_nonassoc(self):
        input = """
        func main()
        begin
            a <- b...c
            a <- b...(c...d)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(..., Id(b), Id(c))), AssignStmt(Id(a), BinaryOp(..., Id(b), BinaryOp(..., Id(c), Id(d))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test342_funccall(self):
        input = """
        func main()
        begin
            t <- getA(a) ... getB(b)
            number x <- getX(x)
            a[1] <- getA1(a[0])
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(t), BinaryOp(..., CallExpr(Id(getA), [Id(a)]), CallExpr(Id(getB), [Id(b)]))), VarDecl(Id(x), NumberType, None, CallExpr(Id(getX), [Id(x)])), AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), CallExpr(Id(getA1), [ArrayCell(Id(a), [NumLit(0.0)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test343_full_order1(self):
        input = """
        func main()
        begin
            a <- -7+6/3/2*3-4%2
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(-, BinaryOp(+, UnaryOp(-, NumLit(7.0)), BinaryOp(*, BinaryOp(/, BinaryOp(/, NumLit(6.0), NumLit(3.0)), NumLit(2.0)), NumLit(3.0))), BinaryOp(%, NumLit(4.0), NumLit(2.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test344_full_order2(self):
        input = """
        func main()
        begin
            a <- (-a + not b) * e[6] and b  >= 6
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(>=, BinaryOp(and, BinaryOp(*, BinaryOp(+, UnaryOp(-, Id(a)), UnaryOp(not, Id(b))), ArrayCell(Id(e), [NumLit(6.0)])), Id(b)), NumLit(6.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    ##### STATEMENTS #####
    def test345_scalar_asm(self):
        input = """
        func main()
        begin
            a <- 5
            b <- "ez"
            c <- 0.2e-3
            d <- [a,b,c,d]
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(5.0)), AssignStmt(Id(b), StringLit(ez)), AssignStmt(Id(c), NumLit(0.0002)), AssignStmt(Id(d), ArrayLit(Id(a), Id(b), Id(c), Id(d)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test346_indexops_asm(self):
        input = """
        func main()
        begin
            a[0] <- 2
            a[1,2,3] <- 1
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(2.0)), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test347_complex_asm(self):
        input = """
        func main()
        begin
            a[0] <- foo(1,2,"3")
            a[1,2] <- omg(omg(1))
            ez <- ez*2 + 6*(7-foo())
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0), StringLit(3)])), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(omg), [CallExpr(Id(omg), [NumLit(1.0)])])), AssignStmt(Id(ez), BinaryOp(+, BinaryOp(*, Id(ez), NumLit(2.0)), BinaryOp(*, NumLit(6.0), BinaryOp(-, NumLit(7.0), CallExpr(Id(foo), [])))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test348_normal_if(self):
        input = """
        func main()
        begin
            if(is_easy("PPL")==true)
                begin
                    printString("de the co a")
                end
            else begin
                    printString("hoc lai di em")
                end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(is_easy), [StringLit(PPL)]), BooleanLit(True)), Block([CallStmt(Id(printString), [StringLit(de the co a)])])), [], Block([CallStmt(Id(printString), [StringLit(hoc lai di em)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    
    def test349_if_sequence(self):
        input = """
        func main()
        begin
            if(a)
                begin
                end
            elif (b)
                begin
                end
            else begin
                end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((Id(a), Block([])), [(Id(b), Block([]))], Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test350_if_nested1(self):
        input = """
        func main()
        begin
            if(calc_score(score)==9)
            begin
                printString("idolll :3")
            end
            else begin
                if (calc_score(score)==5)
                begin
                    printString("vua du qua mon")
                end
                else begin
                    printString("doan xem")
                end
            end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(calc_score), [Id(score)]), NumLit(9.0)), Block([CallStmt(Id(printString), [StringLit(idolll :3)])])), [], Block([If((BinaryOp(==, CallExpr(Id(calc_score), [Id(score)]), NumLit(5.0)), Block([CallStmt(Id(printString), [StringLit(vua du qua mon)])])), [], Block([CallStmt(Id(printString), [StringLit(doan xem)])]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test351_if_nested2(self):
        input = """
        func main()
        begin
            if(rich==true)
            begin
                if(nice==true)
                begin
                    setState("kind and rich")
                end
                else setState("unkind and rich")
            end 
            else setState("not rich")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, Id(rich), BooleanLit(True)), Block([If((BinaryOp(==, Id(nice), BooleanLit(True)), Block([CallStmt(Id(setState), [StringLit(kind and rich)])])), [], CallStmt(Id(setState), [StringLit(unkind and rich)]))])), [], CallStmt(Id(setState), [StringLit(not rich)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test352_if_oneline(self):
        input = """
        func main()
        begin
            if(happy) setHappy(true)
            else setHappy(false)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), [], \
Block([\
If(\
(Id(happy), CallStmt(Id(setHappy), [BooleanLit(True)])), \
[], \
CallStmt(Id(setHappy), [BooleanLit(False)])\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test353_if_oneline_nested(self):
        input = """
        func main()
        begin
            if(rich==true)
                if(nice==true)
                    setState("kind and rich")
                else setState("unkind and rich")
            else setState("not rich")
        end
        """
        expect = """Program([\
FuncDecl(Id(main), [], \
Block([\
If(\
(BinaryOp(==, Id(rich), BooleanLit(True)), If((BinaryOp(==, Id(nice), BooleanLit(True)), CallStmt(Id(setState), [StringLit(kind and rich)])), [], CallStmt(Id(setState), [StringLit(unkind and rich)]))), \
[], \
CallStmt(Id(setState), [StringLit(not rich)])\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test354_normal_loop(self):
        input = """
        func main()
        begin
            for i until i<=5 by i+2
            begin
                printNumber("Yoooo!")
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main), [], \
Block([\
For(Id(i), \
BinaryOp(<=, Id(i), NumLit(5.0)), \
BinaryOp(+, Id(i), NumLit(2.0)), \
Block([\
CallStmt(Id(printNumber), [StringLit(Yoooo!)])\
])\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test355_nested_forloop(self):
        input = """
        func main()
        begin
            for i until i<5*2 by i+2
            begin
                for j until j<5*2 by j+1
                begin
                    printNumber(i+j)
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main), [], \
Block([\
For(Id(i), \
BinaryOp(<, Id(i), BinaryOp(*, NumLit(5.0), NumLit(2.0))), \
BinaryOp(+, Id(i), NumLit(2.0)), \
Block([\
For(Id(j), \
BinaryOp(<, Id(j), BinaryOp(*, NumLit(5.0), NumLit(2.0))), \
BinaryOp(+, Id(j), NumLit(1.0)), \
Block([\
CallStmt(Id(printNumber), [BinaryOp(+, Id(i), Id(j))])\
])\
)\
])\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test356_normal_while(self):
        input = """
        func main()
        begin
            if (a<5)
            begin
                printNumber(a)
                a <- a+1
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main), [], \
Block([\
If(\
(BinaryOp(<, Id(a), NumLit(5.0)), Block([CallStmt(Id(printNumber), [Id(a)]), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))])), \
[], \
None\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test357_nested_while(self):
        input = """
        func main()
        begin
            number a <- 0
            if (match(a)<10)
                printNumber(a)
            elif (match(a)*match(a)<69)
                printNumber(10-a)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
VarDecl(Id(a), NumberType, None, NumLit(0.0)), \
If(\
(BinaryOp(<, CallExpr(Id(match), [Id(a)]), NumLit(10.0)), CallStmt(Id(printNumber), [Id(a)])), \
[\
(BinaryOp(<, BinaryOp(*, CallExpr(Id(match), [Id(a)]), CallExpr(Id(match), [Id(a)])), NumLit(69.0)), CallStmt(Id(printNumber), [BinaryOp(-, NumLit(10.0), Id(a))]))\
], \
None\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test358_normal_dowhile(self):
        input = """
        func boolean () 
        begin
            if (a[10] >= 100 ) a <- a + 1
            elif (a[1,1] == 10)  writeNumber(1)
            elif (a[-1, 10]  or false) b[-1] <- 10
            else return foo(2 + 2)
        end
        """
        expect = """Program([\
FuncDecl(Id(boolean), \
[], \
Block([\
If(\
(BinaryOp(>=, ArrayCell(Id(a), [NumLit(10.0)]), NumLit(100.0)), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), \
[\
(BinaryOp(==, ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), NumLit(10.0)), CallStmt(Id(writeNumber), [NumLit(1.0)])), \
(BinaryOp(or, ArrayCell(Id(a), [UnaryOp(-, NumLit(1.0)), NumLit(10.0)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(b), [UnaryOp(-, NumLit(1.0))]), NumLit(10.0)))\
], \
Return(CallExpr(Id(foo), [BinaryOp(+, NumLit(2.0), NumLit(2.0))]))\
)\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test359_nested_block(self):
        input = """
        ## khai bao ham func
        func integer () 
        begin
            begin
            begin
                if (a[10] >= 100 )
                    if (a[1,1] == 10)  printInteger(1)
                    else if (a[-1, 10]  or false) b[-1] <- 10
            end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(integer), \
[], \
Block([\
Block([\
Block([\
If((\
BinaryOp(>=, ArrayCell(Id(a), [NumLit(10.0)]), NumLit(100.0)), \
If((BinaryOp(==, ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), NumLit(10.0)), CallStmt(Id(printInteger), [NumLit(1.0)])), [], If((BinaryOp(or, ArrayCell(Id(a), [UnaryOp(-, NumLit(1.0)), NumLit(10.0)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(b), [UnaryOp(-, NumLit(1.0))]), NumLit(10.0))), [], None))\
), \
[], \
None)\
])\
])\
])\
)\
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test360_break_and_return(self):
        input = """
        func main()
        begin
            for i until i<2 by i+1
            begin
                if(i==t)
                    break
                elif(i<0)
                    continue
                else printNumber(i)
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
For(Id(i), \
BinaryOp(<, Id(i), NumLit(2.0)), \
BinaryOp(+, Id(i), NumLit(1.0)), \
Block([\
If(\
(BinaryOp(==, Id(i), Id(t)), Break), \
[(BinaryOp(<, Id(i), NumLit(0.0)), Continue)], \
CallStmt(Id(printNumber), [Id(i)])\
)\
])\
)\
]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test361_mixed_loop(self):
        input = """
        func main()
        begin
            for i until i<getMax() by i+1
            begin
                if (true)
                begin
                    print("kaka")
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
For(Id(i), \
BinaryOp(<, Id(i), CallExpr(Id(getMax), [])), \
BinaryOp(+, Id(i), NumLit(1.0)), \
Block([\
If((BooleanLit(True), Block([CallStmt(Id(print), [StringLit(kaka)])])), [], None)\
]))\
]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test362_oneline_loop(self):
        input = """
        func main()
        begin
            number k <- 5
            for i until i<getMax() by i+1
                printNumber(i)
        end
        """
        expect = """Program([\
FuncDecl(Id(main), \
[], \
Block([\
VarDecl(Id(k), NumberType, None, NumLit(5.0)), \
For(Id(i), \
BinaryOp(<, Id(i), CallExpr(Id(getMax), [])), \
BinaryOp(+, Id(i), NumLit(1.0)), \
CallStmt(Id(printNumber), [Id(i)]))]))\
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test363_normal_call(self):
        input = """
        func main()
        begin
            hello()
            hello("Sang")
            hello("Sang","Kha")
            hello(hello("Sang"),"Kha")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(hello), []), CallStmt(Id(hello), [StringLit(Sang)]), CallStmt(Id(hello), [StringLit(Sang), StringLit(Kha)]), CallStmt(Id(hello), [CallExpr(Id(hello), [StringLit(Sang)]), StringLit(Kha)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test364_nested_call(self):
        input = """
        func main()
        begin
            f(f())
            f(f(f(f(f()))))
            f(f(f(f(f(f())))),f(f(f(f(f())))))
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(f), [CallExpr(Id(f), [])]), CallStmt(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [])])])])]), CallStmt(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [])])])])]), CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [CallExpr(Id(f), [])])])])])])]))])"""    
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test365_expr_call(self):
        input = """
        func main()
        begin   
            f(1*x,_123,"sss"..."aaa",dsa("dsa"),x%5)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(f), [BinaryOp(*, NumLit(1.0), Id(x)), Id(_123), BinaryOp(..., StringLit(sss), StringLit(aaa)), CallExpr(Id(dsa), [StringLit(dsa)]), BinaryOp(%, Id(x), NumLit(5.0))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test366_normal_block(self):
        input = """
        func main()
        begin
            begin
            end
            begin 
                hello()
            end
            begin 
                number a <- 1
            end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([Block([]), Block([CallStmt(Id(hello), [])]), Block([VarDecl(Id(a), NumberType, None, NumLit(1.0))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test367_normal_return(self):
        input = """
            func hello()
            begin
                printString("hello")
            end
            func one (number x)
            begin
                return 1
            end
        """
        expect = """Program([FuncDecl(Id(hello), [], Block([CallStmt(Id(printString), [StringLit(hello)])])), FuncDecl(Id(one), [VarDecl(Id(x), NumberType, None, None)], Block([Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test368_complex_return(self):
        input = """
            func isOdd(number x)
            begin
                return x!=0
            end
            func getArr(number x)
            begin
                return [x,x*2,x*3]
            end
        """
        expect = """Program([FuncDecl(Id(isOdd), [VarDecl(Id(x), NumberType, None, None)], Block([Return(BinaryOp(!=, Id(x), NumLit(0.0)))])), FuncDecl(Id(getArr), [VarDecl(Id(x), NumberType, None, None)], Block([Return(ArrayLit(Id(x), BinaryOp(*, Id(x), NumLit(2.0)), BinaryOp(*, Id(x), NumLit(3.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test369_single_if(self):
        input = """
        func main()
        begin   
            if(a==1) return 1
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, Id(a), NumLit(1.0)), Return(NumLit(1.0))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test370_empty_loops(self):
        input = """
        func main()
        begin   
            for i until i<5 by i+1
            begin 
            end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(5.0)), BinaryOp(+, Id(i), NumLit(1.0)), Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test371_idx_for_loops(self):
        input = """
        func main()
        begin   
            begin
                for i until v < 10 by 1
                    return a
            end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([Block([For(Id(i), BinaryOp(<, Id(v), NumLit(10.0)), NumLit(1.0), Return(Id(a)))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test372_idx_for_loops(self):
        input = """
        func main()
        begin   
            var i <- 5
            for i until i<5 by i+1 
                begin 
                end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(5.0)), For(Id(i), BinaryOp(<, Id(i), NumLit(5.0)), BinaryOp(+, Id(i), NumLit(1.0)), Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test373_if_stmt_1(self):
        input = """func integer () 
        begin
            break
            if (true) a <- 1 + 1
            else b <- b
        end
        """
        expect = """Program([FuncDecl(Id(integer), [], Block([Break, If((BooleanLit(True), AssignStmt(Id(a), BinaryOp(+, NumLit(1.0), NumLit(1.0)))), [], AssignStmt(Id(b), Id(b)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test374_if_nested_2(self):
        input = """func integer () 
        begin
            if (a + 1 and true)
                if (a + 1 and true)
                    if (a + 1 and true)
                        if (a + 1 and true)
                            if (a + 1 and true)
                                continue
        end
        """
        expect = """Program([FuncDecl(Id(integer), [], Block([If((BinaryOp(and, BinaryOp(+, Id(a), NumLit(1.0)), BooleanLit(True)), If((BinaryOp(and, BinaryOp(+, Id(a), NumLit(1.0)), BooleanLit(True)), If((BinaryOp(and, BinaryOp(+, Id(a), NumLit(1.0)), BooleanLit(True)), If((BinaryOp(and, BinaryOp(+, Id(a), NumLit(1.0)), BooleanLit(True)), If((BinaryOp(and, BinaryOp(+, Id(a), NumLit(1.0)), BooleanLit(True)), Continue), [], None)), [], None)), [], None)), [], None)), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    #### MIXED CASES #####
    def test375_simple_program(self):
        """Simple program"""
        input = """func main ()
        begin
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test376_more_complex_program(self):
        """More complex program"""
        input = """func main ()
        begin
            printNumber(4)
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([CallStmt(Id(printNumber), [NumLit(4.0)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test377_full_decl_program(self):
        input = """
        number i <- 6
        func main ()
            begin
                number x <- 7
            end
        number j <- 8
        func foo ()
            begin
                number y <- 8
            end
        """
        expect = """Program([VarDecl(Id(i), NumberType, None, NumLit(6.0)), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, NumLit(7.0))])), VarDecl(Id(j), NumberType, None, NumLit(8.0)), FuncDecl(Id(foo), [], Block([VarDecl(Id(y), NumberType, None, NumLit(8.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test378_full_stmt_program_1(self):
        input = """func main ()
        begin
            ## cond stmt
            if (a>1)
            begin
                a <- 1
            end
            elif (a<1)
            begin
                a <- 0
            end
            else begin
                a <- 0.5
            end
            ## iter stmt
            if (a>0)
            begin
                a <- a*0.4
                print(a)
                if (a<1) break
            end
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(>, Id(a), NumLit(1.0)), Block([AssignStmt(Id(a), NumLit(1.0))])), [(BinaryOp(<, Id(a), NumLit(1.0)), Block([AssignStmt(Id(a), NumLit(0.0))]))], Block([AssignStmt(Id(a), NumLit(0.5))])), If((BinaryOp(>, Id(a), NumLit(0.0)), Block([AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(0.4))), CallStmt(Id(print), [Id(a)]), If((BinaryOp(<, Id(a), NumLit(1.0)), Break), [], None)])), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test379_full_stmt_program_2(self):
        input = """func main ()
        begin
            number a
            if (a>0)
                for a  until a>0 by a-1
                    if (a>5) print("a>5")
                    else continue
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(>, Id(a), NumLit(0.0)), For(Id(a), BinaryOp(>, Id(a), NumLit(0.0)), BinaryOp(-, Id(a), NumLit(1.0)), If((BinaryOp(>, Id(a), NumLit(5.0)), CallStmt(Id(print), [StringLit(a>5)])), [], Continue))), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test380_binary_search(self):
        input = """
            func binarySearch (number arr, number x, number low, number high)
            begin
                if (low>high) return -1
                else begin
                    number mid <- (low+high)/2
                    if (x == arr[mid]) return mid
                    else if (x > arr[mid]) return binarySearch(arr,x,mid+1,high)
                    else return binarySearch(arr,x,low,mid-1)
                end
            end
        """
        expect = """Program([FuncDecl(Id(binarySearch), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(x), NumberType, None, None), VarDecl(Id(low), NumberType, None, None), VarDecl(Id(high), NumberType, None, None)], Block([If((BinaryOp(>, Id(low), Id(high)), Return(UnaryOp(-, NumLit(1.0)))), [], Block([VarDecl(Id(mid), NumberType, None, BinaryOp(/, BinaryOp(+, Id(low), Id(high)), NumLit(2.0))), If((BinaryOp(==, Id(x), ArrayCell(Id(arr), [Id(mid)])), Return(Id(mid))), [], If((BinaryOp(>, Id(x), ArrayCell(Id(arr), [Id(mid)])), Return(CallExpr(Id(binarySearch), [Id(arr), Id(x), BinaryOp(+, Id(mid), NumLit(1.0)), Id(high)]))), [], Return(CallExpr(Id(binarySearch), [Id(arr), Id(x), Id(low), BinaryOp(-, Id(mid), NumLit(1.0))]))))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test381_interpolation_search(self):
        input = """
            func interpolationSearch(number arr, number lo, number hi, number x)
            begin
                if ((lo <= hi) and (x >= arr[lo]) and (x <= arr[hi]))
                begin
                    ## Probing the position with keeping
                    ## uniform distribution in mind.
                    pos <- lo + ((hi - lo) / (arr[hi] - arr[lo]) * (x - arr[lo]))
                    
                    ## Condition of target found
                    if (arr[pos] == x)
                        return pos
            
                    ## If x is larger, x is in right subarray
                    if (arr[pos] < x)
                        return interpolationSearch(arr, pos + 1, hi, x)
            
                    ## If x is smaller, x is in left subarray
                    if (arr[pos] > x)
                        return interpolationSearch(arr, lo, pos - 1, x)
                end
            return -1
            end
        """
        expect = """Program([FuncDecl(Id(interpolationSearch), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(lo), NumberType, None, None), VarDecl(Id(hi), NumberType, None, None), VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(and, BinaryOp(and, BinaryOp(<=, Id(lo), Id(hi)), BinaryOp(>=, Id(x), ArrayCell(Id(arr), [Id(lo)]))), BinaryOp(<=, Id(x), ArrayCell(Id(arr), [Id(hi)]))), Block([AssignStmt(Id(pos), BinaryOp(+, Id(lo), BinaryOp(*, BinaryOp(/, BinaryOp(-, Id(hi), Id(lo)), BinaryOp(-, ArrayCell(Id(arr), [Id(hi)]), ArrayCell(Id(arr), [Id(lo)]))), BinaryOp(-, Id(x), ArrayCell(Id(arr), [Id(lo)]))))), If((BinaryOp(==, ArrayCell(Id(arr), [Id(pos)]), Id(x)), Return(Id(pos))), [], None), If((BinaryOp(<, ArrayCell(Id(arr), [Id(pos)]), Id(x)), Return(CallExpr(Id(interpolationSearch), [Id(arr), BinaryOp(+, Id(pos), NumLit(1.0)), Id(hi), Id(x)]))), [], None), If((BinaryOp(>, ArrayCell(Id(arr), [Id(pos)]), Id(x)), Return(CallExpr(Id(interpolationSearch), [Id(arr), Id(lo), BinaryOp(-, Id(pos), NumLit(1.0)), Id(x)]))), [], None)])), [], None), Return(UnaryOp(-, NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test382_selection_sort(self):
        input = """
            func selectionSort(number arr, number n)
            begin
                number i 
                number j 
                number min_idx 
                ## One by one move boundary of
                ## unsorted subarray
                for i until i < n-1 by i+1
                begin
                    ## Find the minimum element in
                    ## unsorted array
                    min_idx <- i
                    for j until j < n by j+1
                    begin
                        if (arr[j] < arr[min_idx])
                            min_idx <- j
                    end
                    ## Swap the found minimum element
                    ## with the first element
                    if (min_idx!=i)
                        swap(arr[min_idx], arr[i])
                end
            end
        """
        expect = """Program([FuncDecl(Id(selectionSort), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(min_idx), NumberType, None, None), For(Id(i), BinaryOp(<, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), BinaryOp(+, Id(i), NumLit(1.0)), Block([AssignStmt(Id(min_idx), Id(i)), For(Id(j), BinaryOp(<, Id(j), Id(n)), BinaryOp(+, Id(j), NumLit(1.0)), Block([If((BinaryOp(<, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j))), [], None)])), If((BinaryOp(!=, Id(min_idx), Id(i)), CallStmt(Id(swap), [ArrayCell(Id(arr), [Id(min_idx)]), ArrayCell(Id(arr), [Id(i)])])), [], None)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test383_merge_sort(self):
        input = """
            func mergeSort (number y[100], number n, number m)
            begin
                if (m > n)
                    return 
                ## Returns recursively
            
                var mid <- m + (n - m) / 2
                mergeSort(arr, m, mid)
                mergeSort(arr, mid + 1, n)
                merge(arr, m, mid, n)
            end
        """
        expect = """Program([FuncDecl(Id(mergeSort), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([If((BinaryOp(>, Id(m), Id(n)), Return()), [], None), VarDecl(Id(mid), None, var, BinaryOp(+, Id(m), BinaryOp(/, BinaryOp(-, Id(n), Id(m)), NumLit(2.0)))), CallStmt(Id(mergeSort), [Id(arr), Id(m), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(n)]), CallStmt(Id(merge), [Id(arr), Id(m), Id(mid), Id(n)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test384_quick_sort(self):
        input = """
            func quickSort(number y[100], number n, number m)
            begin
                if (low < high) 
                begin
                    ## pi is partitioning index, arr[p] is now at right place
                    number pi <- partition(arr, low, high)
            
                    ## Separately sort elements before
                    ## partition and after partition
                    quickSort(arr, low, pi - 1)
                    quickSort(arr, pi + 1, high)
                end
            end
        """
        expect = """Program([FuncDecl(Id(quickSort), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([If((BinaryOp(<, Id(low), Id(high)), Block([VarDecl(Id(pi), NumberType, None, CallExpr(Id(partition), [Id(arr), Id(low), Id(high)])), CallStmt(Id(quickSort), [Id(arr), Id(low), BinaryOp(-, Id(pi), NumLit(1.0))]), CallStmt(Id(quickSort), [Id(arr), BinaryOp(+, Id(pi), NumLit(1.0)), Id(high)])])), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test385_heap_sort(self):
        input = """
            func heapSort(number y[100], number n, number m)
            begin
                ## Build heap (rearrange array)
                for i until i >= 0 by i-1
                    heapify(arr, N, i)
            
                ## One by one extract an element
                ## from heap
                for i until i > 0 by i-1 
                begin
                    ## Move current root to end
                    swap(arr[0], arr[i])
            
                    ## call max heapify on the reduced heap
                    heapify(arr, i, 0)
                end
            end
        """
        expect = """Program([FuncDecl(Id(heapSort), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([For(Id(i), BinaryOp(>=, Id(i), NumLit(0.0)), BinaryOp(-, Id(i), NumLit(1.0)), CallStmt(Id(heapify), [Id(arr), Id(N), Id(i)])), For(Id(i), BinaryOp(>, Id(i), NumLit(0.0)), BinaryOp(-, Id(i), NumLit(1.0)), Block([CallStmt(Id(swap), [ArrayCell(Id(arr), [NumLit(0.0)]), ArrayCell(Id(arr), [Id(i)])]), CallStmt(Id(heapify), [Id(arr), Id(i), NumLit(0.0)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test386_insertion_sort(self):
        input = """
            func insertionSort(number y[100], number n, number m)
            begin
                number i
                number key
                var j <- 2
                for i until i < n by i+1
                begin
                    key <- arr[i]
                    j <- i - 1
            
                    ## Move elements of arr[0..i-1], 
                    ## that are greater than key, to one
                    ## position ahead of their
                    ## current position
                    if ((j >= 0) and (arr[j] > key))
                    begin
                        arr[j + 1] <- arr[j]
                        j <- j - 1
                    end
                    arr[j + 1] <- key
                end
            end
        """
        expect = """Program([FuncDecl(Id(insertionSort), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(key), NumberType, None, None), VarDecl(Id(j), None, var, NumLit(2.0)), For(Id(i), BinaryOp(<, Id(i), Id(n)), BinaryOp(+, Id(i), NumLit(1.0)), Block([AssignStmt(Id(key), ArrayCell(Id(arr), [Id(i)])), AssignStmt(Id(j), BinaryOp(-, Id(i), NumLit(1.0))), If((BinaryOp(and, BinaryOp(>=, Id(j), NumLit(0.0)), BinaryOp(>, ArrayCell(Id(arr), [Id(j)]), Id(key))), Block([AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), ArrayCell(Id(arr), [Id(j)])), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), [], None), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), Id(key))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test387_find_depth_tree(self):
        input = """
            func findDepthRec(number y[100], number n, number m)
            begin
                if ((index >= n) or (tree[index] == "l"))
                    return 0
            
                ## calc height of left subtree (In preorder
                ## left subtree is processed before right)
                index <- index+1
                number left <-  findDepthRec(tree, n, index)
            
                ## calc height of right subtree
                index <- index+1
                number right  <-  findDepthRec(tree, n, index)
            
                return max(left, right) + 1
            end
            func findDepth(number y[100], number n, number m)
            begin
                number index  <-  0
                return findDepthRec(tree, n, index)
            end
        """
        expect = """Program([FuncDecl(Id(findDepthRec), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(>=, Id(index), Id(n)), BinaryOp(==, ArrayCell(Id(tree), [Id(index)]), StringLit(l))), Return(NumLit(0.0))), [], None), AssignStmt(Id(index), BinaryOp(+, Id(index), NumLit(1.0))), VarDecl(Id(left), NumberType, None, CallExpr(Id(findDepthRec), [Id(tree), Id(n), Id(index)])), AssignStmt(Id(index), BinaryOp(+, Id(index), NumLit(1.0))), VarDecl(Id(right), NumberType, None, CallExpr(Id(findDepthRec), [Id(tree), Id(n), Id(index)])), Return(BinaryOp(+, CallExpr(Id(max), [Id(left), Id(right)]), NumLit(1.0)))])), FuncDecl(Id(findDepth), [VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([VarDecl(Id(index), NumberType, None, NumLit(0.0)), Return(CallExpr(Id(findDepthRec), [Id(tree), Id(n), Id(index)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test388_lcs(self):
        input = """
            func lcs (number x[100], number y[100], number n, number m)
            begin
                if ((m == 0) or (n == 0))
                    return 0
                if (X[m-1] == Y[n-1])
                    return 1 + lcs(X, Y, m-1, n-1)
                else return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
            end
        """
        expect = """Program([FuncDecl(Id(lcs), [VarDecl(Id(x), ArrayType([100.0], NumberType), None, None), VarDecl(Id(y), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(==, Id(m), NumLit(0.0)), BinaryOp(==, Id(n), NumLit(0.0))), Return(NumLit(0.0))), [], None), If((BinaryOp(==, ArrayCell(Id(X), [BinaryOp(-, Id(m), NumLit(1.0))]), ArrayCell(Id(Y), [BinaryOp(-, Id(n), NumLit(1.0))])), Return(BinaryOp(+, NumLit(1.0), CallExpr(Id(lcs), [Id(X), Id(Y), BinaryOp(-, Id(m), NumLit(1.0)), BinaryOp(-, Id(n), NumLit(1.0))])))), [], Return(CallExpr(Id(max), [CallExpr(Id(lcs), [Id(X), Id(Y), Id(m), BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(lcs), [Id(X), Id(Y), BinaryOp(-, Id(m), NumLit(1.0)), Id(n)])])))]))])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test389_spiral_matrix(self):
        input = """
            func spiralPrint(number a[100, 100], number n, number m)
            begin
                number i <- -1
                number k <- 0
                var l <- 0
                ## k - starting row index
                ## m - ending row index
                ## l - starting column index
                ## n - ending column index
                ## i - iterator
                
            
                if ((k < m) and (l < n)) 
                begin
                    ## Print the first row
                    for i until i < n by i+1 
                    begin
                        printString(a[k,i])
                    end
                    k <- k+1
            
                    ## Print the last column
                    for i until i < m by i+1 
                    begin
                        printString(a[i,n-1])
                    end
                    n <- n-1
            
                    ## Print the last row from
                    if (k < m) 
                    begin
                        for i until i >= l by i-1 
                        begin
                            printString(a[m-1,i])
                        end
                        m <- m-1
                    end
            
                    ## Print the first column from
                    if (l < n) 
                    begin
                        for i until i >= k by i-1 
                        begin
                            printString(a[i,l])
                        end
                        l <- l+1
                    end
                end
            end
        """
        expect = """Program([FuncDecl(Id(spiralPrint), [VarDecl(Id(a), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(m), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, UnaryOp(-, NumLit(1.0))), VarDecl(Id(k), NumberType, None, NumLit(0.0)), VarDecl(Id(l), None, var, NumLit(0.0)), If((BinaryOp(and, BinaryOp(<, Id(k), Id(m)), BinaryOp(<, Id(l), Id(n))), Block([For(Id(i), BinaryOp(<, Id(i), Id(n)), BinaryOp(+, Id(i), NumLit(1.0)), Block([CallStmt(Id(printString), [ArrayCell(Id(a), [Id(k), Id(i)])])])), AssignStmt(Id(k), BinaryOp(+, Id(k), NumLit(1.0))), For(Id(i), BinaryOp(<, Id(i), Id(m)), BinaryOp(+, Id(i), NumLit(1.0)), Block([CallStmt(Id(printString), [ArrayCell(Id(a), [Id(i), BinaryOp(-, Id(n), NumLit(1.0))])])])), AssignStmt(Id(n), BinaryOp(-, Id(n), NumLit(1.0))), If((BinaryOp(<, Id(k), Id(m)), Block([For(Id(i), BinaryOp(>=, Id(i), Id(l)), BinaryOp(-, Id(i), NumLit(1.0)), Block([CallStmt(Id(printString), [ArrayCell(Id(a), [BinaryOp(-, Id(m), NumLit(1.0)), Id(i)])])])), AssignStmt(Id(m), BinaryOp(-, Id(m), NumLit(1.0)))])), [], None), If((BinaryOp(<, Id(l), Id(n)), Block([For(Id(i), BinaryOp(>=, Id(i), Id(k)), BinaryOp(-, Id(i), NumLit(1.0)), Block([CallStmt(Id(printString), [ArrayCell(Id(a), [Id(i), Id(l)])])])), AssignStmt(Id(l), BinaryOp(+, Id(l), NumLit(1.0)))])), [], None)])), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test390_random_1_empty(self):
        input = """func main ()
        """
        expect = """Program([FuncDecl(Id(main), [], None)])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test391_random_2_id(self):
        input = """func main()
            begin
                a <- 1
                a <- b
                a[0] <- 1
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.0)), AssignStmt(Id(a), Id(b)), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test392_random_Numberlit1(self):
        input = """func main()
            begin
                a <- 1.e23
                b <- 10.21e2
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1e+23)), AssignStmt(Id(b), NumLit(1021.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test393_random_4_vardecl_single_if(self):
        input = """func main()
            begin
                if (n == 1)  begin
                    number a
                    number b
                end
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, Id(n), NumLit(1.0)), Block([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)])), [], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test394_random_Numberlit2(self):
        input = """func main()
            begin
                a <- 1.1e23
                a <- 1.1e-23
                a <- -12.0
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.1e+23)), AssignStmt(Id(a), NumLit(1.1e-23)), AssignStmt(Id(a), UnaryOp(-, NumLit(12.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test395_random_stringlit1(self):
        input = """func main()
            begin
                a <- "abc\txyz"
            end
            """
        expect = r"""Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), StringLit(abc	xyz))]))])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test396_random_stringlit2(self):
        input = r"""func main()
            begin
                a <- "abc\\nxyz"
            end
            """
        expect = r"""Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), StringLit(abc\\nxyz))]))])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    def test397_ultimate_001(self):
        input = r"""func main()
            begin
                a <- -1.
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), UnaryOp(-, NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test398_ultimate_002(self):
        input = """number a[3]
        """ 
        expect = """Program([VarDecl(Id(a), ArrayType([3.0], NumberType), None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test399_ultimate_003(self):
        input = r"""func main()
            begin
                dynamic a <- 6
            end
            """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, NumLit(6.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    
      