import os
import csv

#Variables
candidates = []
number_votes = []
percent_votes = []
total_votes = 0

#Path
csvpath=os.path.join("Resources", "election_data.csv")

#Csv reader
with open(election_data,"") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

        #for row in csvreader:
        
        #vote-counter 
        total_votes += 1  
         #Testing code   
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
        #List of percent votes
        for votes in num_votes:
         percent_votes.append(percentage)
         percentage = (votes/total_votes) * 100

        for row in csvreader:
         candidate=row[2]
        
        if candidate in candidates:
         vote_counter[candidate]+=1
        else:
         candidates.append(candidate)
         vote_counter[candidate]=1
         total_votes+=1
        #Testing code
        for i in range(len(candidates)):
	     vote_share = round((vote_counter[candidates[i]]/total_votes)*100, 3)
	     vote_percentage.append(vote_share)

	    if vote_counter[candidates[i]] > max_vote:
		 max_vote = vote_counter[candidates[i]]
		 winner = candidates[i]   

        #Winner
         winner = max(number_votes)
         winner_candidate = candidates[index]

#Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print(f"Winner: {winning_candidate}")
