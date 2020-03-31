# Modules
import os
import csv

#variables
total_months = []
total_revenue = []
avg_change = 0
greatest_increase = 0
greatest_decrease = 0
revenue = 0
previous_revenue = 0
revenue_change = []
row = []


#Set path to file
budget_path = os.path.join("budget_data.csv")

#Read and open in csv file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)

#Loops
    for row in csvreader: 
        months.append(row[0])
        total_revenue.append(int(row[1]))
        monthly_change = int(row[1])- previous_revenue
        revenue_change.append(monthly_rev_change)
        if (monthly_change > greatest_increase):
            greatest_increase_month = row [0]
            greatest_increase = monthly_change
        elif (monthly_change < greatest_decrease):
             greatest_decrease_month = row [0]
             greatest_decrease = monthly_change
        previous_revenue = int(row[1])

        total_revenue_change =(sum(revenue_change))
        #avg_change = (total_revenue_change/(total_months))
        avg_change = total_change / len(rev_change)




#Print Financial Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total_revenue)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease})")

# Output files
output_file = Path("python-challenge", "PyBank", "Financial_Analys.txt")

with open(output_file,"w") as file:
    
#Print to Financial_Analysis
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
