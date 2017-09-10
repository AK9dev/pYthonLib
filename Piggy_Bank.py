n = int(input("How many nickels do you have: "))
q = int(input("How many quarters do you have: "))
pennies = int(input("How many pennies do you have: "))
d = int(input("How many dimes do you have: "))
fif = int(input("How many fifty cent coins do you have: "))
one = int(input("How many one dollar coins do you have: "))


counter = 0

nickel = n*5;

quarter = q*25;

dime = d*10;

fifty = fif*50;

oned = one*100;


total = nickel+quarter+dime+fifty+oned+pennies;
total = total/100


print("total money in your piggy bank is ${0:.2f}".format(total))
