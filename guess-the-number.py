from tkinter import *

window = Tk()

window.title('Программа')
window.config(bg = 'green')

# Название программы
label_name = Label(window, text = 'Угадай число', bg = 'green', padx = 10, pady = 10, fg = 'white', font = '"Comic Sans MS" 15 bold')

# Диапазон целых чисел
frame_range = Frame(window)

label_range_text = Label(frame_range, text = 'Задай диапазон целых чисел', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')

label_range_first = Label(frame_range, text = 'от', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
entry_range_first = Entry(frame_range, bd = 5, width = 4, font = '10')

label_range_second = Label(frame_range, text = 'до', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
entry_range_second = Entry(frame_range, bd = 5, width = 4, font = '10')

# Кнопка Принять диапазон
button_range = Button(window, text = 'Принять диапазон', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')

label_range_text.pack(side = LEFT)
label_range_first.pack(side = LEFT, padx = 5, pady = 5)
entry_range_first.pack(side = LEFT, padx = 5, pady = 5)
label_range_second.pack(side = LEFT, padx = 5, pady = 5)
entry_range_second.pack(side = LEFT, padx = 5, pady = 5)

# Виджеты для ввода числа
frame_number = Frame(window)

label_number_text = Label(frame_number, text = 'Введите ваше число', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
entry_number_text = Entry(frame_number, bd = 5, width = 4, font = '"Comic Sans MS" 10 bold')
button_number = Button(frame_number, text = 'Принять число', bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
button_number_clear = Button(frame_number, text = 'Очистить', bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')

label_number_text.pack(side = LEFT)
entry_number_text.pack(side = LEFT, padx = 5, pady = 5)
button_number.pack(side = LEFT, padx = 5, pady = 5)
button_number_clear.pack(side = LEFT, padx = 5, pady = 5)

# Результат Label верно или неверно, кнопки СТАРТ, Очистить
frame_start = Frame(window, bg = 'green')

label_result = Label(frame_start, text = '', bg = 'green', fg = 'white', padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
button_start = Button(frame_start, text = 'СТАРТ', bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')
button_clear = Button(frame_start, text = 'Очистить', bd = 5, padx = 5, pady = 5, font = '"Comic Sans MS" 10 bold')

label_result.pack(side = LEFT)
button_start.pack(side = LEFT, padx = 5, pady = 5)
button_clear.pack(side = LEFT, padx = 5, pady = 5)

# Контакты для связи
label_email = Label(window, text = 'Email для связи: sergzxq@gmail.com', bg = 'green', fg = '#e2e2e2', font = 'Arial 10')

label_name.pack()
frame_range.pack()
button_range.pack(padx = 10, pady = 10)
frame_number.pack()
frame_start.pack(padx = 10, pady = 10)
label_email.pack(side = LEFT)

window.mainloop()