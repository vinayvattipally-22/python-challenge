import os
import csv
import locale


# Path to collect data from the Resources folder
CSV_PATH = os.path.join("Resources", "budget_data.csv")
PROFIT_INDEX = 1

data=[]
# Using python library locale for formating currency
locale.setlocale( locale.LC_ALL, '' )

# Setting default values
months_count = 0
total = 0   
total_change = 0

# Opening a csvfile
with open(CSV_PATH) as f:
    headerline = next(f)
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    
    prev_profit = data[0][1]
    

    profit_var = int(data[0][1])
    loss_var = int(data[0][1])
    
    max_profit = []
    min_profit = []     

    # Computing min_profit and max_profit using a for loop
    for i in range(len(data)):
        if(int(data[i][1])>=profit_var):
            profit_var = int(data[i][1])
        
            max_profit = data[i]
            

        if(int(data[i][1])<=loss_var):
            loss_var = int(data[i][1])
    
            min_profit = data[i]
    

    for i in data:
    
        months_count += 1
        current_profit = int(i[PROFIT_INDEX])
    
        total += current_profit
        current_change = current_profit - int(prev_profit)
        total_change += current_change
        #prepare for next row
        prev_profit = current_profit
    
average_change = total_change/(months_count-1)

# Displaying the output
print(average_change)

print("Financial Analysis")
       
print(f'Total number of months: {months_count}')
    
print(f'Total: {locale.currency(total)}')

print(f'Average change: {locale.currency(average_change)}')

print(f'Greatest Increase in Profits: {max_profit[0] + " " +locale.currency(int(max_profit[1]))}')

print(f'Greatest Decrease in Profits: {min_profit[0] + " " + locale.currency(int(min_profit[1]))}')

# Declaring an output path
output_path = os.path.join("analysis", "Financial_analysis.txt")

# Creating an output file using "write" mode.
with open(output_path, "w") as f:
    print("Financial Analysis\n", file = f)
    print("-----------------------------------------",file = f)
    
    print(f'\nTotal number of months: {months_count}\n', file=f)
    
    print(f'Total: {locale.currency(total)}\n', file=f)

    print(f'Average change: {average_change}\n', file=f)

    print(f'Greatest Increase in Profits: {max_profit[0] + " " +locale.currency(int(max_profit[1]))}\n', file=f)

    print(f'Greatest Decrease in Profits: {min_profit[0] + " " + locale.currency(int(min_profit[1]))}\n', file=f)

