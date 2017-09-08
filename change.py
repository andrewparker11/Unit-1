#Andrew Parker
#9/8/17
#change.py - Tells how many coins you need to make up a given change

cents = int(input('How many cents? '))
quarters = (cents//25)
dimes = ((cents-(quarters*25))//10)

print('You have', quarters, 'quarters and', dimes, 'dimes')
