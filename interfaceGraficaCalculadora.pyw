from tkinter import *

raiz=Tk()

miframe=Frame(raiz)
miframe.pack()
operacion=""
reset_pantalla= False
resultado=0

#------------pantalla de la calculadora-----------
numeroPantalla=StringVar()

pantalla=Entry(miframe, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=20, pady=20, columnspan=4) # el metodo (columnspan) sirve para dar el ancho deacuerdo a las columnas q se estan realizando mas abajo
pantalla.config(background="black", fg="#33FF5B", justify="right")

#------------pulsaciones de los botones-------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla= False # con esta funcio lo q estamos haciendo es q cada vez q uno oproma un caracter diferente a vacio vuelva y comience a escribir nuevamente
    else:
        numeroPantalla.set(numeroPantalla.get()+num) #  el metodo (get) sirve para mostara lo obtenido en panatalla y con el (+)concatenamos para poder repetirvarias veces el mismo numero

#-------------- funcion suma------------------------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=int(num)
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)
    
#-------------- funcion resta--------------------------
num1=0
contadorResta=0
def resta(num):
    global operacion
    global resultado
    global num1
    global contadorResta
    global reset_pantalla
    
    if contadorResta==0: 
        num1=int(num)
        resultado=num1
    else:
        if contadorResta==1: 
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)
            
        numeroPantalla.set(resultado)  
        resultado=numeroPantalla.get() 
        
    contadorResta=contadorResta+1
    operacion="resta"
    reset_pantalla=True
    
#-------------funcion multiplicacion---------------------
contadorMulti=0

def multiplica(num):
    global operacion
    global resultado
    global num1
    global contadorMulti
    global reset_pantalla
    
    if contadorMulti==0:
        num1=int(num)
        resultado=num1
    else:
        if contadorMulti==1:
           resultado=num1*int(num)
        else:
            resultado=int(resultado)*int(num)	

        numeroPantalla.set(resultado)		
        resultado=numeroPantalla.get()

    contadorMulti=contadorMulti+1
    operacion="multiplicacion"
    reset_pantalla=True
 
 #-----------------funcion division---------------------
contadorDivi=0

def divide(num):
	global operacion
	global resultado
	global num1
	global contadorDivi
	global reset_pantalla
	
	if contadorDivi==0:
		num1=float(num)		
		resultado=num1
	else:
		if contadorDivi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)
   	
		numeroPantalla.set(resultado)		
		resultado=numeroPantalla.get()
  
	contadorDivi=contadorDivi+1
	operacion="divide"
	reset_pantalla=True

#-------------- funcion total (=)-------------------
def total():
    global resultado
    global operacion
    global contadorResta
    global contadorDivi
    global contadorMulti
    
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(resultado-int(numeroPantalla.get()))
        resultado=0
        contadorResta=0 
    elif operacion=="multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado=0
        contadorMulti=0
    elif operacion=="divide":
        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
        resultado=0
        contadorDivi=0 
    
    

#------------fila 1 botone------------------
buton7=Button(miframe, text="7", width=4, command=lambda:numeroPulsado("7"))
buton7.grid(row=2, column=1)
buton7.config(background="Aquamarine", fg="#000000")

buton8=Button(miframe, text="8", width=4, command=lambda:numeroPulsado("8"))
buton8.grid(row=2, column=2)
buton8.config(background="Aquamarine", fg="#000000")


buton9=Button(miframe, text="9", width=4, command=lambda:numeroPulsado("9"))
buton9.grid(row=2, column=3)
buton9.config(background="Aquamarine", fg="#000000")


butonDividir=Button(miframe, text="/", width=4, command=lambda:divide(numeroPantalla.get()))
butonDividir.grid(row=2, column=4)
butonDividir.config(background="LightBlue", fg="#000000")


#------------fila 2 botone------------------
buton4=Button(miframe, text="4", width=4, command=lambda:numeroPulsado("4"))
buton4.grid(row=3, column=1)
buton4.config(background="Aquamarine", fg="#000000")

buton5=Button(miframe, text="5", width=4, command=lambda:numeroPulsado("5"))
buton5.grid(row=3, column=2)
buton5.config(background="Aquamarine", fg="#000000")

buton6=Button(miframe, text="6", width=4, command=lambda:numeroPulsado("6"))
buton6.grid(row=3, column=3)
buton6.config(background="Aquamarine", fg="#000000")

butonMultiplicar=Button(miframe, text="*", width=4, command=lambda:multiplica(numeroPantalla.get()))
butonMultiplicar.grid(row=3, column=4)
butonMultiplicar.config(background="LightBlue", fg="#000000")

#------------fila 3 botone------------------
buton1=Button(miframe, text="1", width=4, command=lambda:numeroPulsado("1"))
buton1.grid(row=4, column=1)
buton1.config(background="Aquamarine", fg="#000000")

buton2=Button(miframe, text="2", width=4, command=lambda:numeroPulsado("2"))
buton2.grid(row=4, column=2)
buton2.config(background="Aquamarine", fg="#000000")

buton3=Button(miframe, text="3", width=4, command=lambda:numeroPulsado("3"))
buton3.grid(row=4, column=3)
buton3.config(background="Aquamarine", fg="#000000")

butonResta=Button(miframe, text="-", width=4, command=lambda:resta(numeroPantalla.get()))
butonResta.grid(row=4, column=4)
butonResta.config(background="LightBlue", fg="#000000")

#------------fila 4 botone------------------
buton0=Button(miframe, text="0", width=4, command=lambda:numeroPulsado("0"))
buton0.grid(row=5, column=1)
buton0.config(background="Aquamarine", fg="#000000")

butonComa=Button(miframe, text=",", width=4, command=lambda:numeroPulsado("."))
butonComa.grid(row=5, column=2)
butonComa.config(background="Aquamarine", fg="#000000")

butonSuma=Button(miframe, text="+", width=4, command=lambda:suma(numeroPantalla.get()))
butonSuma.grid(row=5, column=3)
butonSuma.config(background="LightBlue", fg="#000000")

butonIgual=Button(miframe, text="=", width=4, command=lambda:total())
butonIgual.grid(row=5, column=4)
butonIgual.config(background="red", fg="#000000")



raiz.mainloop()