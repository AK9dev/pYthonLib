number = int(input("Please enter the ending number"
              "for the prime number series"
              "(enter number > 1) :"))

if (number <2):
    print("Invalid Number!!")
else:
    print ("FOllowing are the prime numbers: ")
    for i in range (2, number+1):
        for j in range (2,i):
            if (i % j == 0):
                break

        else:
            print (i)

    print ("that's it........")
        
