import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """number ez[6.36] <- [Cu]
bool MET[58.38]
dynamic vTBf <- [false]
number KA[33.96]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
