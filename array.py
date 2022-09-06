'''Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.'''


def array_diff(a, b):
    result = [x for x in a if x not in b]
    return result


print(array_diff([1, 2, 2, 2, 3], [2]))
print(array_diff([1, 2], [1]))
