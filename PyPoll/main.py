#importing needed tools to read csv and reading them
import os
import csv
csvpath = os.path.join('python-challenge','PyPoll','Resources','election_data.csv')
csvpath2 = os.path.join('python-challenge','PyPoll','analysis','writeup.txt')
#writing on txt file and counting the number of rows for total votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    counter = 0

    for row in csvreader:
        counter = counter + 1
    f = open(csvpath2, 'w')
    f.write(f'Election Results\n-------------------------\nTotal Votes: {counter}\n-------------------------\n')
    firstrow = 0
    name = ""
    votecounter = 0
#votex represents the votes for the respective voters. The letteres represent the first letter of their name and stores a string for comparing and printing. Rest of the code counts 
#their votes and prints out the highest and writes on text file
with open(csvpath) as csvfile2:

    csvreader2 = csv.reader(csvfile2, delimiter=',')
    csv_header2 = next(csvreader2)
    c = "Charles Casper Stockham"
    d = "Diana DeGette"
    r = "Raymon Anthony Doane"
    votec = 0
    voted = 0
    voter =  0
    for row in csvreader2:
        if(row[2] == c):
            votec = votec + 1
        if(row[2] == d):
            voted = voted + 1
        if(row[2] == r):
            voter = voter + 1
    f.write(f'{c}: {round(votec/counter*100, 3)}% ({votec})\n{d}: {round(voted/counter*100, 3)}% ({voted})\n{r}: {round(voter/counter*100, 3)}% ({voter})\n-------------------------\n')
    winner = ''
    if votec > voted and votec > voter:
        winner = c 
    if voted > votec and voted > voter:
        winner = d
    if voter > voted and voter > votec:
        winner = r
    f.write(f'Winner: {winner}\n-------------------------')
    print(f'Election Results\n-------------------------\nTotal Votes: {counter}\n-------------------------\n')
    print(f'{c}: {round(votec/counter*100, 3)}% ({votec})\n{d}: {round(voted/counter*100, 3)}% ({voted})\n{r}: {round(voter/counter*100, 3)}% ({voter})\n-------------------------\n')
    print(f'Winner: {winner}\n-------------------------')


        
        
            
        

