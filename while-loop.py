x = 0
while x < 10:
    print(f'the current value of x is {x}')
    x = x + 1
else:
    print(f"this is the else statement, x is not less than 10, x is {x}")


y = 12
while y < 100:
    y += 1
    if y % 13 != 0: continue
    print(y)