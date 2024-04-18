##################### 100 TC #############################
from TestUtils import TestChecker

class StaticCheck:
    
    ## TYPE MISMATCH STMT: RETURN-STMT
    

    def test501(self):
        input = """
func f()
begin
    dynamic x
    x <- [[1, 2, 3], [4, 5, 6]]
    return x[0, 0]
end

func main()
begin
    number x <- f()
end

"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501))
        
    def test502(self):
        input = """
func f(number x)

func main()
begin
    number x <- f(2)
    writeNumber(x)
end

func f(number x)
begin
    if (x <= 2) return f(x - 1) + f(x - 2)
    return 1
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test546(self): 
        input = """
func f(number x)
begin
    return f(x)
end

func main()
begin
    dynamic d <- f(10)
end
"""
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 546))


    def test551(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    dynamic a <- add(x, y) + 1
end

func add(number x, number y)
    return "Hello"
"""
        expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 551))
        
        
    def test559(self):
        input = """
func foo(number a)

func main()
begin
    number a <- foo(1)
    return
end

func foo(number a)
begin
    return
end
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 559))
        
    def test573(self):
        input = """
func f(number arr[10], number n)
begin
    if ((n < 0) or (n >= 10)) return -999
    number i <- 0
    for i until i >= n by 1
        if (arr[i] < 10) return i
    
    return not (n < 20)
end

func main()
begin
    f([1, 9, 6, 5, 3, 8, 10, 28, 0, -10], 10)
end
"""
        expect = "Type Mismatch In Statement: Return(UnaryOp(not, BinaryOp(<, Id(n), NumLit(20.0))))"
        self.assertTrue(TestChecker.test(input, expect, 573))
                
    ## ARRAYLITERAL
    def test503(self):
        input = """
func main()
begin
    var x <- [[1, 2, 3], [4, 5, 6]]
    var y <- x[0, 0] + 1
    writeBool(y)
end

"""
        expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test509(self):
        input = """
func f(number x[2, 3])
    return x[2]

func main()
begin
    number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    writeNumber(f()[2])
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 509))
        

    def test510(self):
        input = """
func f(number x[2, 3])
    return x

func main()
begin
    number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    writeNumber(f(x)[0, 1])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 510))
        
        
    def test511(self):
        input = """
func f(number x[2, 3])
    return x

func main()
begin
    dynamic x <- [[1, 2, 3], [4, 5, 6]]
    var y <- x[0, 0]
    writeString(y)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 511))
        
    def test519(self):
        input = """
func main()
begin
    var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 519))
        
    def test574(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    var arr <- [[a, 1], [b, true], [c, "Hello"]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
        self.assertTrue(TestChecker.test(input, expect, 574))

    def test575(self):
        input = """
dynamic x
dynamic y
func main()
begin
    dynamic z
    dynamic arr <- [[1, x], [2, y], [3, z]]
    x <- 20
    y <- 30
    z <- "Hi"
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
        self.assertTrue(TestChecker.test(input, expect, 575))

    def test576(self):
        input = """
func main()
begin
    var x <- [10, 20, 40]
    var y <- [true, false, true]
    number a[2, 3] <- [x, y]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 576))
        
    def test577(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 3] <- [x, y]
    x <- [10, 20, 40]
    y <- [true, false, true]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input, expect, 577))
    
    def test578(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 3] <- [x, y]
    y <- [y[1] + y[2], y[2] - y[0], y[0] + y[1] < y[2]]
    x <- [1, 9, 6]
    writeNumber(a[0, 0])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(BinaryOp(+, ArrayCell(Id(y), [NumLit(1.0)]), ArrayCell(Id(y), [NumLit(2.0)])), BinaryOp(-, ArrayCell(Id(y), [NumLit(2.0)]), ArrayCell(Id(y), [NumLit(0.0)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(y), [NumLit(0.0)]), ArrayCell(Id(y), [NumLit(1.0)])), ArrayCell(Id(y), [NumLit(2.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 578))

    def test580(self):
        input = """
func main()
begin
    var x <- [[1, 2], [3, 4, 5]]
    writeNumber(x[0, 2])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 580))

    def test583(self): ## Bởi vì trường hợp dynamic d <- d 
        input = """
dynamic a
func main()
begin
    number a[2, 3] <- [a, [10, 20, 30]] ## a type is number a[2,3]
    a <- [1, 9, 6]
    writeNumber(a[0])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(NumLit(10.0), NumLit(20.0), NumLit(30.0)))"
        self.assertTrue(TestChecker.test(input, expect, 583))

    def test584(self):
        input = """
dynamic a
func main()
begin
    var x <- [a, [1, 2, 3]]
    a <- [1, 9, 6]
    x <- [[3, 9, 6], [1, 3, 2]]
    writeNumber(x[0, 0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 584))


    def test586(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    var x <- [a, b, c, [[1, 2, 3, 4], [5, 6, 7, 8]]]
    c[0] <- d
    d <- [0, 3, 1]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(d), ArrayLit(NumLit(0.0), NumLit(3.0), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 586))


    def test597(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [a, [b, c], [2, 3]]
    writeNumber(a[0] + a[1] + b + c)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 597))
    
    def test598(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic x <- [a, [b, c], [2, d]]
    d <- x[0, 0] + x[0, 1]
    writeNumber(a[0] + a[1] + b + c + d)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 598))
    
    def test599(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic x <- [a, [b, c], [d + 20, d ... "Hello"]]
    d <- x[0, 0] + x[0, 1]
    writeNumber(a[0] + a[1] + b + c + d)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(d), StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 599))
    
    def test500(self):
        input = """
func main()
begin
    number arr[2, 2] <- [1, 2, 3, 4]
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 500))
        
    def test_ifs_auto_inherit_empty(self): 
        input = """
        func main() 
        begin
            dynamic x
            dynamic y
            dynamic z
            number a[3, 3] <- [x, y, z]
            x <- [1, 2, 3]
            y <- [4, 5, 6]
            z <- [7, 8, 9]
            writeNumber(x[0] + z[0] + y[1])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4000))
    
    def test_ifs_auto_inherit_empty2(self): ## Bug here
        input = """
        func main() 
        begin
            dynamic x
            dynamic y
            dynamic z
            number a[3, 3] <- [x, y, [1, 2, 3]]
            x <- [1, 2, 3]
            y <- [4, 5, 6]
            z <- [7, 8, 9]
            writeNumber(x[0] + z[0] + y[1])
            dynamic t
            number b[1,3,4] <- [t]
            t <- [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4001))
    
    def test_ifs_mixed_inherit(self):
        input = """
        func main()
        begin
            var x <- [[[1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 4002))        
        
        
        
        
        
                        
    ## ARRAY-CELL
    def test505(self):
        input = """
dynamic x
func main()
begin
    x <- [1, 2, 3, 4, 5, 6]
    var y <- x[0, 0] + 1
    writeNumber(y)
end

"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 505))


    def test523(self):
        input = """
func f(number x)
begin
    if (x = 0) return 0
    elif (x = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- [1, 2, 3]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 523))


    def test552(self): ## Không lỗi vì trong forum (Khai báo array)
        input = """
func add(number x, number y)

func main()
begin
    dynamic a
    a[0] <- [1,2,3] 
end

func add(number x, number y)
    return "Hello"
"""
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 552))


    def test553(self):
        input = """
func main()
begin
    number arr[3, 2] <- [[1, 2], [3, 4], [5, 6]]
    number b[2] <- arr[1]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 553))
        
    ## UNDECLARED/REDECLARED FUNCTIONS
    def test506(self):
        input = """
dynamic x <- f(2)
func f(number x)

func main()
begin

end
"""
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 506))
    
    
    def test527(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(pow(x, y))
end

func add(number a, number b)
begin
    return a + b
end
"""
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input, expect, 527))
    
    def test529(self):
        input = """
func f(number x)

func main()
begin
    number x <- 10
    number y <- f(x)
    writeNumber(y)
end

func f(string x)
begin
    return x == "Hello"
end
"""
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 529))   


    def test542(self):
        input = """
func f()

func main()
begin
    number x <- g(1, 2, 3)
end
"""
        expect = "Undeclared Function: g"
        self.assertTrue(TestChecker.test(input, expect, 542))   

    def test554(self):
        input = """
func f(number arr[10], number x)

func main()
begin
    dynamic n
    var i <- 0
    number arr[10]
    for i until true by 1
    begin
        n <- readNumber()
        if ((n > 10) or (n <= 0)) writeString("Try again")
        else break
    end
    
    for i until i >= n by 1
        arr[i] <- readNumber()
    
    f(arr, n)
end

func f(number a[5], number n)
    return
"""
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 554))


    def test560(self): ## Tên biến có thể trùng với tên hàm
        input = """
var f <- 10
func f()
    return

func main()
begin
    dynamic a
    dynamic b
    number c
    dynamic x <- f([a, b, c])
    x <- ["Hello", ", my name is ", "Kien"]
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [ArrayLit(Id(a), Id(b), Id(c))])"
        self.assertTrue(TestChecker.test(input, expect, 560))


    def test571(self):
        input = """
func main()

func main()

func main()
begin
    if (1) writeBool(true)
    else writeBool(false)
end
"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 571))
                    
    ## NO ENTRY POINT
    
    def test507(self):
        input = """
func f(number x)

dynamic x <- f(2) + 1

func f(number y)
begin
    if (y <= 1) return 1
    return y * f(y - 1)
end

func main()
begin
    return 2
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 507))


    def test531(self):
        input = """
func f(number arr[10], number n)
begin
    var i <- 0
    for i until i >= n by 1
        writeNumber(arr[i])
end

"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 531))


    def test545(self):
        input = """
func f()
begin

end
dynamic a
number b
bool c
string d
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 545))


    def test582(self):
        input = """
func test(number x)
begin
    var a <- x
    var b <- -a
    var c <- a + b
    writeNumber(a + b + c)
end

func main()
begin
    test(2018)
    return -1
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 582))

    def test_426 (self):
        input = """
        bool x <- true
        func foo() begin
            return x
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 4003))
                
    ## NO FUNCTION DEFINITION

    def test508(self):
        input = """
func f(number x)

dynamic x <- f(2) + 1

func main()
begin
    return
end
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 508))


    def test543(self):
        input = """
number x
number y
func f()

func main()
    return
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 543))


    def test544(self): ## Tên biến được trùng với tên hàm
        input = """
func f()

number f
dynamic x
func main()
    return
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 544))
        
    def test589(self): # Confused
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
        expect = "No Function Definition: test"
        self.assertTrue(TestChecker.test(input, expect, 589))
        
                
    ## UNDECLARED IDENTIFIER
    def test512(self):
        input = """
func f(number x[2, 3], number i, number j)
    return x[i, j]

func main()
begin
    dynamic x <- [[1, 2, 3], [4, 5, 6]]
    var i <- 0
    for i until i >= 2 by 1
        for j until j >= 3 by 1
            writeNumber(f(x, i, j))
end
"""
        expect = "Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input, expect, 512))
        
    def test581(self):
        input = """
func test(number x)
begin
    var y <- test
    test(2018)
end
"""
        expect = "Undeclared Identifier: test"
        self.assertTrue(TestChecker.test(input, expect, 581))
               
    ## BUILT-IN FUNC
    def test513(self):
        input = """
func main()
begin
    number x <- readNumber()
    if (x <= 10) writeString("Number is less than or equal to 10")
    elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
    else writeString("Invalid number!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 513))


    def test536(self):
        input = """
func main()
begin
    dynamic x <- readBool()
    dynamic y <- not readBool()
    if (x and y) writeNumber(1)
    else writeNumber(0)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 536)) 
        
    def test557(self):
        input = """
func main()
begin
    dynamic x <- "Hello"
    if (x == "Hello") writeString(x)
    else writeString("Something weird!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 557))
        
           
    ## MIXED
    def test514(self):
        input = """
func isPrime(number x)

func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("x is a prime number")
    else writeString("x is not a prime number")
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 514))
        
        
    def test515(self):
        input = """
func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main()
begin
    var num1 <- readNumber()
    var num2 <- readNumber()
    if (areDivisors(num1, num2)) writeString("Yes")
    else writeString("No")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 515))

    def test528(self):
        input = """
func add(number x, number y)

func main()
begin
    var i <- 0
    for i until i > 10 by 0
    begin
        i <- add(i, 1)
        writeNumber(i)
    end
end

func add(number a, number b)
begin
    number x <- a + b
    return x
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 528))
        
    def test550(self):
        input = """
number x
number y
func add()
    return x + y

func main()
begin
    x <- readNumber()
    y <- readNumber()
    writeNumber(add())
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 550))
        
    def test562(self):
        input = """
dynamic a <- [[3, 9, 2, 10, -1], [0, -10, 5, 3, 11], [10, 9, -27, 36, 4]]
func sort(number a[5])
begin
    var i <- 0
    var j <- 0
    for i until i > 4 by 1
        for j until j > 4 by 1
            if (a[i] > a[j])
            begin
                var temp <- a[i]
                a[i] <- a[j]
                a[j] <- temp
            end
end

func main()
begin
    var i <- 0
    for i until i > 2 by 1
        sort(a[i])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 562))


    def test_4011(self):
        input = """
        func areDivisors(number num1, number num2) 
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Nope")
            else writeString("What?")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4011))
    
    def test_4012(self):
        input = """
        func main()
        begin
            number x <- readNumber()
            if (x <= 5) writeString("Number is smaller or equal 5")
            elif ((x < 5) and (x <= 10)) writeString("Number between 5 and 10")
            else writeString("Number greater than 10")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4012))
                        
    ## BREAK/CONTINUE IN LOOP
    def test516(self):
        input = """
func f()
begin
    var i <- 0
    for i until i > 10 by 1
    begin

    end
    continue
end

func main()
begin
    f()
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 516))
    
    def test530(self):
        input = """
func main()
begin
    var i <- 0
    for i until i < 0 by 1
    begin
        string x <- readString()
        if (x == "Hello") 
        begin
            x <- x ... ", world!"
            writeString(x)
        end
        else writeString("Try again")
    end
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 530))

    def test548(self):
        input = """
func main()
begin
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 548))
        
    def test549(self):
        input = """
func main()
begin
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 549))
        
                        
    ## VARDECL ARRAYLITERAL
    def test520(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[3, 3] <- [a, b, c]
    a <- [1, 2, 3]
    b <- [4, 5, 6]
    c <- [7, 8, 9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 520))
    
    def test555(self):
        input = """

    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic e
    number arr[2, 2] <- [[a, b]]
    ## number c[2, 2] <- arr

"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 555))
        
    def test556(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    var arr <- [[a], [b], [c], [1]]
    arr <- [[1], [2], [3], [4]]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test558(self):
        input = """
func main()
begin
    dynamic x <- [1, 2, 3]
    dynamic a <- x
    writeNumber(a[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 558))


    def test564(self):
        input = """
func f(number n)

number a[2, 3] <- [[f(1), f(2), f(3)], [f(4), f(5), f(6)]]
func main()
begin
    var i <- 0
    dynamic j <- 0
    for i until i > 1 by 1
        for j until j > 2 by 1
            writeNumber(a[i, j])
end

func f(number a)
    return a
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 564))

    def test587(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c <- a ... ", world!"
    a <- b
    b <- [1, 2, 3]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 587))
    
    def test588(self): # Confused
        input = """
func main()
begin
    number x
    begin
        number x <- (10 + x) * 2
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 588))
                   
    ## CALL-EXPRESSION
    def test521(self):
        input = """
func f(number x[3])
begin
    return
end
    
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    f([a, b, c])
    a <- 3
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521))

    def test522(self):
        input = """
func f(number x[2, 3])
    
func main()
begin
    dynamic a
    number x[2, 3] <- f(a)
    a[0] <- [1, 2, 3]
end

func f(number x[2, 3])
    return x
"""
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 522))
    
    def test524(self):
        input = """
func max(number x, number y)
begin
    if (x <= y) return y
    return x
end

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    number z <- readNumber()
    writeNumber(max(max(x, y), z))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524))


    def test525(self):
        input = """
func pow(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(pow(x, y))
end

func pow(number a, number b)
begin
    if (b = 0) return 1
    number k <- pow(a, b / 2)
    if (b % 2 = 0) return k * k
    return a * k * k
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 525))
    
    
    def test532(self):
        """INFER PARAMETERS"""
        
        input = """
func f(number arr[10], number n)
begin
    var i <- 0
    for i until i >= n by 1
        writeNumber(arr[i])
end

func main()
begin
    dynamic n
    f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
    n <- 10
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 532))

    def test561(self):
        input = """
func f(number a[3], number b[3])
    return

func main()
begin
    f([1, 3, 2], [1, "Hello", 2])
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 561))


    def test565(self):
        input = """
func f(number x[2, 3])
    return x[0]

func main()
begin
    dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 565))


    def test566(self):
        input = """
func f(number n)

func main()
begin
    var i <- f(2, 3)
end

func f(number a)
    return a
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 566))


    def test567(self):
        input = """
func f(number x, number y)

func main()
begin
    var i <- f(2)
end

func f(number a)
    return a
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 567))
        
        
    def test579(self):
        """INFER PARAM"""
        input = """
func f(number x, bool y, string z)
    return not y

func main()
begin
    dynamic x
    dynamic y
    dynamic z
    bool t <- f(x, y, z)
    writeBool(y and not t)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 579)) 
        
    def test590(self):
        input = """
dynamic x
func f(number x)
    return x + 1

func main()
begin
    x <- f(20, 30, 40) + 1
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(20.0), NumLit(30.0), NumLit(40.0)])"
        self.assertTrue(TestChecker.test(input, expect, 590))
                          
    ## REDECLARED PARAMETERS
    def test526(self):
        input = """
func add(number x, number x)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(add(x, y))
end

func add(number a, number b)
begin
    return a + b
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 526))

    ## INFER AND ASSIGN-STMT
    def test533(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[2, 2] <- [a, [b, 2]]
    a <- 2
    b <- 3
    c <- true
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 533))
    
    def test534(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[3, 2] <- [a, b, [c, 0]]
    a <- [1]
    b <- [3, 4]
    c <- 0
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 534))

    def test535(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [readNumber(), a, b, c]
    a <- 3
    b <- x[0]
    c <- a + b
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 535))
    
    def test591(self):
        input = """
func main()
begin
    number a[1, 2, 3, 4]
    var b <- a[0]
    number c[2, 3, 4]
    b <- c
    number d[1, 3, 4]
    b <- d
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 591))
        
    def test_ifs_redecl_param(self): ## Check again, output should be error on assignstmt
        input = """
        func foo(number a, number b)
        begin
            return a + b
        end
        string a <- "Hello"
        func main() begin
            a <- foo(1.1, 2)
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(foo), [NumLit(1.1), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 4013))
        
                
    ## BINARY-OP
    def test537(self):
        input = """
func main()
begin
    dynamic x
    if (x) writeString("x is infer to true value")
    else writeString("x is infer to false value")
    x <- 1 + true
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 537))

    def test538(self):
        input = """
func main()
begin
    dynamic x
    if (x) writeString("x is infer to true value")
    else writeString("x is infer to false value")
    x <- not (true and not false) and not (false and not true)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 538))
        
    
    def test540(self):
        input = """
func f()
begin
    dynamic x
    x <- (x - 2) * (x + true)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 540))


    def test541(self):
        input = """
number a <- 1 + "Hello"
func main()
    return
"""
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 541))
    

    def test568(self):
        input = """
dynamic a
func main()
begin
    var i <- a ... 2.75
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
        self.assertTrue(TestChecker.test(input, expect, 568))
    
    def test569(self):
        input = """
dynamic a
func main()
begin
    var i <- a[2] ... 2.75
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75)))"
        self.assertTrue(TestChecker.test(input, expect, 569))    

    def test592(self):
        input = """
func f(number x, number y)
begin
    if (y == 0) return x
    return f(y, x % y)
end

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    dynamic res <- f(x, y)
    writeString(res)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(y), NumLit(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 592))

    
    def test596(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- (a ... b) ... c
    writeString(x)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 596))

    ## CALL-STMT
    def test547(self):
        input = """
func f(number x)
begin
    return 1
end

func main()
begin
    f(2018)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2018.0)])"
        self.assertTrue(TestChecker.test(input, expect, 547))
    

    ## UNDECLARED/REDECLARED VARIABLES
    def test563(self):
        input = """
number x <- 10
func f(number x)
begin
    number x <- x + 20
    writeNumber(x)
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 563))


    ## IF-STMT
    def test570(self):
        input = """
func main()
begin
    if (1) writeBool(true)
    else writeBool(false)
end
"""
        expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 570))

    def test572(self):
        input = """
number a
bool b
string c
dynamic d
func main()
begin
    if (b) d <- 1 + a
    else d <- a - 1.75
    c <- "Hello, world!"
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 572))
    

    ## FOR-STMT
    def test593(self):
        input = """
func f(number x, number y)
begin
    if (y = 0) return x
    return f(y, x % y)
end

func main()
begin
    number x[10]
    number y[10]
    var i <- 0
    for i until i >= 10 by 1
        x[i] <- readNumber()
    
    for i until i >= 10 by "Hello"
        y[i] <- readNumber()
    
end
"""
        expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), StringLit(Hello), AssignStmt(ArrayCell(Id(y), [Id(i)]), CallExpr(Id(readNumber), [])))"
        self.assertTrue(TestChecker.test(input, expect, 593))

#################### ERROR TCs ##########################

    
    def test594(self):
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
        self.assertTrue(TestChecker.test(input, expect, 594))
        
    def test595(self):
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
        self.assertTrue(TestChecker.test(input, expect, 595))


###################### TC array #####################

    def test_001(self):
        input = """var a <- [[1,2],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 1))
    
    def test_002(self):
        input = """
        string b
        var a <- [[1,2,4],[1,2,3],[b,b,b]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 2))
        
    def test_003(self):
        input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 3))
    def test_004(self):
        input = """
        dynamic t
        var a <- [[1,2],[1,t],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 4))
    def test_005(self):
        input = """
        dynamic ans
        dynamic temp <- "abc"
        var a <- [[1,2],[1,ans],[temp,ans]]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 5))
    def test_006(self):
        input = """
        dynamic ans
        number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 6))
    def test_007(self):
        input = """number a[2,3] <- [[2,3],[2,3]]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
        self.assertTrue(TestChecker.test(input, expect, 7))
    def test_008(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2,3] <- [[b,t,d],[c,e,f]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 8))
    def test_009(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 9))
    
    def test_010(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 10))
    
    

        
        
    def test585(self):
        input = """
dynamic a
func main()
begin
    dynamic b
    dynamic c
    dynamic d
    var e <- 1
    var x <- [a, [[b]], [ [ [d, e] ] ] ]
    ## c <- [-10, 2 / 3 % 0.75]
    ## b <- [c]
    ## a <- [b]
    ## var arr <- [[1,2,3], [1,2,3], [7,8,9]]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 585))

    def test1000(self):
        input = """
func foo() begin
    dynamic a
    dynamic b
    dynamic c
    for a until b by c return
    a <- 1
    b <- true
    c <- 1
end
func main() return
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1000))
        
    def test1001(self):
        input = """
        func main()
        func main() begin
            number main
        end
"""

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1001))
        
        
############################ VO TIEN ####################
    def test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_2_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_3_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
        
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_3_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 428))
        

        
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))


    def test_4_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_5_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    
    def test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

            
        
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
        
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
        
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   
        
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
        
        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  


    def test_6_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        


        
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
    


    def test_7_full(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test471(self):    
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))   
        
        
    def test459(self):    
        input = """
        func foo() begin
            number a
            return 1
            return a
            return "!"
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
        
##################### TESTCASE ###############
    def test0(self): # no entry point
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test1(self): # no entry point
        input = """
            func main()
            return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test2(self): # no entry point
        input = """
            func main(string a)
            return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test3(self): # no entry point
        input = """
            func main()
            func f(string ba, number g)
            return 0
            func main()
            begin
            return "abc"
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test4(self): # no entry point
        input = """
            func f(string ba, number g)
            begin
            number main
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test5(self): # no entry point
        input = """
            func main(string ba, number g)
            begin
            number a <- 1
            return 7
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test6(self): # no entry point
        input = """
            number a <- 1
            number b <- 2
            number c <- 3
            func calc()
            begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 106))

    def test7(self): # no entry point
        input = """
            func mainn() return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test8(self): # no entry point
        input = """
            string a
            bool b
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test9(self): # entry point
        input = """
            func main()
            func abc() return 1
            func main()
            begin
            number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test10(self): # entry point
        input = """
            func main()
            return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test11(self): # redeclared variable
        input = """
            func main()
            begin
            number a
            number a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test12(self): # redeclared function
        input = """
            func main()
            return
            func abc12() return 1
            func abc12() return "abc"
        """
        expect = "Redeclared Function: abc12"
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test13(self): # redeclared parameter
        input = """
            func main()
            return
            func abc(string aaa, bool aaa)
        """
        expect = "No Function Definition: abc"
        self.assertTrue(TestChecker.test(input, expect, 113))

    def test14(self): # redeclared variable (different scope)
        input = """
            bool ayu
            func main()
            begin
            string ayu
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test15(self): # redeclared variable (different scope)
        input = """
            bool a
            func main()
            begin
            string a
                begin
                number a
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test16(self): # redeclared function (definition for function)
        input = """
            func iiiii(number x)
            func main() return
            func iiiii(number y) return y
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 116))

    def test17(self): # redeclared function
        input = """
            func f17(number x)
            func main() return
            func f17(string y) return y
        """
        expect = "Redeclared Function: f17"
        self.assertTrue(TestChecker.test(input, expect, 117))

    def test18(self): # redeclared parameter
        input = """
            func main() return
            func f(string gh, string gh)
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 118))

    def test19(self): # redeclared function
        input = """
            func main() return
            func f(string gh) return 0
            func f(string gh)
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 119))

    def test20(self): # redeclared parameter
        input = """
            func main() return
            func f(string gh, string gh)
            func f(string gh, string a) return gh
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 120))

    def test21(self): # redeclared built-in function
        input = """
            func main() return
            func readNumber() return 123
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 121))

    def test22(self): # undeclared identifier
        input = """
            func main() return
            func f() return a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 122))

    def test23(self): # undeclared identifier
        input = """
            func main() return
            func f() return a
            number a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 123))

    def test24(self): # undeclared identifier
        input = """
            func main()
            begin
            number a
            end
            func f() return a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 124))

    def test25(self): # declared identifier
        input = """
            string a
            func main()
            begin
            number a
            end
            func f() return a
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 125))

    def test26(self): # declared identifier
        input = """
            func main() return
            func f(bool a) return a
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 126))

    def test27(self): # undeclared function
        input = """
            func main() return
            func f(bool a27)
            begin
            a27 <- foo27()
            end
        """
        expect = "Undeclared Function: foo27"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test28(self): # undeclared identifier
        input = """
            func main() return
            func f()
            begin
            a <- 123
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 128))

    def test29(self): # undeclared identifier
        input = """
            func main()
            begin
            number a <- 123 + b * 100 / 78
            end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 129))

    def test30(self): # undeclared identifier
        input = """
            func main()
            begin
            number a
            for b until b > 10 by 1
            a <- b
            end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 130))

    def test31(self): # undeclared identifier
        input = """
            func main()
            begin
            if (abc % 5 == 0) abc <- 5
            end
        """
        expect = "Undeclared Identifier: abc"
        self.assertTrue(TestChecker.test(input, expect, 131))

    def test32(self): # declared function (IO)
        input = """
            func main()
            begin
            number t1 <- readNumber()
            bool t2 <- readBool()
            string t3 <- readString()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 132))

    def test33(self): # declared function
        input = """
            func a33()
            func main()
            begin
            a33()
            end
            func a33() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 133))

    def test34(self): # undeclared function
        input = """
            func main()
            begin
            a34()
            end
            func a34()
            func a34() return
        """
        expect = "Undeclared Function: a34"
        self.assertTrue(TestChecker.test(input, expect, 134))

    def test35(self): # redeclared function
        input = """
            func abcc() return
            func main()
            begin
            abcc()
            end
            func abcc()
            func abcc() return
        """
        expect = "Redeclared Function: abcc"
        self.assertTrue(TestChecker.test(input, expect, 135))

    def test36(self): # undeclared identifier
        input = """
            func main()
            begin
            a <- 1
            number a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 136))

    def test37(self): # type mismatch in expression
        input = """
            func main()
            begin
            number a
            number b <- a[0]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 137))

    def test38(self): # type mismatch in expression
        input = """
            func main()
            begin
            number a[2]
            number b <- a["hi"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(hi)])"
        self.assertTrue(TestChecker.test(input, expect, 138))

    def test39(self): # type mismatch in expression
        input = """
            func main()
            begin
            string a[2]
            string b <- a[1, 2, 3, "hi"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(hi)])"
        self.assertTrue(TestChecker.test(input, expect, 139))

    def test40(self): # undeclared function
        input = """
            func main()
            begin
            abc()
            end
            func abc() return
        """
        expect = "Undeclared Function: abc"
        self.assertTrue(TestChecker.test(input, expect, 140))

    def test41(self): # type mismatch in expression
        input = """
            func main()
            begin
            bool a[2]
            bool b <- a[true, false]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [BooleanLit(True), BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input, expect, 141))

    def test42(self): # type mismatch in expression
        input = """
            func main()
            begin
            number b <- 1 + "hi"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(hi))"
        self.assertTrue(TestChecker.test(input, expect, 142))

    def test43(self): # undeclared identifier (note)
        input = """
            func main()
            begin
            number b <- b + 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test44(self): # type mismatch in expression
        input = """
            func main()
            begin
            number b <- true + "hi"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, BooleanLit(True), StringLit(hi))"
        self.assertTrue(TestChecker.test(input, expect, 144))

    def test45(self): # type mismatch in expression
        input = """
            func main()
            begin
            string a
            number b <- (a + 1) = 5
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 145))

    def test46(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- "abc" ... "aa"
            dynamic b <- a == false
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 146))

    def test47(self): # type mismatch in expression
        input = """
            func calc47(number a, number b) return a = b
            func main()
            begin
            var a <- calc47(1, 4) * 2
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(*, CallExpr(Id(calc47), [NumLit(1.0), NumLit(4.0)]), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 147))

    def test48(self): # type mismatch in expression
        input = """
            func calc(number a, number b) return a + b
            func main()
            begin
            var a <- calc(1, 4) * 2
            a <- a and a
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(a), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test49(self): # type mismatch in expression
        input = """
            func calc49(number a49, number b49) return [a49, b49]
            func main()
            begin
            var arr49 <- calc49(1, 4)
            var b <- arr49[0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 149))

    def test50(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a50[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            number b <- a50[0]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, ArrayCell(Id(a50), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 150))

    def test51(self): # type mismatch in expression (note2)
        input = """
            func f() return
            func main()
            begin
            number a51 <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 151))

    def test52(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a[2, 2, 2] <- [[[1, 2], [3, 4]], [[4, 5], [6, 7]]]
            number b <- a[0, 1, 1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 152))

    def test53(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- -true
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 153))

    def test54(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- not true
            var b <- not 1
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 154))

    def test55(self): # undeclared identifier
        input = """
            func f() return 1
            func main()
            begin
            number a <- f
            end
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 155))

    def test56(self): # redeclared variable
        input = """
            func f()
            string f
            func main() return
            func f() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 156))

    def test57(self): # type mismatch in expression
        input = """
            func f() return "abcd"
            func main()
            begin
            number a <- f()[0]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), []), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 157))

    def test58(self): # type mismatch in expression
        input = """
            func f() return [1, 2]
            func main()
            begin
            number a <- f() + 1
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(f), []), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 158))

        input = """
            func f() return "ahu"
            func main()
            begin
            string a <- f() ... "aaa"
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 159))

        input = """
            func f60(number x)
            begin
            if (x % 2 = 0)
            return true
            else
            return false
            end
            func main()
            begin
            var a60 <- not f60(readNumber())
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 160))

    def test59(self): # type mismatch in expression
        input = """
            func f() return [1, 2]
            func main()
            begin
            number a <- f() + 1
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(f), []), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 161))

    def test60(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            number b[3] <- a[0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 162))

    def test61(self): # type mismatch in expression
        input = """
            func f61(string x61)
            begin
            if (x61 == "a") return x61 ... "a"
            elif (x61 == "b") return x61 ... "b"
            else return x61
            end
            func main()
            begin
            var a <- f61("a") == "ab"
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 163))

    def test62(self): # type cannot be inferred
        input = """
            func f62()
            begin
            dynamic a62
            return a62
            end
            func main()
            begin
            var a <- f62()
            end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a62))"
        self.assertTrue(TestChecker.test(input, expect, 164))

    def test63(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic x
            var a63 <- x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a63), None, var, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 165))

    def test64(self): # type mismatch in expression
        input = """
            func f(number a, number b) return a + b
            func main()
            begin
            dynamic x <- f(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 166))

    def test65(self): # type mismatch in statement
        input = """
            func f(number a, number b) return
            func main()
            begin
            f(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 167))

    def test66(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic x
            dynamic y <- x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 168))

    def test67(self): # type cannot be inferred
        input = """
            func f()
            func main()
            begin
            dynamic x <- f()
            end
            func f() return 1
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 169))

    def test68(self): # initialize implicit keywords with array expr
        input = """
            func main()
            begin
            var a <- [1,2,3,4]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 170))

    def test69(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            if (x) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((Id(x), AssignStmt(Id(x), NumLit(0.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 171))

    def test70(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            if (x > 0) x <- 0
            elif (x - 9) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((BinaryOp(>, Id(x), NumLit(0.0)), AssignStmt(Id(x), NumLit(0.0))), [(BinaryOp(-, Id(x), NumLit(9.0)), AssignStmt(Id(x), NumLit(0.0)))], None)"
        self.assertTrue(TestChecker.test(input, expect, 172))

    def test71(self): # type mismatch in statement
        input = """
            func f(number x)
            begin
            if (x > 5) return x % 2
            elif (x <= 5) return x - 1
            end
            func main()
            begin
            number x
            if (f(2)) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((CallExpr(Id(f), [NumLit(2.0)]), AssignStmt(Id(x), NumLit(0.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 173))

    def test72(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            for x until x by 1 x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(x), Id(x), NumLit(1.0), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 174))

        input = """
            func main()
            begin
            string x
            for x until x == "a" by 1 x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(x), BinaryOp(==, Id(x), StringLit(a)), NumLit(1.0), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 175))

        input = """
            func main()
            begin
            string x
            number y
            for y until x == "a" by x
            x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(y), BinaryOp(==, Id(x), StringLit(a)), Id(x), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 176))

    def test73(self): # type mismatch in expression (note2)
        input = """
            func f() return
            func main()
            begin
            number x <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 177))

    def test74(self): # type mismatch in statement
        input = """
            func f() return "abc"
            func main()
            begin
            number x <- f()
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 178))

    def test75(self): # type mismatch in statement
        input = """
            func main()
            begin
            number y
            number x[1, 2] <- y
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([1.0, 2.0], NumberType), None, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 179))

    def test76(self): # type mismatch in statement
        input = """
            func main()
            begin
            number y[2, 2]
            number x[1, 2] <- y
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([1.0, 2.0], NumberType), None, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 180))

    def test77(self): # type mismatch in statement
        input = """
            func main()
            begin
            dynamic a
            number x[2] <- [a, 1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 181))

    def test78(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x[2] <- [1]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 182))

    def test79(self): # type mismatch in statement (note)
        input = """
            func f() return 1
            func main()
            begin
            f()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 183))

    def test80(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            f(1, 2)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 184))

    def test81(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            f(true)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 185))

    def test82(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            dynamic x
            f(x)
            x <- x + 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 186))

    def test83(self): # type mismatch in expression (note2)
        input = """
            func f(number x) return x
            func main()
            begin
            number x <- f(1, 2) * 8
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 187))

        input = """
            func f(number x) return x
            func main()
            begin
            number x <- f("abc") + 1
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 188))

    def test84(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic c
            c <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 189))

    def test85(self): # type mismatch in expression
        input = """
            func main()
            begin
            number temp[3] <- [1, 2, true]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 190))

    def test86(self): # type mismatch in statement
        input = """
            func f(number a, string b, bool c)
            begin
            if (a > 5) return [a + 1, a % 2]
            elif (a % 5 = 0) return [a, a - 1]
            else return [a * 6, a / 6]
            end
            func main()
            begin
            number temp[3] <- f(1, "a", true)
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(temp), ArrayType([3.0], NumberType), None, CallExpr(Id(f), [NumLit(1.0), StringLit(a), BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 191))

    def test87(self): # type mismatch in statement
        input = """
            func f(number a)
            func main()
            begin
            number temp <- f(1)
            end
            func f(number a) return "abc"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 192))

    def test88(self): # type mismatch in statement
        input = """
            func f(number a)
            begin
            if (a > 5) return a
            elif (a < 5) return "a"
            end
            func main()
            begin
            number temp <- f(1)
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 193))

    def test89(self): # type mismatch in statement (note)
        input = """
            func f89(number a)
            func main()
            begin
            f89(1)
            end
            func f89(number a) return a
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 194))

    def test90(self): # type mismatch in expression (note2)
        input = """
            func f(number a) return a
            func f2(string a) return a
            func main()
            begin
            dynamic a
            a <- f(1)
            a <- f("a")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 195))

    def test91(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- 1 + 1 * 1 / 1 = "1"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, BinaryOp(+, NumLit(1.0), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(1.0)), NumLit(1.0))), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 196))

    def test92(self): # no definition for a function
        input = """
            func f()
            func main() return
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 197))

    def test93(self): # break/continue not in loop
        input = """
            func main()
            begin
            continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 198))

    def test94(self): # break/continue not in loop
        input = """
            func main()
            begin
            break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 199))

    def test95(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            if (a > 5) continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 200))

        input = """
            func main()
            begin
            number a
            if (a > 5)
                begin
                    begin
                    break
                    end
                end
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 201))

        input = """
            func main()
            begin
            number a
            for a until a > 10 by 5
            begin
                if (a > 5)
                    begin
                        begin
                        break
                        end
                    end
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 202))

    def test96(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            continue
            break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 203))

    def test97(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            if (a % 2 = 0) continue
            elif (a > 1) break
            else continue
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 204))

    def test98(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            if (a % 2 = 0)
                if (a > 2)
                    a <- a + 1
                elif (a > 3)
                    a <- a - 2
            elif (a % 3 = 1)
                continue
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 205))

    def test99(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            begin
                for a until a > 5 by 5
                begin
                continue
                end
                break
            end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 206))

    def test100(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            begin
                for a until a > 5 by 5
                begin
                    for a until a > 5 by 5
                    begin
                        for a until a > 5 by 5
                        begin
                        continue
                        end
                        begin
                            break
                        end
                    end
                break
                end
                break
            end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 207))

    def test101(self): # undeclared identifier
        input = """
            func f() return 1
            func main()
            begin
            number a <- f
            end
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 208))

    def test102(self): # undeclared function
        input = """
            func main()
            begin
            number f
            number a <- f()
            end
        """
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 209))

    def test103(self): # undeclared function
        input = """
            number a
            func main()
            begin
            string a
            a <- "abc"
            end
            func f() return a + 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 210))

    def test104(self): # redeclared
        input = """
            func f() return 1
            number f <- 1
            func main()
            begin
            number a <- f + f()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 211))

    def test105(self): # no definition for a function
        input = """
            func main()
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 212))

    def test106(self): # type cannot be inferred (note)
        input = """
            func main()
            begin
            var b <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 213))

        input = """
            func main()
            begin
            dynamic b <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 214))

    def test107(self): # type mismatch in statement
        input = """
            func main()
            begin
            dynamic x107
            x107 <- (x107 = 1) or ("abc" == "abc")
            ##bool a107 <- x107
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x107), BinaryOp(or, BinaryOp(=, Id(x107), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 215))
    
    def test108(self): # type mismatch in expression
        input = """
            func main()
            begin
            dynamic x
            var y <- (x = 1) or (x + 1)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(+, Id(x), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 216))



    def test113(self): # type mismatch in expression
        input = """
            func foo()
            begin
                dynamic x113
                for x113 until x113 > 5 by 1
                continue
                x113 <- x113 and x113
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(x113), Id(x113))"
        self.assertTrue(TestChecker.test(input, expect, 221))

    def test114(self): # type mismatch in statement + expression
        input = """
            func foo()
            begin
                dynamic x
                number a
                if (x) a <- 1
                x <- 1
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 222))

        input = """
            func foo()
            begin
                dynamic x
                number a
                if (x) a <- 1
                elif (x + 1 > 2) a <- 2
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 223))

    def test115(self): # type mismatch in statement
        input = """
            func foo()
            begin
                dynamic x
                dynamic a
                for a until x by a continue
                x <- a
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 224))

        input = """
            func main()
            begin
                dynamic x
                for x until true by 1
                begin
                x <- x + 1
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 225))

    def test116(self): # type mismatch in statement
        input = """
            dynamic a
            dynamic b
            dynamic c
            func main()
            begin
            var c <- a * b = 5
            for a until c by c break
            end
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(c), Id(c), Break)"
        self.assertTrue(TestChecker.test(input, expect, 226))

    def test117(self): #
        input = """
            dynamic a
            dynamic b117
            dynamic c
            func foo117()
            begin
                var c <- a = 5
                if (c)
                begin
                    begin
                        begin
                        b117 <- b117 + 1
                        end
                    end
                end
                return b117
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 227))

    def test118(self): # type mismatch in statement
        input = """
            func f()
            begin
                if (1 < 2)
                begin
                end
                elif (1 < 2)
                begin
                    return 1
                end
                elif (1 < 2)
                begin
                end
                else
                begin
                    return "abc"
                end
                return 2
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 228))

    def test119(self): # type mismatch in expression (note2)
        input = """
            dynamic a
            dynamic b
            dynamic c
            func f(number b)
            begin
                dynamic c
                c <- not c
                a <- c and (-b = 6)
                return c
            end
            func main()
            begin
            c <- f(a)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 229))

    def test120(self): # type cannot be inferred
        input = """
            dynamic a
            dynamic b
            dynamic c
            func f(number b)
            begin
                dynamic c
                c <- not c
                a <- c and (-b = 6)
                return c
            end
            func main()
            begin
            dynamic d <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 230))

    def test121(self): #
        input = """
            func main()
            begin
            var x <- readNumber()
            writeNumber(x)
            var y <- readBool()
            writeBool(y)
            y <- x = 4
            string z <- readString()
            writeString(z)
            z <- z ... "a"
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 231))


    def test123(self): # type cannot be inferred
        input = """
            func a()
            begin
            dynamic x
            return x
            return 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 233))

    def test124(self): #
        input = """
            dynamic z
            func a()
            begin
                dynamic x
                dynamic y
                return 1
                return x
                return y
                if (x > 5)
                begin
                    begin
                        return x + y
                    end
                end
                for x until x > y by 1
                begin
                    return z
                end
            end
            func main()
            begin
            z <- z + 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 234))

    def test125(self): # type mismatch in expression (note2)
        input = """
            func a()
            begin
            end
            func main()
            begin
            number a <- a()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 235))



    def test127(self): # type mismatch in statement (note)
        input = """
            func main()
            begin 
                dynamic a127
                dynamic b
                dynamic c127
                number x127[3,3] <- [a127,b,c127]
                a127 <- [1,2,3]
                b <- [4,5,6]
                c127 <- [7,8,9]
                writeNumber(a127[0] + b[0] + c127[0])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 237))

    def test128(self): #
        input = """
            func main()
            begin 
                number a[2,2,2] <- [[[1,2], [2,3]], [["abc",5], [6,7]]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(StringLit(abc), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 238))

    def test129(self): #
        input = """
            func main()
            begin 
                dynamic a
                a <- [1,2,3]
                dynamic b
                b <- [1,2]
                bool c <- a = b
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 239))

    def test130(self): # type mismatch in expression
        input = """
        func foo()
            begin
            end

        func main()
            begin
                dynamic x <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 240))

    def test131(self): # type mismatch in expression
        input = """
        func f(number a)
        begin
            number a
        end
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 241))

    def test132(self): # redeclared function (note)
        input = """
        func f(string a)
        func f(number a)
        begin
        end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 242))

    def test133(self): # redeclared parameter
        input = """
        func f(string a, string a)
        begin
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 243))

    def test134(self): # debug test
        input = """
        func f134(number a, string b)
        func f134(number a, string b)
        begin
        end
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 244))

    def test135(self): #
        """ Array Literals: RHS in Assign Statement """
        input = """
        func foo(number x[4])
        func main()
            begin
                dynamic x
                number arr135[2,3,4] 
                arr135 <- [foo(x),[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
            end
        func createArr(number n)
            begin
                return [[n + n % n, n - n, -n, n * n],[n + 12.5, n % n - n, n, n],[n + - n, - n - - n, n, n]]
            end
        func foo(number n[4])
            return createArr(n[0])
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 245))

    def test136(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a136[2,2,2,2]
            a136 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            ##a136 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [[[1,2], [3,4]], [[1,2], [3,4]]]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 246))

    def test137(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a[2,2,2,2]
            a <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            x <- [[5,6], [7,8]]
        end
        """
        expect = ""
        #self.assertTrue(TestChecker.test(input, expect, 247))

    def test138(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a138[2,2,2,2]
            a138 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0))), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)))), ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 248))

    def test139(self): # type mismatch in statement (note)
        input = """
        func f()
        begin
            dynamic x
            dynamic y
            number a[2,2,2,2]
            return a
            return [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            x <- [[5,6], [7,8]]
        end
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 249))

    def test140(self): # type mismatch in expression (note)
        input = """
        func f(number a[2,2,2,2])
        begin
            return 1
        end
        func main()
        begin
            dynamic x
            dynamic y
            number a <- f([[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]])
            x <- [[5,6], [7,8]]
            y <- x
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 250))

    def test141(self): # type mismatch in statement (note)
        input = """
        func f(number a[2,2,2,2])
        begin
        end
        func main()
        begin
            dynamic x
            dynamic y
            f([[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]])
            x <- [[5,6], [7,8]]
            y <- x
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 251))

    def test142(self):
        input = """number a[2] <- [1]
        func main() 
        begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 252))
        
        
##################### DIEM #################################
    def test_001(self):
        input = """var a <- [[1,2],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_002(self):
        input = """
        string b
        var a <- [[1,2,4],[1,2,3],[b,b,b]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_003(self):
        input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_004(self):
        input = """
        dynamic t
        var a <- [[1,2],[1,t],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_005(self):
        input = """
        dynamic ans
        dynamic temp <- "abc"
        var a <- [[1,2],[1,ans],[temp,ans]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(ans)), ArrayLit(Id(temp), Id(ans)))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_006(self):
        input = """
        dynamic ans
        number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_007(self):
        input = """number a[2,3] <- [[2,3],[2,3]]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_008(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2,3] <- [[b,t,d],[c,e,f]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_009(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_010(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test011(self):
        input = """
    dynamic a
    dynamic b
    dynamic c
    number arr[1, 2,2] <- [[a, b]]
    ## number c[2, 2] <- arr
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test012(self):
        input = """
dynamic a
    dynamic b
    dynamic c
    dynamic d
    var e <- 1
    var x <- [a, [b], [[c]], [[[d, e]]] ]
    ##c <- [-10, 2 / 3 % 0.75]
    ##b <- [c]
    ##a <- [b]
"""
        expect = "No Entry Point"
        
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test013(self):
        input = """
dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic e
    var x <- [a, [b], [[c]], [[[d, e]]] ]
    ##c <- [-10, 2 / 3 % 0.75]
    ##b <- [c]
    ##a <- [b]
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c))), ArrayLit(ArrayLit(ArrayLit(Id(d), Id(e))))))"
        self.assertTrue(TestChecker.test(input, expect, 413)) 
    def test014(self):
        input = """
        func b()
        dynamic b
        number a[2,3]<- [[b(),b,b],[b,b,b()]]
        func b()
        return true
        """
        result="Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,result,414))
    def test015(self):
        input ="""
        func main()
        begin
        number a <- [a,a,a,a,a]
        end
        """
        expect="Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(a), Id(a), Id(a), Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test016(self):
        input ="""
        func a()
        number a
        func main()
        begin
            number a[5] <- [a(),2,3,4,5]
        end
        func a()
            return
    """
        expect="Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test017(self):
        input="""
        dynamic a
        var c <-[a,[a],[[a,a,a]]]
        """
        expect="Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayLit(Id(a), ArrayLit(Id(a)), ArrayLit(ArrayLit(Id(a), Id(a), Id(a)))))"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test018(self):
        input="""
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        var g <-[a,[b],[[c,d,e]]]
        """
        expect="Type Cannot Be Inferred: VarDecl(Id(g), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c), Id(d), Id(e)))))"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test019(self):
        input="""
       
        
       
        number d
        var c <-[c,c,c,c,d]   ## visit bien truoc roi moi visit init value
        """
        expect="Type Mismatch In Statement: VarDecl(Id(c), None, var, ArrayLit(Id(c), Id(c), Id(c), Id(c), Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test020(self):
        input="""
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        string g[6,99,100,101] <-[a,b,c,d,e,f]
        """
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,420))
    # test func_para
    def test021(self):
        input="""
        func a1(number a,number b, number c)
        func main()
        begin
            number a <- 1
            a1(1,2,3)
        end
        func a(number a,number b, number c)
        begin
            a<-a1(a,b,c)
            return "lo ve du"
        end
        """
        expect="Type Mismatch In Expression: CallExpr(Id(a1), [Id(a), Id(b), Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test022(self):
        input="""
        func a(number a,number b, number b)
        func main()
        return 0
        """
        expect=""
        self.assertTrue(TestChecker.test(input,expect,422))
    def test023(self):
        input="""
        func test()
        func main()
        begin
            number a[2,3]<- test()
        end
        func test()
        begin
            begin
                begin
                    begin
                        return 1
                    end
                end
            end
        end
        """
        expect="Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test024(self):
        input="""
        func test(number a[2,3])

        func main()
        begin
            number a[2,3]<- test(test(a))
        end
        """
        expect="No Function Definition: test"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test025(self):
        input="""
        func test(number a, string b)
        func main()
            begin
            dynamic a
            dynamic b
                a <-test(test(a,b),test(a,b))
            end
        
        """
        expect="Type Mismatch In Expression: CallExpr(Id(test), [CallExpr(Id(test), [Id(a), Id(b)]), CallExpr(Id(test), [Id(a), Id(b)])])"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test026(self):
        input="""
        func hehe()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            a[hehe()]<-[hehe(),hehe(),hehe(),hehe()]
        end
        """
        expect="Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [CallExpr(Id(hehe), [])]), ArrayLit(CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), [])))"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test027(self):
        input="""
        func hehe()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe()
        begin
            begin
            end
        end
        """
        expect="Type Mismatch In Statement: Block([Block([])])"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test028(self):
        input="""
        func hehe(number a, number b)
        func main()
        begin
            number a[2,3]
            a[hehe(1,2),hehe(1,2)]<-hehe(1,2)
            a[hehe(1,2)]<-[hehe(1,2),hehe(1,2),hehe(1,2)]
            
        end
        func hehe1(number a, number b)
        func hehe(number hehe1,number hehe)
        begin
            hehe<-hehe1(hehe,hehe)
            hehe1<-hehe1(hehe1,hehe1(hehe1,hehe1))+hehe(hehe1,hehe1(hehe1,hehe))
        
        end
        """
        expect="Type Mismatch In Statement: Block([AssignStmt(Id(hehe), CallExpr(Id(hehe1), [Id(hehe), Id(hehe)])), AssignStmt(Id(hehe1), BinaryOp(+, CallExpr(Id(hehe1), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe1)])]), CallExpr(Id(hehe), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe)])])))])"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test029(self):
        input="""
        func hehe()
        func hehe1()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe()
        begin
            return 1
        end
        """
        expect="No Function Definition: hehe1"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test030(self):
        input="""
        func hehe()
        func hehe1()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe(number hehe1, string hehe, number hehe2)
        begin
            hehe<- hehe...hehe
            return hehe1
        end
        """
        expect="Redeclared Function: hehe"
        self.assertTrue(TestChecker.test(input,expect,430))
    # test func_decl:10
    def test031(self):
        input="""
        func hehe()
        func hehe1(number a, number b)
        func main()
        return 0
        func hehe1(number c, number d)
        begin
        end
        
        """
        expect="No Function Definition: hehe"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test032(self):
        input="""
       
        func hehe1(number a, number b)
        begin
            number c[2,3]
            begin 
                number a <- 1
            end
            number a <- a
        end
        func main()
            return 0
        
        """
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test033(self):
        input="""
        func hehe1(number a, number b, number c[1,2,3])
        begin
            dynamic t
            dynamic hehe1 <- [c,t]
            return hehe1
        end
        
        func main()
        begin
            dynamic a
            hehe1(1,1,a)
        end
        
        """
        expect="Type Mismatch In Statement: CallStmt(Id(hehe1), [NumLit(1.0), NumLit(1.0), Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test034(self):
        input="""
        func hehe()
        func hehe(number a)
        func main()
        return 0
        """
        expect="Redeclared Function: hehe"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test035(self):
        input="""
        func hehe(number a)
        func hehe1(number a)
        return true
        
        func main()
        return 3
        func hehe(number t)
        return t
        func hehe1(number t)
        return t
        """
        expect="Redeclared Function: hehe1"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test036(self):
        input="""
        func test1()
        func test2()
        func test3()
        func test(number test1, string test2, bool test3)
        begin
            return (test1 > test1()) and (test2 == test2()) or (test3 and test3())
        end
        func main()
        begin
            return test(1,"abc",true)
        end

        """
        expect="No Function Definition: test1"
        self.assertTrue(TestChecker.test(input,expect,436)) 
    def test037(self):
        input="""
        func test()
        return true
        func main()
        begin
            string t[2,3]
            dynamic a <- t[test(),test()]
        end
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(t), [CallExpr(Id(test), []), CallExpr(Id(test), [])])"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test038(self):
        input="""
        func happy()
        return 2
        func happy()
        return 1
        func main()
        return 0
        """
        expect="Redeclared Function: happy"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test039(self):
        input="""
        func happy(string a, string b)
        begin
            a <- "Vi ngay em dep nhat"
            b <- "La ngay anh mat em"
            return a ... b
        end
        func main()
        begin
            dynamic a <- "Hen em kiep sau"
            dynamic b <- "Kiep nay thoi tim den nhau"
            happy()
        end
        return 0
        """
        expect="Type Mismatch In Statement: CallStmt(Id(happy), [])"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test040(self):
        input="""
        func happy()
        number a <- happy()
        func happy()
        return 1
        

        func main()
        begin
            string a <- "Tu nay duyen kiep bo lai phia sau, troi nhu muon khoc ngay minh mat nhau"
            a <- happy()
            
        end
        """
        expect="Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(happy), []))"
        self.assertTrue(TestChecker.test(input,expect,440))