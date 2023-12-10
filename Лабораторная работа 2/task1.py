money_capital = int(input())
salary = int(input())
spend = int(input())
increase = 0.05
months = 0
budget = money_capital+salary
while budget >= spend:
    budget -= spend
    months += 1
    spend += spend*increase
    budget += salary
print(months)