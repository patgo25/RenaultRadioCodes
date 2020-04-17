import math

print("Welcome to the renault radio code generator")
precode=input("Enter the precode: ")
#The precode has the form of a capital letter and 3 numbers (Abcd)
A = precode[0]
A= A.upper()
b = precode[1]
c = precode[2]
d = precode[3]

i=ord(A)*5
j = ord(b) + i*2 -698
k = ord(d) + ord(c)*5*2 +j -528
m = ((k<<3)-k)%100

code = math.floor(m/10)+m%10*5*2+259%j%100*5*5*4

if(100<=code < 1000):
    print("0%i" %code)
elif(10<=code < 100):
    print("00%i" %code)
elif(code < 10):
    print("000%i" %code)
else:
    print(code)


