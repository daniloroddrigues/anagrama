"""
Este problema foi utilizado em 345 Dojo(s).

Escreva um programa que gere todos os anagramas potenciais de uma string.

Por exmplo, os anagramas potenciais de "biro" são:

    1. biro bior brio broi boir bori
    2. ibro ibor irbo irob iobr iorb
    3. rbio rboi ribo riob roib robi
    4. obir obri oibr oirb orbi orib

Temos um fatorial 4! = 4 * 3 = 12 * 2 = 24 * 1 = 24

Traduzido de: http://www.cyber-dojo.com/
"""


def anagrama(s):
    if len(s) == 1:
        return list(s)
    else:
        i = 0
        li = list()
        while i < len(s):
            if i == 1:
                li.append(s[i] + s[0])
            else:
                li.append(s[i] + s[-1])
            i = i + 1

        return li


assert anagrama('b') == ['b']
assert anagrama('bi') == ['bi', 'ib']
assert anagrama('bir') == ['bir', 'bri', 'ibr', 'irb', 'rbi', 'rib']

"""
def anagram(string):
    # biro
    s1 = string

    # bior = b + i + o + r
    s2 = string[0] + string[1] + string[3] + string[2]

    # broi = b + r + o + i
    s4 = string[0] + string[2] + string[3] + string[1]

    # brio = b + r + i + o
    s3 = string[0] + string[3] + string[1] + string[2]

    # bori = b + o + r + i
    s5 = string[0] + string[3] + string[2] + string[1]

    n = 0
    list_ = []
    while n < len(string):
        print(string[:n] + string[(n + 1):])
        n = n + 1

    # b = 0
    # i = 1
    # r = 2
    # o = 3

    # print(s1)
    # print(s2)
    # print(s3)
    # print(s4)
    # print(s5)


anagram('biro')
"""

"""
def permuta(s, s1=''):

    if len(s) == 0:
        print(s1)
    else:
        for i in range(len(s)):
            permuta(s[:i] + s[(i + 1):], s1 + s[i])


permuta('bir')

assert permuta('biro') == 'biro'
assert permuta('bior') == 'bior'
assert permuta('brio') == 'brio'
assert permuta('broi') == 'broi'
assert permuta('boir') == 'boir'
assert permuta('bori') == 'bori'

assert permuta('ibro') == 'ibro'
assert permuta('ibor') == 'ibor'
assert permuta('irbo') == 'irbo'
assert permuta('irob') == 'irob'
assert permuta('iobr') == 'iobr'
assert permuta('iorb') == 'iorb'

assert permuta('rbio') == 'rbio'
assert permuta('rboi') == 'rboi'
assert permuta('ribo') == 'ribo'
assert permuta('riob') == 'riob'
assert permuta('roib') == 'roib'
assert permuta('robi') == 'robi'

assert permuta('obir') == 'obir'
assert permuta('obri') == 'obri'
assert permuta('oibr') == 'oibr'
assert permuta('oirb') == 'oirb'
assert permuta('orbi') == 'orbi'
assert permuta('orib') == 'orib'
"""
