conversion = 1.38
yearly = int(input('desired yearly amount: '))
wage = int(input('current hourly wage in USD: '))
# daily_hours = int(input('hours work per day: '))
days_per_week = int(input('days worked per: '))
monthly = wage * daily_hours * 4
print(f'USD: ${monthly} CAD: ${monthly*conversion}')
