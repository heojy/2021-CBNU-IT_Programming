import random

while True :
    print(" ")
    print("======dice_game() 호출======")
    a = random.randint(1,6)
    print(f"인간   : 주사위값 ={a}")
    b = random.randint(1,6)
    print(f"컴퓨터 : 주사위값 ={b}")
    if a>b:
        print("인간의 승리!")
    elif a==b:
        print("무승부")
    else:
        print("컴퓨터의 승리!")
    print("======dice_game() 복귀======")
    print(" ")
    o = input("중단할까요? Y/N  ")
    if o == "Y" or o== "y":
        print("게임 중단.")
        break
    
        
            
            