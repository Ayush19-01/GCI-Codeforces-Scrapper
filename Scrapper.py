from bs4 import BeautifulSoup
from tkinter import *
from tkinter import Tk
from tkinter import StringVar
import requests
def info(event):
    global root
    global s1
    user=s1.get()
    url=requests.get('https://codeforces.com/api/user.info?handles='+user)
    soup=BeautifulSoup(url.text,'lxml')
    a=(soup.get_text())
    b=eval(a)
    d=b['result'][0]
    print(d)
    rank=d['rank']
    handle=d['handle']
    rating=d['rating']
    rated=d['maxRating']
    ranked=d['maxRank']
    root.destroy()
    data(rank,handle,rating,rated,ranked,user)
def data(a,b,c,d,e,f):
    root2=Tk()
    root2.title('Statistics')
    root2.geometry('450x400')
    root2.config(bg="#220047")
    hd1=Label(root2,text='Data for user:',font='Arial 17',bg='#220047',fg='#CE9141')
    hd1.place(x=30,y=10)
    hd2=Label(root2,text=f,font='Arial 17',bg='#220047',fg='#CE9141')
    hd2.place(x=240,y=10)
    hd3=Label(root2,text="Rank:",font='Arial 17',bg='#220047',fg='#CE9141')
    hd3.place(x=30,y=80)
    hd4=Label(root2,text=a,font='Arial 17',bg='#220047',fg='#CE9141')
    hd4.place(x=240,y=80)
    hd5=Label(root2,text="Handle:",font='Arial 17',bg='#220047',fg='#CE9141')
    hd5.place(x=30,y=120)
    hd6=Label(root2,text=b,font='Arial 17',bg='#220047',fg='#CE9141')
    hd6.place(x=240,y=120)
    hd7=Label(root2,text="Current Rating",font='Arial 17',bg='#220047',fg='#CE9141')
    hd7.place(x=30,y=160)
    hd8=Label(root2,text=c,font='Arial 17',bg='#220047',fg='#CE9141')
    hd8.place(x=240,y=160)
    hd9=Label(root2,text="Max Rating:",font='Arial 17',bg='#220047',fg='#CE9141')
    hd9.place(x=30,y=200)
    hd10=Label(root2,text=d,font='Arial 17',bg='#220047',fg='#CE9141')
    hd10.place(x=240,y=200)
    hd11=Label(root2,text="Max Ranking:",font='Arial 17',bg='#220047',fg='#CE9141')
    hd11.place(x=30,y=240)
    hd12=Label(root2,text=e,font='Arial 17',bg='#220047',fg='#CE9141')
    hd12.place(x=240,y=240)
    
def window():
    global root
    global s1
    root=Tk()
    root.title('Codeforces Scrapper')
    root.geometry('500x200')
    root.configure(bg='#220047')
    s1=StringVar()
    hd1=Label(root,text='Data Scrapper',font='Arial 30',bg='#220047',fg='#CE9141')
    hd1.place(x=150,y=10)
    hd2=Label(root,text='Enter User Handle:',font='Arial 17',bg='#220047',fg='#CE9141')
    hd2.place(x=20,y=80)
    handle=Entry(root, textvariable=s1, bd=5)
    handle.place(x=320,y=80)
    B1=Button(root,text='Submit',font='Arial 17',fg='#220047',bg='#CE9141')
    B1.bind("<Button-1>",info)
    B1.place(x=180,y=150)
    root.mainloop()
window()