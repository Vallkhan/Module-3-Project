import os.path
import csv

with open(r'C:\Users\vallk\Desktop\Boot_Camp\Python\Repository\Module-3-Project\PyPoll\Resources\election_data.csv') as file:
    raw_data = csv.reader(file)
    header = next(raw_data)
    
    election_data = []
    for line in raw_data:
        election_data.append(line)
        

ballot = []
for line in election_data:
    ballot.append(int(line[0]))
    
county = []
for line in election_data:
    county.append(line[1])
     
candidate = []
for line in election_data:
    candidate.append(line[2])
    
total_votes = len(ballot)

#A complete list of candidates who received votes 

names = []
for x in range(len(candidate)):    
    if candidate[x] == candidate[0] and ballot[x] == 1:
        names = names.append(candidate[x])
    elif candidate[x] != candidate[x-1] and candidate[x] not in names:
        names.append(candidate[x])

Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

#The percentage of votes each candidate won
for x in range(len(candidate)):
    if candidate[x] == "Charles Casper Stockham":
        Stockham_votes = Stockham_votes + 1
    elif candidate[x] == "Diana DeGette":
        DeGette_votes = DeGette_votes + 1
    else:
        Doane_votes =  Doane_votes + 1    
        
if Stockham_votes > DeGette_votes and Stockham_votes > Doane_votes:
    winner = names[0]
elif DeGette_votes > Stockham_votes and DeGette_votes > Doane_votes:
    winner = names[1]
else:
    winner = names[2]
        
Stockham_percentage = format(Stockham_votes/len(candidate),".3%")
DeGette_percentage = format(DeGette_votes/len(candidate),".3%")
Doane_percentage = format(Doane_votes/len(candidate),".3%")

results_path = os.path.join(r'C:\Users\vallk\Desktop\Boot_Camp\Python\Repository\Module-3-Project\PyPoll\analysis','Election_results.txt')

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