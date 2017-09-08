#Andrew Parker
#9/8/17
#change.py - Tells how many coins you need to make up a given change

cents = int(input('How many cents? '))
quarters = (cents//25)
dimes = ((cents-(quarters*25))//10)
nickels = ((cents-((quarters*25)+(dimes*10))//5)
pennies = (cents-((quarters*25)+(dimes*10)+(nickels*5)))

print('You have', quarters, 'quarters', dimes, 'dimes', nickels,'nickels, and', pennies, 'pennies')
