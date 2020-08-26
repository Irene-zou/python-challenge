import os
import csv
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

month_year = []
profit = []
difference = []
average_changes =[]

with open(csvpath) as financial_data:
    csvreader = csv.reader(financial_data, delimiter=',')
    
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for column in csvreader:
        month_year.append(column[0])
        profit.append(int(column[1]))

    print("Financial_Analysis")
    print("____________________")


    Total_Months = (len(month_year))
    print (f"Total Months: {Total_Months}")

    Total_Profits = sum(profit)
    print(f"Total Profits = ${Total_Profits}")

    for column in range (0,len(profit)-1):
        difference.append(int(profit[column+1])-int(profit[column]))
        average_changes = sum(difference)/len(difference)
    
    print(f"Average Change: (${average_changes})")

    Greatest_positive_change =max(difference)
    Greatest_negative_change =min(difference)

    Greatest_increase_month = month_year[difference.index(Greatest_positive_change)+ 1]
    Greatest_decrease_month = month_year[difference.index(Greatest_negative_change)+ 1]
    print(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    print(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")

    output_path = os.path.join('PyBank','analysis','Financia_Analysis.txt')
    with open(output_path,'w') as txtfile:
        txtfile.write(f"Total Month:{Total_Months}")
        txtfile.write(f"\nTotal: ${Total_Profits}")
        txtfile.write(f"\nAverage Change: ${average_changes}")
        txtfile.write(f"\nGreatest Increase in Profits:{Greatest_decrease_month}(${Greatest_negative_change})")
        txtfile.write(f"\nGreatest Decrese in Profits :{Greatest_decrease_month}(${Greatest_negative_change})")
        txtfile.close()