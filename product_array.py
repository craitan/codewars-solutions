'''Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to
The Product of all the elements of Arr[] except Arr[i].'''

import numpy


def product_array(numbers):
    result = []
    for _ in range(len(numbers)):
        first_element = numbers.pop(0)
        multiplied_list = numpy.prod(numbers)
        numbers.append(first_element)
        result.append(multiplied_list)

    return result


print(product_array([12, 20]))
print(product_array([3, 27, 4, 2]))
