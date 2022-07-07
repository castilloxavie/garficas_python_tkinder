from tkinter import *
raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()


cuadroNombre= Entry(miFrame)# la plabara (Entry)sirve para crear cuadros de tecto en la interface grafica de py
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)  # con con el metodo (gid) lo q se hace es formar un tipo de tabal donde hay columnas y filas y hay podremos ubicar lo q queramos ya q ese grid a cada celda o cuadro se le puede dar las pociciones teniendo encuenta q se cuenta desde 0 tanto pra (row)o filas y para las (column) oculumnas.
cuadroNombre.config(fg="red", justify="center")
cuadroContrasena= Entry(miFrame)
cuadroContrasena.grid(row=1, column=1, padx=10, pady=10)
cuadroContrasena.config(show="*")

cuadroApellido= Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion= Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

# utilizando el metodo (sticky) nos permite cuadrarlo decuerto a los cuatros puntos cardinales ("n")norte, ("s")sur, ("e")este y ("w")oeste.
# tambien con puntos cardinales intermedio ("ne")nor este, ("se") sureste, ("sw")suroeste, (nw)noroeste
# el metodo (padx)sirve para dar un espacio entre izquierda y derecha y el (pady)sirve para dar un espacion ariba y abajo
# el metodo (fg) sirve para dar color a las letras
# el metodo (justify)ubicacion de las plabras  en este caso
# el metodo (show)sirve para cuando se debe de ocultar una contraseña o lo q ustedes deseen en su programa de py

nombrelabel=Label(miFrame, text="nombre:")
nombrelabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

contrasenalabel=Label(miFrame, text="pass:")
contrasenalabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)


apellidolabel=Label(miFrame, text="apellido:")
apellidolabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miFrame, text="direccion:")
direccionlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop() 

