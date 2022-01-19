o = int(input("몇 번째 항까지 구할까요? "))

def fib(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range (1,o+2):
    print(fib(i), end="  ")