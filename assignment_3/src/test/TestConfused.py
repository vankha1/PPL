import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):   
    
    def test483(self): ## Confused !!!
        input = """
dynamic a
func main()
begin
    number a[2, 3] <- [a, [10, 20, 30]]
    a <- [1, 9, 6]
    writeNumber(a[0])
end
"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 483))
     
    
    def test489(self): # Confused
        input = """
func test(number x)

func main()
begin
    number test
    begin
        number x <- test(2018) + 1
    end
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(test), [NumLit(2018.0)])"
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test494(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [a, b, c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test495(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x
    x <- [a, b, [c]]
end
"""
        expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 495))
        
        
    