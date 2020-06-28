def sum_item(items):
    return sum(items)


print(sum_item([1, 2, 3]))


def multi_item(item):
    mult =1
    for x in item:
        mult *= x
    return mult


print(multi_item([1,2,3]))


def larger_item(item):
    return max(item)


print(larger_item([5, 4, 6,9,7]))


def small_item(item):
    return min(item)


print(small_item([5, 4, 6,8]))
