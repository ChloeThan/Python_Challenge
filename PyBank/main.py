import os
import csv
from sqlite3 import Date, Row
budget_data_csv = os.path.join("PyBank","Resources","budget_data.csv")
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print("Finalcial analysis")
    row[1] = Date
    row[2] = Profit/Losses
    Total_months = len(row)
    print (f"Total months: ", Total_months) 
