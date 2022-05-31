import os
import csv

election_data_csv = os.path.join("ByPoll","Resources","election_data.csv")
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
   

#	The total number of votes cast

    count = 0
    candidate = {}

    for i in csv_reader:
        count += 1
        name = i[2]
        if name in candidate.keys():
            candidate[name] += 1
        else:
            candidate[name] = 1



import sys
 
# Saving the reference of the standard output
original_stdout = sys.stdout  

def printResult():
    maxVote = 0
    winner = None

    Total_vote = count
    print("Election Results")
    print("-------------------------")
    print (f"Total Votes: ", Total_vote) 
    print("-------------------------")
    for name in candidate.keys():
        if candidate[name] > maxVote:
            maxVote = candidate[name] 
            winner = name
        print (name + ": " + str(round(candidate[name]/count*100,3))  + "% (" + str(candidate[name]) + ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

with open('Election_result.txt', 'w') as f:
    sys.stdout = f 
    printResult()
    sys.stdout = original_stdout 

printResult()