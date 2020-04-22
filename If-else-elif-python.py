"""
if some condition is true:
    #execute this code
elif some other condition is true:
    #excute this code
else:
    #execute this code

"""



"""
age = input('Enter your age:')
if age < 18:
    print('Your are a minor')
else:
    print('You are an adult')
"""

price = 100
balance = 190

if balance >= price:
    print(f'You can buy this product and your new balance will be ${balance - price}')
else:
    print(f'Insufficient Funds. Please desposit ${price - balance}')


answer = input('Do you want to continue? Enter yes or no:').lower()
if answer == 'yes':
    print("We'll move on then. ")
elif answer == 'no':
    print("We'll stop then.")
else:
    print("Invalid answer")