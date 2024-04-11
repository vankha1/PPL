
#     def test501(self):
#         input = """
#         func f(number x)
# func g() begin
#     return 2
# end
# func f(number y) begin
#     return y
# end
# func main() begin
#     return
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 502))
        
#     def test502(self):
#         input = """
#     func a()
#         return true
#     func main()
#     begin
#         dynamic b <- a
#         dynamic c <- b() 
#     end     
#         """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 503))
    
#     def test503(self):
#         input = """
#         func inc(number a) 
# func main() begin
#     string c <- "hello world" 
#     var x <- inc(3)...c 
# end 
# func inc(number a) return a+1 
#         """
#         expect = "Type Mismatch In Statement: Return(BinaryOp(+, Id(a), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 519))
        
#     def test504(self):
#         input = """
#         func foo()
# begin
#     number x
#     if (x = 1)
#         return true
#     else
#         return 1
# end
#         """
#         expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
#         self.assertTrue(TestChecker.test(input, expect, 504))
        
#     def test505(self):
#         input = """
#         func main() begin
#  if (false) var x <- 1
# x <- 1
# end
#         """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 505))
    
#     # This test wrong at AST gen stage
# #     def test506(self):
# #         input = """
# #     func writeNumber(number x) begin
# #         return
# #     end
# #     func main() begin
# #     writeNumber(4)
# # end
# #         """
# #         expect = "Redeclared Function: writeNumber"
# #         self.assertTrue(TestChecker.test(input, expect, 506))
        
#     def test507(self):
#         input = """
#     func foo(number u) begin
#         return 5
#     end
#         func main() begin
#     number a
#     dynamic x
#     var y <- a + foo(x)
#     x <- 5
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 507))
        
#     def test508(self):
#         input = """
#         func main() begin
#  dynamic x
#  if (x) begin
#     number y <- 1
# end
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 508))
        
#     def test509(self):
#         input = """
#         func main() begin
#  dynamic x
#  for x until true by 1 begin
#     x <- x + 1
# end
# end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 509))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8428
#     def test510(self):
#         input = """func f(number x, number x)
# func f(number x, number y) begin
#  return x + y
# end
#     func main() begin
#         return
#     end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 510))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8404
#     def test511(self):
#         input = """func main() begin
#         dynamic x
#         x <- (x = 1) or ("abc" == "abc")
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
#         self.assertTrue(TestChecker.test(input, expect, 511))
        
#     def test512(self):
#         input = """func f() return 1
# func main() begin
#  var x <- f
# end
# """
#         expect = "Undeclared Identifier: f"
#         self.assertTrue(TestChecker.test(input, expect, 512))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9576
#     def test513(self):
#         input = """func main() begin
#         var c <- c
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 513))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9576
#     def test514(self):
#         input = """func main() begin
#         dynamic c <- c
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, Id(c))"
#         self.assertTrue(TestChecker.test(input, expect, 514))
    
#     def test515(self):
#         input = """func main() begin
#         number a[4] <- [1, true, false, "a"]
#         end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), BooleanLit(False), StringLit(a))"
#         self.assertTrue(TestChecker.test(input, expect, 515))
        
#     def test516(self):
#         input = """func main()
#         """
#         expect = "No Function Definition: main"
#         self.assertTrue(TestChecker.test(input, expect, 516))
        
#     def test517(self):
#         input = """ func x()
#         func main() return
#         """
#         expect = "No Function Definition: x"
#         self.assertTrue(TestChecker.test(input, expect, 517))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9824
#     def test518(self):
#         input = """dynamic a
# func foo() return a
# func main()
# begin
#       number num <- foo()
# end
# """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 518))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5815
#     def test520(self):
#         input = """
# func main()
# begin
#       dynamic a
#       a <- [1, 2, true, false]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 520))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5591
#     def test521(self): # VAR
#         input = """
#         func main() begin
#             number x[1.2]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 521))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=5591
#     def test522(self):
#         input = """
#         func f(bool x) begin
#         if (x)
#             return 1
#         end
#         func main() begin
            
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 522))
    
#     def test523(self):
#         input = """
#         func f() begin
#   var input <- readString()
#   return input
# end
#     var x <- f()
#     func main() begin
    
#     end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 523))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=8632
#     def test524(self):
#         input = """
#         func hello(number x)
#         begin
#             dynamic a
#             string b[4]
#             dynamic c <- b[a]
#             ## type a is Number
#             bool d <- c == ""
#             bool e <- not a
#         end
#         func main()
#         begin
#             hello(1)
#         end
        
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 524))
        
#     def test525(self):
#         input = """
#         ## Function scope: parameter a
#         func hello(number a)
#         begin
#             ## Block scope: local variables a
#             dynamic a
#         end
#         func main()
#         begin
#             hello(1)
#         end
        
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 525))


#     def test526(self):
#         input = """
#         func hello(number a)
#         begin
#         end
        
#         func main()
#         begin
#             dynamic b
#             hello(b)
#             ## b is Number, because the parameter of hello() is number
#             number c <- b + 1
#         end
        
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 526))


#     def test527(self):
#         input = """
#         func hello(number a)
#         begin
#         end
        
#         func main()
#         begin
#             dynamic a 
#             dynamic b <- [[1,2,3], a]
#             ## a is type number[3]
#             number c <- a[0]
#             number d <- a
#         end
        
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(d), NumberType, None, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 527))
        
#     def test528(self):
#         input = """func main() begin
#         dynamic a
#         dynamic b
#         number x[2,1] <- [[a], [1]]
#         number y[2,2] <- [[1, 2], b]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 528))
        
#     def test529(self):
#         input = """func foo() begin
#             dynamic a
#             return 3
#             return true
#         end
#         func main() begin
        
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 529))
        
#     def test530(self):
#         input = """func foo() begin
#             dynamic a
#             bool b
#             if (2 = 5) return b
#             else return a
#         end
#         func main() begin
        
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 530))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9664
#     def test531(self): # VAR
#         input = """func foo() 
#         begin
#             dynamic a
#             return a
#         end
#         func main() begin
#             number b <- foo()
#         end
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 531))
        
#     def test532(self):
#         input = """
#         func foo (number i)
#         begin
#             if (i>=0)
#                 return 69 
#         end
#         func main ()
#         begin
#             var i <- foo(10)
#             writeNumber(i)
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 532))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9900
#     def test533(self):
#         input = """func foo(number a, number b)
# func main()
# begin
# 	return 1 + foo(1, "str")
# end
# func foo(number a, number b)
# begin
# 	return 0
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(str)])"
#         self.assertTrue(TestChecker.test(input, expect, 533))
        
#     def test534(self):
#         input = """func foo(number a)
#         func foo(number a, number b) return 0
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 534))
        
#     def test535(self):
#         input = """func foo(number a, number b)
#         func foo(number b) return 0
#         func main() begin
        
#         end
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 535))
        
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=9968
#     # def test536(self):
#     #     input = """func a()
#     #     func main() begin
#     #         number a
#     #         a()
#     #     end
#     #     """
#     #     expect = ""
#     #     self.assertTrue(TestChecker.test(input, expect, 536))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10008
#     # def test537(self):
#     #     input = """
#     #     func foo(number a) return a
#     #     func foo(number a)
#     #     func main() begin
        
#     #     end
#     #     """
#     #     expect = ""
#     #     self.assertTrue(TestChecker.test(input, expect, 537))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10012
#     def test538(self):
#         input = """func main()
# begin 
#     dynamic a
#     number x[3,3] <- a[1]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayCell(Id(a), [NumLit(1.0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 538))
    
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10252
#     def test539(self):
#         input = """func main()
# begin
#     number arr[2,2] <- [[1,2],[1,2]]
#     var x <- arr[0,3]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 539))
       
#     # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=10132 
#     # def test540(self): # VAR
#     #     input = """
#     #     func main()
#     #         begin
#     #             dynamic num
#     #             bool arr <- num and (num > num)
#     #         end
#     #     """
#     #     expect = "Type Mismatch In Expression: BinaryOp(and, Id(num), BinaryOp(>, Id(num), Id(num)))"
#     #     self.assertTrue(TestChecker.test(input, expect, 540))

#     #     expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
#     #     self.assertTrue(TestChecker.test(input, expect, 540))

#     def test546(self): 
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
#         self.assertTrue(TestChecker.test(input, expect, 546))