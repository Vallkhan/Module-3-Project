import os
import csv

with open(r'C:\Users\vallk\Desktop\Boot_Camp\Python\Repository\Module-3-Project\PyBank\Resources\budget_data.csv') as file:
    raw_data = csv.reader(file)
    header = next(raw_data)
        
    data = []
    for line in raw_data:
        data.append(line)    
          
dates = []   
for line in data:
    dates.append(line[0])    

profit = []
for line in data:
    profit.append(int(line[1])) 

change = []

for x in range(len(profit)):
   if profit[x] != profit[0]:
      change.append(profit[x] - profit[x-1])
      
total_months = len(dates) 
Total = sum(profit)   
Average_change = round(sum(change)/len(change),2)
max_profit = max(change) 
max_profit_date = dates[change.index(max_profit)+1]
min_profit = min(change)
min_profit_date = dates[change.index(min_profit)+1]

analysis_path = os.path.join(r'C:\Users\vallk\Desktop\Boot_Camp\Python\Repository\Module-3-Project\PyBank\analysis','Financial_Analysis.txt')

analysis = open('Financial_Analysis.txt','w')

analysis.write("\n"+"\n"+"Financial Analysis")
analysis.write("\n"+"\n"+"---------------------------")
analysis.write("\n"+"\n"+f"Total Months: {total_months}")
analysis.write("\n"+"\n"+f"Total: ${Total}")
analysis.write("\n"+"\n"+f"Average Change: ${Average_change}")
analysis.write("\n"+"\n"+f"Greatest Increase in Profits: {max_profit_date} (${max_profit})")
analysis.write("\n"+"\n"+f"Greatest Decrease in Profit: {min_profit_date} (${min_profit})")

analysis.close()