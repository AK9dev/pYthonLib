
x = int(input("please enter your current grade: "))
if x <= 59:
    print("Your Grade is an F")
elif x <= 69:
    print("Your grade is a D")
elif x <= 79:
    print("YOur Grade is a C")
elif x <= 89:
    print("YOur Grade is a B")
elif x <= 100:
    print("YOur Grade is a A")
elif x <= 120 and x >= 100:
    print("your grade is an A+")
else:
    print("your grades are strange, go back to school!!!!")
