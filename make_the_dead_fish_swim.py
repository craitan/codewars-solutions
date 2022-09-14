'''Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.'''

def parse(data):
    answer = 0
    ll = []
    for x in data:
        if x == 'i':
            answer += 1
        elif x == 'd':
            answer -= 1
        elif x == 's':
            answer *= answer
        elif x == 'o':
            ll.append(answer)

    return ll


print(parse('ooo'))
print(parse('ioioio'))
print(parse('"idoiido"'))