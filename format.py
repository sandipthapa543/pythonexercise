def formats(num):
    str1 = 'emp{0}'

    list = [str1.format(i) for i in num]
    return list


print(formats([1,2,3,4,5]))


def list_add(num1, num2):
    num1 = num1[:-1]+num2
    return num1


print(list_add([1,3,5,6,10],[2,4,7,8]))


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


def concat(dict1,dict2,dict3):
    dict4={}
    for d in [dict1,dict2,dict3]:
        return dict4.update(d)


print(concat({1:10, 2:20},{3:30, 4:40},{5:50,6:60}))