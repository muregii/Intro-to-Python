import random

dice_rolls = 100000
num_dices = 3
value = 10

random.seed(2024)
count = 0
for i in range(dice_rolls):
    dice = random.choices(population=range(1,7), k=num_dices)
    
    if(sum(dice) == value):
        count+=1
print(count/dice_rolls)
    
        
