#import modules for os and csv
import os
import csv

#set the path
election_data_path = "Resources/election_data.csv"

#Variables
count_of_votes = 0

#instruct python to read csv file
with open(election_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    total_votes = []
    Khan_votes = []
    Correy_votes = []
    Li_votes = []
    OTooley_votes = []
    election_winner = []    
    
    #read each row of data
    for row in csvreader:
        
        total_votes.append(str(row[1]))
        
        if row[2] == "Khan":
            Khan_votes.append(str(row[2]))

        if row[2] == "Correy":
            Correy_votes.append(str(row[2]))
        
        if row[2] == "Li":
            Li_votes.append(str(row[2]))
        
        if row[2] == "O'Tooley":
            OTooley_votes.append(str(row[2]))              
                
    #The total number of votes cast
    total_vote_count = len(total_votes)
    
    #Calculating total votes for each candidate
    Khan_total = len(Khan_votes)
    
    Correy_total = len(Correy_votes)
    
    Li_total = len(Li_votes)
    
    OTooley_total = len(OTooley_votes)
    

    #Calculating the percentage of votes each candidate won
    pct_Khan = (Khan_total / total_vote_count) * 100
    pct_Khan_rounded = round(pct_Khan, 2)
    
    pct_Correy = (Correy_total / total_vote_count) * 100
    pct_Correy_rounded = round(pct_Correy, 2)
    
    pct_Li = (Li_total / total_vote_count) * 100
    pct_Li_rounded = round(pct_Li, 2)
    
    pct_OTooley = (OTooley_total / total_vote_count) * 100
    pct_OTooley_rounded = round(pct_OTooley, 2)
    

    if (pct_Khan > pct_Correy) and (pct_Khan > pct_Li) and (pct_Khan > pct_OTooley):
        election_winner.append("Khan")
    elif (pct_Correy > pct_Khan) and (pct_Correy > pct_Li) and (pct_Correy > pct_OTooley):
        election_winner.append("Correy")
    elif (pct_Li > pct_Correy) and (pct_Li > pct_Khan) and (pct_Li > pct_OTooley):
        election_winner.append("Li")
    elif (pct_OTooley > pct_Correy) and (pct_OTooley > pct_Khan) and (pct_OTooley > pct_Li ):
        election_winner.append("O'Tooley")
    else:
        election_winner.append("Undecided")

    #Results
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_vote_count))
    print("-------------------------")
    print("Khan: " + str(pct_Khan_rounded) + "% " + " (" + str(Khan_total) + ")")
    print("Correy: " + str(pct_Correy_rounded) + "% " + " (" + str(Correy_total) + ")")
    print("Li: " + str(pct_Li_rounded) + "% " + " (" + str(Li_total) + ")")
    print("O'Tooley: " + str(pct_OTooley_rounded) + "% " + " (" + str(OTooley_total) + ")")
    print("-------------------------")
    print("Winner: " + (election_winner[0]))
    print("-------------------------")


# Export File
# Specify the file to write to
import os
import csv

output_path = os.path.join("Output", "Election_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    #Write Title Row
    csvwriter.writerow(["Election Results"])
    # Write header row
    csvwriter.writerow([" ", "% Votes Won", "Vote Count"]) 
    # Write the Khan row
    csvwriter.writerow(["Khan", str(pct_Khan_rounded) + "%", str(Khan_total)])
    # Write the Correy row
    csvwriter.writerow(["Correy", str(pct_Correy_rounded) + "%", str(Correy_total)])
    # Write the Li row
    csvwriter.writerow(["Li", str(pct_Li_rounded) + "%", str(Li_total)])
    # Write the O'Tooley Row
    csvwriter.writerow(["O'Tooley", str(pct_OTooley_rounded) + "%", str(OTooley_total)])
    # Write the Total Votes row
    csvwriter.writerow(["Total Votes" ," " , str(total_vote_count)])
    #Black row to seperate individual results from final results
    csvwriter.writerow([" "])
    # Write the results row
    csvwriter.writerow(["Winner", str(election_winner[0])])