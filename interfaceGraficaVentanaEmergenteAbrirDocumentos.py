from tkinter import *
from tkinter import filedialog # libreria para abrir archivos

rootRaiz=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetype=(("ficheros de excel", "*.xlsx"),("fecheros de texto", "*.txt"),("todos los ficheros", "*.*"))) # el metodo (initialdir) sirve para establecer en donde especificamente debe de abrir
    # el metodo (filetype) sirve para crear la tupla o tipo de archivo q deseas abrir 
    print(fichero)# este print nos va a permitirnen este momento la rutan de donde esta el documento
Button(rootRaiz, text="abrir fichero", command=abreFichero).pack()

rootRaiz.mainloop()