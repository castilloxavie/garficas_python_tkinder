from tkinter import *

rootRaiz=Tk()
rootRaiz.title("ejemplo de lista de chequeo")

#-------------variables de funcionalidad---------------
playa=IntVar()
montalla=IntVar()
turismo=IntVar()

def opcionViaje():
    opcionesEscogidas=""
    
    if(playa.get()==1):
        opcionesEscogidas+= " playa"
    
    if(montalla.get()==1):
        opcionesEscogidas+= " montaña"
    
    if(turismo.get()==1):
        opcionesEscogidas+= " turismo Rural"
        
    textoFinal.config(text=opcionesEscogidas)

foto= PhotoImage(file=R"C:\\Users\\Xavier\\Desktop\\SQL\\python-php-javascript-htmlcss\\PYTHON\\codigo_python\\graficos\\avion.png")
Label(rootRaiz, image=foto).pack()

frame=Frame(rootRaiz)
frame.pack()

Label(frame, text="Elija destinos de vacacciones", width=50).pack()

Checkbutton(frame, text= "Paya", variable=playa, onvalue=1, offvalue=0, command=opcionViaje ).pack()
Checkbutton(frame, text= "Montaña", variable=montalla, onvalue=1, offvalue=0, command=opcionViaje ).pack()
Checkbutton(frame, text= "Turismo rural", variable=turismo, onvalue=1, offvalue=0, command=opcionViaje ).pack()

textoFinal=Label(frame)
textoFinal.pack()

rootRaiz.mainloop()