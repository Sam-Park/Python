nn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
    n1 = ''.join(str(e) for e in n[0:3])
    n2 = ''.join(str(e) for e in n[3:6])
    n3 = ''.join(str(e) for e in n[6:len(n)])
    newNum = f'"({n1}) {n2}-{n3}"'
    print(type(newNum))
    print(newNum)


create_phone_number(nn)