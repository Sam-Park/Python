nums = [1, 2, 3, 4, 5]
# append used for single non iterable object, extend only used for iterable objects

nums.append('a')
nums.extend([6, 7])
nums.extend('Hello')
# insert exactly what it sounds like (pos, value)
nums.insert(3, 200)
nums.insert(len(nums), 201) #adds items to end of list
numbers = nums
numbers.append(-1) 
nums_copy = nums.copy()
print(id(nums), id(nums_copy))
print(nums)

letters = list('abcd')
# letters.clear() will clear the list
# letters.pop() will remove last element of list
value = letters.pop(0) #will remove element at index 0 and add it to value
letters1 = list('asdasadsasdas')
letters1.remove('a') #will remove only the first occurence of the letter a

while 'a' in letters1: #will remove ALL occurences of the letter a in the list
    letters1.remove('a')

letters1.index('s') #will return the index of item in list, will return only the first match

letters1.index('s', 4) #will look for the letter s in list after index 4, 4 is inclusive