os = ['Windows', 'Mac', 'Linux', 'Android']

for i in os:
    print(f'The name of the item in the list is {i}')

str1 = "python is great!"

for char in str1:
    print(char, end='-')

numbers = [0, 5, 6, 11, 23, 120]

for i in range(100):
    if i % 2 == 0:
        print(f'even number {i}')
    else:
        print(f'odd number: {i}')