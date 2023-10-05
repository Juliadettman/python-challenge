# Import Modules
import os
import csv

# Capture path in variable
budget_csv = os.path.join( 'PyBank2', 'Resources', 'budget_data.csv')
output_analysis - os.path.join( 'PyBank2', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0 
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]

# Open and read CSV file
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Count number of months
        total_months += 1
        # Get total amount of profit/losses
        total_profit_loss += int(row[1])
        #Calculate change in profit/losses
        profit_loss_change = int(row[1]) - prev_profit_loss
        # Set previous profit to current profit 
        prev_profit_loss = int(row[1])

# Find the greatest increase in profits (date and amount) over the entire period
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

# Find the greatest decrease in losses (date and amount) over the entire period
        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average change in profit/loss over the entire period
average_change = round(total_profit_loss/total_months, 2)

# Print results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")  

# Export the results to text file
output = (
f"Financial Analysis\n"
f"--------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit_loss}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")       

with open(output_analysis, "w") as txt_file:
    txt_file.write(output)
