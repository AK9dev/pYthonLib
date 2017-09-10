string = input("Enter any string to check if it is a palindrome or not:")



if( string == string[::-1]): # The [::-1] is reading the string in a certain way

# the first colon is the start value, the second colon is the end value
# and the number -1 is the direction
#default start value is 0, end value is the length of string and direction is 1




    print("{} is a palindrome".format(string))
else:
    print("{} is not a Palindrome".format(string))
