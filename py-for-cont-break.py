for x in range(100):
    if x % 2 == 0:
        print('Found an even number: ', x)
        continue
    print('Found an odd number: ', x)


for letter in 'Python':
    if letter == "t": #T will not be printed
        continue
    print('Current letter: ', letter)


for x in range(10):
    #implement this block of code to display even numbers between 0 and 99
    pass #null instruction

for num in range(10):
    if num == 5:
        break
    print(num)

for lett in 'Python':
    print(lett)
    if lett == 'o':
        break

for x in range(1, 20):
    if x % 13 == 0:
        break
else:
    print('Theres is no # divisible by 13 in the range')