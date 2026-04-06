import pandas as pd


df = pd.read_csv('orders.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])


df['TotalAmount'] = df['Quantity'] * df['Price']

print("----------------ЗАВДАННЯ 3-------------------")
print(f"a. Сумарний дохід: {df['TotalAmount'].sum()}")
print(f"b. Середнє значення TotalAmount: {df['TotalAmount'].mean()}")
print("c. Кількість замовлень по клієнтах:")
print(df['Customer'].value_counts())

print("\n------------------ЗАВДАННЯ 4 (Сума > 500)--------------------")
print(df[df['TotalAmount'] > 500])

print("\n-------------------------ЗАВДАННЯ 5 (Сортування за датою)----------------")
print(df.sort_values(by='OrderDate', ascending=False))

print("\n-----------------------ЗАВДАННЯ 6 (З 5 по 10 червня)------------------")
print(df[(df['OrderDate'] >= '2023-06-05') & (df['OrderDate'] <= '2023-06-10')])

print("\n--------------------ЗАВДАННЯ 7 (Групування за категоріями)----------------")
grouped = df.groupby('Category').agg({'Quantity': 'sum', 'TotalAmount': 'sum'})
print(grouped)

print("\n---------------------ЗАВДАННЯ 8 (ТОП-3 клієнтів)--------------------")
print(df.groupby('Customer')['TotalAmount'].sum().sort_values(ascending=False).head(3))