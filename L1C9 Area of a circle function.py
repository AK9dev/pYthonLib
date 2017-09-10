

def circle_input(radius):
    area = 3.14*radius*radius
    return area

    
r = int(input("Please enter the radius of the circle: "))
a = circle_input(r)
print("the area is ",a)
