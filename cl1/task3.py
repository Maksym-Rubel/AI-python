import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("./electricity_consumption.csv")


X = df[['temperature','humidity','hour','is_weekend']] 
y = df['consumption']         

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


my_electricity_consumption = pd.DataFrame({'temperature': [25], 'humidity': [60], 'hour': [12], 'is_weekend': [0]})
predicted_consumption = model.predict(my_electricity_consumption)
print(f"Прогнозований витрата електроенергії при температурі 25°C: {predicted_consumption[0]:.2f} кВт·год")


y_pred = model.predict(X_test)

mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(f"MAPE: {mape:.2f}")


plt.scatter(y_test, y_pred, color='blue', alpha=0.3)
plt.xlabel("Фактичне споживання електроенергії (кВт·год)")
plt.ylabel("Прогнозоване споживання електроенергії (кВт·год)")
plt.title("Оцінка моделі: Фактичне vs Прогнозоване споживання")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red')

plt.grid(True, linestyle='--', alpha=0.6)
plt.show()