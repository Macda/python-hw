# -*- coding: UTF-8 -*-
"""PyBank Homework."""


import csv
import os

load_data = os.path.join("Resources", "budget_data.csv")
output_data = os.path.join("analysis", "budget_analysis.txt")

tmonth = 0
month_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
total_net = 0

with open(load_data) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)


    first_row = next(reader)
    tmonth = tmonth + 1
    total_net = total_net + int(first_row[1])
    net_pre = int(first_row[1])

    for row in reader:

        tmonth = tmonth + 1
        total_net = total_net + int(row[1])


        net_change = int(row[1]) - net_pre
        net_pre = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]]

        
        if net_change > greatest_pincrease[1]:
            greatest_pincrease[0] = row[0]
            greatest_pincrease[1] = net_change

 
        if net_change < greatest_pdecrease[1]:
            greatest_pdecrease[0] = row[0]
            greatest_pdecrease[1] = net_change


monthly_avg = sum(net_change_list) / len(net_change_list)


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {tmonth}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${monthly_avg:.2f}\n"
    f"Greatest Profits Increase: {greatest_pincrease[0]} (${greatest_pincrease[1]})\n"
    f"Greatest Profits Decrease: {greatest_pdecrease[0]} (${greatest_pdecrease[1]})\n")

print(output)


with open(output_data, "w") as txt_file:
    txt_file.write(output)
