monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input('Enter your total monthly expenses: '))

#calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculating projected savings
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#display projected annual and monthly savings
print(f'Your monthly savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')

