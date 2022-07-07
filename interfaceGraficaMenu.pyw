from tkinter import *

rootRaiz= Tk()

#configuracion de la barra de menu
barraMenu=Menu(rootRaiz)
rootRaiz.config(menu=barraMenu, width=300, height=300)

# la cantidiad de elementos  q lleba la barra del menu
archivoMenu=Menu(barraMenu, tearoff=0) # el metodo (tearoff) sirve prara quitar las lineas q trae por predertemidado el submenu. 
# agregar el submenu para los elementos q conforman el menu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() # el metodo (add_separator) nos sirve para mostar la separacion de las diferentes grupos q hay en un submenu.
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")


archivoHerramienta=Menu(barraMenu, tearoff=0)
archivoHerramienta.add_command(label="Buscar")


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")


#especificacion del menu para q se vea la barra en la interface grafica
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #el metodo (add_cascade)sirve para agrebar los elementos del munu y tambien para agregar a cada elemento el submenu
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

rootRaiz.mainloop()