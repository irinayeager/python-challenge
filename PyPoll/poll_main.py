import os
import csv

infile = os.path.join('Resources', 'election_data.csv')

outfile = os.path.join('analysis', 'pypoll.txt')

# Declare variables
totalVotes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
maxVotes = 0
winner = ""

with open(infile) as csvfile:
    rows = csv.reader(csvfile)

    csv_header = next(rows)
    # print(csv_header)
    # exit()

    for row in rows:
        totalVotes += 1

        # print(row)
        # break

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

print(totalVotes)

dict_candidates_and_votes = {
    "Khan": Khan_votes,
    "Correy": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes
}

# Find winner
for candidate, votes in dict_candidates_and_votes.items():
    if votes > maxVotes:
        maxVotes = votes
        winner = candidate


output = f"""
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: {(Khan_votes / totalVotes)*100:.3f} % ({Khan_votes:,})
Correy: {(Correy_votes/totalVotes)*100:.3f}%  ({Correy_votes:,})
Li: {(Li_votes/totalVotes)*100:.3f}%  ({Li_votes})
O'Tooley: {(OTooley_votes/totalVotes)*100:.3f}%  ({OTooley_votes:,})
------------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(outfile, 'w') as outputFile:
    outputFile.write(output)
