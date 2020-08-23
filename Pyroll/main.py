import os
import csv

csvpath=os.path.join('..','Resources','election_data.csv')
print("Election Results")
print("__________________")
votes = []
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for column in csvreader:
        votes.append(column[0])
        candidates.append(column[2])

    Total_Votes = (len(votes))
    print(f"Total Votes:{Total_Votes}")

    

    Khan = int(candidates.count("Khan")) 
    Correy = int(candidates.count("Correy"))
    Li = int(candidates.count("Li"))
    O_Tooley = int(candidates.count("O'Tooley"))

    Khan_percentage = round((Khan/Total_Votes) * 100, 2)
    Correy_percentage = round((Correy/Total_Votes) * 100, 2)
    Li_percentage = round((Li/Total_Votes) * 100, 2)
    O_Tooley_percentage = round((O_Tooley/Total_Votes) * 100, 2)

    print(f"Khan: {Khan_percentage}% ({Khan})") 
    print(f"Correy: {Correy_percentage}% ({Correy})") 
    print(f"Li: {Li_percentage}% ({Li})")
    print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")

    if Khan > Correy > Li > O_Tooley:
        Winner = "Khan"
    elif Correy > Khan > Li > O_Tooley:
        Winner = "Correy"
    elif Li > Khan > Correy > O_Tooley:
        Winner = "Li"
    elif O_Tooley > Khan > Correy > Li:
        Winner = "O'Tooley"
    print(f"Winner: {Winner}")

output_path = os.path.join("election_poll.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f"Total Votes: {Total_Votes}")
    txtfile.write(f"Khan: {Khan_percentage}% ({Khan})")
    txtfile.write(f"Correy: {Correy_percentage}% ({Correy})")
    txtfile.write(f"Li: {Li_percentage}% ({Li})")
    txtfile.write(f"O'Tooley: {O_Tooley_percentage}% ({Correy})")
    txtfile.write(f"Winner: {Winner}")
    txtfile.close()
