y = 1000
while y > 1:
    x = y // 2 + 1
    while x > 1:
        if y % x == 0: break # if modulo returns 0 print factor and break

        x -= 1
    else:
        print(y, 'is prime')
    y -= 1