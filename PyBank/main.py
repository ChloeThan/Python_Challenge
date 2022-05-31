import os
import csv
from sqlite3 import Date, Row
import statistics
budget_data_csv = os.path.join("Resources","budget_data.csv")
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    count = 0
    total = 0
    profit = []
    months = []
    differences = []

#	The total number of months included in the dataset
#	The net total amount of "Profit/Losses" over the entire period
#	The average of the changes in "Profit/Losses" over the entire period

    for i in csv_reader:
        
        count += 1
        total += int(i[1])
        
        profit.append(i[1])
        change = (int(profit[-1]) - int(profit[0]))
        months.append(i[0])

        
    Total_months = count
    Net_total_amount = total
    Average_change = change/(Total_months -1)

#	The greatest increase in profits (date and amount) over the entire period

    for i in range(0,len(profit)):

        if(i+1<86):
            current_value = profit[i]
            next_value = profit[i+1]
            difference_in_profit = int(next_value) - int(current_value)
            differences.append(difference_in_profit)
       
index_of_month = differences.index(max(differences))


#	The greatest decrease in losses (date and amount) over the entire period

index_of_month = differences.index(min(differences))

def printResult():
    print("Financial Analysis")
    print("---------------------------")
    print (f"Total Months: ", Total_months) 
    print ("Net Total Amount: $" + str(Net_total_amount)) 
    print ("Average Change: $" + str(Average_change))
    print(f"Greatest Increase in Profits: ", months[index_of_month+1], "($" + str(max(differences)) + ")")
    print(f"Greatest Decrease in Losses: ", months[index_of_month+1], "($" + str(min(differences)) + ")")

import sys
 
# Saving the reference of the standard output
original_stdout = sys.stdout  

with open('Analysis_result.txt', 'w') as f:
    sys.stdout = f 
    printResult()
    sys.stdout = original_stdout 

printResult()