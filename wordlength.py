def len_word(words):
    count=0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
          count += 1
    return count


print(len_word(['abc', 'xyz', 'aba', '1221']))


def sort_tuple(number):
    number.sort(key=lambda x:x[-1])
    return number


print(sort_tuple( ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])))


def duplicates(list1):
    list2 = []
    for n in list1:
        if n not in list2:
            list2.append(n)
    return list2


print(duplicates([1,1,3,3,2,2,4,4]))


def empty_list(lists):
    if not lists:
        return 1
    else:
        return 0

lists=[]
if empty_list(lists):
    print("the list is empty")
else:
    print("the list is not empty")


def list_copy(words):
    new_list = words.copy()
    return new_list


print(list_copy(['cow', 'dog', 1, 2]))

my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]

print(all(not d for d in my_list))
print(all(not d for d in my_list1))