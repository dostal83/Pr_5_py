# Обработка данных временных рядов
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # импорт библиотек

# Считывание исходника
def read_data(input_file): 
    input_data = np.loadtxt(input_file, delimiter = None)
    dates = pd.date_range('1950-01', periods = input_data.shape[0], freq = 'M') # Преобразование данных во временные ряды
    output = pd.Series(input_data[:, dates], index = dates) # создание врем. рядов
    return output


if __name__=='__main__': # Путь файла
    input_file = "/QQQ/pr/wow.txt"
    timeseries = read_data(input_file) # преобразование столбца
    
    # Визуал данных
    plt.figure()
    timeseries.plot()
    plt.show()
