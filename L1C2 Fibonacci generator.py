"""
Fibonaci Number Generator
"""



Value = int(input("please enter MaxxValue for Fibonacci sequence : "))

print ("the fibonacci sequence <+",Value, "is: ")

a, b = 0, 1
temp = 0
print ("0 ")
while (b <= Value): 
    print (b)
    temp = a+b
    a = b
    b = temp
