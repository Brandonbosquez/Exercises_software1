#EXERCISE 05
#1
import random
from typing import List

#1
result = []
print("Roll the dices and I will sum up the results")
roll = int(input("How many times do you want me to roll the dice: "))
n = 0
sum = 0
while n < roll :
    n = n + 1
    luck = random.randint(1, 6)
    result.append(luck)

for rolls in result :
    sum += rolls
print("The results of your rolls were: ", result)
print(sum)
