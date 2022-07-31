from tkinter import *

window = Tk()

window.title('Программа')
window.config(bg = 'green')

# Название программы
label_name = Label(window, text = 'Угадай число', bg = 'green', padx = 10, pady = 10, fg = 'white', font = '"Comic Sans MS" 15 bold')

label_name.pack()

window.mainloop()