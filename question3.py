# Daily sales data
daily_sales = [150, 200, 180, 220, 170, 190, 210]

# 1. Calculate the total sales for the week
total_sales = sum(daily_sales)
print("Total sales for the week:", total_sales)

# 2. Calculate the average sales per day
average_sales = total_sales / len(daily_sales)
print("Average sales per day:", average_sales)

# 3. Identify the day with the highest sales and print the sales amount
max_sales = max(daily_sales)
max_sales_day = daily_sales.index(max_sales) + 1
print("Highest sales:", max_sales, "on day", max_sales_day)

# 4. Determine the days where the sales were above the average sales
above_average_days = [day for day, sale in enumerate(daily_sales, start=1) if sale > average_sales]
print("Days with sales above average:", above_average_days)

# 5. Increase the sales amount of each day by 10% and print the updated sales list
updated_sales = [sale * 1.1 for sale in daily_sales]
print("Updated sales list:", updated_sales)