import re

"""
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no Area Code
    if text[3] != '-':
        return False # Missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
"""
message = 'call me at 860-455-0269 tomorrow or at 415-555-5555 after that'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)

# print(isPhoneNumber('860-455-0269'))