n = int(input("Enter the ending point for the amount"
              "of numbers in the generator"
              "(enter number > 1) : "))

if(n == 0):
    print("Invalid Number dude")
else:
     print("The following are divisible by 3:")
     for i in range (1, n+1):
            if (i % 3 == 0):
                 print (i)
                
                 

        
