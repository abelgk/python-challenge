import csv
from collections import OrderedDict
from operator import itemgetter

#files we will work with
vote_data = "Resources/election_data.csv"
vote_data_analysed = "Resources/election_data_analysed.txt"

vote_count = 0
winning_votes = 0
number_of_candidates = 0 
candidates_list = []
votes_won = {}
biggest_vote = ["", 0]


with open (vote_data) as poll_data:
    csv_reader = csv.DictReader(poll_data)

    for row in csv_reader:
        vote_count = vote_count + 1
        number_of_candidates = row["Candidate"]

        if row["Candidate"] not in candidates_list:
            candidates_list.append(row["Candidate"])
            votes_won[row["Candidate"]] = 1

        else:
            votes_won[row["Candidate"]] = votes_won[row["Candidate"]] + 1

    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(vote_count))
    print("-------------------------")

        #calculate the %votes each candidate won
    for opponent in votes_won:
        print(opponent + " " + str(round(((votes_won[opponent]/vote_count)*100))) + "%" + " (" + str(votes_won[opponent]) + ")") 
        candidate_results = (opponent + " " + str(round(((votes_won[opponent]/vote_count)*100))) + "%" + " (" + str(votes_won[opponent]) + ")") 
            #print(opponent)
    
    votes_won
    winning_candidate = sorted(votes_won.items(), key = itemgetter(1),reverse = True)
    print("-------------------------")
    print("Winner: " + str(winning_candidate[0]))
    print("-------------------------")

# Output Files
with open(vote_data_analysed, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winning_candidate))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winning_candidate[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(vote_count))

