a= int(input("첫 번째 정수를 입력하시오 :"))
b= int(input("두 번째 정수를 입력하시오 :"))

def plus(a,b):
    add = a+b
    return add

def minus(a,b):
    subtract = a-b
    return subtract

def multiply(a,b):
    multiplication = a*b
    return multiplication

def divide(a,b):
    division = a/b
    return division

add = plus(a,b)
print(a,"+",b,"=",add)

subtract = minus(a,b)
print(a,"-",b,"=",subtract)

multiplication = multiply(a,b)
print(a,"*",b,"=",multiplication)

division = divide(a,b)
print(a,"/",b,"=",division)
