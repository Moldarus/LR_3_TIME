import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
passengers = pd.read_csv('passengers.csv', parse_dates=['Month'], index_col='Month')
passengers2 = pd.read_csv('passengers2.csv', parse_dates=['Month'], index_col='Month')

# Заполнение пропусков в passengers2.csv с использованием интерполяции
passengers2['target'] = passengers2['target'].interpolate()

# 1. Описание годовой сезонности (график и словесное описание)
passengers['Year'] = passengers.index.year
passengers['Month_Column'] = passengers.index.month
seasonality = passengers.groupby('Month_Column')['#Passengers'].mean()

plt.figure(figsize=(10, 6))
seasonality.plot(kind='line')
plt.title('Годовая сезонность')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество пассажиров')
plt.grid(True)
plt.show()

# Словесное описание годовой сезонности
print("Годовая сезонность показывает, что количество пассажиров увеличивается в летние месяцы и снижается в зимние месяцы.")

# 2. Исследование данных по отдельному месяцу
# а) январь по разным годам
january_data = passengers[passengers.index.month == 1]['#Passengers']
plt.figure(figsize=(10, 6))
january_data.plot(kind='line')
plt.title('Количество пассажиров в январе по годам')
plt.xlabel('Год')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()

# б) июль по разным годам
july_data = passengers[passengers.index.month == 7]['#Passengers']
plt.figure(figsize=(10, 6))
july_data.plot(kind='line')
plt.title('Количество пассажиров в июле по годам')
plt.xlabel('Год')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()

#Сравнение количесвта пассажиров в январе и июле по годам
print('Сравнивая два графика изменения пассажиропотока изменения по двум разным месяцам с упором на года, можно заметить что они оба показывают повышения пассажиропотока, но в июле он происходил более плавным и стабильным когда в январе, он был не плавным повышением но таж же возрастал')
# Среднее и дисперсия по данным внутри каждого года
yearly_mean = passengers.groupby('Year')['#Passengers'].mean()
yearly_var = passengers.groupby('Year')['#Passengers'].var()

print("Среднее количество пассажиров по годам:\n", yearly_mean)
print("Дисперсия количества пассажиров по годам:\n", yearly_var)

# а) Абсолютные разности по данным (между соседними месяцами)
passengers['Absolute Difference'] = passengers['#Passengers'].diff()
plt.figure(figsize=(10, 6))
passengers['Absolute Difference'].plot(kind='line')
plt.title('Абсолютные разности по данным')
plt.xlabel('Дата')
plt.ylabel('Абсолютная разность')
plt.grid(True)
plt.show()

#Описание рафика Абсалютной разницы по данным
print('Изучив график можно заметить как с момента начала но момента окончания записей о абсолютной разнице можно заметить насколько сильно увеличился разброс разностей. Увелечение аплитуды можно связвть с двумя факторами, первое это увелечение пассажиропотока а второй это сезонность, где пассажиропоток влияет на размер а сезонность на спад или повышения абсолютной разности')

# б) Относительные разности (в % прироста)
passengers['Relative Difference'] = passengers['#Passengers'].pct_change() * 100
plt.figure(figsize=(10, 6))
passengers['Relative Difference'].plot(kind='line')
plt.title('Относительные разности (в % прироста)')
plt.xlabel('Дата')
plt.ylabel('Относительная разность (%)')
plt.grid(True)
plt.show()

#Опсиание Относительной
print('Изучив график можно заметить, что тееория о сезонности подтверждается, так как если сравнить годовую сезонность среднего пассажиропотока, можно заметить ту самую  зависимость')

# а) Понижение частоты дискретизации до года (квартала)
yearly_data = passengers['#Passengers'].resample('Y').sum()
quarterly_data = passengers['#Passengers'].resample('Q').sum()

plt.figure(figsize=(10, 6))
yearly_data.plot(kind='line')
plt.title('Годовая дискретизация')
plt.xlabel('Год')
plt.ylabel('Суммарное количество пассажиров')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
quarterly_data.plot(kind='line')
plt.title('Квартальная дискретизация')
plt.xlabel('Квартал')
plt.ylabel('Суммарное количество пассажиров')
plt.grid(True)
plt.show()

#Описание графиков годовой а так же квартальной дескретизации
print('Сравнивая два графика годовой а так же квартальной дескретизации, можно так же заметить что пассажиропоток постоянно возрастал имея одинаковую сезонную изменчивость')

# б) Повышение частоты дискретизации до дня (недели)
# Для повышения частоты дискретизации до дня или недели, данные должны быть доступны в соответствующем формате
# В данном случае, это нецелесообразно, так как данные предоставлены в месячном формате

# (*) Выполнение заданий 1-5 для неполного датасета passengers2.csv
# Повторяем аналогичные шаги для passengers2

# 1. Описание годовой сезонности (график и словесное описание)
passengers2['Year'] = passengers2.index.year
passengers2['Month_Column'] = passengers2.index.month
seasonality2 = passengers2.groupby('Month_Column')['target'].mean()

plt.figure(figsize=(10, 6))
seasonality2.plot(kind='line')
plt.title('Годовая сезонность (восполненные данные)')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество пассажиров')
plt.grid(True)
plt.show()

# Словесное описание годовой сезонности для восполненных данных
print("Годовая сезонность для восполненных данных показывает, что количество пассажиров увеличивается в летние месяцы и снижается в зимние месяцы.")

# 2. Исследование данных по отдельному месяцу
# а) январь по разным годам
january_data = passengers[passengers.index.month == 1]
plt.figure(figsize=(10, 6))
plt.plot(january_data.index.year, january_data['#Passengers'], marker='o')
plt.title('Количество пассажиров в январе по годам')
plt.xlabel('Год')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()

# б) июль по разным годам
july_data = passengers[passengers.index.month == 7]
plt.figure(figsize=(10, 6))
plt.plot(july_data.index.year, july_data['#Passengers'], marker='o')
plt.title('Количество пассажиров в июле по годам')
plt.xlabel('Год')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()

# Среднее и дисперсия по данным внутри каждого года
yearly_mean2 = passengers2.groupby('Year')['target'].mean()
yearly_var2 = passengers2.groupby('Year')['target'].var()

print("Среднее количество пассажиров по годам (восполненные данные):\n", yearly_mean2)
print("Дисперсия количества пассажиров по годам (восполненные данные):\n", yearly_var2)

# а) Абсолютные разности по данным (между соседними месяцами)
passengers2['Absolute Difference'] = passengers2['target'].diff()
plt.figure(figsize=(10, 6))
passengers2['Absolute Difference'].plot(kind='line')
plt.title('Абсолютные разности по данным (восполненные данные)')
plt.xlabel('Дата')
plt.ylabel('Абсолютная разность')
plt.grid(True)
plt.show()

# б) Относительные разности (в % прироста)
passengers2['Relative Difference'] = passengers2['target'].pct_change() * 100
plt.figure(figsize=(10, 6))
passengers2['Relative Difference'].plot(kind='line')
plt.title('Относительные разности (в % прироста) (восполненные данные)')
plt.xlabel('Дата')
plt.ylabel('Относительная разность (%)')
plt.grid(True)
plt.show()

# а) Понижение частоты дискретизации до года (квартала)
yearly_data2 = passengers2['target'].resample('Y').sum()
quarterly_data2 = passengers2['target'].resample('Q').sum()

plt.figure(figsize=(10, 6))
yearly_data2.plot(kind='line')
plt.title('Годовая дискретизация (восполненные данные)')
plt.xlabel('Год')
plt.ylabel('Суммарное количество пассажиров')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
quarterly_data2.plot(kind='line')
plt.title('Квартальная дискретизация (восполненные данные)')
plt.xlabel('Квартал')
plt.ylabel('Суммарное количество пассажиров')
plt.grid(True)
plt.show()

# Сравнение результатов исследований
print("Результаты исследований для полных и восполненных данных показывают схожие тенденции, но могут быть небольшие различия из-за интерполяции пропущенных значений.")
