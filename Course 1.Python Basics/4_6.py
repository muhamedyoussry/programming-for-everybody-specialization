def computepay(h, r):
    if h <= 40:
        grossPay = h*r
    elif h > 40:
        grossPay = (40*r) + 1.5*(h-40)*r
    else:
        print("error in entering hours")
    return grossPay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)
