import os
import csv

csv_path = os.path.join("..","PyPoll", "Resources","election_data.csv")

with open(csv_path,"r",encoding="utf") as file:
    raw_data = csv.reader(file)
    header = next(raw_data)
    
    election_data = []
    for each_line in raw_data:
        election_data.append(each_line)        

# Created a numeric list for all the ballot 
ballot = []
for line in election_data:
    ballot.append(int(line[0]))
    
# Created a list for all the counties    
county = []
for line in election_data:
    county.append(line[1])
    
# Created a list of all the candidates    
candidate = []
for line in election_data:
    candidate.append(line[2])

# Extracted the unique names
names = []
for x in range(len(candidate)):    
    if candidate[x] == candidate[0] and ballot[x] == 1:
        names = names.append(candidate[x])
    elif candidate[x] != candidate[x-1] and candidate[x] not in names:
        names.append(candidate[x])
        
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

# Calculated the amount of votes each candidate received
for x in range(len(candidate)):
    if candidate[x] == "Charles Casper Stockham":
        Stockham_votes = Stockham_votes + 1
    elif candidate[x] == "Diana DeGette":
        DeGette_votes = DeGette_votes + 1
    else:
        Doane_votes =  Doane_votes + 1   
         
# Determined the winner of the election       
if Stockham_votes > DeGette_votes and Stockham_votes > Doane_votes:
    winner = names[0]
elif DeGette_votes > Stockham_votes and DeGette_votes > Doane_votes:
    winner = names[1]
else:
    winner = names[2]

# Determined the percentages        
Stockham_percentage = format(Stockham_votes/len(candidate),".3%")
DeGette_percentage = format(DeGette_votes/len(candidate),".3%")
Doane_percentage = format(Doane_votes/len(candidate),".3%")
total_votes = len(ballot)

# Created the txt file 
results_path = os.path.join("..","PyPoll", "analysis", "Election_Results.txt")
results = open(results_path, 'w')

results.write("Election Results") 
results.write("\n"+"\n"+"---------------------------")
results.write("\n"+"\n"+f"Total Votes: {total_votes}")  
results.write("\n"+"\n"+"---------------------------") 
results.write("\n"+"\n"+f"{names[0]}: {Stockham_percentage} ({Stockham_votes})")
results.write("\n"+"\n"+f"{names[1]}: {DeGette_percentage} ({DeGette_votes})")
results.write("\n"+"\n"+f"{names[2]}: {Doane_percentage} ({Doane_votes})")
results.write("\n"+"\n"+"---------------------------")
results.write("\n"+"\n"+f"Winner: {winner}")
results.write("\n"+"\n"+"---------------------------")

results.close()