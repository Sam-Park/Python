
def duplicate_encode(word):
    count ={}
    new_str = ""
    for char in word.lower():
        count.setdefault(char, 0)
        count[char] += 1
    for v in count.values():
        if v == 1 :
           new_str += "("
        elif v > 1:
            new_str += ")" 
        else:
            return 
    print(new_str)   

duplicate_encode('din')
duplicate_encode('Success')