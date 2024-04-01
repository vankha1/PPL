import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main()
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
