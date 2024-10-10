# Module
import csv

# Set path to the CSV file
election_data_csv = "C:/Users/somay/OneDrive/Boot Camp/Class Activity/Homeworks/3/python-challenge/PyPoll/Resources/election_data.csv"

# Set variables
total_votes = 0
candidates = []
candidate_votes = {}

# Open and read the CSV file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Loop through the rows in the CSV file
    for row in csvreader:
        total_votes += 1           # Count the total number of votes

        candidate = row[2]         # Candidate name is in the third column
        
        # If the candidate is not in the list, add them
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        # Increment vote count for each candidate
        candidate_votes[candidate] += 1

# Print Election Results header
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Variables to track the winner
winner = ""
winning_count = 0

# Calculate the percentage and number of votes for each candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    
    # Print candidate results
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Print the winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Store the election results in a variable
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Add each candidate's results to the variable
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

# Add winner information to the results
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the analysis results to the terminal
print(results)

# Export the results to a text file
output_path = "C:/Users/somay/OneDrive/Boot Camp/Class Activity/Homeworks/3/python-challenge/PyPoll/analysis/election_results.txt"
with open(output_path, "w") as txt_file:
    txt_file.write(results)

