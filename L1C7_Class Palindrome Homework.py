number = int(input("enter the number to check for palindrome : "))

temp_number=number
reversed_number = 0
temp = 0
while(temp_number > 0):
    temp = temp_number % 10
    temp_number = int(temp_number/10)
    reversed_number = (reversed_number *10) + temp

if( number == reversed_number):
    print("{} is a Palindrome number".format(number))
else:
    print("{} is not a Palindrome number".format(number))
