Original_amount = float(input('Enter the shopping amount :'))

if Original_amount > 100:
    final_price = Original_amount-(Original_amount*0.1)
elif Original_amount < 100:
    final_price = Original_amount-(Original_amount*0.1)

print('final_price:', final_price)
