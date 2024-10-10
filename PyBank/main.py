# Moduale
import csv

# Set path to the CSV file
budget_data_csv = "C:/Users/somay/OneDrive/Boot Camp/Class Activity/Homeworks/3/python-challenge/PyBank/Resources/budget_data.csv"

# Set variables
total_months = 0
net_total = 0
data = []
changes = []
dates = []

# Open and read the CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Print the analysis header
    print("Financial Analysis")
    print("-------------------------")
    
    # Initialize previous_value to track the first row
    previous_month_profit_loss = None

    # Loop through the rows in the CSV file
    for row in csvreader:
        total_months += 1           # Count the total number of months
        net_total += int(row[1])    # Sum the total Profit/Losses
        
        # Store data and calculate changes
        data.append(row)
        
        # Calculate changes after the first month
        current__month_profit_loss = int(row[1])
        if previous_month_profit_loss is not None:
            change = current__month_profit_loss - previous_month_profit_loss
            changes.append(change)
            dates.append(row[0])       # Store the date of the change
        previous_month_profit_loss = current__month_profit_loss

# Print total months and total profit/losses
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the average change
print(f"Average Change: ${average_change:.2f}")

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding dates for greatest increase and decrease
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Store the analysis results in a variable
results = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis results to the terminal
print(results)

# Export the results to a text file
output_path = "C:/Users/somay/OneDrive/Boot Camp/Class Activity/Homeworks/3/python-challenge/PyBank/analysis/financial_analysis.txt"
with open(output_path, "w") as txt_file:
    txt_file.write(results)