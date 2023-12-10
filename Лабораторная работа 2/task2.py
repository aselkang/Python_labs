money_capital = 0
salary = int(input())
spend = int(input())
increase = 0.03
months = 10
for i in range(10):
    money_capital += spend-salary
    spend += increase*spend
print(money_capital)