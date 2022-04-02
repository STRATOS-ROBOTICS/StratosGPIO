#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Programme à interface graphique permettant de contrôler
3 sorties du Raspberry Pi.

Plus d'infos:
http://electroniqueamateur.blogspot.ca/2017/02/une-interface-graphique-pour-controler.html

'''
 
from tkinter import *       # bibliothèque Tkinter, pour création facile d'une interface graphique
import RPi.GPIO as GPIO     # bibliothèque permettant d'accéder aux pins GPIO

# la routine "miseAjour" s'exécute chaque fois qu'on clique sur une case à cocher
def miseAjour():
    GPIO.output(2,gpio2.get())
    GPIO.output(3,gpio3.get())
    GPIO.output(4,gpio4.get())


GPIO.setmode (GPIO.BCM)  #nous choisissons la notation BCM

# les pins GPIO 2, 3, et 4 seront des sorties
GPIO.setup(2,GPIO.OUT)  # réglage de la pin GPIO 2
GPIO.setup(3,GPIO.OUT)  # réglage de la pin GPIO 3
GPIO.setup(4,GPIO.OUT)  # réglage de la pin GPIO 4

fenetre = Tk()    # création d'une fenêtre

fenetre.geometry("250x150+300+300")   # taille de la fenêtre et position initiale sur l'écran
fenetre.title("Contrôleur de LEDs")   # titre de la fenêtre

# création des variables qui contiendront l'état des 3 cases à cocher
gpio2 = IntVar()
gpio3 = IntVar()
gpio4 = IntVar()

label = Label(fenetre, text=" ")  # ligne vide
label.pack()

label = Label(fenetre, text="Cochez les LEDs à  allumer")
label.pack()

label = Label(fenetre, text=" ")  # ligne vide
label.pack()

# création des 3 cases à cocher:

bouton = Checkbutton(fenetre, text="GPIO 2", variable=gpio2, command=miseAjour)
bouton.pack()

bouton = Checkbutton(fenetre, text="GPIO 3", variable=gpio3, command=miseAjour)
bouton.pack()

bouton = Checkbutton(fenetre, text="GPIO 4", variable=gpio4, command=miseAjour)
bouton.pack()

fenetre.mainloop()
