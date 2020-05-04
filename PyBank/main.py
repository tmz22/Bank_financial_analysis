#Import Dependencies
import os
import csv

#Data File Name and Path

budget_path = os.path.join("Resources","budget_data.csv")
#csvpath = "budget_data.csv"
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

#Read Header Row
    csv_header = next(csvreader)
    

# Variable
    month = []
    monthly_rev_change = []
    avg_monthly_revenue_chg = []
    total_revenue = 0
    total_revenue_change = 0
    prev_month_rev = 0

#Calculate Number of Months, and Sum Up total Profit or Loss
    for row in csvreader:
        month.append(row[0])
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - prev_month_rev
        prev_month_rev = int(row[1])
        monthly_rev_change.append(revenue_change)
 


# Calculate average monthly change
    average_monthly_change = round((sum(monthly_rev_change) - monthly_rev_change[0]) / (len(month) -1 ),2)
    
    
# Determine the greatest monthly profit increase amount, and identify month
    largest_increase = max(monthly_rev_change)
    
    lg_inc_mnth = monthly_rev_change.index(largest_increase)
    largest_increase_month = month[lg_inc_mnth]
    

# Determine the greatest monthly decrease change amount, and identify month
    largest_decrease = min(monthly_rev_change)
    
    lg_dec_mnth = monthly_rev_change.index(largest_decrease)
    largest_decrease_month = month[lg_dec_mnth]
   
  
# Print Results on Terminal
print("Financial Analysis")
print("----------------------------------------------")
print("Total Months: " + str(len(month)))
print("Total Profit: $" + str(total_revenue))
print("Average Change: $" + str(average_monthly_change))
print("Greatest Increase in Profits: " + largest_increase_month + " ($" + str(largest_increase) +")")
print("Greatest Decrease in Profits: " + largest_decrease_month + " ($" + str(largest_decrease) +")")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(len(month))+ "\n")
    text.write("    Total Profits: " + "$" + str(total_revenue) +"\n")
    text.write("    Average Change: " + '$' + str((average_monthly_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(largest_increase_month) + " ($" + str(largest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(largest_decrease_month) + " ($" + str(largest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")



