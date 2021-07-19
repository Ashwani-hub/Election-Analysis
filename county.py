import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "county_only.txt")

total_votes = 0

county_list = []
county_votes = {}

largest_turnout_county = ""
county_votes_count = 0
county_votes_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1

#print(total_votes)

        county_name = row[1]

        if county_name not in county_list:
            county_list.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] += 1

#with open(file_to_save, "w") as txt_file:
election_results = (
    f"\nElection Results\n"
    f"------------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------------------\n"
    f"\nCounty Votes:\n"
)  
print(election_results, end="")

for county_name in county_votes:
    c_votes = county_votes[county_name]
    c_vote_percentage = float(c_votes) / float(total_votes)*100

    county_results = (
        f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})"
    )
    print(county_results)

    if (c_votes > county_votes_count) and (c_vote_percentage > county_votes_percentage):
        county_votes_count = c_votes
        county_votes_percentage = c_vote_percentage
        largest_turnout_county = county_name

County_turnout_summary = (
    f"\n-------------------------------\n"
    f"Largest County Turnout: {largest_turnout_county}"
    f"\n--------------------------------\n"
)

print(County_turnout_summary)


