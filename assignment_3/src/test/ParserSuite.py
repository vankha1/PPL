import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func foo()
        func main()
        begin
            number a
            a <- foo() + 5
        end
        func foo()
        begin
           return 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
