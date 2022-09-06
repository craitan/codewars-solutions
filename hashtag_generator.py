def generate_hashtag(s):

    new_hashtag = "#" + ''.join([word.capitalize() for word in s.split(' ')])

    return False if (s == "" or len(new_hashtag) > 140) else new_hashtag


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
