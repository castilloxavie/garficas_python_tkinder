from tkinter import *
from tkinter import messagebox #libreria para crear las ventanas emergentes
# ventanas emergentes
rootRaiz= Tk()

#----------- funcion para las ventana emergentes------------
def inforAdicional():
    messagebox.showinfo("procesdor xavier", "procesador de textos 2022")
    # la funcion del metodo (messagebox.showinfo) sirve para mostrar una ventana de informacion
    
#modificacion de la ventana emergente
def avisoLicencia():
    messagebox.showwarning("licencias", "licencia de codigo abierto")
    # la funcion del metodo (messagebox.showwarning) sirve para mostrar una ventana de error

def salirPrograma():
    valor=messagebox.askquestion("salir", "desea salir del programa")
    # la funcion del metodo (messagebox.askquestion) sirve para mostrar una ventana de 

    if valor=="yes":
        rootRaiz.destroy() # el metodo(destroy)sirve para cerrar automaticamente el programa  q esta en ejecucuion
        
def cerrarVentan():
    valor1=messagebox.askokcancel("caerrar la ventana", "¿estas seguro(a) q quieres cerrar la ventana?")
    # la funcion del metodo (messagebox.askokcancel) sirve para mostrar si decea aceptaro cancelar el cierre  del programa

    if valor1==True:
        rootRaiz.destroy()
        
def prueDocumento():
    valor2=messagebox.askretrycancel("Reintentar","no es posible cerrar el documento: EL DOCUMENTO SE ENCUENTRA EN USO")
    # la funcion del metodo (messagebox.askretrycancel) sirve para advertir cuando no se puede cerrar un archivo  y sale reintentar.

    if valor2==False:
        rootRaiz.destroy()
        
barraMenu=Menu(rootRaiz)
rootRaiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)  
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() 
archivoMenu.add_command(label="Cerrar", command=cerrarVentan)
archivoMenu.add_command(label="Salir", command=salirPrograma)


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")


archivoHerramienta=Menu(barraMenu, tearoff=0)
archivoHerramienta.add_command(label="Buscar")
archivoHerramienta.add_command(label="Prueba para documento", command=prueDocumento)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=inforAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #el metodo (add_cascade)sirve para agrebar los elementos del munu y tambien para agregar a cada elemento el submenu
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

rootRaiz.mainloop()