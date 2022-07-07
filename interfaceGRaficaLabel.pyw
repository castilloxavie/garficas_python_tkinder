from tkinter import *
root=Tk()

miframe=Frame(root, width=500, height=400)
miframe.pack()

miimg=PhotoImage(file=R"C:\Users\Xavier\Desktop\SQL\python-php-javascript-htmlcss\PYTHON\codigo_python\graficos\pelea.gif")
Label( miframe, image=miimg).place(x=300, y=200)
#Label(miframe, text="hl word of python", fg="blue", font=("Comic Sans Ms", 18)).place(x=100, y=200)# el (label)sirve para ingresar texto e imagenes 

root.mainloop()