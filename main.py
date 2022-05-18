import matplotlib.pyplot as plt
from numpy import linspace
import tkinter as tk

def lerp(prev_y, final_y, diapason):
    return prev_y + (final_y - prev_y) * diapason

def createOXY():
    fig, ax = plt.subplots()
    plt.title("Линейная интерполяция")
    s = textBox.get()
    A, B, diapason = [ float(num) for num in s.split() ]
    interpolation, t, elem, cnt = [A,], [0,], A, 1
    while elem <= B * (1 - 0.0001):
        elem = lerp(elem, B, diapason)
        interpolation.append(elem)
        t.append(cnt)
        cnt += 1
    ax = ax.plot(t, interpolation)
    plt.show()

root = tk.Tk()
root.title("Введите начальное и конечное значение")
root.minsize(400, 1)

textBox = tk.Entry(root, font='Arial 14')
textBox.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
btn = tk.Button(root, text="Получить график", font='Arial 14', command=createOXY)
btn.grid(row=1, column=0, padx=5, pady=5, sticky='we')
root.mainloop()
