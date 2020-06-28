def remove_n(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_n('Python', 0))
print(remove_n('Python', 3))
print(remove_n('Python', 5))