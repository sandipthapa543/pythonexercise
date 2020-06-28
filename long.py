def long_word(str1):
    word =[]
    for n in str1:
        word.append((len(n), n))
    word.sort()
    return word[-1][1]


print(long_word(['hi','hello','bye']))