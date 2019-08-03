# PyBank Week 3 Challenge

# Create script that does the following:

    
    
    
   
import os
import csv

csvpath = os.path.join("..","Pybank","Resources", "budget_data.csv")

months = []
profits = []
profits_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

# The total number of month included in the dataset
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
       

    total_months=len(months)
    total_profit=sum(profits)

 # The net total amount of "Profit/Losses" over the entire period   
    for x in range(1,len(profits)):
        profits_change.append((int(profits[x])- int(profits[x-1])))

# The average of the changes in "Profit/Losses" over the entire period
    profits_average = round(sum(profits_change)/len(profits_change),2)

 # The greatest increase in profit (date and amount) over the entire period
    greatest_increase = str(months[profits_change.index(max(profits_change)) + 1]) + " " + "$" + str(max(profits_change))

# The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = str(months[profits_change.index(min(profits_change)) + 1]) + " " + "$" + str(min(profits_change))

# Printed Results

print("Finacial Analysis")
print("--------------------------------")
print("Total Months: "+ str(total_months))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(profits_average))
print("Greatest Increase in Profits: " + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease))
    
output_hw = os.path.join("..", "Pybank", "PyBank" + ".txt")

with open (output_hw,"w") as writefile:
    writefile.writelines("Finacial Analysis" + "\n")
    writefile.writelines("--------------------------------" + "\n")
    writefile.writelines("Total Months: "+ str(total_months) + "\n")
    writefile.writelines("Total: " + "$" + str(total_profit) + "\n")
    writefile.writelines("Average Change: " + "$" + str(profits_average) + "\n")
    writefile.writelines("Greatest Increase in Profits: " + str(greatest_increase) + "\n")
    writefile.writelines("Greatest Decrease in Profits: " + str(greatest_decrease))

with open(output_hw, "r") as readfile:
    print(readfile.read())


