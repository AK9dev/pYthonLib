def reverse_name(name):
    rev_name=""
    length = len(name)
    for i in range(1,length+1):
        rev_name=rev_name+name[length-i:length-i+1]


    return rev_name


user_name = input("Enter your name... ")
name_backwards=reverse_name(user_name)
print("Let me write your name backwards: ",name_backwards)

print()
print("Let me write your name backwards, again!!: ",user_name[::-1])


