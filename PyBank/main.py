import os
import csv


# Path to collect data from Resources folder
budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, newline= '') as csvfile:
   # Read in the CSV file and split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skips the header
    header = next(csvreader)

   

# define needed variables
    
    
    total_months = 0
    total_profit = 0
    profit_change = 0
    initial_profit = 0
    
    
    
    stored_profit = []
    stored_months = []
    stored_change_profit = []

   
   
    # count = 0
    # loop through the data

    for row in csvreader:
    # count rows for total month count
        total_months += 1
# print(total-months)
    # add row 1 for total profit
        current_month = int(row[1])
        total_profit += current_month
        
   
   
    # store date in a list make  
        stored_months.append(row[0])
    # store monthly profit as a list 
        stored_profit.append(row[1])
    #subtract current month from previous month, add the difference and divide by the row count minus one for average change 

        final_profit = int(row[1])
        
        monthly_change_profits = final_profit

        stored_change_profit.append(monthly_change_profits)
    #calculate average P & L changes
        profit_change = sum(stored_change_profit)/total_months 

        
        
        greatest_increase_profit = max(stored_change_profit)


        greatest_decrease_profit = min(stored_change_profit)

        
        
     


print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${total_profit}")
print(f"Average Change:  ${profit_change}")
print(f"Greatest Increase in Profits:  ${greatest_increase_profit}")
print(f"Greatest Decrease in Losses:  ${greatest_decrease_profit}")


