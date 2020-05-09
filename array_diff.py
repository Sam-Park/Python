#! python3
a = [1, 2]
b = [2]
a_sum = 0
b_sum = 0

def array_diff(a, b):
    for i in b:
      if i in a:
        for j in range(a.count(i)):
          a.remove(i)
    print(a)

array_diff(a, b)