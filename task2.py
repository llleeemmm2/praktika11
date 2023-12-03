import numpy as np
import matplotlib.pyplot as plt

# Генерация данных для нормального распределения
mu, sigma = 0, 0.1  # среднее значение и стандартное отклонение
data = np.random.normal(mu, sigma, 1000)

# Отрисовка гистограммы нормального распределения
count, bins, ignored = plt.hist(data, 30, density=True, alpha=0.5, color='b', edgecolor='black')

# Добавление кривой плотности вероятности
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')

plt.title('Нормальное распределение')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')
plt.show()
