import turtle

x = int(input("How long do you want each side of the triangle"))

for i in range  (6):
    turtle.fd(x)
    turtle.lt(120)
    turtle.fd(x)
    turtle.lt(120)
    turtle.fd(x)
    
turtle.exitonclick()
