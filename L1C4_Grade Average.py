print(" Hello, Today you will be telling me your Scores for all of your classes")

sci = int(input("Enter your science scores:"))

mat = int(input("Enter your Math scores:"))

lng = int(input("Enter your Language scores:"))

hst = int(input("Enter your History scores:"))

pe = int(input("Enter your PE scores:"))

mus = int(input("Enter your Music scores:"))

add = sci + mat + lng + hst + pe + mus

avg = (add / 6)

print("your average score is :", avg)




if avg <= 59:
    print("Your  average Grade is an F")
elif avg <= 69:
    print("Your average grade is a D")
elif avg <= 79:
    print("Your average average Grade is a C")
elif avg <= 89:
    print("Your average Grade is a B")
elif avg <= 100:
    print("Your average Grade is a A")
elif avg <= 120 and x >= 100:
    print("your average grade is an A+")
else:
    print("your grades are strange, go back to school!!!!")
