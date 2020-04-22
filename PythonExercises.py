# Printing Format literal strings
a = 1.33
b = 2

print(f'a is {a} and b is {b}, a times b is {a * b:.3f}')
print('a is {0}, b is {1} and a times b is {2:.4f}'.format(a, b, a * b))


# String Functions
language ='$Python$$'
message = 'I love Python!'
 
# YOUR CODE GOES HERE:
language1 = language.strip('$')   #remove all leading and trailing $ signs
language2 = language1.lower()     #lowercase version of language1 variable
message1 = message.upper()        #uppercase version of message variable
message2 = message.replace('Python', 'Java')  #replace Python with Java