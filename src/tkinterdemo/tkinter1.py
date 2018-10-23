import tkinter as tk
import turtle

top=tk.Tk()
top.title("Hello world")
top.geometry('400x200')

l = tk.Label(top,
    text='OMG! this is TK!',    # 标签的文字
    bg='green',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=15, height=2          # 标签长宽
    )
l.pack()    # 固定窗口位置

top.mainloop()