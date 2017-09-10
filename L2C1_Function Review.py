print("Welcome to Simple Interest Caluclator")
print("______________________________________")
print()





pa = int(input("What is the principal amount?:  "))
inr = int(input("what is the interest rate?: "))
tm = int(input("What is the time in years for the interest"))



def sic(pa,inr,tm,):
    rt = inr/100;
    return  pa*tm*rt + pa;
   
    return tm






   


tot = sic(pa, inr, tm)

print(" This is your interest after {0} years is ${1:0.2f}:".format(tm, tot))
