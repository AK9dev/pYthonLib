def is_prime(count):
    for x in range(2, count):
        if count % x == 0:
            print(count,"is not a Prime Number")
            break
        else:
            print(count,"This is a prime number")

limit = int(input("please enter a +ve integer? "))
is_prime(limit)

x = input("Would you like to enter another number? Y/N: ")
if x == "Y":
     is_prime(limit)

else:
    print("Wow, Ok Then")
