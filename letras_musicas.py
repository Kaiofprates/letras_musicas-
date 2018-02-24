# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 00:27:43 2018

@author: kaio
"""

import requests
import json
from tkinter import *

root = Tk()
root.title("Letras de Músicas")
root.geometry('390x580')
root['bg'] = '#4B0082'

letra1= Text(root, height = 28, width = 45)
letra1.place(x = 10, y = 100)

def busca():
    letra1.delete(1.0,END)
    mus = music.get()
    art = artis.get()
    url = requests.get("https://api.vagalume.com.br/search.php?apikey=f86df64c617743ad212ce779f8c5a4e8&art=" + art +"&mus=" + mus)
    letra = json.loads(url.text)
    texto = (letra['mus'][0]['text'])
    if texto:
        letra1.insert(INSERT, texto)
    else:
        letra1.insert(INSERT, "Letra não encontrada")
    


lab = Label(root, text = "Nome da Música:", bg = '#4B0082',fg = "white")
lab.place(x = 10, y = 10)
lab2 = Label(root, text = "Nome do Artista:", bg = '#4B0082',fg = "white")
lab2.place(x = 10, y = 40)

music = Entry(root,width = 40)
music.place(x = 130, y = 10)

artis = Entry(root,width = 40)
artis.place(x = 130, y = 40)


bot = Button(root,text = "Pesquisar",bg = '#4B0082', fg = 'white', command = busca)
bot.place(x = 300, y = 70)



root.mainloop()
