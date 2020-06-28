def alpha(a):
    if len(a)<= 2 or a[-3:] =='ing':
        a += 'ly'

    else:
        a += 'ing'

    return a


print(alpha('abc'))
print(alpha('string'))




