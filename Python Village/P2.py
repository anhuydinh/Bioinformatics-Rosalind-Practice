from math import *
value = "864 841"
# a,b = pow(int(value.split(),2))
# c = squrt(a+b)
# print(c)
a,b = value.split()
# print(type(a))
print(a,b) #Test to see if splitting works
c = sqrt(pow(int(a),2)+pow(int(b),2))
print(pow(c,2))
