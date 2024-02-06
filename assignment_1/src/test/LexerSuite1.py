import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    '''
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    '''
    # Operator Suite
    def test_operators(self):
        self.assertTrue(TestLexer.test("+-*/%+...-", "+,-,*,/,%,+,...,-,<EOF>", 122))
        
    def test_operators_1(self):
        input = "(<><><>)"
        expect = "(,<,>,<,>,<,>,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))
        
    def test_operators_2(self): 
        input = "[)false,(]"
        expect = "[,),false,,,(,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))
        
    def test_operator_ambiguity(self):
        input = "!====!=>==/and"
        expect = "!=,==,=,!=,>=,=,/,and,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    # Keyword Suite
    def test_keywords(self):
        self.assertTrue(TestLexer.test("return var dynamic func elif", "return,var,dynamic,func,elif,<EOF>", 123))
        
    # Variable Declaration Suite:
    def test_declaration_1(self):
        input = "a <- true, b != false"
        expect = "a,<-,true,,,b,!=,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
        
    def test_declaration_2(self):
        input = "var i <- 0"
        expect = "var,i,<-,0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))
        
    def test_declaration_3(self):
        input = "number a[1.5] <- [2.3, 4.5]"
        expect = "number,a,[,1.5,],<-,[,2.3,,,4.5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))
        
    def test_declaration_4(self):
        input = "dynamic a[1.5e-3] <- [2.3, 4.5]"
        expect = "dynamic,a,[,1.5e-3,],<-,[,2.3,,,4.5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))
        
    def test_declaration_5(self):
        input = "bool a[1...2] <- [true, false]"
        expect = "bool,a,[,1.,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 185))
        
    def test_declaration_6(self):
        input = "number a[1+2, foo(3), 3*4]"
        expect = "number,a,[,1,+,2,,,foo,(,3,),,,3,*,4,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185_1))
        
    # Function Declaration Suite:
    def test_function_declaration(self):
        input = "func foo()"
        expect = "func,foo,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))
        
    def test_function_declaration_1(self):
        input = "func foo(number a, string b)"
        expect = "func,foo,(,number,a,,,string,b,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_function_declaration_2(self): 
        input = "func foo(number a[5], string b)"
        expect = "func,foo,(,number,a,[,5,],,,string,b,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_function_declaration_3(self): 
        input = """func xyz()
                begin 
                end
                """
        expect = """func,xyz,(,),
,begin,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))
        
    def test_function_declaration_4(self):
        input = """func xyz(string a, dynamic b)
                begin 
                    var x <- 5
                end
                """
        expect = """func,xyz,(,string,a,,,dynamic,b,),
,begin,
,var,x,<-,5,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156))
        
    def test_function_declaration_5(self):
        input = """func integer()
                begin 
                    return test
                end
                """
        expect = """func,integer,(,),
,begin,
,return,test,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))
    
        
    # Identifier Suite
    def test_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
        
    def test_uppercase_identifier(self):
        self.assertTrue(TestLexer.test("ASDFASDF", "ASDFASDF,<EOF>", 105))
        
    def test_identifier_with_underscore(self):
        self.assertTrue(TestLexer.test("ab_sdfsd_sdfc_", "ab_sdfsd_sdfc_,<EOF>", 106))
    
    def test_identifier_with_underscore_1(self):
        self.assertTrue(TestLexer.test("_ab_sdfsd_sdfc_", "_ab_sdfsd_sdfc_,<EOF>", 1060))
        
    def test_lower_id_with_tripe_quotes(self):
        self.assertTrue(TestLexer.test(""" "abc" """, """abc,<EOF>""", 117))

    def test_id_with_tab_character(self):
        self.assertTrue(TestLexer.test(""" "abc\t" """, """abc\t,<EOF>""", 118))
    
    def test_id_separated_by_whitespace(self): 
        self.assertTrue(TestLexer.test("asdfasd asdfas dfghwerty ", "asdfasd,asdfas,dfghwerty,<EOF>", 138))

    def test_id_separated_by_ws_with_a_ws_at_the_end(self): 
        self.assertTrue(TestLexer.test("im wanna go study abroad", "im,wanna,go,study,abroad,<EOF>", 139))

    def test_LS140(self): 
        self.assertTrue(TestLexer.test("he he", "he,he,<EOF>", 140))
        
    def test_ws_at_the_beginning(self): 
        self.assertTrue(TestLexer.test(" same format as", "same,format,as,<EOF>", 144))

    def test_LS145(self):
        self.assertTrue(TestLexer.test("ExpoWeanaSFSst part ", "ExpoWeanaSFSst,part,<EOF>", 145))
        
    # Number Suite - Integer
    def test_integer(self):
        self.assertTrue(TestLexer.test("12234", "12234,<EOF>", 102))
        
    def test_negative_int(self):
        self.assertTrue(TestLexer.test("-123456789", "-,123456789,<EOF>", 106_1))
        
    def test_multiple_zeros(self):
        self.assertTrue(TestLexer.test("000", "000,<EOF>", 103))

        
    # Number Suite - Float
    def test_float_with_underscore_and_exp(self):
        self.assertTrue(TestLexer.test("1234128765e+1632", "1234128765e+1632,<EOF>", 113))
        
    def test_float_underscore_with_triple_quote(self):
        self.assertTrue(TestLexer.test(""" 13.987235E123 """, """13.987235E123,<EOF>""", 116))
        
    def test_float_without_decmial_part(self):
        self.assertTrue(TestLexer.test(" 7E-10 ", "7E-10,<EOF>", 141))

    def test_standard_float(self):
        self.assertTrue(TestLexer.test("1320.3e+9 0.332e5","1320.3e+9,0.332e5,<EOF>", 142))

    def test_float_without_exp(self):
        self.assertTrue(TestLexer.test("1234.567","1234.567,<EOF>", 143))
    
    def test_float_without_int(self):
        self.assertTrue(TestLexer.test(".25e+3", "Error Token .", 101_1))
        
    def test_float_with_leading_zero(self):
        self.assertTrue(TestLexer.test("0.25", "0.25,<EOF>", 102_1))
    
    # String Suite
    def test_string_with_underscore(self):
        self.assertTrue(TestLexer.test("a_bcd_ef", "a_bcd_ef,<EOF>", 103_1))
        
    def test_leading_underscore(self):
        self.assertTrue(TestLexer.test("_this_is_id", "_this_is_id,<EOF>", 104_1))
        
    def test_string_with_invalid_char(self):
        self.assertTrue(TestLexer.test("@198016abc", "Error Token @", 105_1))
    
    def test_standard_stringlit(self):
        self.assertTrue(TestLexer.test(""" "ab cdef gh: ab cdef gh?" """, """ab cdef gh: ab cdef gh?,<EOF>""", 199))    

    def test_stringlit_with_backspace_escape(self):
        self.assertTrue(TestLexer.test(""" "abvc\bcd" """, """abvc\bcd,<EOF>""", 200))     

    def test_stringlit_with_whitespace(self):
        input = """ "   vb     " """
        expect = """   vb     ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_193(self): 
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_194(self): 
        input = "cba"
        expect = "cba,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))
    
    def test_empty_string(self):
        self.assertTrue(TestLexer.test("", "<EOF>", 121))
    
    def test_string_with_whitespace(self):
        self.assertTrue(TestLexer.test("this is whitespace", "this,is,whitespace,<EOF>", 104))
    
    def test_string_with_tab_and_newline(self):
        input = """ " \\naaa\\t" """
        expect = """ \\naaa\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178))
        
    def test_string_with_integer(self):
        self.assertTrue(TestLexer.test("test_LS 123 asdasdq456","test_LS,123,asdasdq456,<EOF>",107))
        
    def test_string_with_bracket(self):
        self.assertTrue(TestLexer.test("abc [sad]", "abc,[,sad,],<EOF>", 108))
        
    def test_string_with_unmatched_bracket(self):
        self.assertTrue(TestLexer.test("{this is an unmatch)", "Error Token {", 115))
        
    def test_string_with_special_char_1(self):
        self.assertTrue(TestLexer.test("ewrw<wq.QWE>eqw", "ewrw,<,wq,Error Token .", 112))
        
    def test_string_with_special_char_2(self):
        self.assertTrue(TestLexer.test("i<3u", "i,<,3,u,<EOF>", 111))
        
    def test_string_with_special_char_7(self):
        self.assertTrue(TestLexer.test("...a...ghje34...,dsfeiewqo/", "...,a,...,ghje34,...,,,dsfeiewqo,/,<EOF>", 114))
        
    def test_string_with_special_char_3(self):
        self.assertTrue(TestLexer.test(":a:ghje34:,dsfeiewqo.", "Error Token :", 114))
        
    def test_string_with_special_char_4(self):
        self.assertTrue(TestLexer.test("asdf +f dshj+sa g-sadw21 hga*", "asdf,+,f,dshj,+,sa,g,-,sadw21,hga,*,<EOF>", 110))
        
    def test_string_with_special_char_5(self):
        self.assertTrue(TestLexer.test("abc + -", "abc,+,-,<EOF>", 125))
        
    def test_string_with_special_char_6(self):
        input = "sdfgh<...>rtyui"
        expect = "sdfgh,<,...,>,rtyui,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))
        
    def test_double_quote_escape_in_stringlit(self):
        input = """ "\\" """
        expect = r"""Illegal Escape In String: \""""
        self.assertTrue(TestLexer.test(input, expect, 186))
    
    # Array Suite
    def test_array_declaration(self):
        input = "number abc[5]"
        expect = "number,abc,[,5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))
    
    def test_1d_number_arr(self):
        input = "number a[5] <- [1, 2., 3.2e5, 40, -5]"
        expect = "number,a,[,5,],<-,[,1,,,2.,,,3.2e5,,,40,,,-,5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_2d_number_arr(self):
        input = "number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]"
        expect = "number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_bool_arr(self):
        input = "bool a[3] <- [true, true, false]"
        expect = "bool,a,[,3,],<-,[,true,,,true,,,false,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))
        
    def test_index_operation(self):
        input = "a[0] <- s"
        expect = "a,[,0,],<-,s,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))
    
    def test_array_with_whitespace(self):
        input = """[                   1,             2     ,               3                ]"""
        expect = """[,1,,,2,,,3,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
        
    # Expression Suite 
    def test_simple_exp(self):
        self.assertTrue(TestLexer.test("1+1=3", "1,+,1,=,3,<EOF>", 109))
        
    def test_standard_exp(self):
        input = "F88 + nha - 40 > 12"
        expect = "F88,+,nha,-,40,>,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))
        
    # Statement Suite
    def test_assignstmt(self):
        input = "s<-r*r*this%myPI"
        expect = "s,<-,r,*,r,*,this,%,myPI,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))
        
    # Mixed Token Suite
    def test_mixed_token(self):
        input = "number bool [4]"
        expect = "number,bool,[,4,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))
        
    def test_mixed_token_1(self):
        self.assertTrue(TestLexer.test("!a!=%53245andbora123+*", "Error Token !", 131))

    def test_mixed_token_2(self):
        self.assertTrue(TestLexer.test("c==h==12341!=dfsg1234<>!", "c,==,h,==,12341,!=,dfsg1234,<,>,Error Token !", 132))
    
    def test_mixed_token_with_tab(self):
        input = "[(]sdfghsdfgwaDSFGHEWdsfg\t" 
        expect = "[,(,],sdfghsdfgwaDSFGHEWdsfg,<EOF>" # TRAP, I guess... (see testcase 118)
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_mixed_token_with_whitespace(self):
        input = ",12=dfgh==,dfgh 213"
        expect = ",,12,=,dfgh,==,,,dfgh,213,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
        
    def test_mixed_token_with_int_as_first_char(self): 
        input = "3e...x() sdfg/dfg*dfsg()adsa"
        expect = "3,e,...,x,(,),sdfg,/,dfg,*,dfsg,(,),adsa,<EOF>" 
        self.assertTrue(TestLexer.test(input, expect, 157))
        
    # Comment Suite
    def test_comment(self):
        self.assertTrue(TestLexer.test("## This is a <- 5", "<EOF>", 133))
        
    def test_incomplete_comment(self):
        self.assertTrue(TestLexer.test("# This is a comment", "Error Token #", 134)) 
    
    def test_invalid_comment(self):
        input = "number a <- 5 ## This is a comment"
        expect = "number,a,<-,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect,182))
        
    
    def test_comment_then_assignment(self):
        input = """ ## This is a comment
        a <- 5
        """
        expect = """
,a,<-,5,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
        
    def test_assignment_then_comment(self): 
        input = """ a <- 5
        ## This is a comment
        """
        expect = """a,<-,5,
,
,<EOF>""" 
        self.assertTrue(TestLexer.test(input, expect, 137))
    
    # Unclosed String Error Suite
    def test_unclosed_string(self):
        input = """ "hjhasdfasdk\n" """
        expect = """Unclosed String: hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect,119)) 
    # New line character is not accepted in STRINGLIT
    # NOTE: string of characters that are whitespace-separated
    # but enclosed by double quotes is considered as 1 token only
    def test_unclosed_string_1(self):
        input = """a= "No one said: " Hello " \n ";"""
        # "No one said: " is considered as 1 token only
        expect = """a,=,No one said: ,Hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 167))

    def test_unclosed_string_2(self):
        input = """aa = "Hello \n world !";"""
        expect = """aa,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(input, expect, 168))
        
    def test_unclosed_string_with_operator(self):
        input = """>">"""
        expect = """>,Unclosed String: >"""
        self.assertTrue(TestLexer.test(input, expect, 180))
    
    def test_LS187(self): # DUPLICATE TEST!
        input = """ "dshf"""
        expect = """Unclosed String: dshf"""
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_comment_with_unclosed_quote(self):
        input = """ ## aa " """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_unclosed_string_due_to_multiline_span(self):
        input = """vbnm"-a)
                    " """
        expect = """vbnm,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input, expect, 189))

    # Error Token Test Suite
    # e.g: ^, @, &, #, ? are invalid token
    def test_error_token_1(self):
        self.assertTrue(TestLexer.test("!= == ^ & != && * % $ ... ","!=,==,Error Token ^",126))

    def test_error_token_2(self):
        self.assertTrue(TestLexer.test(""" % erty == != @ ksmdk ""","""%,erty,==,!=,Error Token @""",127))
    
    def test_error_token_3(self):
        self.assertTrue(TestLexer.test("<> == & != && * % $ ... ","<,>,==,Error Token &",128)) 
         
    def test_error_token_4(self):
        self.assertTrue(TestLexer.test("#dzFdadsf/*this is a comment */", "Error Token #", 135))
        
    def test_error_token_5(self):
        self.assertTrue(TestLexer.test("?hello my friend \n asda", "Error Token ?", 136))
        
    def test_error_token_6(self):
        input = "...3?"
        expect = "...,3,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 165))
    
    def test_error_token_7(self):
        input = """a= "He said: " Im Super?Man "s" testtt; __world = 5; imple = 8;"""
        expect = """a,=,He said: ,Im,Super,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 166))
        
    def test_error_token_8(self):
        input = "ab?svn" # DUPLICATE TEST!
        expect = "ab,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 195))
        
    # Illegal Escape Suite
    # Note: illegal token: '\\' ~[bfrnt"'\\]
    def test_illegal_escape_with_DQ_escape_1(self):
        self.assertTrue(TestLexer.test(""" 1+1>=2+2 \"**dfshg324+\\^ def\" ""","""1,+,1,>=,2,+,2,Illegal Escape In String: **dfshg324+\^""",129))
    
    def test_illegal_escape_DQ_escape_2(self):
        self.assertTrue(TestLexer.test("""  \"\\!asdgqwetrew\" ""","""Illegal Escape In String: \!""",130))
         
    def test_illegal_escape_DQ_escape_3(self):
        self.assertTrue(TestLexer.test(""" ",cxvbcvb\\12" """, """Illegal Escape In String: ,cxvbcvb\\1""", 146))
        
    def test_illegal_escape_DQ_escape_4(self):
        input = """ \"dsfg\\e def\" """
        expect = """Illegal Escape In String: dsfg\\e"""
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_illegal_escape_no_DQ_escape_1(self):
        input = """ " \\wqe " """
        expect = """Illegal Escape In String:  \w"""
        self.assertTrue(TestLexer.test(input, expect, 177))
        
    def test_illegal_escape_no_DQ_escape_2(self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_illegal_escape_no_DQ_escape_3(self):
        input = """ "\\n\\ " """ # How about """ "\\n" """ ?
        expect = """Illegal Escape In String: \\n\\ """
        self.assertTrue(TestLexer.test(input, expect, 191))
        
    # Sample Program Suite
    def test_program_1(self):
        input = """func areDivisors(number num1, number num2)
                        return (num1 % num2 = 0 or num2 % num1 = 0)
                    func main()
                        begin
                            var num1 <- readNumber()
                            var num2 <- readNumber()
                            if areDivisors(num1, num2) printString("Yes")
                            else printString("No")
                        end
                """
        expect = """func,areDivisors,(,number,num1,,,number,num2,),
,return,(,num1,%,num2,=,0,or,num2,%,num1,=,0,),
,func,main,(,),
,begin,
,var,num1,<-,readNumber,(,),
,var,num2,<-,readNumber,(,),
,if,areDivisors,(,num1,,,num2,),printString,(,Yes,),
,else,printString,(,No,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159))

    def test_program_2(self):
        input = """ func isPrime(number x)
                        begin
                            if x <= 1 return false
                            var i <- 2
                            for i until i > x / 2 by 1
                            begin
                                if x % i = 0 return false
                            end
                            return true
                        end

                    """
        expect = """func,isPrime,(,number,x,),
,begin,
,if,x,<=,1,return,false,
,var,i,<-,2,
,for,i,until,i,>,x,/,2,by,1,
,begin,
,if,x,%,i,=,0,return,false,
,end,
,return,true,
,end,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    def test_literals_string_8(self):
        input = """ "He asked me: '"Where is John?'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 408))
        
    def test_literals_string_9(self):
        input = """ "He asked me: \"Where is John?\"" """
        expect = """He asked me: ,Where,is,John,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 409))
        
    def test_case_41(self):
        input = r""" "Double quote '"" """
        expect = r"""Double quote '",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 41))

    
    def test_single_index_in_function_body(self):
        input = """ func test(number a, bool b)
        return a + b
        """
        expect = """func,test,(,number,a,,,bool,b,),\n\n,return,a,+,b,\n\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 231))
        
    def test_single_index_in_function_body(self):
        input = """func test ()
        begin
            a[1] <- a[2]
        end
"""
        expect = """func,test,(,),
,begin,
,a,[,1,],<-,a,[,2,],
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 999))
    
    def test102_normal_boolean(self):
        input = """true \r\n false """
        expect = """true,Error Token 
"""
        self.assertTrue(TestLexer.test(input, expect, 507))
    
    def test107_normal_line_comments(self):
        input = """
        ##This is a line comment
        """
        expect = """
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 508))
        
    def test139_mixed_cmt(self):
        input = r"""printhere
            ## Line /* and also block */
            ##
            #    Block //and also line
             #   notprinthere
            ##
        """
        expect = """printhere,
,
,
,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 509))
        
    def test_501(self):
        input = "## This is a single comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 501))
        
    def test_502(self):
        input = "a <- 5 ## This comment is not allowed"
        expect = "a,<-,5,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 502))
        
    def test_503(self):
        input = "true false number bool string return var dynamic func function for until"
        expect = "true,false,number,bool,string,return,var,dynamic,func,function,for,until,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 503))
        
    def test_504(self):
        input = "+-not and or= <-<=<>=>==!== /%..."
        expect = "+,-,not,and,or,=,<-,<=,<,>=,>=,=,!=,=,/,%,...,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 504))
        
    def test_505(self):
        input = "if+(else)*[elif],begin/end<=>== !=>"
        expect = "if,+,(,else,),*,[,elif,],,,begin,/,end,<=,>=,=,!=,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 505))
        
    def test_506(self):
        input = "0 199 12. 12.3 12.3e3 -12.3e-30 0.45E+31 .25e-4"
        expect = "0,199,12.,12.3,12.3e3,-,12.3e-30,0.45E+31,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 506))
    
        
        
    
    