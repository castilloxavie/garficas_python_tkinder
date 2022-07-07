from tkinter import *
#botones de radio
#debemos de realizae una variable  dodne se le adjudican o se asigana (Intvar()) y en el boton se coloca las caracteristicas q se pueden observar en el ejemplo de la linea 6 y 7 (variable=varopcion, value=1)esro nos sive para la funcianalidad correcta
root=Tk()
varopcion=IntVar()

def imprimir(): # con esta funcion lo q hacemos es rescatar el valor de q se a establecido en el radio bottun.
    #print(varopcion.get())
    if varopcion.get()==1:
      etiqueta.config(text="Masculino.")
    elif varopcion.get()==2:
        etiqueta.config(text="Femenino.")  
    else:
        etiqueta.config(text="Otras Opciones.")

Label(root, text="Genero: ").pack()
Radiobutton(root, text="Maculino", variable=varopcion, value=1, command=imprimir).pack() #con la palabra reservada (Radiobutton) sirve para hacer botones de radio
Radiobutton(root, text="Femenino", variable=varopcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otras Opciones", variable=varopcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()



root.mainloop()