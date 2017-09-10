print ("this python program will calculate money in your piggybank")




options = ["dollar coins", "fifty cents","quarters","dimes","nickels","pennies"]


#

multi_factor = [1, 0.5, 0.25, 0.1, 0.05, 0.01]





#
total = 0





# the {0} in the line below is replaced by the actual value
for i in range(6):
    coin = int(input("Enter how many {0} you have? ".format(options[i])))
    total = total+ (coin * multi_factor[i])

#the {0} is replaced by the value given by the .format command, starting 
# with zero and going through each one of the coins in options




#
print("total money in your piggy bank is ${0}".format(total))
