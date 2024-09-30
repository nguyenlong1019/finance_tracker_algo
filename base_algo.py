spending = {
    'Bill': 250,
    'Food': 300,
    'Entertainment': 150,
    'Shopping': 200,
    'Save': 100,
}

save_target = 200 

decrement_spend = save_target - spending['Save'] 

unnecessary = ['Entertainment', 'Shopping']

unnecessary = sorted(unnecessary, key=lambda x: spending[x], reverse=True) 

for category in unnecessary:
    if decrement_spend <= 0:
        break

    down = min(spending[category], decrement_spend)
    spending[category] -= down 
    decrement_spend -= down 


spending['Save'] += (save_target - spending['Save']) 

print('Solution recommendation: ')
for category, money in spending.items():
    print(f"{category}: {money} $")
