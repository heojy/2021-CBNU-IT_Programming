import random
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,4)


if c == "1":
    cal = "+"
    answer = a+b
        
elif c == "2":
    cal = "-"
    answer = a-b
        
elif c == "3":
    cal = "*"
    answer = a*b
        
else:
    cal = "/"
    answer = a/b
    
dap = float(input(f"{a}{cal}{b} ="))

if dap == answer:
    print("맞았습니다.")
else:
    print("틀렸습니다.")