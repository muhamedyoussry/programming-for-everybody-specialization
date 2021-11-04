hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hrs <= 40:
    grossPay = hrs*rate
elif hrs > 40:
    grossPay = (40*rate) +  1.5*(hrs-40)*rate
else:
    print("error in entering hours")

print(grossPay)
