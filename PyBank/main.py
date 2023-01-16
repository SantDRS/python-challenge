# Import modules
import pandas as pd
import os
import csv

print('\n')
print("Jose Santos")
print("Python-Challenge - PyBank Analysis")

# Save path to data set in a variable & read file
budget_file = pd.read_csv("../PyBank/Resources/budget_data.csv", encoding = "utf-8")
#print(budget_file)


# Calculations
# The total number of months included in the dataset
total_months = len(budget_file['Date'].unique())
            
# The net total amount of "Profit/Losses" over the entire period
Net_Profit = budget_file["Profit/Losses"].sum()

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
Changes = budget_file["Profit/Losses"].diff(+1)
budget_file["Changes"] = Changes

Avg_Change = budget_file["Changes"].mean()
Avg_Change = round(int(Avg_Change))
#print(Avg_Change)
#print(budget_file)

# The greatest increase in profits (date and amount) over the entire period
Greatest_Increase = budget_file["Changes"].max()
Greatest_Increase = round(int(Greatest_Increase))
#print(Greatest_Increase)

# The greatest decrease in profits (date and amount) over the entire period
Greatest_Decrease = budget_file["Changes"].min()
Greatest_Decrease = round(int(Greatest_Decrease))
#print(Greatest_Decrease)


#Print the Financial Analysis
print("Financial Analysis")
print(".................................................")
print("Total Months: " + str(total_months))
print("Net Profit: $" + str(Net_Profit))
print("Average Change: $" + str(Avg_Change))
print("Greatest Increase in Profit: " + budget_file.loc[budget_file["Changes"] == 1862002, "Date"].values[0], " $" + str(Greatest_Increase))
print("Greatest Decrease in Profit: " + budget_file.loc[budget_file["Changes"] == -1825558, "Date"].values[0], " $" + str(Greatest_Decrease))
    
print(".................................................")

# Write the Text File Out

fname = "../PyBank/analysis/PyBank_Analysis.txt"
f = open(fname, 'w')
f.write("Jose Santos")
f.write('\n')
f.write("Python-Challenge - PyBank Analysis")
f.write('\n')
f.write("Financial Analysis")
f.write('\n')
f.write(".................................................")
f.write('\n')
f.write("Total Months: " + str(total_months))
f.write('\n')
f.write("Net Profit: $" + str(Net_Profit))
f.write('\n')
f.write("Average Change: $" + str(Avg_Change))
f.write('\n')
f.write("Greatest Increase in Profit: Aug-16 $1862002")
f.write('\n')
f.write("Greatest Decrease in Profit: Feb-14 $-1825558")
f.write('\n')
f.write(".................................................")
f.close()


