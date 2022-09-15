'''Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.'''


def in_array(array1, array2):
    answer = set()
    while array1:
        word_to_check = array1[0]
        array1.pop(0)

        for word in array2:
            if word_to_check in word:
                answer.add(word_to_check)

    return sorted(answer)


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
