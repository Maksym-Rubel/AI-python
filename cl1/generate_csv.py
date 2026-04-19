import csv
import random

# Кількість рядків
num_rows = 5000

with open('fuel_consumption_1000.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['speed_kmh', 'fuel_consumption_l_per_100km'])
    
    for _ in range(num_rows):
        # Генеруємо випадкову швидкість від 20 до 130 км/год
        speed = round(random.uniform(20.0, 130.0), 1)
        
        # Базова математична модель на основі ваших даних (парабола)
        # Мінімум витрат (6.3 л) досягається приблизно на 65 км/год
        base_consumption = 0.00133 * ((speed - 65) ** 2) + 6.3
        
        # Додаємо трохи випадкового "шуму" (-0.4 до +0.4 л), щоб дані були реалістичними
        noise = random.uniform(-0.4, 0.4)
        consumption = round(base_consumption + noise, 1)
        
        writer.writerow([speed, consumption])

print("Файл 'fuel_consumption_1000.csv' успішно згенеровано на 1000 рядків!")