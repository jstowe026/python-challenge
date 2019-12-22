#!/usr/bin/env python
# coding: utf-8

#import pandas
import pandas as pd

#locate file
budget_csv = 'C:/Users/Nytes/Desktop/DAbootcamp/Homework/Python_Homework/budget_data.csv'

#read file and display top 5 rows
data_df = pd.read_csv(budget_csv)
data_df.head()

#Count of Months
month = data_df['Date']
month.count()
#print("Total Months: " + str(month.count()))

#Net total amount of "Profit/Losses" over the entire period
profit_losses = data_df['Profit/Losses']
profit_losses.sum()
#print("Total: $" + str(profit_losses.sum()))

#Calculate the month to month changes in "Profit/Losses" & create new column with values
monthly_change = profit_losses.diff(periods=1);
data_df["Monthly Change"] = monthly_change
data_df.head()

#The average of the changes in "Profit/Losses" over the entire period
mean_change = monthly_change.mean()
#print("Average Change: $" + str(round(monthly_change.mean(),2)))

#The greatest increase in profits (date and amount) over the entire period
max_change = data_df['Monthly Change'].max()
#print(max_change)

#The greatest decrease in losses (date and amount) over the entire period
min_change = data_df['Monthly Change'].min()
#print(min_change)

#find the month associated with the max
data_new_df = data_df.set_index("Date")
data_new_df.head()
month_max = data_new_df.loc[data_new_df['Monthly Change'] == max_change, :]
#print(month_max)
#print("Greatest Increase in Profits: " + "($" + str(max_change) +")")

#find the month associated with the min
data_new_df = data_df.set_index("Date")
data_new_df.head()
month_min = data_new_df.loc[data_new_df['Monthly Change'] == min_change, :]
#print(month_min)
#print("Greatest Increase in Profits: " + "($" + str(min_change) +")")

#Print statistics
print("Financial Analysis")
print("-------------------------------------")
print("Total Months: " + str(month.count()))
print("Total: $" + str(profit_losses.sum()))
print("Average Change: $" + str(round(mean_change,2)))
print("Greatest Increase in Profits: " + "($" + str(max_change) +")")
print("Greatest Decrease in Profits: " + "($" + str(min_change) +")")


#Export text file with results
#Export file as a text with the header
data_new_df.to_csv("PyBank.csv", header=True)
