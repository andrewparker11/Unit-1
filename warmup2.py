#Andrew Parker
#8/31/17
#luckynumero - Finds your lucky numero

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

answer = int(input(str(num1)+ '+' + str(num2)+'? '))
print(answer == num1 + num2)