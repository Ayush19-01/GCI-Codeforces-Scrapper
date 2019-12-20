#Made for the sole purpose of GCI 2019
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import Tk
from tkinter import StringVar
from tkinter import messagebox
import requests


def info(event):
    global root
    global s1
    global user

    try:
        user=s1.get()
        url=requests.get('https://codeforces.com/api/user.info?handles=' + user)
        soup=BeautifulSoup(url.text, 'lxml')
        a=(soup.get_text())
        b=eval(a)
        d=b['result'][0]
        print(d)
        rank=d['rank']
        handle=d['handle']
        rating=d['rating']
        rated=d['maxRating']
        ranked=d['maxRank']
        data(rank, handle, rating, rated, ranked, user)
    except:
       messagebox.showerror("Error","The handle entered doesn't exist or has no trackable data!")


def data(a, b, c, d, e, f):
    global root2
    root2 = Tk()
    root2.title('Statistics')
    root2.geometry('600x300')
    root2.config(bg="#220047")
    hd1=Label(root2, text='Codeforces stats for :'+" "+f, font='Arial 24 underline', bg='#220047', fg='#CE9141')
    hd1.place(x=110, y=10)
    hd3=Label(root2, text="I) Rank >>>>>>>>>>>"+" "+str(a), font='Arial 17', bg='#220047', fg='#CE9141')
    hd3.place(x=50, y=80)
    hd5=Label(root2, text="II) Handle >>>>>>>>>"+" "+str(b), font='Arial 17', bg='#220047', fg='#CE9141')
    hd5.place(x=50, y=120)
    hd7=Label(root2, text="III) Current Rating >>>"+" "+str(c), font='Arial 17', bg='#220047', fg='#CE9141')
    hd7.place(x=50, y=160)
    hd9 = Label(root2, text="IV) Max Rating >>>>>"+" "+str(d), font='Arial 17', bg='#220047', fg='#CE9141')
    hd9.place(x=50, y=200)
    hd11 = Label(root2, text="V) Max Ranking >>>"+" "+str(e), font='Arial 17', bg='#220047', fg='#CE9141')
    hd11.place(x=50, y=240)
    root2.mainloop()
def main():
    global root
    global s1
    root = Tk()
    root.title('Codeforces Scrapper')
    root.geometry('500x200')
    root.configure(bg='#220047')
    s1 = StringVar()
    hd1 = Label(root, text='Data Scrapper', font='Arial 30', bg='#220047', fg='#CE9141')
    hd1.place(x=120, y=10)
    hd2 = Label(root, text='Enter User Handle:', font='Arial 17', bg='#220047', fg='#CE9141')
    hd2.place(x=20, y=80)
    handle = Entry(root, textvariable=s1,width=40)
    handle.place(x=220, y=87)
    B1 = Button(root, text='Submit', font='Arial 17', fg='#220047', bg='#CE9141',activebackground='#220047', activeforeground='#CE9141')
    B1.bind("<Button-1>", info)
    B1.place(x=200, y=140)
    root.mainloop()
main()
