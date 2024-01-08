from math import ceil, pow

numbers = [1, 2, 3, 4, 5, 6]
strings = ['apple', 'grape', 'orange']
'''
h(x) = x mod m
x: key
m: 소수(prime number)
'''


def modular(arr):
    table = [None] * 11
    for n in numbers:
        table[n % 11] = n
    return table


'''
h(x) = (((x * A) mod 1) * m)
m: 최대 버킷 개수
A: 황금비 => 0.6183
'''


def multiplex(arr):
    table = [None] * 11
    for n in numbers:
        k = (((n * 0.6183) % 1) * 11)
        table[ceil(k)] = n
    return table


'''
h(x) = (s[0] + s[1]*p + s[2]*p^2 + s[n-1]*]p^n-1) mod m
p: 31(메르센소수)
m: 해시테이블 최대 크기

'''


def stringHashing(arr):
    table = [None] * 11
    for string in arr:
        h = 0
        for i, s in enumerate(string):
            re_s = ord(s.upper()) - 64
            re_s *= int(pow(31, i))
            h += re_s % 20
        table[h % 11] = string
        h = 0
    return table


# print(modular(numbers))
# print(multiplex(numbers))
print(stringHashing(strings))
