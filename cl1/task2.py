import matplotlib.pyplot as plt
import numpy as np


#----------------Завдання 1----------------------
x = np.linspace(-10, 10, 500)
y = (x**2) * np.sin(x)

plt.plot(x, y)
plt.title("Графік функції sin(x)")
plt.xlabel("x")
plt.ylabel("x^2 * sin(x)")
plt.grid(True)
plt.show()


#----------------Завдання 2----------------------
data = np.random.normal(loc=5, scale=2, size=1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Гістограма розподілу")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.show()


#----------------Завдання 3----------------------
labels = ['Sleep', 'Code', 'Guitar', 'Eat']
sizes = [40, 30, 25, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Популярність мов програмування")
plt.axis('equal')
plt.show()


#----------------Завдання 4----------------------
apples = np.random.normal(loc=150, scale=15, size=100) 
bananas = np.random.normal(loc=120, scale=10, size=100) 
oranges = np.random.normal(loc=200, scale=20, size=100) 
peaches = np.random.normal(loc=130, scale=12, size=100)

data = [apples, bananas, oranges, peaches]
labels = ['Яблука', 'Банани', 'Апельсини', 'Персики']

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=labels)

plt.title("Діаграма розмаху (Box-plot) маси фруктів")
plt.xlabel("Тип фрукта")
plt.ylabel("Маса (у грамах)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#----------------Завдання 5----------------------
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, color='green',alpha=0.6)
plt.title("Точкова діаграма")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


#----------------Завдання 6----------------------
x = np.linspace(-10, 10, 500)
y = np.sin(x) 
x1 = np.linspace(-10, 10, 500)
y1 = np.cos(x)
x2 = np.linspace(-10, 10, 500)
y2 = np.sin(x) + np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0,color="red")
ax.plot(x1, y1, linewidth=2.0,color="blue")
ax.plot(x2, y2, linewidth=2.0,color="green")

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()