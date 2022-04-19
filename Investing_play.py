money = 1000
daily_profit_procent = 7
spektrum_day = 7


for i in range(spektrum_day):
     extra_money = float((money*daily_profit_procent)/100)
     money = float(money+extra_money)

print(money, end="$")