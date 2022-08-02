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

label_name.pack()
frame_range.pack()
button_range.pack(padx = 10, pady = 10)

window.mainloop()