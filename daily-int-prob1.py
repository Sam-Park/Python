list = [10, 15, 3, 7]
num = 17

def find_add(num):
    # for i in list:
    #     # print(i, list[i+1])
    #     for k in range(i+1, len(list)):
    #         print(k)
    #         if list[i] + list[k] == num:
    #             print("true")

    for i, add1 in enumerate(list):
        for k, add2 in enumerate(list, i+1):
            print(add1, add2)
            if add1 + add2 == num:
                print('true')
print(find_add(num))