#tools needed to read and write csv
import os
import csv
csvpath = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')
csvpath2 = os.path.join('python-challenge','PyBank','analysis','writeup.txt')
with open(csvpath) as csvfile:
#counter is total number of rows, money is the total amount of change, the change variables represent the difference between this months profits and last month
#rest of the variables should be explanatory. reads and writes to file with all the information
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    counter = 0
    money = 0
    change = 0
    counter2 = 0
    change1 = 0
    change2 = 0
    truedate1 = ""
    truedate2 = ""
    highchange = 0
    lowchange = 0
    for row in csvreader:
        counter = counter + 1
        money = money + int(row[1])
        change0 = change1
        change1 = int(row[1])
        if counter2 == 0:
            counter2 = counter2 + 1
            continue
        change2 = change2 + (change1 - change0)
        truechange = change1 - change0
        if truechange > highchange:
            truedate1 = row[0]
            highchange = truechange
        if truechange < lowchange:
            truedate2 = row[0]
            lowchange = truechange
    change2 = change2 / (counter-1)

        

    print(row[1], row[0])
    print(counter)
f = open(csvpath2, 'w')
f.write(f'Financial Analysis\n--------------------\nTotal Months:{counter}\nTotal: ${money}\nAverage Change: ${round(change2,2)}\nGreatest Increase in Profits: {truedate1} (${highchange})\nGreatest Increase in Profits: {truedate2} (${lowchange})')
print(f'Financial Analysis\n--------------------\nTotal Months:{counter}\nTotal: ${money}\nAverage Change: ${round(change2,2)}\nGreatest Increase in Profits: {truedate1} (${highchange})\nGreatest Increase in Profits: {truedate2} (${lowchange})')