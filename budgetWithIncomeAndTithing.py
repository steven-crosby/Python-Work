#!/bin/python2
print "======================="
print "Building Your Monthly Budget"
print "======================="
exp_1 = input("Enter Expense 1: ")
exp_2 = input("Enter Expense 2: ")
exp_3 = input("Enter Expense 3: ")
exp_4 = input("Enter Expense 4: ")
exp_5 = input("Enter Expense 5: ")
monthly_1 = float(input("Enter Expense 1 Monthly Amount: "))
monthly_2 = float(input("Enter Expense 2 Monthly Amount: "))
monthly_3 = float(input("Enter Expense 3 Monthly Amount: "))
monthly_4 = float(input("Enter Expense 4 Monthly Amount: "))
monthly_5 = float(input("Enter Expense 5 Monthly Amount: "))
yearly_1 = float(monthly_1)*12
yearly_2 = float(monthly_2)*12
yearly_3 = float(monthly_3)*12
yearly_4 = float(monthly_4)*12
yearly_5 = float(monthly_5)*12
totalExpenses_month = float(monthly_1)+float(monthly_2)+float(monthly_3)+float(monthly_4)+float(monthly_5)
totalExpenses_annual = float(yearly_1)+float(yearly_2)+float(yearly_3)+float(yearly_4)+float(yearly_5)
moneyEarned = float(input("Enter how much money you earned last month: "))
fastOffering = float(input("Enter how much you would like to pay for fast-offerings each month:"))
totalSavings_month = float(moneyEarned)-float(totalExpenses_month)
totalSavings_annual = float(totalSavings_month)*12
monthTithing = moneyEarned * 0.10
annualTithing = monthTithing * 12
print " "
print "=======================" 
print "Ta-Da Your Budget"
print "======================="
print "Month Income"
print "$ %s" % (moneyEarned)
print "Annual Income"
print "$ %s" % (moneyEarned*12)
print "1. " + "%-10s $%-10.2f $%-10.2f" % (exp_1, monthly_1, yearly_1)
print "2. " + "%-10s $%-10.2f $%-10.2f" % (exp_2, monthly_2, yearly_2)
print "3. " + "%-10s $%-10.2f $%-10.2f" % (exp_3, monthly_3, yearly_3)
print "4. " + "%-10s $%-10.2f $%-10.2f" % (exp_4, monthly_4, yearly_4)
print "5. " + "%-10s $%-10.2f $%-10.2f" % (exp_5, monthly_5, yearly_5)
print "======================="
print "Monthly Savings: " + str(totalSavings_month)
print "Annual Savings: " + str(totalSavings_annual)
print "Monthly Tithing: " + str(monthTithing)
print "Annual Tithing: " + str(annualTithing) 
