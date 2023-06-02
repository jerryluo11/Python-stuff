import random

class Dice:
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x, y)

dice1 = Dice()

result = dice1.roll()
print(result)