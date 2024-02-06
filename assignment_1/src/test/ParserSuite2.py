import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    '''
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    '''
    
    # TEST FUNCTION DECLARATION
    def test_if_cond_without_bracket(self):
        input = """func fact(number n)
            begin
                if n = 0 return 
                else return 
            end
        """
        expect = "Error on line 3 col 19: n"
        self.assertTrue(TestParser.test(input, expect, 292))
        
        
    def test_if_cond_with_bracket(self):
        input = """func fact(number n)
            begin
                if (n = 0) return 
                else return 
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
        
    def test_invalid_array_param_in_funcdecl(self):
        input = """func fact(number n[4])
            begin
                if (n = 0) return 
                else return 
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 315))
        
    def test_blockstmt_on_same_line_with_funcdecl(self):
        input = """func fact(number n) begin
                if (n = 0) return 
                else return 
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 304))
        
    def test_returnstmt_on_same_line_with_funcdecl(self):
        input = """func fact(number n) return 10
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))
        
    def test_forstmt_on_same_line(self):
        input = """func fact(number n) begin
                for i until i >= 10 by 1 return 10
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_invalid_param_type(self):
        input = """func fact(int n)
            begin
                if n = 0 return 1
                else return 
            end
        """
        expect = "Error on line 1 col 10: int"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_func_decl_with_incorrect_param_type(self):
        input = """        func fact(dynamic n)"""
        expect = "Error on line 1 col 18: dynamic"
        self.assertTrue(TestParser.test(input, expect, 289))
        
    def test_func_decl_but_missing_the_newline(self):
        input = """        func fact(number n)"""
        expect = "Error on line 1 col 27: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 2890))

    def test_func_decl_with_func_body_but_missing_the_open__brace(self):
        input = """        func fact(number n) var a <- 5"""
        expect = "Error on line 1 col 28: var"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_func_decl_with_func_body_but_missing_the_open__brace_1(self):
        input = """        func fact(number n) return 1"""
        expect = "Error on line 1 col 36: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_var_decl_mismatch_in_func_decl(self):
        input = """        func fact(number a)
            begin
                break
                for (number a <- 912 until a <= 1000 by 1) 
                begin
                    return 15
                end
            end
        number a <- 15, 2
"""
        expect = "Error on line 4 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 281))
        
    def test_var_decl_mismatch_in_func_decl_1(self):
        input = """        func fact(number a)
            begin
                break
                for number a <- 912 until a <= 1000 by 1
                begin
                    return 15
                end
            end
        number a <- 15, 2
"""
        expect = "Error on line 4 col 20: number"
        self.assertTrue(TestParser.test(input, expect, 301))
        
    def test_var_decl_mismatch_in_func_decl_2(self):
        input = """        func fact(number a)
            begin
                break
                for a until a <= 1000 by 1
                begin
                    return 15
                end
            end
        number a <- 15, 2
"""
        expect = "Error on line 9 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 302))
    
    def test_auto_type_func_decl(self):
        input = """func fact(bool abc)
                    begin
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test_main_func_decl(self):
        input = """func main() 
                    begin
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_main_func_with_params(self):
        input = """func main(number a, bool b)
                begin
                end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_main_func_with_invalid_paramdecl(self):
        input = """func main(a, bool b)
                begin
                end
            """
        expect = "Error on line 1 col 10: a"
        self.assertTrue(TestParser.test(input, expect, 2180))
        
    def test_main_func_with_invalid_paramdecl_1(self):
        input = """func main(number a, bool)
                begin
                end
            """
        expect = "Error on line 1 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 2181))
    

    def test_empty_statement_with_semicolon(self):
        # It should be invalid:
        input = """func fact(number a)
                    begin
                        ;
                    end"""
        expect = ";"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test_func_decl_with_auto_var(self):
        input = """func fact(number a)
            begin
                var b <- 5
                dynamic c
                number d[6]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test_comment_inside_func_decl(self):
        input = """func fact(number a)
            begin
                ##
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    
    def test_comment_inside_func_decl_1(self):
        input = """func fact(number a)
            begin
                begin
                    ##
                end
                test(1,2)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_comment_inside_func_decl_2(self):
        input = """func fact(number a)
            begin
                begin
                    ##
                end
                a[1,3] <- test(1,2)
            end
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
        
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
    
    def test_array_decl_in_function_decl(self):
        input = """func fact(number n) 
        begin
            number a[4] <- [1, 2, 3, 4.]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
        
    def test_standard_func_decl(self):
        input = """func fact(number b)
                begin
                    var a <- b
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test_standard_func_decl_1(self):
        input = """func fact(number a, number b)
                begin
                    a[1,a[0]] <- 9
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        
    # TEST VARIABLE DECLARATION
    def test_neg_num_decl(self):
        input = """number a <- -123456789
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202_1))
    
    def test_float_decl_with_no_int_part(self):
        input = """number a <- .25e+3;"""
        expect = "."
        self.assertTrue(TestParser.test(input, expect, 201_1))
    
    def test_var_decl_withoud_semicolon(self): 
        input = """dynamic x <- 1.0"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test_var_decl_withoud_semicolon(self): 
        input = """dynamic x <- 1.0;"""
        expect = ";"
        self.assertTrue(TestParser.test(input, expect, 274_1))
    
    
    def test_float_type_as_index(self):
        # The following should be invalid as index cannot be of float type:
        input = """func fact(number a[2])
        begin
            a[1.5] <- 90
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_int_with_underscore_as_index(self):
        input = """func fact(number b)
                begin
                    a[1230e-1] <- b
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
     
    def test_incosistencies_between_type_name_and_value(self):
        input = """bool a <- 5
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_incosistencies_between_type_name_and_value_1(self):
        input = """number a[3] <- [2, true, false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_incosistencies_between_type_name_and_value_2(self):
        input = """string b[3] <- [3, "fire", false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    
    # CHECK AGAIN
    def test_incosistencies_between_type_name_and_value_3(self):
        # "a = 5;" is valid only if it is placed inside a funcdecl:
        input = """a <- 5"""
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_multiple_var_decl(self):
        # ZCode only accept single declaration
        input = """number x, y <- 3, 4"""
        expect = "Error on line 1 col 8: ,"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_var_decl_mismatch_1(self):
        # Num. of var < Num. of expressions
        input = """number x <- 3.4, 5.6"""
        expect = "Error on line 1 col 15: ,"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test_array_decl_with_values(self):
        input = """number a[2] <- [1, 2, 3,4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        
    def test_array_decl_with_no_values(self):
        input = """number a[5,6,8]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_array_of_array_decl(self):
        input = """number a[2,3] = [1,2,3,4,5,6]"""
        expect = "Error on line 1 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 206))
    
    def test_array_of_function_type(self):
        # Parser should recognize the illegal keyword "var", "dynamic" if data type is array
        input = """dynamic x[2] <- [1, 2]"""
        expect = "Error on line 1 col 9: ["
        self.assertTrue(TestParser.test(input, expect, 207))

    # CHECK AGAIN
    def test_array_decl(self):
        # 1...2 should be OK because lexer does not separate data type in concat operation
        input = """number a[1....2] <- 4
        """
        expect = "Error on line 1 col 11: ..."
        self.assertTrue(TestParser.test(input, expect, 229))
    
    # CHECK AGAIN
    def test_array_decl_with_mixed_expressions(self):
        input = """func fact(number n)
            begin
                a[1] <- begin
                    a(0)
                end
                begin
                    ## Function call
                    a(0)
                end
                return 1
            end
"""
        expect = "Error on line 3 col 24: begin"
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test_var_decl_but_type_mismatch(self):
        input = """number a <- true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    def test_var_decl_but_rhs_is_a_list_2(self): # IMPORTANT TESTCASE
        input = """string b <- 102e3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    
    # CHECK AGAIN
    def test_missing_value_initialization_in_var_decl(self):
        input = """number a <- """
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_double_index_declaration(self):
        input = """number a[5][5]"""
        expect = "Error on line 1 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test_standard_block_var_decl(self):
        input = """func fact(number a, number b, number c) 
        begin
                  number d <- a == (b >= c[1])
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    # TEST PARAMETER DECLARATIONS
    def test_valid_params_decl(self):
        input = """func fact(number a, string b, bool c, number d)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_invalid_identifier(self):
        # Should return error if function type is used in param. decl.
        input = """func fact(number a, string b, bool break, var d)"""
        expect = "Error on line 1 col 35: break"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_invalid_data_type(self):
        input = """func fact(number a, string b, bool c, var d, dynamic e, troll f)"""
        expect = "Error on line 1 col 38: var"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    # TEST PROGRAM
    def test_specification_example(self):
        input = """ func isPrime(number x)
                    func main()
                        begin
                            number x <- readNumber()
                            if isPrime(x) printString("Yes")
                            else printString("No")
                        end
                    func isPrime(number x)
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
        expect = "Error on line 5 col 31: isPrime"
        self.assertTrue(TestParser.test(input, expect, 214))
        
    def test_program_1(self):
        input = """number a
                number b
                number c
            func foo(number a, number b) 
            begin
                number e
                e <- a + 4
                c <- a * d / 2.0 
                return c + 1
            end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    
    def test_mixed_statement_1(self):
        input = """        func fact(number a) 
            begin
            break
            if (a==2) a <- 3
            else for a until a >= 10 by 1
                writeNumber(a)
            begin
            continue
            return 12
            begin
                break
            end
            end
            end
            var a <- 131
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test_mixed_statement_2(self):
        input = """        func fact(number a) 
            begin
            break
            if (a==2) a <- 3
            else for a until a >= 10 by 1
                writeNumber(a)
            begin
            continue 
            return 12
            begin
                break
            end
            end
            var a <- 131
"""
        expect = "Error on line 15 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_mistyped_concat_operator(self):
        input = """string test <- "depressed"
                    func stringconcat(string test) 
                    begin
                        var i <- 0
                        for i until i >= 10 by 1 
                            concattest = test .... "z"... "asd" ... "sadasd"
                        return concattest;
                    end
                    """
        expect = "."
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_program_2(self):
        input = """ number a <- 123456
                    func fib(number n) 
                    begin
                        if (n == 1 or n == 0) n <- 2
                        else  
                            number a <- 0
                            number b <- 1
                            var i <- 2
                            for i until i >= n + 1 by 1
                            begin
                                c <- a + b
                                a <- b
                                b <- c
                            end
                            return b
                    end
                    func print() 
                    begin
                        print(fib(3+1))
                    end
                """
        expect = "Error on line 4 col 40: =="
        self.assertTrue(TestParser.test(input, expect, 299))
    
    def test_high_prec_op_between_low_prec_ops_without_paren(self): 
        # EXTREME IMPORTANT TESTCASE!!!
        # The expression (a < b || b > c) is not parsable
        # Because || has higher precedence than < and >
        input = """ func fact() 
                    begin
                        number a <- 10
                        number b <- 20
                        number c <- 30
                        if ((a < b or b > c) and (c < a or a > b)) 
                        begin
                            var i <- 0
                            for i until i >= 5 by 1 
                            begin
                                var d <- i * 3
                            end
                        end
                        else 
                        begin
                            break
                        end
                    end 
                    """
        expect = "Error on line 6 col 40: >"
        self.assertTrue(TestParser.test(input, expect, 303))
    
    # TEST ASSIGNMENT STATEMENT
    def test_lhs_is_index_and_rhs_is_an_array(self):
        input = """ func count_vowels(string str)
                    begin
                        string vowels[5] <- ["a", "e", "i", "o", "u"]
                        number integer <- 0
                        return count
                    end
                    func main()
                    begin
                        result <- count_vowels("Hello, World!")
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_invalid_double_assignment_operator(self):
        # The second '=' operator is invalid in an assignment statement:
        input = """ func main(number c) 
                    begin
                        var x <- 5
                        a <- b < ca <- b > ca <- b <= ca <- b >= c
                        x <- 3
                        return a
                    end
                """
        expect = "Error on line 4 col 36: <-"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_block_stmt_hidden_as_expression(self):
        # In all case, the first token of an assignment stmt is an Identifier 
        # Section 7.2: lhs can be a local variable or an element of an array
        input = """        func fact(number a) 
        begin
            a[1] <- 1
            [1]a <- 1
        end
"""
        expect = "Error on line 4 col 12: ["
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_invalid_function_assignment(self):
        # Function call cannot be the LHS of an assignment statement
        input = """func fact()
        begin
            foo() <- 1
        end
        """
        expect = "Error on line 3 col 18: <-"
        self.assertTrue(TestParser.test(input, expect, 224))
        
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
                   a <- ((a[10]... "2" + b(0))[10] 
                end
                """
        expect = "Error on line 3 col 46: ["
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test_subexp_on_lhs(self):
        # Not yet understand why '(' of '(a[1])' is invalid 
        # Because there isn't any statement that starts with '(',
        # check the spec carefully
        input = """func fact(number a)
        begin
            (a[1,2]) = b[2] + c[3]
        end
"""
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 236))
    
    # TEST IF STATEMENT
    def test_if_without_any_other_stmt(self):
        # Return error if the if-statement does not followed by any statement (or an empty block stmt)
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2)
                    end
                """
        expect = "Error on line 6 col 20: end"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_if_with_inline_stmt(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 308)) 
        
    def test_if_with_newline_stmt(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) 
                    
                        a <- 3
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 309)) 
        
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
        
    def test_elif_without_stmt(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3
                    elif (a > 3) 
                    elif
                    end
                """
        expect = "Error on line 7 col 20: elif"
        self.assertTrue(TestParser.test(input, expect, 311)) 
        
    def test_elif_with_inline_stmt(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3
                    elif (a > 3) a <- 4
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312)) 
        
    def test_elif_with_newline_stmt(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3
                    elif (a > 3) 
                    
                        a <- 4
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 313)) 
        
    def test_elif_inline_with_if(self):
        input = """func test(number a, string c) 
                    begin
                        begin
                        end
                    if (a > 2) a <- 3 elif (a > 3) 
                    
                        a <- 4
                    end
                """
        expect = "Error on line 5 col 38: elif"
        self.assertTrue(TestParser.test(input, expect, 314)) 
        
    def test_if_with_empty_block_stmt(self):
        input = """func test()
        begin
            if (a = (b >= c)) begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_if_else_stmt(self):
        input = """func test ()
        begin
    if (a==(b >= c)) 
    begin
    end
    else return 1
    end
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test_if_stmt_with_invalid_expression(self): # IMPORTANT
        # if (a=2) ... is not a valid expression
        input = """        func fact(number a) 
            begin
                if (a <- 2) a <- 3
                else
                for a until a >= 5 by 1.2
                begin
                    break
                end
                continue
                return 12
                break
            end
            number a <- 12901
"""
        expect = "Error on line 3 col 22: <-"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    # TEST FOR STATEMENT
    def test_for_stmt_with_rhs_as_an_index_op(self):
        input = """func test() 
                begin
                    for a[1] until a[1] > 5 by 1
                    begin
                    end
                end
        """
        expect = "Error on line 3 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_for_stmt_with_update_exp_as_index_(self):
        input = """func fact(number a)
        begin
            var b <- 5
            for b until b > c[3] by a[1] + foo()
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test_for_stmt_with_concat_operator(self):
        input = """func test()
        begin
            var a <- 3
            for a until "A"..."B"..."C" by 1
            begin
            end
        end
        """
        expect = "Error on line 4 col 33: ..."
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def test_standard_for_stmt(self):
        input = """        func fact(number a)
            begin
                break
                for a until a >= 10 by 2
                begin
                end
            end
        number a <- 131
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test_forstmt_on_same_line_with_blockstmt(self):
        input = """func fact(number a) begin ## comment
            for i until i >= 10 by 1 begin ## comment
                                c <- a + b
                                a <- b
                                b <- c
                            end
        end
        
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))
    # TEST CALL STATEMENT
    def test_call_stmt(self):
        input = """func a ()
        begin
    foo(2+x)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        
    def test_call_stmt_name_near_same_as_special_func(self):
        input = """func teask(number a, dynamic b, number c[5], string d) 
        begin
                print()
            end
            """
        expect = "Error on line 1 col 21: dynamic"
        self.assertTrue(TestParser.test(input, expect, 261))
    '''  
    def test_standard_for_stmt_1(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for (a=9_1_2_3 ,foo({}) ,{}+1_12_2) return 1_5;
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_for_stmt_with_empty_expressions(self):
        input = """        fact: function integer ( a : integer) {
            break;
            for ( , ,) return 1;
        }
"""
        expect = "Error on line 3 col 18: ,"
        self.assertTrue(TestParser.test(input, expect, 285))
    '''
    def test_case_121(self):

        input = """
            func name()
            begin
                a[3 + foo(2)] <- a[b[2, 3]] + 4
        """
        expect = """Error on line 5 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 121))
    # TEST SPECIAL FUNCTION
    # readInteger() function:
    def test_read_integer_1(self):
        input = """func a ()
        begin
    readNumber(a,b)
   end
   """
        expect = "Error on line 3 col 15: a"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    # printInteger() function: must contain exactly 1 param
    def test_print_integer_with_param(self):
        input = """func a() 
        begin
    printInteger(a)
   end
   begin
end
"""
        expect = "Error on line 5 col 3: begin"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_print_integer_without_param(self):
        input = """func test ()
        begin
            writeNumber()
            begin
            end   
        end
"""
        expect = "Error on line 3 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 249))
    
    # printBoolean() function: must contains 1 arg
    def test_print_boolean(self):
        input = """func test ()
        begin
            writeBool()
            begin
            end   
        end
        """
        expect = "Error on line 3 col 22: )"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    # TEST BLOCK STATEMENT
    def test_double_block_stmt_with_var_decl(self):
        input = """func test()
        begin
            begin
                number r
                number s
                r <- 2.0
                number a[5]
                number b[5]
                s <- r * r * myPI
                a[0] <- s
            end
        end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_function_followed_by_another_block_stmt(self):
        input = """func test ()
        begin
            readNumber()
            begin
            end   
        end"""
        expect = "Error on line 6 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_function_decl_inside_block_stmt(self):
    # MT22 does not allow func declaration inside block stmt
        input = """func test ()
        begin
            func test1 ()
            begin
            end
        end
"""
        expect = "Error on line 3 col 12: func"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    # MISCELLANEOUS TESTS
    def test_double_index(self): 
        input = """number arr[1][2]
        """
        expect = "Error on line 1 col 13: ["
        self.assertTrue(TestParser.test(input, expect, 226))
    
    def test_index_list_in_array(self):
        input = """a[1,2] <- 2
        """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test_double_index_in_function_body_1(self):
        input = """func test() 
        begin
            a[1][2] <- a[1][2]
        end
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.test(input,expect, 228))
    
    def test_double_index_in_function_body_2(self):
        input = """func test ()
        begin
            a[1] <- a[1][2]
        end
"""
        expect = "Error on line 3 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 230))
    
    def test_single_index_in_function_body(self):
        input = """func test ()
        begin
            a[1] <- a[2]
        end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    
    def another_double_index_test(self):
        input = """func test(string b, number b) 
                    begin
                        a[1] <- 2 + a[1,2,foo(3)][2]
                    end
        """
        expect = "Error on line 3 col 54: ["
        self.assertTrue(TestParser.test(input, expect, 299))
    
    # HIGH IQ TESTCASE
    def test_51(self):
        # The following testcase is invalid because the "identifier" "foo(a)" contains
        # illegal character '('. Note that a program only contains vardecl or funcdecl.
        # And both of these declarations required an identifier in the first place.
        input = """foo(a) <- {}"""
        expect = "Error on line 1 col 0: foo"
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def test_52(self):
        # Same reason as test_51
        input = """{}"""
        expect = "{"
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_53(self):
        # This testcase is obviously invalid (we can even using the same reasoning as above)
        # But the problem here is to IDENTIFY THE FIRST CHARACTER THAT MAKES IT INVALID,
        # Here, because "if" is a keyword so it cannot be used as an identifier.
        # => IMPORTANT TESTCASE
        input = """if (a>3) return 1;"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_case_101(self):

        input = """ func test(number a, bool b)
        return a + b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))
        
    def test_case_102(self):
        input = """ func test(number a, bool b) return a + b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 102))
        
    def test_case_103(self):

        input = """ func test(number a, bool b)
        
        return a + b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))
    
    def test_case_183(self):

        input = """
            func calculateExpApproximation(number n) ## test here
            begin ## test here
                number result <- 1.0 ## test here
                number term <- 1.0 ## test here
                for i until i <= n by i ## test here
                begin ## test here
                    term <- (1.0 / n) ## test here
                end ## test here
                return result ## test here
            end ## test here
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 183))
    
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

    def test_case_1234(self):
        input = """func main() return 1
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1234))
        
    def test_case_1235(self):
        input = """func main() begin
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1235))
        
    def test_case_1236(self):

        input = """ func interpolationSearch(number arr, number lo, number hi, number x)
            begin
                if (lo <= hi and x < arr[lo] and x < arr[hi])
                begin
                    ## Probing the position with keeping
                    ## uniform distribution in mind.
                    pos <- lo + ((hi - lo) / (arr[hi] - arr[lo]) *
                                (x - arr[lo]))
            
                    ## Condition of target found
                    if arr[pos] == x
                        return pos
            
                    ## If x is larger, x is in right subarray
                    if arr[pos] < x
                        return interpolationSearch(arr, pos + 1, hi, x)
            
                    ## If x is smaller, x is in left subarray
                    if arr[pos] > x
                        return interpolationSearch(arr, lo, pos - 1, x)
                end
            return -1
            end
        """
        expect = "Error on line 3 col 35: <"
        self.assertTrue(TestParser.test(input, expect, 1236))
        
    def test_case_1237(self):

        input = """var a[1,2] <- [12,3] \n"""
        expect = "Error on line 1 col 5: ["
        self.assertTrue(TestParser.test(input, expect, 1237))
        
    def test_case_1238(self):
        input = """number x <- [1, 2, 3]
var x <- [1, 2, 3]
dynamic x <- [1, 2, 3]
number x
     x <- [1, 2, 3]
number x[3]
     ## x <- [1, 2, 3]
number x <- [1, 23, 3]
"""
        expect = "Error on line 5 col 5: x"
        self.assertTrue(TestParser.test(input, expect, 1238))
        
    def test_case_1239(self):
        input = """number x <- [1, 2, 3]
var x <- [1, 2, 3]
dynamic x <- [1, 2, 3]
number x
     ## x <- [1, 2, 3]
number x[3]
     ## x <- [1, 2, 3]
number x <- [1*2, 2+3, 3-5]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1239))
        
    def test_case_1240(self):
        input = """func test() begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
            a[3 + foo(2)] <- foo(2,3)[b[2, 3]] + 4
            a[3 + foo(2)] <- c[10][10]
        end
        """
        expect = "Error on line 4 col 34: ["
        self.assertTrue(TestParser.test(input, expect, 1240))
        
    def test_case_1241(self):
        input = """number a <- []
        """
        expect = "Error on line 1 col 13: ]"
        self.assertTrue(TestParser.test(input, expect, 1241))
    
    def test_case_1242(self):
        input = """func main()
        begin
        string c <- "\mmmp"
        end
        """
        expect = '\m'
        self.assertTrue(TestParser.test(input,expect,1242))
        
    def test_case_1243(self):
        input = """func main()
        begin
        string c <- "\\mmmp"
        end
        """
        expect = '\m'
        self.assertTrue(TestParser.test(input,expect,1243))
        
    def test_case_1244(self):
        input = """
             
        func main()
        
        begin
        
        
        string c <- "\\\mmmp"
        
        
        end
        
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input,expect,1244))
        
    def test_case_1245(self):
        input = """func test(number a[1,2,3])
        begin
            return 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1245))
        
    def test_case_1246(self):
        input = """var x
        """
        expect = "Error on line 1 col 5: \n"
        self.assertTrue(TestParser.test(input,expect,1246))
        
    def test_case_1247(self):
        input = """func main() begin
            foo([1,2,3],1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1247))
    
    # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=2695
    def test_case_1248(self):
        input = """number a <- 0001.200
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1248))
        
    def test_case_1249(self):
        input = """func main()
begin
           if (a) do(a)
           elif (a=2=2) do(b)
end
"""
        expect = "Error on line 4 col 20: ="
        self.assertTrue(TestParser.test(input,expect,1249))
        
    def test_case_1250(self):
        input = """
        ## test
"""
        expect = "Error on line 3 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1250))
        
    def test_case_1251(self):
        input = """var x <- [1,2,3]
        dynamic x <- [1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1251))
        
    def test_case_1252(self):
        input = """var arr <- [1,2,3]
func test() begin
    print( ((arr))[0] )
end
        """
        expect = "Error on line 3 col 18: ["
        self.assertTrue(TestParser.test(input,expect,1252))
        
    def test_case_1253(self):
        input = """var arr <- [1,2,3]
func test() begin
    print( (f(1,2,3))[0] )
end
        """
        expect = "Error on line 3 col 21: ["
        self.assertTrue(TestParser.test(input,expect,1253))
        
    def test_case_1254(self):
        input = """var arr <- [1,2,3]
func test() begin
    f()[0, 1, 2] <- "abc"
    number x <- [1, 2, 3][1] 
end
        """
        expect = "Error on line 3 col 7: ["
        self.assertTrue(TestParser.test(input,expect,1254))
        
    def test_case_1255(self):
        input = """func foo(number a<-5)
        """
        expect = "Error on line 1 col 17: <-"
        self.assertTrue(TestParser.test(input,expect,1255))
        
    def test_case_1256(self):
        input = """
        ## J:Gx)c
number M_[4.836e+49,28.739] <- Jg
## P8p^
func w52i ()
begin
## PuIz ;:!"VcF.[MQ{|
## /r/
if 77 HYb(false, Tpw1, BCv)[57.680, FHe] <- "'"("
elif "'"'"O'"" if false if "'"" BwN <- oCJv
elif "'"$" return wl
elif true sm(39E01, true, rZ7)
elif true return false
elif "'"-'"" return ":C'"'""
elif "'")'"%" return 95
else continue
elif Et_O p6(13, Oyn)[15E71] <- kJx
elif "&'"'"L'"" break
elif false return false
elif "U'"" I1c(2E+75, "'"E'"'"7", "'"2'"")
elif false dynamic z9_E
elif true begin
for tL30 until true by "*-E"
Su <- VCn
return "G4X'""
end
end
        """
        expect = "Error on line 3 col 31: Jg"
        self.assertTrue(TestParser.test(input,expect,1256))
    
    def test_case_1257(self):
        input = """number a[0] <- []
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input,expect,1257))
        
        
        
    