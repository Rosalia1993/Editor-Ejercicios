from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #utilizada para almacenar la ruta de un fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0,"end")#borra desdde el primer caracter hasta el final
    root.title("Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = FileDialog.askopenfilename(initialdir='.',
                                      filetype=(("Fichero de texto","*.txt"),),
                                      title="Abrir un fichero de texto")
    if ruta != "":
        fichero =open(ruta,'r')
        contenido = fichero.read()
        texto.delete(1.0,"end")
        texto.insert('insert',contenido)
        fichero.close()
        root.title(ruta +" - Mi editor")

def guardar():
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0,"end-1c")#el utlimo caracter es un salto de linea or lo que no lo va a traer
        fichero=open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardarComo()

def guardarComo():
    global ruta
    mensaje.set("Guardar Como Fichero")
    fichero = FileDialog.asksaveasfile(title= "Guardar fichero",mode = "w",
                                       defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name #te da la ruta del fichero
        contenido=texto.get(1.0,"end-1c")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root =Tk()

root.title("Mi editor")
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo", command= nuevo)
filemenu.add_command(label="Abrir", command= abrir)
filemenu.add_command(label="Guardar", command= guardar)
filemenu.add_command(label="Guardar Como",command= guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(menu=filemenu,label="Archivo")

#caja de texto central
texto=Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0,padx=4,pady=4,font=("Consolas",12))

#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root,textvar=mensaje, justify='left')
monitor.pack(side='left')



root.config(menu=menubar)

root.mainloop()