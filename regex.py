import re
#seperate into groups using parens
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 859-223-2211')
print(mo.group(1)) #accessing groups 
print(mo.group(2)) #accessing groups 

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
mo1 = batRegex.search('The adventures of Batwoman')
print(mo.group())
print(mo1.group())

