import tkinter as tk
import random as rd

#personalisation
racine = tk.Tk()

#valeurs
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600


#def des programmes
def carre():
    color= "yellow"
    x=250
    y=250
    canvas.create_rectangle((x, y), (x+100, y+100), fill=color)

    #Diminution du côté du carré lorsque le click est à l'intérieur du carré
while tonclick < 300 and tonclick > 200 :
    x = x - 10
    canvas.delete("all")
    canvas.create_rectangle((x, y), (x+100, y+100), fill=color)

    #Augmentation du côté du carré lorsque le click est à l'extérieur du carré
while tonclick > 300 and tonclick < 200 :
    x = x + 10
    canvas.delete("all")
    canvas.create_rectangle((x, y), (x+100, y+100), fill=color)

    #CLiquer sur le pause met en suspension
if (bouton1=1):
    after(delai_ms=120 , fonc=None, args="jeu en pause")  

#wiget
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="blue")
bouton1 = tk.Button(racine, text="Pause", value=0)
bouton2 = tk.Button(racine, text="Restart")
b_carre=tk.Button(racine,text="ajouter carré",command=carre)

#position
canvas.grid(column=1, row=1, rowspan=3)
bouton1.grid(column=1, row=4)
b_carre.grid(column=2,row=4)

racine.mainloop()