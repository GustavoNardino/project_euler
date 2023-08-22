'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

flag = 0
count = 0
for n in range(100000000, 1000000000):
    if(count != 20):
        for a in range(1, 21):
            # if(count > 19):
            #     print(count)
            #     print(n)
            if(n%a == 0):
                count = a
                flag = n
            else:
                count = 0
                break
    else:
        break

print('aqui ', flag)