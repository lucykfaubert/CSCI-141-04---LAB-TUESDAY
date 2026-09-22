CONVERSION_RATES = [1.08, 1.21, 0.15, 0.012]
currency_names = ["EUR", "GBP", "CNY", "INR"]
FEE = float(0.05)
og_currency = int(input("Choose to convert to 1. EUR 2. GBP 3. CNY 4. INR: "))
amount = (input('Enter dollar amount to exchange: '))
amount1 = (amount[1:])
amount_with_fee = float(amount1) - (float(amount1) * FEE)
new_amount = round(amount_with_fee / CONVERSION_RATES[og_currency - 1],)
print("After fees you will receive", currency_names[og_currency - 1], new_amount)