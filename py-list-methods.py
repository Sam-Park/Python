# method is same thing as a function except it is attached or called on a certain value
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hi'))
#List methods
spam.append('sup')
spam.insert(1, 'hola')
print(spam)
# append adds value to end of list
# insert adds value to list at specific index
spam.remove('hola') #if theres multiple of the same variable .remove() will only remove first
del spam[0]
# .sort() sorts both numbers and strings || .sort(reverse=True) does what sounds like
# .sort() takes into account capitalization, uppercase -> lowercase, ASCII-betical order
# .sort(key=str.lower) will make it go in true alphabetical order