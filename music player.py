######################################################################

#importing necessary modules

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mg
from tkinter import ttk
import pygame as pg
import os

######################################################################
#creating root window and initializing mixer
root=Tk()
root.wm_iconbitmap("media.ico")
root.title("Reaper_music player")
root.geometry("500x250+100+100")
root.resizable(width=False,height=False)
root.config(bg="black")
pg.mixer.init()


######################################################################

f1=Frame(root,background="black")
f1.pack(side=BOTTOM,fill=X,padx=5,pady=5)


######################################################################

#functions to perform when a button is pressed
#obsrve closely delete and play logic

current_song=""
def Clicked(event):
    global current_song
    text=event.widget.cget("text")
    if text=="ADD":
        while True:
            global name
            name=fd.askopenfilename(filetypes=(("MP3 Files",".mp3"),("All Files","*.*")))
            if os.path.splitext(name)[1]=="":
                break
            elif os.path.splitext(name)[1]!=".mp3":
                mg.showwarning("Warning","please select only mp3 files")
            else:
                lst.insert("1",[os.path.basename(name),"----->",name])
                break


    elif text=="PLAY":
        try:
            items=lst.curselection()
            song=lst.get(items[0])
            current_song=song[2]
            pg.mixer.music.load(current_song)
            pg.mixer.music.play(-1)
        except:
            pass   

    elif text=="DELETE":
        items1=lst.curselection()
        try:
            song1=lst.get(items1[0])
            delete_song=song1[2]
            t=lst.get(0,END)
            if len(t)==1:
                pg.mixer.music.stop()
                lst.delete(items1[0])
            elif current_song=="":
                lst.delete(items1[0])
            elif current_song!=delete_song:
                lst.delete(items1[0])    
            elif current_song==delete_song:
                pg.mixer.music.stop()
                lst.delete(items1[0])
            else:
                pass      
        except:
            pass

    elif text=="PAUSE":
        pg.mixer.music.pause()
        b2.config(text="RESUME")

    elif text=="RESUME":
        pg.mixer.music.unpause()
        b2.config(text="PAUSE")

        
    elif text=="STOP":
        pg.mixer.music.stop()

    else:
        pass

 
######################################################################

#buttons for plat,pause,stop.

b1=ttk.Button(f1,text="PLAY")
b1.pack(side=LEFT,padx=30,pady=5)
b1.bind("<Button-1>",Clicked)

b2=ttk.Button(f1,text="PAUSE")
b2.pack(side=LEFT,padx=30,pady=5)
b2.bind("<Button-1>",Clicked)

b3=ttk.Button(f1,text="STOP")
b3.pack(side=LEFT,padx=30,pady=5)
b3.bind("<Button-1>",Clicked)

######################################################################

#buttons for add and delete.
f1=Frame(root,bg="black")
f1.pack(side=BOTTOM,fill=X,padx=5,pady=5)

b4=ttk.Button(f1,text="ADD")
b4.pack(side=LEFT,padx=30,pady=5)
b4.bind("<Button-1>",Clicked)

b5=ttk.Button(f1,text="DELETE")
b5.pack(side=LEFT,padx=30,pady=5)
b5.bind("<Button-1>",Clicked)

######################################################################

#volume control widget

def Set_vol(val):
    value=float(val)
    pg.mixer.music.set_volume(value/100)

pg.mixer.music.set_volume(0.0)
vol=Label(f1,text="Volume:",font=("Ms Sheriff",15),fg="red",bg="black")
vol.place(x=290,y=5)
s1=ttk.Scale(f1,from_=0,to=100,command=Set_vol,orient=HORIZONTAL,length=100)
s1.place(x=370,y=5)

######################################################################

#listbox with scrollbar to list out songs

f2=Frame(root,bg="black",width=300)
f2.pack(side=LEFT,fill=Y,padx=5,pady=5)

scrollbar=Scrollbar(f2)
scrollbar.pack(side=RIGHT,fill=Y)

global lst
lst=Listbox(f2,width=32,selectmode=SINGLE,yscrollcommand=scrollbar.set,bg="black",fg="red",font=("system"))
scrollbar.config(command=lst.yview)
lst.pack()


######################################################################

#madeby title

f3=Frame(root,bg="black")
f3.pack(side=LEFT,fill=Y,padx=5,pady=5)

l3=Label(f3,text="MADE BY\nREAPER\nRESIDES",bg="black",fg="red",font=("times new roman",30,"bold"))
l3.pack(side=LEFT)

root.mainloop()
######################################################################
