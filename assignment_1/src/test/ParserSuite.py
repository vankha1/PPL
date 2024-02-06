import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    
    def test_case_101(self):

        input = """ func test(number a, bool b)
        return a + b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_case_102(self):

        input = """func test(number a, bool b) return a + b"""
        expect = "Error on line 1 col 40: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_case_103(self):

        input = """bool a_b \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))

    def test_case_104(self):

        input = """number x_Y_z \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 104))

    def test_case_105(self):

        input = """func main()
        begin
            if(a)
                begin
                end
            else begin
                end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 105))

    def test_case_106(self):

        input = """number a[3] <- [2, true, false] \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_case_107(self):

        input = """bool array[2,3,10,5,10,10] \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_case_108(self):

        input = """number a <- 2, b <- 3"""
        expect = "Error on line 1 col 13: ,"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_case_109(self):

        input = """number vvk <- 12 + 2 \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_case_110(self):

        input = """string chatgpt <- "uaalo" \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 110))

    def test_case_111(self):

        input = """number array[1,1] <- [[1,2,3]]
                    string x <- "hello" \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 111))

    def test_case_112(self):

        input = """dynamic a <- 2 \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 112))

    def test_case_113(self):

        input = """x <- bool \n"""
        expect = "Error on line 1 col 0: x"
        self.assertTrue(TestParser.test(input, expect, 113))

    def test_case_114(self):

        input = """number Aee123 <- 1 + 1
                number _aDC <- 2 * 1
                number A_bc <- -1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 114))

    def test_case_115(self):

        input = """bool x <- true
                bool y <- false
                number x <- 123.
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 115))

    def test_case_116(self):

        input = """number1 arg1 <- 1 - 1
                    number arg2 <- 1 + a
        """
        expect = "Error on line 1 col 0: number1"
        self.assertTrue(TestParser.test(input, expect, 116))

    def test_case_117(self):

        input = """
            number a[]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 117))

    def test_case_118(self):

        input = """func name(number x, number y) 
        begin
        number a <- 2
        number b <- 3.14
        l[2] <- l[2] + 2
        number l <- value * aPi
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 118))
        
    def test_empty_statement_with_semicolon(self):
        input = """func fact(number a)
                    begin
                        abc;
                    end"""
        expect = ";"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_case_119(self):

        input = """func foo(number a, string b)
        begin
            var i <- 0
            for i until i <= 5 by i
                begin
                a[i] <- a[i] + 2
                end
            return a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 119))

    def test_case_120(self):

        input = """string str <- "a"..."b" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 120))

    def test_case_121(self):

        input = """
            func name()
            begin
                a[3 + foo(2)] <- a[b[2, 3]] + 4
        """
        expect = """Error on line 5 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 121))

    def test_case_122(self):

        input = """number java <- not a and b - "love" / "you" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 122))

    def test_case_123(self):

        input = """string love <- "I" ... "LOVE" ... "YOU" """
        expect = "Error on line 1 col 30: ..."
        self.assertTrue(TestParser.test(input, expect, 123))

    def test_case_124(self):

        input = """number array[3] <- [31, 12, 2002]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 124))

    def test_case_125(self):

        input = """bool array[t]"""
        expect = "Error on line 1 col 11: t"
        self.assertTrue(TestParser.test(input, expect, 125))

    def test_case_126(self):

        input = """number array[] <- a, -1 + 2"""
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.test(input, expect, 126))

    def test_case_127(self):

        input = """number a <- str[1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 127))

    def test_case_128(self):

        input = """string siuuuuuuuuuuuuuuuu <- "Ronaldo" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 128))

    def test_case_129(self):

        input = """string messi <- "Linel Messi" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 129))

    def test_case_130(self):

        input = """number a <- a[1]
                number b <- b[5]
                number c <- c[2]
                number d <- d[3]
                number e <- e[4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 130))

    def test_case_131(self):

        input = """func number ()"""
        expect = "Error on line 1 col 5: number"
        self.assertTrue(TestParser.test(input, expect, 131))

    def test_case_132(self):
        ## error not having new line at the end
        input = """func boolean ()"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 132))

    def test_case_133(self):

        input = """func array[10, 10] ()
            begin
            end
        """
        expect = """Error on line 1 col 10: ["""
        self.assertTrue(TestParser.test(input, expect, 133))

    def test_case_134(self):

        input = """
            func void (number x)
            begin
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 134))

    def test_case_135(self):

        input = """func Func_1 (number t, string z) begin end"""
        expect = "Error on line 1 col 39: end"
        self.assertTrue(TestParser.test(input, expect, 135))

    def test_case_136(self):

        input = """func Siuuuuuuuuu_A7 ()
                begin
                begin
                end
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 136))

    def test_case_137(self):

        input = """func Messssssssssssssssssssi (number a) 
                    begin
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 137))

    def test_case_138(self):
        input = """func Cavani (number a, string b, bool c) 
                begin
                begin
                end
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 138))

    def test_case_139(self):

        input = """func number ()
            begin
            end
        """
        expect = "Error on line 1 col 5: number"
        self.assertTrue(TestParser.test(input, expect, 139))

    def test_case_140(self):

        input = """func /a_a () 
            begin
            end
        """
        expect = "Error on line 1 col 5: /"
        self.assertTrue(TestParser.test(input, expect, 140))

    def test_case_141(self):

        input = """funccxyz Raphinha () 
                begin
                begin
                end
                end
        """
        expect = "Error on line 1 col 0: funccxyz"
        self.assertTrue(TestParser.test(input, expect, 141))

    def test_case_142(self):

        input = """func _Casemiro () 
                begin
                begin
                begin
                end
                end
            """
        expect = "Error on line 7 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 142))

    def test_case_143(self):

        input = """func decl ()
            a <- 1
            b <- 2
        """
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.test(input, expect, 143))

    def test_case_144(self):
        input = """func void ()
            begin
                if (n == 1) return 1
                else break
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 144))

    def test_case_145(self):

        input = """
            func integer ()
            begin
                a[1] <- true and false and not a > 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 145))

    def test_case_146(self):

        input = """func boolean () 
        begin
            continue
            break
            writeNumber(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 146))

    def test_case_147(self):

        input = """
        func vankha () 
        begin
            begin
            end
            return 1
        end"""
        expect = "Error on line 7 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 147))

    def test_case_148(self):

        input = """
        func void () 
        begin
            if (n == 1) a <- true
            continue
            for i until i < 1 by -1 
                a <- b and true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 148))

    def test_case_149(self):

        input = """
        func vankha () 
        begin
            for i until i < 1 by -1 
                break
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 149))

    def test_case_150(self):

        input = """
        func void () 
        begin
            foo()
            return not a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 150))

    def test_case_151(self):

        input = """
        func function () 
        begin
            if ( i <= 1) 
            return i
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 151))

    def test_case_152(self):

        input = """
        func function () 
        begin
            begin
                for i until v < 10 by 1
                    return a
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 152))

    def test_case_153(self):

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 153))

    def test_case_154(self):

        input = """
        func integer () 
        begin
            if (i==1)
                a <- a + 1 
            elif (i == 2) a <- a + 2
            else a <- a + 3
        end            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 154))

    def test_case_155(self):

        input = """func integer () 
        begin
            break
            if (true) a <- 1 + 1
            else b <- b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 155))

    def test_case_156(self):

        input = """
        func boolean () 
        begin
            if (a[10] >= 100 )
                if (a[1,1] == 10)  printInteger(1)
                else if (a[-1, 10]  or false) b[-1] <- 10
                   
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 156))

    def test_case_157(self):
        ## Lack of statement after if-condition
        input = """
        func boolean () 
        begin
            if (a[10] >= 100 )
            elif (a[1,1] == 10)  printInteger(1)
            elif (a[-1, 10]  or false) b[-1] <- 10
        end
        """
        expect = "Error on line 5 col 12: elif"
        self.assertTrue(TestParser.test(input, expect, 157))

    def test_case_158(self):
        input = """
        func boolean () 
        begin
            if (a[10] >= 100 ) a <- a + 1
            elif (a[1,1] == 10)  writeNumber(1)
            elif (a[-1, 10]  or false) b[-1] <- 10
            else return foo(2 + 2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 158))

    def test_case_159(self):

        input = """
        ## khai bao ham func
        func integer () 
            begin
            begin
                if (a[10] >= 100 )
                if (a[1,1] == 10)  printInteger(1)
                else if (a[-1, 10]  or false) b[-1] <- 10
            end
            end
        end
        """
        expect = "Error on line 11 col 8: end"
        self.assertTrue(TestParser.test(input, expect, 159))

    def test_case_160(self):

        input = """
        ## alo
        func void () 
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 160))

    def test_case_161(self):

        input = """
        ### hello
        func integer () 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 161))

    def test_case_162(self):

        input = """
        func integer ()
        begin
            # error
        end
        """
        expect = "#"
        self.assertTrue(TestParser.test(input, expect, 162))

    def test_case_163(self):

        input = """func boolean () 
        begin
            break
            ## error
            dynamic i <- 2
            for i until i <= 10 by i + 1
                begin
                    i <- i + 1
                    foo(a + 2)
                end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 163))

    def test_case_164(self):

        input = """func integer ()
        begin
            continue
            var i <- 0
            for i until i >= 10 by 1
                writeNumber(i)

            if (n == 1)
                return 0
            else break
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 164))

    def test_case_165(self):

        input = """
        func void ()
        begin    
            for a until a >= 10 by 1
            begin
                "something"
            end
        end
        """
        expect = "Error on line 6 col 16: something"
        self.assertTrue(TestParser.test(input, expect, 165))

    def test_case_166(self):

        input = """func integer ()
        begin
           begin
        begin
            b <- b / 2
        end

        for i until i < 3 by i - a
        begin
            if (i == b)
            begin
                continue
            end
             else begin
                b <- 1
            end

        end

            end
            return b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 166))

    def test_case_167(self):

        input = """func integer ()
        begin
            ## sinh code moi
            preventDefault()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 167))

    def test_case_168(self):

        input = """func float (out a)
        begin
           a <- a[1]
        end
        """
        expect = "Error on line 1 col 12: out"
        self.assertTrue(TestParser.test(input, expect, 168))

    def test_case_169(self):

        input = """func float ()
        begin
            readInteger()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 169))

    def test_case_170(self):

        input = """
        func integer () 
        begin
            writeNumber("1+1")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 170))

    def test_case_171(self):

        input = """func array[]() 
        begin
          
               printFloat(12.1e45)
        end
        """
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.test(input, expect, 171))

    def test_case_172(self):

        input = """func integer (var a, string x) 
        begin
           readFloat(1e10)
        end
        """
        expect = "Error on line 1 col 14: var"
        self.assertTrue(TestParser.test(input, expect, 172))

    def test_case_173(self):

        input = """
        func boolean ()
        begin
            readBool()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 173))

    def test_case_174(self):

        input = """
        func boolean (bool a)
        begin
            writeBool(a[1,2,3], 123)   
        end
        """
        expect = "Error on line 4 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 174))

    def test_case_175(self):

        input = """func integer (number a, string b)
        begin
            readString(123123)
        end
        """
        expect = "Error on line 3 col 23: 123123"
        self.assertTrue(TestParser.test(input, expect, 175))

    def test_case_176(self):

        input = """
        var a <- 5
        func integer () 
        begin
           if (true) 10
        end
        """
        expect = "Error on line 5 col 21: 10"
        self.assertTrue(TestParser.test(input, expect, 176))

    def test_case_177(self):

        input = """
        var a
        func integer () 
        begin
           if (true) 10
        end
        """
        expect = """Error on line 2 col 13: \n"""
        self.assertTrue(TestParser.test(input, expect, 177))

    def test_case_178(self):

        input = """
        number a <- funcion(10)
        for i until i <= 10 by i + 1
        begin
            sum <- sum + i
        end
        writeString("I Love you")
        """
        expect = "Error on line 3 col 8: for"
        self.assertTrue(TestParser.test(input, expect, 178))

    def test_case_179(self):

        input = """
            number array[5] <- [1, 2, 3, "a"]
            a <- 10
        """
        expect = "Error on line 3 col 12: a"
        self.assertTrue(TestParser.test(input, expect, 179))

    def test_case_180(self):

        input = """
        string function()
        if (true == a) return 0
        """
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 180))

    def test_case_181(self):

        input = """
        func void ()
        begin
            arr <- [10.5, 20.3, 15.6, 18.9, 25.4]
            number n <- sizeof(arr) / sizeof(arr[0])
            average <- calculateAverage(arr, n)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 181))

    def test_case_182(self):

        input = """func reverseString(string str)
        begin
            n <- strlen(str)
            for (i <- 0 until i < n / 2 by i + 1) 
            begin
                swap(str[i], str[n - i - 1])
            end
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 182))

    def test_case_183(self):

        input = """
            func calculateExpApproximation(number n)
            begin
                number result <- 1.0
                number term <- 1.0
                for i until i <= n by i
                begin
                    term <- (1.0 / n) ## test here
                end
                return result
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 183))

    def test_case_184(self):
        ## test error i <- 1 here
        input = """func float ()
        begin
            float()
            for i <- 1 until n by i 
                i <- i + 1
            return expr
        end

        c = expr
        """
        expect = "Error on line 4 col 18: <-"
        self.assertTrue(TestParser.test(input, expect, 184))

    def test_case_185(self):

        input = """ 
        func calculateExpression(number n) ## test function prototype
        
           ## double result = 0.0;
            ##for (int i = 1; i <= n; i++) {
             ##   result <- (string) i / (i + 1)
            ##}
            ##return result;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 185))

    def test_case_186(self):

        input = """
        func integer ()
        begin
            int e
           
            c = true * d / 20
         
        end
        """
        expect = "Error on line 4 col 16: e"
        self.assertTrue(TestParser.test(input, expect, 186))

    def test_case_187(self):

        input = """ 
       
                    func sumNumbers(string n)
                    begin
                        var sum <- 0
                        var i <- 1
                        foo(a[2], a[2,3,4])
                        return sum
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 187))

    def test_case_188(self):

        input = """##khai bao bien
        func printNumbers (number n)
        begin
            for i until i <= n by i + 10
            begin
                break
            end
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 188))

    def test_case_189(self):

        input = """dynamic x <- 65
        
            func fact (number n)
            begin
                if(n==0) return true
                else return n*fact(n-1)
            end
            
            func inc (number n, number delta)
            begin
                n <- n+delta
            end
            
            func main ()
            begin
                var delta <- fact(3)
                inc(x,delta)
                writeString(x)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 189))

    def test_case_190(self):

        input = """dynamic a <- 65
        func integer (string str)
        begin
            if (n == 0) return 1
            else return n * fact(n - 1)
        end
        func void(number n,number delta)
        begin
            n <- n + delta
        end
       """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 190))

    def test_case_191(self):
        input =	"""bool a <- foo(1)\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 191))
        
    def test192_special_function_not_in_func(self):
        ## Problem with special function: if removing special function from .g4 file, this testcase will work, but it will also work with testcases having dummy parameters in special functions (current expect matches case in which having special function)
        input = """
            bool a <- true
            bool b <- false
            writeString(not a)
            writeString(a and b)
            writeString(a or b)
            writeString(a==b)
            writeString(a!=b)
        """
        expect = "Error on line 4 col 12: writeString"
        self.assertTrue(TestParser.test(input, expect, 192))
        
    def test193_arith_number_type(self):
        input = """
            number a <- 5.e121
            number b <- -12.0
            number c <- 1234e-12
            number d <- -5678.5e+2
            func check()
            begin
                printInteger(a+b)
                printInteger(a-b)
                printInteger(a*b)
                printInteger(a/b)
                printInteger(a%b)
                
                printInteger(c+d)
                printInteger(c-d)
                printInteger(c*d)
                printInteger(c/d)
                printInteger(c%d)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 193))
        
        
    def test194_relation_numeric_type(self):
        input = """
            number a <- 5.e121
            number b <- -12.0
            func check()
            begin
            printBoolean(a>b)
            printBoolean(a>=b)
            printBoolean(a<b)
            printBoolean(a<=b)
            printBoolean(a!=b)
            printBoolean(a==b)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 194))
        
    def test195_string_type(self):
        input = """
            string a <- "Hello"
            string b <- "World"
            func check()
            begin
                printString(a...b)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 195))
        
    def test196_array_type(self):
        input = """
            number a[5]
            func check()
            begin
                printInteger(a[0])
                printInteger(a[2])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 196))

    def test197_multidim_array_type(self):
        input = """
            number a[5,2]
            func check()
            begin
                printInteger(a[0,1])
                printInteger(a[3,0])
                printInteger(a[3,1])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 197))
        
    def test198_invalid_array_size_1(self):
        input = """
            number array[5.123,0]
            func check()
            begin
                printInteger(a[0,1])
                printInteger(a[3,0])
                printInteger(a[3,1])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 198))

    def test199_invalid_array_size_1(self):
        input = """
            number array [5.2]
            func check()
            begin
                printInteger(a[0])
                printInteger(a[2])
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 199))
        
    def test_comment_interleaved_with_block_stmt(self):
        input = """func fact(number n)
            begin
                a[1] <- 2
                begin
                    foo(5)
                    ## end
                    return 3
                    ## begin
                    continue
                    ## return
                    break
                    ## break
                    readNumber()
                    ## continue
                    var a <- 5
                    ## test
                end
            end
        """     
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        
    def test_double_index_in_function_body_2(self):
        input = """func test ()
        begin
            a[1] <- a[1][2]
        end
        """
        expect = "Error on line 3 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_invalid_assignment_involving_function(self):
        input = """func main()
        begin
    call(c) + call(d) <- 1
        end
"""
        expect = "Error on line 3 col 12: +"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_complex_expression_in_assignment(self):
        # It seems like b(0) is a valid expression, but why...
        # => Because the parser can interpret b as a function
        input = """func test(number a, number b)
                begin
                   a <- ((a[10]... "2" + b(0))[10])
                   a <- 2[10]
                end
                """
        expect = "Error on line 3 col 46: ["
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_elif_without_cond(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3
                    elif a <- 4
                    end
                """
        expect = "Error on line 6 col 25: a"
        self.assertTrue(TestParser.test(input, expect, 310))
        
        
    def test_comment_311(self):
        input = """func fact(number a) begin ## comment
        for i until i >= 10 by i begin ## comment
                c <- a + n
                a <-b
                b <- c
                end
            end
                
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 311))
        
    def test_in_docs_312(self):
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()
                    if (areDivisors(num1, num2)) printString("Yes")
                    else printString("No")
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312))
        
    def test_in_docs_313(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                    if (x % i = 0) return false
                    end
                    return true
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 313))
        
    def test_case_314(self):
        input = """number a[0] <- []
                """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 314))
        
    def test_case_315(self):
        input = """func test() begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
            a[3 + foo(2)] <- foo(2,3)[b[2, 3]] + 4
            a[3 + foo(2)] <- c[10][10]
        end
        """
        expect = "Error on line 4 col 34: ["
        self.assertTrue(TestParser.test(input, expect, 315))
        
    def test_case_316(self):
        input = """func test() begin
            a[3 + foo(2)] <- foo([1,2,3], 1) + 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 316))
    
    def test_case_317(self):
        input = """func test() begin
            if (a) do(a)

           elif (a=2=2) do(b)
        end
        """
        expect = "Error on line 4 col 20: ="
        self.assertTrue(TestParser.test(input, expect, 317))
    
    def test_case_318(self):
        input = """## test"""
        expect = "Error on line 1 col 7: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 318))
        
    def test_case_319(self):
        input = """func test() begin
        var arr <- [1,2,3]
        print( ((arr))[0] )
        end
        """
        expect = "Error on line 3 col 22: ["
        self.assertTrue(TestParser.test(input, expect, 319))
    
    def test_case_320(self):
        input = """func test() begin
                print( ( f(1,2,3) )[1,2,3] )
        end
        """
        expect = "Error on line 2 col 35: ["
        self.assertTrue(TestParser.test(input, expect, 320))
    
    def test_case_321(self):
        input = """func test() begin
            var arr["roi"] <- [0, 2]
        end
        """
        expect = "Error on line 2 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 321))
    
    def test_case_322(self):
        input = """func test() begin
            var arr[3] <- [0, "rac", 2]
        end
        """
        expect = "Error on line 2 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 322))
        
    def test_case_323(self):
        input = """func test(number a <- 5) 
        begin
            var arr[3] <- [0, "rac", 2]
        end
        """
        expect = "Error on line 1 col 19: <-"
        self.assertTrue(TestParser.test(input, expect, 323))
    
    def test_case_324(self):
        input = """func test() 
        begin
            for a[2] until i >= 3 by 1
            begin
            end
        end
        """
        expect = "Error on line 3 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_case_325(self):
        input = """func test() 
        begin
            string a <- 1 or true ... "zcd"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 325))
    
    def test_case_326(self):
        input = """func main() begin
            foo(2,3)[2] <- 3
        end
        """
        expect = "Error on line 2 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 326))
    