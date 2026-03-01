import re

# читаем чек
with open("raw.txt", encoding="utf-8") as f:
    text = f.read()

#  ищем названия товаров
products = re.findall(r'\d+\.\s*\n(.+)', text)

#  ищем цены
prices = re.findall(r'\d[\d\s]*,\d{2}', text)

#  ищем итоговую сумму
total = re.search(r'ИТОГО:\s*\n?([\d\s,]+)', text)

#  ищем дату и время
date_time = re.search(r'Время:\s*(.+)', text)

#  ищем способ оплаты
payment = re.search(r'Банковская карта', text)

print("PRODUCTS:")
for p in products:
    print("-", p)

print("\n PRICES:")
print(prices)

if total:
    print("\nTOTAL:", total.group(1))

if date_time:
    print("DATE & TIME:", date_time.group(1))

if payment:
    print("PAYMENT: Bank card")