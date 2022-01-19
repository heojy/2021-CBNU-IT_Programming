def menu():
    print("1. 2부터 50까지 모든 홀수 출력.")
    print("2. 2부터 50까지 모든 짝수 출력.")
    print("3. 2부터 50까지 모든 소수(Prime Number) 출력.")
    print("4. 종료.")
    s= int(input("메뉴를 선택하세요 : "))
    return s

def main() :
    while True :
        index = menu()
        if index == 1:
            for i in range(2,50):
                if i%2 ==0:
                    continue
                print(i, end=" ")
            print(" ")    
            
        elif index == 2:
            for i in range(2,50):
                if i%2 ==1:
                    continue
                print(i, end=" ")
            print(" ")
                
            
                
        elif index == 3:
            number = 2
            while number <= 50:
                divisor = 2
                prime = True
        
                while divisor < number :
                    if number % divisor ==0:
                        prime = False
                        break
                    divisor= divisor +1
            
                if prime:
                    print(number, end=" ")
                    
            
                number = number +1
            print(" ")
        else:
            print("종료.")
            break
            
        
main()