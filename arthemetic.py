#shapping bill calculator
price1=float(input("enter product 1 price:"))
price2=float(input("enter product 2 price"))
price3=float(input("enter product 3 price:"))
total=price1+price2+price3
discount=total*0.30
final_amount=total-discount
print("final_amount:",final_amount)
print("discount:",discount)
print("total_bill:",total)
print("total-discount:",total-discount)


#salary calculator
basic=float(input("enter basic salary"))

hra=basic*0.20
da=basic*0.10

gross_salery=basic+hra+da
print("basic salery:",basic)
print("hra:",hra)
print("da:",da)
print("gross sdalary:",gross_salery)