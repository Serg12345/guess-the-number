from tkinter import *
from random import randint

window = Tk() # Создаём объект window класса Tk()

window.title('Угадай число. Версия 1.0') # Название программы, отображается в верхней части программы
window.geometry('400x240+600+300') # Задаём размеры программе и её расположение на экране
window.resizable(False, False) # Фиксируем размеры программы
window.config(bg = 'green') # Фон окна программы


# Генерируем случайное целое число в диапазоне от 0 до 100
range_number = randint(0, 100)
# print(range_number)

# Функция delete() очищает поле ввода, вызывается при нажатии кнопки Очистить
def delete():
	entry_number.delete(0, END)

# Функция start() Сохраняет введённое число и сравнивает с числом программы. Выводит результат сравнения
def start():
	number = entry_number.get() # Метод get() возвращает введённое число, которое сохраняется в переменной number
	if number == '':
		label_result['text'] = 'Введите ваше число!'
	elif int(number) == range_number:
		label_result['text'] = f'Верно! Число {number}'
	elif int(number) < range_number:
		label_result['text'] = 'Ваше число меньше!'
	else:
		label_result['text'] = 'Ваше число больше!'


# Угадай число от 0 до 100
label_name = Label(window, text = 'Угадай число от 0 до 100', bg = 'green', padx = 10, pady = 10, fg = 'white', font = '"Comic Sans MS" 15 bold')


# Ввод целого числа
frame_number = Frame(window)

label_number_text = Label(frame_number, text = 'Введите целое число', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
entry_number = Entry(frame_number, bd = 5, width = 4, font = '"Comic Sans MS" 10 bold')

label_number_text.pack(side = LEFT)
entry_number.pack(side = LEFT, padx = 5, pady = 5)

# Результат в виде текста
label_result = Label(window, text = '', bg = 'green', fg = 'white', padx = 5, pady = 5, font = '"Comic Sans MS" 15 bold')


# Кнопки СТАРТ, Очистить
frame_start = Frame(window, bg = 'green')


button_start = Button(frame_start, text = 'СТАРТ', command = start, bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
button_clear = Button(frame_start, text = 'Очистить', command = delete, bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')

button_start.pack(side = LEFT, padx = 5, pady = 5)
button_clear.pack(side = LEFT, padx = 5, pady = 5)

# Контакты для связи
label_email = Label(window, text = 'Email для связи: sergzxq@gmail.com', bg = 'green', fg = '#e2e2e2', font = 'Arial 10')

label_name.pack()
frame_number.pack()
label_result.pack()
frame_start.pack(padx = 10, pady = 10)
label_email.pack(side = LEFT)

window.mainloop()