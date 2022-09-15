'''Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
'''

def next_bigger(n):
    ll = list(str(n))
    max_n = int("".join(sorted(ll, reverse=True)))
    min_n = sorted(ll)
    x = n
    while x <= max_n:
        x += 1
        if sorted(list(str(x))) == min_n:
            return x

    return -1

print(next_bigger(2017))
