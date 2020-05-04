import os
import csv

#Set file for path
election_path = os.path.join("Resources","election_data.csv")

#List Variables
total_votes = 0
total_candidates = 0
# candidates = []
percent_received_list = []
candidates_list = []
votes_received_list = []
percent_received = 0
highest_percent = 0
winner_is = ""

with open(election_path) as csvfile:
    csvreader = csv.reader(election_path, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    # print(f"CSV Header: {csvheader}")

    #count votes
    for row in csvreader:
        total_votes += 1
        candidate = row[0]
        if candidate in candidates_list:
            an_index = candidates_list.index(candidate)
            votes_received_list[an_index] += 1
        else:
            candidates_list.append(candidate)
            votes_received_list.append(1)

an_index = 0
for votes_received in (votes_received_list):
    percent_received = ((votes_received/total_votes) *100)
    percent_received_list.append(percent_received)
    if percent_received > highest_percent:
        highest_percent = percent_received
        winner_is = (f"{candidates_list[an_index]}")
    an_index +=1

# print(total_votes)
# print(candidates_list)
# print(votes_received_list)
# print(total_votes)
# print(percent_received_list)
# print(winner_is)

print("Election Results")
print("----------------------------")
print(f"{candidates_list[0]}: {round(percent_received_list[0])}% ({votes_received_list[0]})")
print(f"{candidates_list[1]}: {round(percent_received_list[1])}% ({votes_received_list[1]})")
print(f"{candidates_list[2]}: {round(percent_received_list[2])}% ({votes_received_list[2]})")
print(f"{candidates_list[3]}: {round(percent_received_list[3])}% ({votes_received_list[3]})")
print("----------------------------")
print(f"Winner: {winner_is}")

with open("election_data.txt", 'w') as file:
    # textwriter = textwriter(textfile)

    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"{candidates_list[0]}: {round(percent_received_list[0])}% ({votes_received_list[0]})\n")
    file.write(f"{candidates_list[1]}: {round(percent_received_list[1])}% ({votes_received_list[1]})\n")
    file.write(f"{candidates_list[2]}: {round(percent_received_list[2])}% ({votes_received_list[2]})\n")
    file.write(f"{candidates_list[3]}: {round(percent_received_list[3])}% ({votes_received_list[3]})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner_is}")