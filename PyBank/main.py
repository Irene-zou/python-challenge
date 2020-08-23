import os
import csv
csvpath = os.path.join('..','Resouces','budget_data.csv')

month_year = []
profit = []
difference = []
average_changes =[]

with open(csvpath) as cvsfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for column in csvreader:
        month_year.append(column[0])
        profits.append(column[1])

    print("Financial Analysis")
    print("____________________")

    Total_Months = (len(month_year))
    print (f"Total Months: {Total_Months}")

    Total_Profits = (sum(profits))
    print(f"Total profits = ${Total_profits}")

    for column in range (0,len(profits)-1):
        difference.append(int(profit[column+1])-int(profits[column]))
        average_changes = sum(difference)/len(difference)
    
    print(f"Average Change: (${average_changes})")

    Greatest_positive_change =max(difference)
    Greatest_negatice_change =min(difference)

    Greatest_increase_month = month_year[difference.index(Greatest_positive_change)+ 1]
    Greatest_decrease_month = month_year[difference.index(Greatest_negative_change)+ 1]
    print(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    print(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")

    output_path = os.path.join("Financia_Analysis.txt")
    with open(output_path,'w') as txtfile:
        txtfile.write(f"Total Month:{Total_Months}")
        txtfile.write(f"Total: ${Total_Profits}")
        txtfile.write(f"Average Change: ${average_changes_1}")
        txtfile.write(f"Greatest Increase in Profits:{Greatest_decrease_month}(${Greatest_negatice_change})")
        txtfile.write(f"Greatest Decrese in Profits :{Greatest_decrease_month}(${Greatest_negatice_change})")
        txtfile.close()