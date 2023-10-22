price_bubblegum = float(2)
price_toffee = float(0.2)
price_ice_cream = float(5)
price_milk_chocolate = float(4)
price_doughnut = float(2.5)
price_pancake = float(3.2)

#print("Prices:")
#print("Bubblegum: $", price_bubblegum)
#print("Toffee: $", price_toffee)
#print("Ice cream: $", price_ice_cream)
#print("Milk chocolate: $", price_milk_chocolate)
#print("Doughnut: $", price_doughnut)
#print("Pancake: $", price_pancake)

profit_bubblegum = float(202)
profit_toffee = float(118)
profit_ice_cream = float(2250)
profit_milk_chocolate = float(1680)
profit_doughnut = float(1075)
profit_pancake = float(80)

print("Earned Amount:")
print("Bubblegum: $", profit_bubblegum)
print("Toffee: $", profit_toffee)
print("Ice cream: $", profit_ice_cream)
print("Milk chocolate: $", profit_milk_chocolate)
print("Doughnut: $", profit_doughnut)
print("Pancake: $", profit_pancake)

total_income = (profit_bubblegum
      + profit_toffee
      + profit_ice_cream
      + profit_milk_chocolate
      + profit_doughnut
      + profit_pancake)

print("Income: $", total_income)

staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))
total_expenses = staff_expenses + other_expenses

print("Net Income: $", (total_income - total_expenses))