'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

import os

clear = lambda: os.system('clear')

lista = []
for n in reversed(range(600851475143)):
    clear()
    print(n)
    if(600851475143%n == 0):
        lista.append(n)
        print('aqui', n)
        break


#NÃO FUNCIONOU. O RESULTADO É 6857 MAS ARREGUEI PRO CHATGPT