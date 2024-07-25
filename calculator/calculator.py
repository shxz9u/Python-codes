num1 = int(input("첫번째 숫자를 입력하세요."))
calc = input("연산자를 입력하세요('+', '-', '*', '/')")
num2 = int(input("두번째 숫자를 입력하세요."))

if(calc == "+"):
    print("결과값 :", num1+num2)
if(calc == "-"):
    print("결과값 :", num1-num2)
if(calc == "*"):
    print("결과값 :", num1*num2)
if(calc == "/"):
    print("결과값 :", num1/num2)