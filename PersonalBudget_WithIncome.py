item_1=input("Enter Item 1: ")
item_2=input("Enter Item 2: ")
item_3=input("Enter Item 3: ")
item_4=input("Enter Item 4: ")
item_5=input("Enter Item 5: ")
item_6=input("Enter Item 6: ")
item_7=input("Enter Item 7: ")
monthly_1=float(input("Enter Item 1 Monthly Amount: "))
monthly_2=float(input("Enter Item 2 Monthly Amount: "))
monthly_3=float(input("Enter Item 3 Monthly Amount: "))
monthly_4=float(input("Enter Item 4 Monthly Amount: "))
monthly_5=float(input("Enter Item 5 Monthly Amount: "))
monthly_6=float(input("Enter Item 6 Monthly Amount: "))
monthly_7=float(input("Enter Item 7 Monthly Amount: "))
yearly_1= float(monthly_1)*12
yearly_2=float(monthly_2)*12
yearly_3=float(monthly_3)*12
yearly_4=float(monthly_4)*12
yearly_5=float(monthly_5)*12
yearly_6=float(monthly_5)*12
yearly_7=float(monthly_6)*12
print ("Your Monthly Budget")
print ("Item # | Monthly Spending | Yearly Spending")
print ("1 " + "%-10s $%-10.2f $%-10.2f" % (item_1, monthly_1, yearly_1))
print ("2 " + "%-10s $%-10.2f $%-10.2f" % (item_2, monthly_2, yearly_2))
print ("3 " + "%-10s $%-10.2f $%-10.2f" % (item_3, monthly_3, yearly_3))
print ("4 " + "%-10s $%-10.2f $%-10.2f" % (item_4, monthly_4, yearly_4))
print ("5 " + "%-10s $%-10.2f $%-10.2f" % (item_5, monthly_5, yearly_5))
print ("6 " + "%-10s $%-10.2f $%-10.2f" % (item_6, monthly_6, yearly_6))
print ("7 " + "%-10s $%-10.2f $%-10.2f" % (item_7, monthly_7, yearly_7))
