from django.shortcuts import render
from .models import *
from django.views import generic
from django import forms
from .forms import SearchForm,SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.db.models import Q
import datetime

def td(i, f):
    if f.second>i.second:
        t=(f.first-i.first)*60+f.second-i.second
    else:
        t=(f.first-i.first-1)*60+60-(i.second-f.second)
    return t

class make_pair():
    def __init__(self, a, b):
        self.first = a
        self.second = b

# data = []
print("PRESS\nO FOR AMRITSAR\n1 FOR BATHINDA\n2 FOR CHANDIGARH\n3 FOR JALANDHAR\n4 FOR LUDHIANA\n5 FOR PATIALA\n6 FOR SANGRUR\n7 FOR PATHANKOT\n8 FOR FEROZEPUR\n9 FOR MOGA\n")
##make_pair(make_pair(7,11),make_pair(11,41))
###def fun(a, b, c):
    
    ###def main():
        # a, b = input().split("")
        # fun(a,b,c)
###
def func(a,b,h,m):
    result=[]
    data=[[[0 for x in range(10)] for y in range(10)] for z in range(20)]
    data[0][1][0]=make_pair(make_pair(7,11),make_pair(11,41))
    data[0][1][1]=make_pair(make_pair(13,21),make_pair(17,51))
    data[0][1][2]=make_pair(make_pair(15,52),make_pair(20,22))
    data[0][2][0]=make_pair(make_pair(5,45),make_pair(9,30))
    data[0][2][1]=make_pair(make_pair(9,15),make_pair(14,14))
    data[0][2][2]=make_pair(make_pair(12,10),make_pair(16,55))
    data[0][2][3]=make_pair(make_pair(14,45),make_pair(18,25))
    data[0][3][0]=make_pair(make_pair(5,50),make_pair(7,30))
    data[0][3][1]=make_pair(make_pair(9,0),make_pair(10,45))
    data[0][3][2]=make_pair(make_pair(14,25),make_pair(16,10))
    data[0][4][0]=make_pair(make_pair(6,10),make_pair(9,30))
    data[0][4][1]=make_pair(make_pair(10,50),make_pair(13,40))
    data[0][4][2]=make_pair(make_pair(15,30),make_pair(19,00))
    data[0][5][0]=make_pair(make_pair(5,30),make_pair(11,10))
    data[0][5][1]=make_pair(make_pair(7,20),make_pair(12,40))
    data[0][5][2]=make_pair(make_pair(15,40),make_pair(21,30))
    data[0][5][3]=make_pair(make_pair(17,10),make_pair(23,20))
    data[0][7][0]=make_pair(make_pair(5,30),make_pair(8,10))
    data[0][7][1]=make_pair(make_pair(8,10),make_pair(12,50))
    data[0][7][2]=make_pair(make_pair(12,30),make_pair(16,30))
    data[0][8][0]=make_pair(make_pair(7,30),make_pair(12,00))
    data[0][8][1]=make_pair(make_pair(16,10),make_pair(20,40))

    data[1][0][0]=make_pair(make_pair(4,30),make_pair(8,30))
    data[1][0][1]=make_pair(make_pair(8,40),make_pair(12,50))
    data[1][0][2]=make_pair(make_pair(12,30),make_pair(16,10))
    data[1][0][3]=make_pair(make_pair(17,30),make_pair(21,40))
    data[1][2][0]=make_pair(make_pair(5,1),make_pair(9,00))
    data[1][2][1]=make_pair(make_pair(7,30),make_pair(12,00))
    data[1][2][2]=make_pair(make_pair(11,30),make_pair(16,10))
    data[1][2][3]=make_pair(make_pair(15,30),make_pair(20,30))
    data[1][3][0]=make_pair(make_pair(8,20),make_pair(12,30))
    data[1][3][1]=make_pair(make_pair(11,40),make_pair(15,40))
    data[1][3][2]=make_pair(make_pair(14,20),make_pair(20,00))
    data[1][4][0]=make_pair(make_pair(5,40),make_pair(8,10))
    data[1][4][1]=make_pair(make_pair(8,10),make_pair(11,30))
    data[1][4][2]=make_pair(make_pair(12,30),make_pair(15,30))
    data[1][4][3]=make_pair(make_pair(14,50),make_pair(18,00))
    data[1][5][0]=make_pair(make_pair(6,40),make_pair(9,00))
    data[1][5][1]=make_pair(make_pair(8,30),make_pair(11,40))
    data[1][5][2]=make_pair(make_pair(12,30),make_pair(15,30))
    data[1][5][3]=make_pair(make_pair(15,30),make_pair(19,00))
    data[1][6][0]=make_pair(make_pair(6,00),make_pair(8,30))
    data[1][6][1]=make_pair(make_pair(9,30),make_pair(12,00))
    data[1][6][2]=make_pair(make_pair(13,00),make_pair(15,20))
    data[1][6][3]=make_pair(make_pair(15,30),make_pair(17,30))
    data[1][6][4]=make_pair(make_pair(18,00),make_pair(20,30))
    data[1][7][0]=make_pair(make_pair(6,30),make_pair(11,30))
    data[1][7][1]=make_pair(make_pair(12,50),make_pair(18,30))
    data[1][7][2]=make_pair(make_pair(16,40),make_pair(22,30))
    data[1][8][0]=make_pair(make_pair(5,30),make_pair(7,40))
    data[1][8][1]=make_pair(make_pair(12,40),make_pair(14,30))
    data[1][8][2]=make_pair(make_pair(17,30),make_pair(19,40))
    data[1][9][0]=make_pair(make_pair(6,00),make_pair(8,10))
    data[1][9][1]=make_pair(make_pair(12,10),make_pair(14,00))

    data[2][0][0]=make_pair(make_pair(6,00),make_pair(10,20))
    data[2][0][1]=make_pair(make_pair(9,30),make_pair(13,30))
    data[2][0][2]=make_pair(make_pair(13,00),make_pair(17,30))
    data[2][1][0]=make_pair(make_pair(6,30),make_pair(10,30))
    data[2][1][1]=make_pair(make_pair(9,50),make_pair(14,00))
    data[2][1][2]=make_pair(make_pair(13,40),make_pair(18,00))
    data[2][3][0]=make_pair(make_pair(8,30),make_pair(11,40))
    data[2][3][1]=make_pair(make_pair(12,30),make_pair(15,30))
    data[2][3][2]=make_pair(make_pair(15,30),make_pair(19,00))
    data[2][4][0]=make_pair(make_pair(6,00),make_pair(8,30))
    data[2][4][1]=make_pair(make_pair(9,30),make_pair(12,00))
    data[2][4][2]=make_pair(make_pair(13,00),make_pair(15,20))
    data[2][5][0]=make_pair(make_pair(15,30),make_pair(17,30))
    data[2][5][1]=make_pair(make_pair(18,00),make_pair(20,30))
    data[2][5][2]=make_pair(make_pair(13,00),make_pair(15,20))
    data[2][6][0]=make_pair(make_pair(15,30),make_pair(17,30))
    data[2][6][1]=make_pair(make_pair(18,00),make_pair(20,30))
    data[2][6][2]=make_pair(make_pair(12,30),make_pair(15,30))
    data[2][7][0]=make_pair(make_pair(14,50),make_pair(18,00))
    data[2][7][1]=make_pair(make_pair(6,40),make_pair(9,00))
    data[2][7][2]=make_pair(make_pair(8,30),make_pair(11,40))
    data[2][8][0]=make_pair(make_pair(12,30),make_pair(15,30))
    data[2][8][1]=make_pair(make_pair(15,30),make_pair(19,00))
    data[2][8][2]=make_pair(make_pair(6,00),make_pair(8,30))
    data[2][9][0]=make_pair(make_pair(9,30),make_pair(12,00))
    data[2][9][1]=make_pair(make_pair(13,00),make_pair(15,20))
    data[2][9][2]=make_pair(make_pair(15,30),make_pair(17,30))



    data[3][0][0]=make_pair(make_pair(13,00),make_pair(15,30))
    data[3][0][1]=make_pair(make_pair(15,30),make_pair(17,30))
    data[3][0][2]=make_pair(make_pair(18,00),make_pair(20,30))
    data[3][1][0]=make_pair(make_pair(13,30),make_pair(15,30))
    data[3][1][1]=make_pair(make_pair(14,50),make_pair(18,00))
    data[3][1][2]=make_pair(make_pair(6,40),make_pair(9,00))
    data[3][2][0]=make_pair(make_pair(8,30),make_pair(11,40))
    data[3][2][1]=make_pair(make_pair(13,30),make_pair(15,30))
    data[3][2][2]=make_pair(make_pair(15,30),make_pair(19,00))
    data[3][4][0]=make_pair(make_pair(6,00),make_pair(8,30))
    data[3][4][1]=make_pair(make_pair(9,30),make_pair(13,00))
    data[3][4][2]=make_pair(make_pair(13,00),make_pair(15,30))
    data[3][5][0]=make_pair(make_pair(15,30),make_pair(17,30))
    data[3][5][1]=make_pair(make_pair(18,00),make_pair(20,30))
    data[3][5][2]=make_pair(make_pair(13,00),make_pair(15,30))
    data[3][6][0]=make_pair(make_pair(15,30),make_pair(17,30))
    data[3][6][1]=make_pair(make_pair(18,00),make_pair(20,30))
    data[3][6][2]=make_pair(make_pair(13,30),make_pair(15,30))
    data[3][7][0]=make_pair(make_pair(14,50),make_pair(18,00))
    data[3][7][1]=make_pair(make_pair(6,40),make_pair(9,00))
    data[3][7][2]=make_pair(make_pair(8,30),make_pair(11,40))
    data[3][8][0]=make_pair(make_pair(13,30),make_pair(15,30))
    data[3][8][1]=make_pair(make_pair(15,30),make_pair(19,00))
    data[3][8][2]=make_pair(make_pair(6,00),make_pair(8,30))
    data[3][9][0]=make_pair(make_pair(9,30),make_pair(13,00))
    data[3][9][1]=make_pair(make_pair(13,00),make_pair(15,30))
    data[3][9][2]=make_pair(make_pair(15,30),make_pair(17,30))

    data[4][0][0]=make_pair(make_pair(4,30),make_pair(7,13))
    data[4][0][1]=make_pair(make_pair(9,20),make_pair(12,45))
    data[4][0][2]=make_pair(make_pair(11,00),make_pair(14,30))
    data[4][0][3]=make_pair(make_pair(17,10),make_pair(20,25))
    data[4][1][0]=make_pair(make_pair(5,15),make_pair(7,45))
    data[4][1][1]=make_pair(make_pair(8,50),make_pair(11,20))
    data[4][1][2]=make_pair(make_pair(11,20),make_pair(13,50))
    data[4][1][3]=make_pair(make_pair(18,15),make_pair(21,20))
    data[4][2][0]=make_pair(make_pair(7,55),make_pair(8,58))
    data[4][2][1]=make_pair(make_pair(11,00),make_pair(12,45))
    data[4][2][2]=make_pair(make_pair(16,45),make_pair(18,40))
    data[4][2][3]=make_pair(make_pair(19,30),make_pair(21,15))
    data[4][3][0]=make_pair(make_pair(5,30),make_pair(6,45))
    data[4][3][1]=make_pair(make_pair(7,15),make_pair(8,30))
    data[4][3][2]=make_pair(make_pair(9,30),make_pair(10,45))
    data[4][3][3]=make_pair(make_pair(11,20),make_pair(12,45))
    data[4][3][4]=make_pair(make_pair(14,30),make_pair(15,45))
    data[4][3][5]=make_pair(make_pair(19,30),make_pair(20,45))
    data[4][5][0]=make_pair(make_pair(6,00),make_pair(7,55))
    data[4][5][1]=make_pair(make_pair(8,40),make_pair(10,35))
    data[4][5][2]=make_pair(make_pair(12,5),make_pair(14,00))
    data[4][5][3]=make_pair(make_pair(16,5),make_pair(17,50))
    data[4][7][0]=make_pair(make_pair(9,30),make_pair(13,30))
    data[4][7][1]=make_pair(make_pair(11,2),make_pair(15,2))
    data[4][7][2]=make_pair(make_pair(11,17),make_pair(15,17))
    data[4][8][0]=make_pair(make_pair(12,35),make_pair(13,5))
    data[4][8][1]=make_pair(make_pair(10,30),make_pair(13,00))
    data[4][8][2]=make_pair(make_pair(14,7),make_pair(14,30))
    data[4][9][0]=make_pair(make_pair(16,30),make_pair(18,7))
    data[4][9][1]=make_pair(make_pair(10,00),make_pair(11,47))
    data[4][9][2]=make_pair(make_pair(12,30),make_pair(14,7))


    data[5][0][0]=make_pair(make_pair(4,40),make_pair(9,40))
    data[5][0][1]=make_pair(make_pair(11,30),make_pair(16,30))
    data[5][0][2]=make_pair(make_pair(18,00),make_pair(23,00))
    data[5][0][3]=make_pair(make_pair(12,45),make_pair(17,29))
    data[5][1][0]=make_pair(make_pair(5,30),make_pair(8,10))
    data[5][1][1]=make_pair(make_pair(10,50),make_pair(13,50))
    data[5][1][2]=make_pair(make_pair(12,10),make_pair(15,00))
    data[5][1][3]=make_pair(make_pair(16,20),make_pair(19,00))
    data[5][2][0]=make_pair(make_pair(5,20),make_pair(6,50))
    data[5][2][1]=make_pair(make_pair(8,10),make_pair(10,00))
    data[5][2][2]=make_pair(make_pair(12,40),make_pair(14,50))
    data[5][2][3]=make_pair(make_pair(16,20),make_pair(18,20))
    data[5][3][0]=make_pair(make_pair(10,30),make_pair(13,20))
    data[5][3][1]=make_pair(make_pair(15,30),make_pair(18,30))
    data[5][3][2]=make_pair(make_pair(6,30),make_pair(9,00))
    data[5][4][0]=make_pair(make_pair(14,25),make_pair(16,20))
    data[5][4][1]=make_pair(make_pair(12,20),make_pair(14,00))
    data[5][4][2]=make_pair(make_pair(10,00),make_pair(12,00))
    data[5][4][3]=make_pair(make_pair(5,30),make_pair(7,30))
    data[5][6][0]=make_pair(make_pair(5,30),make_pair(6,30))
    data[5][6][1]=make_pair(make_pair(6,00),make_pair(7,10))
    data[5][6][2]=make_pair(make_pair(11,30),make_pair(12,30))
    data[5][6][3]=make_pair(make_pair(16,30),make_pair(17,30))
    data[5][7][0]=make_pair(make_pair(12,15),make_pair(17,5))
    data[5][7][1]=make_pair(make_pair(10,20),make_pair(15,00))
    data[5][7][2]=make_pair(make_pair(13,15),make_pair(18,15))
    data[5][8][0]=make_pair(make_pair(15,30),make_pair(19,30))
    data[5][8][1]=make_pair(make_pair(5,30),make_pair(9,30))
    data[5][8][2]=make_pair(make_pair(7,10),make_pair(11,10))



    data[6][1][0]=make_pair(make_pair(6,30),make_pair(8,30))
    data[6][1][1]=make_pair(make_pair(9,10),make_pair(11,00))
    data[6][1][2]=make_pair(make_pair(13,40),make_pair(15,40))
    data[6][2][0]=make_pair(make_pair(5,40),make_pair(8,40))
    data[6][2][1]=make_pair(make_pair(9,40),make_pair(12,40))
    data[6][2][2]=make_pair(make_pair(14,40),make_pair(17,40))
    data[6][3][0]=make_pair(make_pair(8,30),make_pair(11,30))
    data[6][3][1]=make_pair(make_pair(12,30),make_pair(15,30))
    data[6][3][2]=make_pair(make_pair(16,20),make_pair(19,30))
    data[6][4][0]=make_pair(make_pair(8,30),make_pair(10,30))
    data[6][4][1]=make_pair(make_pair(13,00),make_pair(15,00))
    data[6][4][2]=make_pair(make_pair(4,00),make_pair(6,00))
    data[6][5][0]=make_pair(make_pair(5,30),make_pair(6,30))
    data[6][5][1]=make_pair(make_pair(9,10),make_pair(10,30))
    data[6][5][2]=make_pair(make_pair(13,50),make_pair(15,00))
    data[6][5][3]=make_pair(make_pair(16,30),make_pair(17,30))
    data[6][9][0]=make_pair(make_pair(9,30),make_pair(12,10))


    data[7][0][0]=make_pair(make_pair(4,00),make_pair(6,50))
    data[7][0][1]=make_pair(make_pair(5,30),make_pair(8,30))
    data[7][0][2]=make_pair(make_pair(10,00),make_pair(13,50))
    data[7][2][0]=make_pair(make_pair(10,00),make_pair(14,30))
    data[7][2][1]=make_pair(make_pair(14,10),make_pair(18,50))
    data[7][2][2]=make_pair(make_pair(15,25),make_pair(19,30))
    data[7][3][0]=make_pair(make_pair(9,20),make_pair(12,10))
    data[7][3][1]=make_pair(make_pair(13,30),make_pair(16,10))
    data[7][3][2]=make_pair(make_pair(7,20),make_pair(10,00))
    data[7][4][0]=make_pair(make_pair(13,00),make_pair(15,50))
    data[7][4][1]=make_pair(make_pair(11,10),make_pair(14,00))
    data[7][4][2]=make_pair(make_pair(9,00),make_pair(11,50))
    data[7][8][0]=make_pair(make_pair(11,40),make_pair(15,55))

    data[8][0][0]=make_pair(make_pair(6,35),make_pair(8,45))
    data[8][0][1]=make_pair(make_pair(11,25),make_pair(13,30))
    data[8][0][2]=make_pair(make_pair(13,00),make_pair(15,10))
    data[8][1][0]=make_pair(make_pair(8,30),make_pair(9,34))
    data[8][1][1]=make_pair(make_pair(14,50),make_pair(15,55))
    data[8][1][2]=make_pair(make_pair(13,40),make_pair(14,45))
    data[8][2][0]=make_pair(make_pair(7,20),make_pair(9,40))
    data[8][2][1]=make_pair(make_pair(10,30),make_pair(12,50))
    data[8][2][2]=make_pair(make_pair(13,40),make_pair(15,55))
    data[8][3][0]=make_pair(make_pair(8,30),make_pair(10,45))
    data[8][3][1]=make_pair(make_pair(13,10),make_pair(15,30))
    data[8][3][2]=make_pair(make_pair(15,30),make_pair(17,40))
    data[8][4][0]=make_pair(make_pair(6,00),make_pair(8,30))
    data[8][4][1]=make_pair(make_pair(9,30),make_pair(12,30))
    data[8][4][2]=make_pair(make_pair(13,00),make_pair(15,50))
    data[8][5][0]=make_pair(make_pair(9,30),make_pair(13,55))
    data[8][5][1]=make_pair(make_pair(11,00),make_pair(15,10))
    data[8][7][0]=make_pair(make_pair(5,55),make_pair(11,10))
    data[8][9][0]=make_pair(make_pair(6,00),make_pair(7,10))
    data[8][9][1]=make_pair(make_pair(8,50),make_pair(10,5))
    data[8][9][2]=make_pair(make_pair(13,00),make_pair(14,5))


    data[9][0][0]=make_pair(make_pair(8,10),make_pair(10,50))
    data[9][0][1]=make_pair(make_pair(11,30),make_pair(14,30))
    data[9][0][2]=make_pair(make_pair(14,10),make_pair(17,30))
    data[9][1][0]=make_pair(make_pair(8,30),make_pair(10,30))
    data[9][1][1]=make_pair(make_pair(11,50),make_pair(13,35))
    data[9][1][2]=make_pair(make_pair(17,00),make_pair(19,00))
    data[9][2][0]=make_pair(make_pair(6,30),make_pair(9,40))
    data[9][2][1]=make_pair(make_pair(12,20),make_pair(15,30))
    data[9][2][2]=make_pair(make_pair(15,30),make_pair(18,7))
    data[9][3][0]=make_pair(make_pair(6,00),make_pair(7,55))
    data[9][3][1]=make_pair(make_pair(9,5),make_pair(11,00))
    data[9][3][2]=make_pair(make_pair(13,00),make_pair(15,55))
    data[9][4][0]=make_pair(make_pair(15,30),make_pair(17,00))
    data[9][4][1]=make_pair(make_pair(18,30),make_pair(20,5))
    data[9][5][0]=make_pair(make_pair(8,00),make_pair(10,40))
    data[9][5][1]=make_pair(make_pair(10,30),make_pair(13,10))
    data[9][5][2]=make_pair(make_pair(12,50),make_pair(15,30))
    data[9][7][0]=make_pair(make_pair(8,30),make_pair(11,40))
    data[9][8][0]=make_pair(make_pair(6,00),make_pair(8,50))
    data[9][8][1]=make_pair(make_pair(9,30),make_pair(11,45))
    data[9][8][2]=make_pair(make_pair(13,00),make_pair(15,50))


    num = [[0 for x in range(10)] for y in range(10)]
    num[0][1]=3
    num[0][2]=4
    num[0][3]=3
    num[0][4]=3
    num[0][5]=4
    num[0][6]=0
    num[0][7]=3
    num[0][9]=0
    num[1][0]=4
    num[1][2]=4
    num[1][3]=3
    num[1][4]=4
    num[1][5]=4
    num[1][6]=5
    num[1][7]=3
    num[1][8]=3
    num[1][9]=2
    num[2][0]=3
    num[2][1]=3
    num[2][3]=3
    num[2][4]=3
    num[2][5]=3
    num[2][6]=3
    num[2][7]=3
    num[2][8]=3
    num[2][9]=3
    num[3][0]=3
    num[3][1]=3
    num[3][2]=3
    num[3][4]=3
    num[3][5]=3
    num[3][6]=3
    num[3][7]=3
    num[3][8]=3
    num[3][9]=3
    num[4][0]=4
    num[4][1]=4
    num[4][2]=4
    num[4][3]=6
    num[4][5]=4
    num[4][6]=0
    num[4][7]=3
    num[4][8]=3
    num[4][9]=3
    num[5][0]=4
    num[5][1]=4
    num[5][2]=4
    num[5][3]=3
    num[5][4]=4
    num[5][6]=4
    num[5][7]=3
    num[5][8]=3
    num[5][9]=0
    num[6][0]=0
    num[6][1]=3
    num[6][2]=3
    num[6][3]=3
    num[6][4]=3
    num[6][5]=4
    num[6][7]=0
    num[6][8]=0
    num[6][9]=1
    num[7][0]=3
    num[7][1]=0
    num[7][2]=3
    num[7][3]=3
    num[7][4]=3
    num[7][5]=0
    num[7][6]=0
    num[7][8]=1
    num[7][9]=0
    num[8][0]=3
    num[8][1]=3
    num[8][2]=3
    num[8][3]=3
    num[8][4]=3
    num[8][5]=2
    num[8][6]=0
    num[8][7]=1
    num[8][9]=3
    num[9][0]=3
    num[9][1]=3
    num[9][2]=3
    num[9][3]=3
    num[9][4]=2
    num[9][5]=3
    num[9][6]=0
    num[9][7]=1
    num[9][8]=3



    reach=[0 for x in range(10)]

    time=[0 for x in range(10)]
    for i in range(10):
        time[i]=make_pair(24,0)
        
    time[a]=make_pair(h,m)

    parent=[0 for x in range(10)]

    cm=1.5
    total=[0 for x in range(10)]


    while(reach[b]==0):
        miin=-1
        for i in range(10):
            if(miin==-1):
                if(reach[i]==0):
                    miin=i
            else:
                if(reach[i]==0):
                    if time[i].first<time[miin].first:
                        miin=i
                    elif time[i].first<time[miin].first and time[i].second<time[miin].second:
                        miin=i
        reach[miin]=-1
        for i in range(10):
            x=-1
            f1=-1
            if(i!=miin):
                for j in range(num[miin][i]):
                    if(x==-1):
                        if(data[miin][i][j].first.first>time[miin].first):
                            x=j
                        elif(data[miin][i][j].first.first==time[miin].first and data[miin][i][j].first.second>time[miin].second):
                            x=j

                    else:
                        if(data[miin][i][j].first.first>time[miin].first):
                            if(data[miin][i][j].first.first<time[i].first):
                                x=j
                            elif(data[miin][i][j].first.first==time[i].first and data[miin][i][j].first.second<time[i].second):
                                x=j
                        elif(data[miin][i][j].first.first==time[miin].first and data[miin][i][j].first.second>time[miin].second):
                            if(data[miin][i][j].first.first<time[i].first):
                                x=j
                            elif(data[miin][i][j].first.first==time[i].first and data[miin][i][j].first.second<time[i].second):
                                x=j
                    if(x!=-1):
                        if(time[i].first>data[miin][i][x].second.first):
                            time[i]=make_pair(data[miin][i][x].second.first,data[miin][i][x].second.second)
                            parent[i]=miin
                            f1=x
                        elif(time[i].first==data[miin][i][x].second.first and time[i].second>data[miin][i][x].second.second):
                            time[i]=make_pair(data[miin][i][x].second.first,data[miin][i][x].second.second)
                            parent[i]=miin
                            f1=x
                if (x!=-1 and f1!=-1):
                    total[i]=total[miin]+(td(make_pair(data[miin][i][f1].first.first,data[miin][i][f1].first.second),make_pair(data[miin][i][f1].second.first,data[miin][i][f1].second.second)))


    # p=0
    # q=b
    # par=[0 for x in range(10)]
    # while(q!=a):
    #     par[p]=q
    #     p+=1
    #     q=parent[q]

    # par[p]=a
    if(miin==b):
        print("\nYOU CAN REACH DESTINATION AT {}  HOUR AND  {}  MIN VIA = ".format(time[miin].first,time[miin].second))
        # for i in range(p, 0, -1):
        #     print(par[i])

        print("AND TOTAL COST  \nCONSIDERING Rs. 1.5 PER MIN WOULD BE APPROXIMATELY=Rs. {}".format(cm*(total[miin])))
        result.append(time[miin].first)
        result.append(time[miin].second)
        result.append(cm*(total[miin]))
    time[a]=make_pair(h,m)
    x=-1
    time[b]=make_pair(24,0)
    miin=a
    i=b
    f=-1
    for j in range(num[miin][i]):
        if(x==-1):
            if(data[miin][i][j].first.first>time[miin].first):
                x=j
            elif(data[miin][i][j].first.first==time[miin].first and data[miin][i][j].first.second>time[miin].second):
                x=j

        else:
            if(data[miin][i][j].first.first>time[miin].first):
                if(data[miin][i][j].first.first<time[i].first):
                    x=j
                elif(data[miin][i][j].first.first==time[i].first and data[miin][i][j].first.second<time[i].second):
                    x=j
            elif(data[miin][i][j].first.first==time[miin].first and data[miin][i][j].first.second>time[miin].second):
                if(data[miin][i][j].first.first<time[i].first):
                    x=j
                elif(data[miin][i][j].first.first==time[i].first and data[miin][i][j].first.second<time[i].second):
                    x=j
        if(x!=-1):
            if(time[i].first>data[miin][i][x].second.first):
                time[i]=make_pair(data[miin][i][x].second.first,data[miin][i][x].second.second)
                parent[i]=miin
                f=x
            elif(time[i].first==data[miin][i][x].second.first and time[i].second>data[miin][i][x].second.second):
                time[i]=make_pair(data[miin][i][x].second.first,data[miin][i][x].second.second)
                parent[i]=miin
                f=x 
    result.append(x)
    if(x==-1):
        print("\nNO DIRECT BUS AVAILABLE\n")
    else:
        print("\nOR YOU CAN GET A DIRECT BUS AT = {}  HOURS AND {}  MIN AND REACH BY {}  HOUR {}  MIN AND WHICH WILL COST = {}".format(data[a][b][f].first.first,data[a][b][f].first.second,
            data[a][b][f].second.first,data[a][b][f].second.second,cm*(td(make_pair(data[a][b][f].first.first,data[a][b][f].first.second),make_pair(data[a][b][f].second.first,data[a][b][f].second.second)))))

        # return x,time[miin].first,time[miin].second,cm*(total[miin])
    result.append(data[a][b][f].first.first)
    result.append(data[a][b][f].first.second)
    result.append(data[a][b][f].second.first)
    result.append(data[a][b][f].second.second)
    result.append(cm*(td(make_pair(data[a][b][f].first.first,data[a][b][f].first.second),make_pair(data[a][b][f].second.first,data[a][b][f].second.second))))
    return result
# print("ENTER SOURCE AND DESTINATION=")
# a, b = map(int, input().split(" "))

# print("ENTER STARTING TIME IN HH MM=")    
# h, m = map(int, input().split(" "))
def index(request):
	return render(request,'index1.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
      
            form.save()

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class SearchListView(generic.ListView):
	model=Search
	template_name = 'search.html'
	paginate_by = 15
    
	def get_queryset(self):
		queryset=Search.objects.all().filter(user=self.request.user).distinct().order_by('-pk')
		return queryset

class NotificationCreateView(LoginRequiredMixin,generic.CreateView):
	model=Search
	form_class=SearchForm
	template_name='notification_create.html'

	def form_valid(self,form):
		search=form.save(commit=False)
		search.user=User.objects.get(username=self.request.user)

		#search.save()

		##variables of form to be used in function
		source = search.source
		des = search.des
		# # print(des)
		HH = search.HH
		MM = search.MM
		# search.result,search=project(s,des,hh,mm)

		res=func(source,des,HH,MM)

		search.xm=res[3]

		search.am=res[0]
		search.bm=res[1]
		search.cm=res[2]
		search.dm=res[4]
		search.em=res[5]
		search.fm=res[6]
		search.gm=res[7]

		print(res)
		search.save()
		return redirect('history')







