def high_and_low(numbers):
    # ...
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers))+" "+str(min(numbers))


high_and_low(("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

aaa