#Add dependencies
import csv
import os
#Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the election results and read the file
with open(file_to_load) as election_data:
    #Read file object with reader function
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    print(headers)
#print each row in csv
    #for row in file_reader:
        #print(row)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
