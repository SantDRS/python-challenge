# Import modules
import pandas as pd
import os
import csv

# Set up Title
print("\n")
print("Jose Santos")

print("Python-Challenge - PyPoll Analysis \n\n")


# Save the path to data set in a variable & read file
PollFile = pd.read_csv("../PyPoll/Resources/election_data.csv", encoding = "utf-8")
#print(PollFile)


# Create a DataFrame with columns needed
Poll_df = PollFile[["Candidate", "Ballot ID"]]
Poll_df = Poll_df.rename(columns={"Candidate": "Candidate Name"})
#print(Poll_df)


# Calculate Results
# The total number of votes cast
Votes = len(Poll_df["Ballot ID"].unique())

# A complete list of candidates who received votes
Candidates = Poll_df["Candidate Name"].unique()
#print(Candidates)

# The total number of votes each candidate won
# Groupby the Candidate Name and count votes
PollGroup = Poll_df.groupby(["Candidate Name"])
PollTotals = PollGroup.count()

# Rename Ballot ID columnb to Ballot Count
PollTotals = PollTotals.rename(columns={"Ballot ID": "Ballot Count"})
#print(PollTotals)

# The percentage of votes each candidate won
PollTotals["Percent of Votes"] = round((PollTotals["Ballot Count"] / Votes) * 100)

# Rearrange columns to show percentage first
PollTotals = PollTotals[["Percent of Votes", "Ballot Count"]]
#print(PercentVotes)

# The winner of the election based on popular vote.
PollWinner = PollTotals["Ballot Count"].max()
PollWinner = PollTotals.loc[PollTotals["Ballot Count"] == PollWinner]


# Print the Financial Analysis
print("Election Results")
print("-----------------------------------------")
print("Total Votes: " + str(Votes))
print("-----------------------------------------")
print("Candidate Summary: \n")
print(PollTotals)
print("-----------------------------------------")
print("Winner: \n" + str(PollWinner))
print("-----------------------------------------")


# Write to Txt File
# Setup file path & creation
fname = "../PyPoll/analysis/PyBank_Analysis.txt"
f = open(fname, 'w')

# Set up Title
f.write("\n")
f.write("Jose Santos \n")

f.write("Python-Challenge - PyPoll Analysis \n\n")

# File Content
f.write("Election Results \n")
f.write("----------------------------------------- \n")
f.write("Total Votes: " + str(Votes))
f.write('\n')
f.write("----------------------------------------- \n")
f.write("Candidate Summary: \n")
f.write(str(PollTotals))
f.write('\n')
f.write("----------------------------------------- \n")
f.write("Winner: \n" + str(PollWinner))
f.write('\n')
f.write("-----------------------------------------")

# Close the file
f.close()
