# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:47:23 2020

@author: Asus
"""


import tkinter as tk
window = tk.Tk()#創造一個tk物件
window.title("my")#設定物件顯示名稱
window.geometry('200x100')#設定物件大小 長X高 
#創造在window上面的lable,顯示文字,背景,字體,寬,高
var=tk.StringVar()
lable = tk.Label(window,textvariable=var,bg='red',font=('Arial',12),width=10,height=2)
lable.pack()#把創造的物件選擇放置的中間上面

on_hit = False

def hit_me():
    global on_hit
    if on_hit ==False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set(" ")
        
bon = tk.Button(window,text='hit',width=5,height=1,command=hit_me)#設定他點擊後會運行hit_me函數
bon.pack()

window.mainloop()#不斷顯示刷新視窗,才會因為操作而更新顯示