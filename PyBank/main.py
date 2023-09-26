# Import Modules
import os
import csv

# Capture path in variable
budget_csv = os.path.join( 'PyBank2', 'Resources', 'budget_data.csv')
# Initialize variables
total_months = 0 
total_profit = 0
previous_profit = 0
profit_changes = []

# Open and read CSV file
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Count number of months
        total_months += 1
        # Get total amount of profit/losses
        total_profit += int(row[1])
        #Calculate change in profit/losses
        profit_change = int(row[1]) - previous_profit
        # Add change to list
        profit_changes.append(profit_change)
        # Set previous profit to current profit 
        previous_profit = int(row[1])

# Calculate average change in profit/losses
average_change = sum(profit_changes) / len(profit_changes)

# Calculate greatest increase in profit and corresponding date
greatest_increase = max(profit_changes)
greatest_increase_date = str([profit_changes.index(greatest_increase) + 1][0])

# Calculate greatest decrease in profit and corresponding date
greatest_decrease = min(profit_changes)
greatest_decrease_date = str([profit_changes.index(greatest_decrease) + 1][0])

# Print results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
