number = int(input("please enter the ending number"))

print("All the even Numbers <=",number ,"are:")
for i in range(1,number+1):
    if(i%2==0):
        print(i, 'is even number')

print("All the odd number <=",number ,"are:")
for i in range(1,number+1):
    if(i%2==1):
        print(i,"is an odd number")
