# PyPoll Week 3 Challenge

# Create script that does the following:

import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

voter_id = []
county = []
candidates= []
vote_number = []
vote_percent = []
poll = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

# The total number of votes cast
    for row in csvreader:
        voter_id.append(row[0])
        total_votes = len(voter_id)
        
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

# A complete list of candidates who received votes
for key, value in poll.items():
    candidates.append(key)
    vote_number.append(value)

#The percentage of votes each candidate won
for n in vote_number:
    vote_percent.append(round(int(n)/ total_votes * 100, 3))

# The total number of votes each candidate won
final_results = list(zip(candidates, vote_number, vote_percent))

# The winner of the election based on popular vote.
winner_list = []

for name in final_results:
    if max(vote_number) == name[1]:
        winner_list.append(name[0])
    
winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]


print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
print(candidates[0] + ": " + str(vote_percent[0]) + "% " + "(" + str(vote_number[0]) + ")")
print(candidates[1] + ": " + str(vote_percent[1]) + "% " + "(" + str(vote_number[1]) + ")")
print(candidates[2] + ": " + str(vote_percent[2]) + "% " + "(" + str(vote_number[2]) + ")")
print(candidates[3] + ": " + str(vote_percent[3]) + "% " + "(" + str(vote_number[3]) + ")")
print("--------------------------")
print("Winner: " + (winner))

output_hw = os.path.join("..", "PyPoll", "PyPoll" + ".txt")

with open (output_hw,"w") as writefile:
    writefile.writelines("Election Results" + "\n")
    writefile.writelines("--------------------------------" + "\n")
    writefile.writelines("Total Votes: " + str(total_votes) + "\n")
    writefile.writelines("--------------------------------" + "\n")
    writefile.writelines(candidates[0] + ": " + str(vote_percent[0]) + "% " + "(" + str(vote_number[0]) + ")" + "\n")
    writefile.writelines(candidates[1] + ": " + str(vote_percent[1]) + "% " + "(" + str(vote_number[1]) + ")" + "\n")
    writefile.writelines(candidates[2] + ": " + str(vote_percent[2]) + "% " + "(" + str(vote_number[2]) + ")" + "\n")
    writefile.writelines(candidates[3] + ": " + str(vote_percent[3]) + "% " + "(" + str(vote_number[3]) + ")" + "\n")
    writefile.writelines("--------------------------------" + "\n")
    writefile.writelines("Winner: " + (winner))


with open(output_hw, "r") as readfile:
    print(readfile.read())
