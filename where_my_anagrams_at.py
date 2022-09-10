'''What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false'''


def anagrams(word, words):
    return [new_word for new_word in words if sorted(word) == sorted(new_word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
