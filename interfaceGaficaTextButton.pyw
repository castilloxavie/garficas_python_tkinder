from tkinter import *
raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre= Entry(miFrame, textvariable=minombre )# la plabara (Entry)sirve para crear cuadros de tecto en la interface grafica de py
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)  # con con el metodo (gid) lo q se hace es formar un tipo de tabal donde hay columnas y filas y hay podremos ubicar lo q queramos ya q ese grid a cada celda o cuadro se le puede dar las pociciones teniendo encuenta q se cuenta desde 0 tanto pra (row)o filas y para las (column) oculumnas.
cuadroNombre.config(fg="red", justify="center")
cuadroContrasena= Entry(miFrame)
cuadroContrasena.grid(row=1, column=1, padx=10, pady=10)
cuadroContrasena.config(show="*")

cuadroApellido= Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion= Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

nombrelabel=Label(miFrame, text="nombre:")
nombrelabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

contrasenalabel=Label(miFrame, text="pass:")
contrasenalabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=10)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
scrollvertical=Scrollbar(miFrame, command=textoComentario.yview)
scrollvertical.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollvertical.set)

apellidolabel=Label(miFrame, text="apellido:")
apellidolabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miFrame, text="direccion:")
direccionlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

# aca utilizamo  el metodo (text) para hacer comentarios extensos o un narea de texto
# el metodo (scrollbar) sirve para colocar la barra de scroll o mas conocido como la barrada de dezplasamiento de arriba abajo y se viceversa
# en la constrccion de la barra desplazamiento o scroll se debe hace con los parametros q se indican el la lineas 29 y 30 de este codigo
# se debe configurara para su funcionamiento  del scroll  como se realiza en la linea 31 el metodo (yscrollcommand) sirve para dar la forma de del scroll ariba abajo
# la palabra (button) sirve para agregar botones a lo q se esta realizando.
# el (StringVar) sirve para decir q es una acdena de cararcteres
# el (textvariable) sirve para asociar lo q se desea o enlasar nueva url
# el (set)es una funcion q se le coloca a una variable para obtener la informacion en un cuadro de texto

comentarioslabel=Label(miFrame, text="comentarios:")
comentarioslabel.grid(row=4, column=0, stick="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("xavier")

botonEnvios=Button(raiz, text="enviar", command=codigoBoton)
botonEnvios.pack()

raiz.mainloop() 
