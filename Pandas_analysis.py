import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap
Coffee_Data = pd.read_csv("Coffee_sales.csv")

#Functions using pandas to calulate various metrics such as Total_Sales.


def total_sales():
    #Function adds up all the numbers in the money column, could also easily be done with sum() but I forgot lol
    Total_Sales = 0
    for sale in Coffee_Data["money"]:
        Total_Sales = Total_Sales + sale
    print(Total_Sales)

def item_with_highest_sales():
    #Calcultes the item with the highest amount of sales. I think this would be easier to do with .groupby(),
    # but i just discovered the method so i'm not 100% sure how to use it. Looks simple though.
    Highest_Sales = []
    All_Coffee_Names = Coffee_Data["coffee_name"].unique()
    for name in All_Coffee_Names:
        sum = Coffee_Data.query(f"coffee_name == '{name}'")["money"].sum()
        Highest_Sales.append(sum)
    Highest_Sales = max(Highest_Sales)
    for name in All_Coffee_Names:
        if Coffee_Data.query(f"coffee_name == '{name}'")["money"].sum() == Highest_Sales:
            print(f"{name} has the highest amount of sales with a total of {Highest_Sales}")
            break
        else:
            continue


def day_with_highest_sales():
    # reused the code from the earlier function pretty much, but I changed one of the columns accessed from coffee_name
    # to Weekday, i looked on chatgpt and it looks like all this code can be simplified alot by using groupby and idxmax
    # i definantly have to look into them.
    days = Coffee_Data["Weekday"].unique()
    Highest_day = []
    for day in days:
        sum = Coffee_Data.query(f"Weekday == '{day}'")["money"].sum()
        Highest_day.append(sum)
    Highest_day = max(Highest_day)
    for day in days:
        if Coffee_Data.query(f"Weekday == '{day}'")["money"].sum() == Highest_day:
            print(f"'{day}' is the day with the highest sales.")
            break
        else:
            continue

# Bar chart showing Highest sales vs different coffees

def bar_chart():
    Coffee_Names = Coffee_Data["coffee_name"].unique()
    print(Coffee_Names)
    amounts = []
    for name in Coffee_Names:
        amounts.append(Coffee_Data.query(f"coffee_name == '{name}'").shape[0])
    
    wrapped_text = ["\n".join(textwrap.wrap(label,10)) for label in Coffee_Names]
    plt.figure(figsize=(20,20))
    plt.bar(wrapped_text,amounts)
    plt.title("Bar chart")
    plt.xticks(rotation=90, fontsize = 7)
    plt.show()



bar_chart()
