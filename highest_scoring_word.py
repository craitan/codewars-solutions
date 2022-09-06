'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.'''


def high(x):
    high_score = 0
    high_scored_word = ''

    for word in x.split(" "):
        word_score = sum(ord(ch) - 96 for ch in word)
        if word_score > high_score:
            high_score = word_score
            high_scored_word = word

    return high_scored_word


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('aa b'))
