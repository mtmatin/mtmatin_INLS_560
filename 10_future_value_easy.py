future_value = 30000

rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money will grow: '))
present_value = future_value / (1.0 + rate)**years

print('You will need to deposit this amount:', present_value)