'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''


def pig_it(text):
    new_txt = ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in text.split(' ')])

    return new_txt


print(pig_it('O tempora o mores !'))
print(pig_it('Pig latin is cool'))
