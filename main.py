#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import LEFT, S, Frame, StringVar, Entry
# from tkinter import ttk



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.framepriklad = Frame(self)
        self.framepriklad.pack()
        self.framebuttons = Frame(self)
        self.framebuttons.pack()

        self.lblx = tk.Label(self.framepriklad, text="")
        self.lblx.pack(side=LEFT)
        self.lbl = tk.Label(self.framepriklad, text="")
        self.lbl.pack(side=LEFT)
        self.lbly = tk.Label(self.framepriklad, text="")
        self.lbly.pack(side=LEFT)
        self.lblrovno = tk.Label(self.framepriklad, text="")
        self.lblrovno.pack(side=LEFT)
        self.pole = Entry(self.framepriklad, width=3, textvariable="")
        self.pole.pack(side=LEFT)
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack(anchor=S)
        self.btn2 = tk.Button(self, text="Count", command=self.generuj)
        self.btn2.pack(anchor=S)

        self.generuj()

    def generuj(self):
        self.funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        self.funkce()

    def plus(self):
        self.x = random.randint(1,99)
        self.y = random.randint(1,100-self.x)
        self.vysledek = self.x + self.y
        self.lbl.config(text="+")
        self.lblx.config(text=self.x)
        self.lbly.config(text=self.y)
        self.lblrovno.config(text="=")


    def minus(self):
        self.x = random.randint(1,99)
        self.y = random.randint(1,100-self.x)
        if self.x >= self.y:
            self.vysledek = self.x - self.y
        else:
            self.vysledek = self.y - self.x
        self.lbl.config(text="-")
        self.lblx.config(text=self.x)
        self.lbly.config(text=self.y)
        self.lblrovno.config(text="=")

    def krat(self):
        self.x = random.randint(1,10)
        self.y = random.randint(1,10)
        self.vysledek = self.x * self.y
        self.lbl.config(text="*")
        self.lblx.config(text=self.x)
        self.lbly.config(text=self.y)
        self.lblrovno.config(text="=")

    def deleno(self):
        self.y = random.randint(1,9)
        self.vysledek = random.randint(1,9)
        self.x = self.y * self.vysledek
        self.lbl.config(text="/")
        self.lblx.config(text=self.x)
        self.lbly.config(text=self.y)
        self.lblrovno.config(text="=")

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
