def area_rect(len, wid, name="James"):
    print("Hello",name,".I am working on it...")
    print("Length+",len, " Width=",wid)
    a=len*wid

    return a

length = int(input("Enter length of the rectangle: "))
width = int(input("Enter width of the rectangle: "))
if((length<1) or (width<1)):
    print("Invalid values, both length and width should be >+ 1")
else:
    area=area_rect(wid=width,len=length,name="akhil")
    print("Area of rectangle with length",length,"and width",width)
    print("is equal to",area)
    
