'''
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
'''
a = 4790 
b = 9721
#expected: 1+3=5+7 = 16
total = 0
for i in range(a,b+1):
    if i%2 == 0:
        pass
    else:
        total += i

print(total)