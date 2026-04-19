import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("./fuel_consumption_1000.csv")

X = df[['speed_kmh']] 
Y = df['fuel_consumption_l_per_100km']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

degree = 3
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(X_train, Y_train)
y_pred = model.predict(X_test) 


X_plot = pd.DataFrame({'speed_kmh': np.linspace(X['speed_kmh'].min(), X['speed_kmh'].max(), 100)})
y_plot = model.predict(X_plot)


plt.scatter(X_test, Y_test, color='blue', alpha=0.5, label='Реальні дані (Тест)')
plt.plot(X_plot['speed_kmh'], y_plot, label=f'Прогноз (Поліном {degree} ст.)', color='red', linewidth=3)
plt.xlabel('Швидкість (км/год)')
plt.ylabel('Витрата палива (л/100км)')
plt.title('Реальна витрата палива vs Прогноз моделі')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

my_speed = pd.DataFrame({'speed_kmh': [100]}) 
predicted_value = model.predict(my_speed)
print(f"Прогноз при швидкості 100 км/год: {predicted_value[0]:.2f} л/100км")


mae = mean_absolute_error(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.4f} літра") 
print(f"Mean Squared Error (MSE): {mse:.4f}")