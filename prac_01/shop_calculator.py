
numberofitems = int(input("Number of items:"))
while(numberofitems <= 0):
    print("Invalid number of items!")
    numberofitems = int(input("Number of items:"))

totalprice=0
for i in range(0, numberofitems):
    price = float(input("Price of item:"))
    totalprice = totalprice + price

if(totalprice>100):
    discount = totalprice * 0.1
    totalprice = totalprice - discount
    print("Total price for", numberofitems, "items is {:.2f}".format(totalprice))
else:
    print("Total price for", numberofitems, "items is {:.2f}".format(totalprice))