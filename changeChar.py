def changes(str):
    str1 = str[5]
    str =str.replace(str1, '$')
    str= str1 + str[1:]

    return str


print(changes("restart"))
