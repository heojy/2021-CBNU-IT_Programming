print("날짜를 입력하시오(월과 일)")

def getIntRange(m,d):
    
    m = int(input("월을 입력하시오(1부터 12 사이의 값): "))
    while m<1 or m>12:
        m = int(input("월을 입력하시오(1부터 12 사이의 값을 입력하시오):"))
                
    d = int(input("일을 입력하시오(1부터 31 사이의 값): "))
    while d<1 or d>31:
        d = int(input("일을 입력하시오(1부터 31 사이의 값을 입력하시오):"))
    
    return m,d

month = 0
day = 0

month, day = getIntRange(month, day)
print(f"입력된 날짜는 {month}월 {day}일 입니다.")