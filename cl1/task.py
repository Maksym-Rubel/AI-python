import pandas as pd


df = pd.read_csv('orders.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])


df['TotalAmount'] = df['Quantity'] * df['Price']

print("----------------ЗАВДАННЯ 3-------------------")
print(f"  Сумарний дохід : {df['TotalAmount'].sum()}")
print(f"  Середнє  TotalAmount: {df['TotalAmount'].mean()}")
print(" Кількість замовлень по  клієнтах:")
print(df['Customer'].value_counts())

print("\n------------------ ЗАВДАННЯ 4--------------------")
print(df[df['TotalAmount'] > 500])

print("\n-------------------------ЗАВДАННЯ 5----------------")
print(df.sort_values(by='OrderDate', ascending=False))

print("\n----------------------- ЗАВДАННЯ 6------------------")
print(df[(df['OrderDate'] >= '2023-06-05') & (df['OrderDate'] <= '2023-06-10')])

print("\n--------------------ЗАВДАННЯ 7----------------")
grouped = df.groupby('Category').agg({'Quantity': 'sum', 'TotalAmount': 'sum'})
print(grouped)

print("\n---------------------ЗАВДАННЯ 8--------------------")
print(df.groupby('Customer')['TotalAmount'].sum().sort_values(ascending=False).head(3))