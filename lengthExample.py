def remove_two(str):
    if len(str) < 2:
        return'empty string'

    return str[0:2] + str[-2:]


print(remove_two('python'))
print(remove_two('py'))
print(remove_two('w'))

