def odd_remove(str1):
    str2=""
    for st in range(len(str1)):
        if st % 2 == 0:
            str2 += str1[st]
    return str2


print(odd_remove('legs'))



