# import modules csv files

import os

import csv

# file path for csv
election_data = os.path.join('Resources', 'election_data.csv')




# Define Variables
vote = 0
candidates = []
unique_candidates = []
vote_tally = {}



with open(election_data, 'r') as file:
        
        for row in file:
                candidate = row[2]
                vote = vote + 1

        if vote_tally[candidate]:

                 current_vote = vote_tally[candidate] + 1
                 vote_tally[candidate] = current_vote
        else:
                vote_tally[candidate] = 1

print(vote_tally)

#  I am out of time with another week I would have killed it, sorry.