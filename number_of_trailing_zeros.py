'''Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.'''


def zeros(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y


print(zeros(6))
print(zeros(12))
print(zeros(30))