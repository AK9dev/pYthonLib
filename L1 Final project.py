print("Welcome to the currency converter system")
print()
def to_dollar(Cur_from, amount):
    if Cur_from=="US":
        dollarValue=amount/1
    elif Cur_from=="EU":
        dollarValue=amount/0.91
    elif Cur_from=="BP":
        dollarValue=amount/0.70
    elif Cur_from=="AU":
        dollarValue=amount/1.36
    elif Cur_from=="CY":
        dollarValue=amount/6.53
    elif Cur_from=="JY":
        dollarValue=amount/113.60
    elif Cur_from=="CD":
        dollarValue=amount/1.34
    else:
        dollarValue=0

    return dollarValue

def to_target_curr(Cur_to, value):
    if Cur_to == "US":
        convValue = value * 1
    elif Cur_to == "EU":
        convValue = value * 0.91
    elif Cur_to== "BP":
        convValue = value * 0.70
    elif Cur_to== "AU":
        convValue = value * 1.36
    elif Cur_to== "CY":
        convValue = value * 6.53
    elif Cur_to== "JY":
        convValue = value * 113.60
    elif Cur_to== "CD":
        convValue = value * 1.34
    else:
        convValue=0

    return convValue







print("Following Currency codes are supported by this convertor:")
print("""US Dollar = US
Euro = EU
British Pound Sterling = BP
Australian Dollar = AU
Chinese Yuan = CY
Japanese Yen = JY
Canadian Dollar = CD
""")

Cur_from=input("Enter Currency to convert from?: ")
Cur_to=input("Enter currency to convert to?: ")
amount=int(input("Enter Amount to convert? "))


Cur_from=Cur_from.upper()
Cur_to=Cur_to.upper()
dollar_amount = to_dollar(Cur_from, amount)
finalValue = to_target_curr(Cur_to, dollar_amount)

if finalValue !=0:
    print("Converted Value of",amount,Cur_from,"to",
          Cur_to,"is","{:10.2f}".format(finalValue))
else:
    print("Invalid input!!!")
























    
    
