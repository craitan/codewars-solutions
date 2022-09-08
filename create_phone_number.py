'''Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!'''


def create_phone_number(number):
    local_code = ''.join(str(el) for el in number[0:3])
    first_part = ''.join(str(el) for el in number[3:6])
    second_part = ''.join(str(el) for el in number[6:])
    return f'({local_code}) {first_part}-{second_part}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
