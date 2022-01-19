import random

class Dice:
    def __init__(self):
        pass

    def roll(self):
        d = random.randint(1,6)
        return d
    
class FraudDice(Dice):
    def roll(self):
            d = super().roll()
            while d <= 3:
                d = random.randint(1,6)
            return d
        
aa=Dice()
bb=FraudDice()
print("Dice 객체 5번 :")
for i in range(1,6):
    print(aa.roll())
print("\nFraudDice 객체 5번 ")
for i in range(1,6):
    print(bb.roll())