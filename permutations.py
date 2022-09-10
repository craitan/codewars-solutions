from itertools import permutations

'''In this kata you have to create all permutations of a non empty input string and remove duplicates,
if present. This means, you have to shuffle all letters from the input in all possible orders.'''


def permutations(s):
    if len(s) == 1:
        return [s]

    recursive_perms = []
    for c in s:
        for perm in permutations(s.replace(c, '', 1)):
            recursive_perms.append(c + perm)

    return list(dict.fromkeys(recursive_perms))

print(permutations('aabb'))
print(permutations('a'))
