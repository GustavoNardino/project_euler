'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

soma = 0
for m in range(0, 1000):
    if(m%3 == 0 or m%5 == 0):
        soma+=m

print(soma)