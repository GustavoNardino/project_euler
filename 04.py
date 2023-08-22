'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def compara(original):
    inverted = int(str(original)[::-1])
    if(original == inverted):
        return True



for a in range(100, 999):
    for b in range(100, 999):
        if(compara(a*b)):
            print(a, '*', b, ' = ', a*b)