'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.'''


def move_zeros(lst):
    ll = []
    to_remove = 0
    try:
        while True:
            lst.remove(to_remove)
            ll.append(to_remove)
    except ValueError:
        pass

    return lst + ll


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # returns [1, 1, 2, 1, 3, 0, 0]
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
