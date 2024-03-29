#!/usr/bin/env python
# coding: utf-8

#import pandas
import pandas as pd

#locate file
election_csv = 'C:/Users/Nytes/Desktop/DAbootcamp/Homework/Python_Homework/election_data.csv'

#read file and display top 5 rows
election_df = pd.read_csv(election_csv)
election_df.head()


#Count of Votes
total_votes = election_df['Voter ID']
total_votes.count()
#print("Total Votes: " + str(total_votes.count()))

#List of candidates that received votes
candidates = election_df['Candidate']
candidates.unique()

# Count how many votes occured for each candidate
candidate_counts = election_df["Candidate"].value_counts()
candidate_counts.head()

# Looking only at Khan
khan_df = election_df.loc[election_df["Candidate"] == "Khan", :]
khan_votes = khan_df['Voter ID']
khan_percent = ((khan_votes.count())/(total_votes.count())*100).round(1)
#print("Khan: " + str(khan_percent) +"% " + "(" + str(khan_votes.count()) + ")")

# Looking only at Correy
correy_df = election_df.loc[election_df["Candidate"] == "Correy", :]
correy_votes = correy_df['Voter ID']
correy_percent = ((correy_votes.count())/(total_votes.count())*100).round(1)
#print("Correy: " + str(correy_percent) +"% " + "(" + str(correy_votes.count()) + ")")

# Looking only at Li
li_df = election_df.loc[election_df["Candidate"] == "Li", :]
li_votes = li_df['Voter ID']
li_percent = ((li_votes.count())/(total_votes.count())*100).round(1)
#print("Li: " + str(li_percent) +"% " + "(" + str(li_votes.count()) + ")")

# Looking only at O'Tooley
otooley_df = election_df.loc[election_df["Candidate"] == "O'Tooley", :]
otooley_votes = otooley_df['Voter ID']
otooley_percent = ((otooley_votes.count())/(total_votes.count())*100).round(1)
#print("O'Tooley: " + str(otooley_percent) +"% " + "(" + str(otooley_votes.count()) + ")")

#summary table
election_summary_df = pd.DataFrame({"Candidate Name": ["Khan", "Correy", "Li", "O'Tooley"],
                                  "Percent of Votes": [khan_percent, correy_percent,
                                                       li_percent, otooley_percent]})
election_summary_df

#find winner
election_summary_df = election_summary_df.sort_values(
    ["Percent of Votes"], ascending=False)
election_summary_df.head()
winner = election_summary_df.iloc[0, 0]
#print(winner)

print("Election Results")
print("-----------------------")
print("Khan: " + str(khan_percent) +"% " + "(" + str(khan_votes.count()) + ")")
print("Correy: " + str(correy_percent) +"% " + "(" + str(correy_votes.count()) + ")")
print("Li: " + str(li_percent) +"% " + "(" + str(li_votes.count()) + ")")
print("O'Tooley: " + str(otooley_percent) +"% " + "(" + str(otooley_votes.count()) + ")")
print("-----------------------")
print("Winner: " + str(winner))
print("-----------------------")

#Export file as a text with the header
election_summary_df.to_csv("PyPoll_summary.csv", header=True, index=False)
