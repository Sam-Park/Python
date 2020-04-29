"""for i in range(4):
    print(i)
"""

supplies = ['pens', 'staplers', 'chairs', 'cups', 'binders', 'party favors']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# multiple assignment

cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
# will assign each new variable the string stored in the first three indexes.
a = "AAA"
b = "BBB"
a, b = b, a
# way to swap information stored using multiple assignment

# augmented assignment operators
spam = 42
spam = spam + 1
spam += 1
# spam += 1 is equal to spam = spam + 1, works for all operators

print("a: ", a, "b: ", b)
print(size)