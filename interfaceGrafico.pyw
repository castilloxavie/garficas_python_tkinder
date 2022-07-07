from tkinter import *
# la raiz es la estructura donde colocamos los frames (los frames es papel donde vamos a dibujar) y los widget (es lo q se dibuja en el lienzo)
# la extencion pyw basicamente sirve para cuando uno va a brir directamente desde donde tiene guardado el archivo_texto
# esto permite q cuando uno lo baya abrir no abra la consola y luego si el aplicativo.


raiz=Tk()
raiz.title("ventana de prueba") # colocar titulo (title)
#raiz.resizable(True,True) # la (resizable) sirve para dar personalizacion al ancho y alto de la ventana
raiz.iconbitmap(r"C:\\Users\\Xavier\\Desktop\\SQL\\python-php-javascript-htmlcss\\PYTHON\codigo_python\\graficos\\prueba.ico") # la palabra reservada  (iconbitmap) sirve para cambiar la imagen predeterminada de la interface  de py
#raiz.geometry("650x400") # la palabra (geometry)sirve para estandarizar lo ancho y lo alto
raiz.config(bg="red")# la palabra (config)sirve para configurar el color de fondo con (bg)
raiz.config(bd=28)
raiz.config(relief="groove")
raiz.config(cursor="trek")

miframe=Frame() # la pañabra (frame)serve para empaquetar y colocar la hoja o lienzo en la raiz o estructura principal.
#miframe.pack( side="left", anchor="n") # caca con (pack) podemos pasar parametros como ubicacion( side y ancher) son dos palabras q nos ayudaran a colocar con presicion la ubicacion de lo q usted  quiere dentro del lienzo o papel no en la raiz o  estructura principal.
#miframe.pack(fill="both", expand=True) # tambien con (pack) se puede trabajar  como (both) que sirve para expanadir todo el lienzo sobre la raiz con ayuda de la palabra reservada (expand)
miframe.pack()
miframe.config(bg="green")
miframe.config(width="650", height="400")
miframe.config(bd=35) # la configracion de borde (bd)
miframe.config(relief="groove")# forma de borde (relief)
miframe.config(cursor="pirate")

raiz.mainloop() # es para ejecutar la ventana (mainloop) es un ciclo infinito tambien

# tipo de cursores cursors 
        #"arrow",  flecha
        #"circle", circulo
        #"clock",  reloj
        #"cross", cruzar
        #"dotbox", dotbox
        #"exchange", intercambiar
        #"fleur", fluer
        #"heart", corazon
        #"man", hombre
        #"mouse", raton
        #"pirate", pirata
        #"plus", mas
        #"shuttle", lanzadera
        #"sizing", dimencionamiento
        #"spider", araña
        #"spraycan", lata de aerosol
        #"star", estrella 
        #"target", obgetivo
        #"tcross", tcross
        #"trek"emigrar

  