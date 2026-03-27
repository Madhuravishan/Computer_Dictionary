from tkinter import*
win=Tk()
win.title("dictionary")
win.geometry("600x400")
dic={"padx":10,"pady":10}

Label(win,text="Computer Dictionary",font="none 20")\
        .grid(row=0,column=0,columnspan=3,**dic,sticky=N)

lb1=Label(win,text="input word to define",font="none 15",**dic)
lb1.grid(row=2,column=0,sticky=W,columnspan=3)


def search():
    word=entr1.get()
    word=word.lower()
    txt1.delete(0.0,END)
    try:
        defi=dic[word]
    except:
        defi="Sorry! This word is not in my Dictionary"
    txt1.insert(END,defi)
        
    
def clear():
    entr1.delete(0,END)
    txt1.delete(0.0,END)
    
win=Tk()
win.title("dictionary")
win.geometry("800x250")
win.configure(bg="#708090")
win.resizable(0,0)


dic= {
    "cpu": "Central Processing Unit",
    "ram": "Random Access Memory",
    "alu": "Arithmetic and Logic Unit",
    "rom": "Read Only Memory",
    "http": "Hyper Text Transfer Protocol",
    "ip": "Internet Protocol",
    "url": "Uniform Resource Locator",
    "usb": "Universal Serial Bus",
    "ssd": "Solid State Drive",
    "hdd": "Hard Disk Drive",
    "gui": "Graphical User Interface",
    "cli": "Command Line Interface",
    "os": "Operating System",
    "vpn": "Virtual Private Network",
    "api": "Application Programming Interface",
    "sql": "Structured Query Language",
    "xml": "Extensible Markup Language",
    "dns": "Domain Name System",
    "lan": "Local Area Network",
    "wan": "Wide Area Network",
    "mac": "Media Access Control",
    "ip": "Internet Protocol",
    "pdf": "Portable Document Format",
    "jpg": "Joint Photographic Experts Group",
    "png": "Portable Network Graphics",
    "html": "HyperText Markup Language",
    "css": "Cascading Style Sheets",
    "js": "JavaScript",
    "dos": "Disk Operating System"
}


lbl=Label(win,text="Computer Dictionary",font="none 20",bg="#708090")
lbl.place(x=250,y=10)

lbl1=Label(win,text="Input a word to define",font="none 15",bg="#708090")
lbl1.place(x=20,y=100)
lbl2=Label(win,text="Definition of word:",font="none 15",bg="#708090")
lbl2.place(x=20,y=150)
entr1=Entry(win,font="none 15",width=25)
entr1.place(x=250,y=100)
txt1=Text(win,font="none 15",height=2,width=25)
txt1.place(x=250,y=150)

btnsrh=Button(win,text="Search",font="none 15",width="6",bg="darkgray",command=search)
btnsrh.place(x=600,y=100)
win.bind("<Return>",lambda event:search())

btnclr=Button(win,text="Clear",font="none 15",width="6",bg="darkgray",command=clear)
btnclr.place(x=600,y=155)
win.bind("<Escape>",lambda event:clear())




win.mainloop()

