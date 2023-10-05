# Import Modules
import os
import csv

# Log file address in py_poll_csv
py_poll_csv = os.path.join( 'PyPoll2', 'Resources', 'election_data.csv')
output_analysis = os.path.join( 'PyPoll2', 'Resources', 'election_data.csv')
total_votes = 0
candidate_votes = {}

# Scan CSV file
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    #Loop through the file
    for row in csvreader:
        #Count number of total votes
        total_votes += 1

        #Capture unique candidates names
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        #Count the votes for each candidate
        candidate_votes[candidate_name] += 1

#Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
winner = ""
winner_votes = 0
for candidate_name, votes in candidate_votes.items():
    percentage = round(votes/total_votes*100, 3)
    print(f"{candidate_name}: {percentage}% ({votes})")
    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Create Analysis text file
output = (
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total_votes}\n"
f"-------------------------\n"
f"Winner: {winner}\n"
f"-------------------------\n")

# Export the results to text file
with open(output_analysis, "w") as txt_file:
    txt_file.write(output)
