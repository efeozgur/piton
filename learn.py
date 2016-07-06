#coding: cp857

from turtle import *
import math

kap = Turtle()

def daire(alan):
    kap.circle(alan)
def ileri(deger):
    kap.forward(deger)
def kalemBuyuklugu(buyukluk):
    kap.pensize(buyukluk)
def yer(x,y):
    kap.setposition(x,y)
def kalemRengi(renk):
    kap.color(renk)
def yukari(deger):
    kap.up(deger)
def hiz (hiz):
    kap.speed(hiz)
def sag (aci):
    kap.right(aci)

kalemBuyuklugu(3)

def yildiz(buyuklugu):
    for i in range(5):
        ileri(buyuklugu)
        sag(144)
    
yildiz(50)
kap.up()
ileri(100)
kap.down()

yildiz(100)

kap.up()
ileri(150)
kap.down()
yildiz(150)

mainloop()



