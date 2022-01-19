a= input("MM/DD/YYYY 형식으로 날짜를 입력하시오.")

b = a.split("/")
b1 = b[2]+b[0]+b[1]
c= "".join(b1)

print(c)