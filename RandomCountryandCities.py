#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:07:49 2023

@author: vishuddhimakeshwaran
"""
from tkinter import *
import random

root = Tk()
root.title("Random Cities and Countries")
root.geometry("500x600")

listCountry = []
listCity = []

entry1 = Entry(root)
entry1.place(relx = 0.2, rely = 0.2, anchor = CENTER)
entry2 = Entry(root)
entry2.place(relx = 0.8, rely = 0.2, anchor = CENTER)

labelCountries = Label(root)
labelCountries.place(relx = 0.5, rely = 0.4, anchor = CENTER)

labelCities = Label(root)
labelCities.place(relx = 0.5, rely = 0.5, anchor = CENTER)

labelAns1 = Label(root)
labelAns1.place(relx = 0.2, rely = 0.7, anchor = CENTER)

labelAns2 = Label(root)
labelAns2.place(relx = 0.8, rely = 0.7, anchor = CENTER)

def add(): 
    listCountry.append(entry1.get())
    entry1.delete(0, END)
    listCity.append(entry2.get())
    entry2.delete(0, END)
    labelCountries["text"] = "List of countries: " + str(listCountry)
    labelCities["text"] = "List of cities: " + str(listCity)
    
    
button1 = Button(root, text = "Add country and city", command = add)
button1.place(relx = 0.5, rely = 0.3, anchor = CENTER)

def gen(): 
    random1 = random.randint(0, len(listCountry) - 1)
    random2 = random.randint(0, len(listCity) - 1)
    labelAns1["text"] = "Random Country: " + str(listCountry[random1])
    labelAns2["text"] = "Random City: " + str(listCity[random2])
    
    
button2 = Button(root, text = "Generate random country and city", command = gen)
button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()
