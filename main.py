import tkinter
from tkinter import *
import string
import random
from tkinter import messagebox
#===============Root Window=====================
root=tkinter.Tk()

root.title('Password Generator')
root.resizable(0,0)
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
h=610
w=600

x=ws//2-w//2
y=hs//2-h//2
window=str(w)+'x'+ str(h)+'+'+str(x)+'+'+str(y)

root.geometry(window)
# root.wm_iconbitmap('Icon.ico')

#=====================Functions=================

def about():
    messagebox.showinfo('Password Generator','Password Generator\nVersion 1.1  -Nabla')



dark=IntVar()
def darkon():
    dark.set(1)
    global BtnGetpass
    
    tops.configure(bg='#181818')
    Bottoms.configure(bg='#181818',)
    passtext.configure(bg='#181818')
    lbl_length.configure(bg='#181818',fg='white')
    lbl_much.configure(bg='#181818',fg='white')
    BtnGetpass.configure(bg='#181818',fg='white')

def exit():
    p=tkinter.messagebox.askyesno('Password Generator','Do You Want to exit ?')
    if p>0:
        root.destroy()

def getpass(size=8,chars=string.digits+string.ascii_letters+string.punctuation):

    r=int(muchtry.get())
    k=int(lentry.get())
    try:
        if (r>1000000):
            messagebox.showinfo('Password Generator','Out of Range!')
            muchtry.set('')
            lentry.set('')



        elif k<=7:
            messagebox.showinfo('Password Generator','Password Length Would be Greater Than 7 Character')
            muchtry.set('')
            lentry.set('')

        elif (r==0 or k==0):
                        messagebox.showinfo('Password Generator','Zero is not a valid option!')
                        muchtry.set('')
                        lentry.set('')


        elif r==1:
            for r in range(r,0,-1):
                p= f'{r}:\t{"".join(random.choice(chars) for _ in range(int(lentry.get())))}'
                passtext.insert(0.0,p)
                passtext.insert(0.0,'\n')

            q='Your unique Password is:\n'
            passtext.insert(0.0,q)
            nabla=dark.get()
            if nabla==1:
                resetbtn=Button(Bottoms,text='Reset',bd=5,bg='#181818',font='lucida 12 bold',fg='white',command=Reset,height=2,width=11)
                resetbtn.grid(row=0,column=3,rowspan=2,padx=10)
            else:
                resetbtn=Button(Bottoms,text='Reset',bd=5,bg='cadet blue',font='lucida 12 bold',command=Reset,height=2,width=11)
                resetbtn.grid(row=0,column=3,rowspan=2,padx=10)

        else:
            for r in range(r,0,-1):
                p= f'{r}:\t{"".join(random.choice(chars) for _ in range(int(lentry.get())))}'
                passtext.insert(0.0,p)
                passtext.insert(0.0,'\n')

            q='Your unique Passwords Are:\n'
            passtext.insert(0.0,q)
            nabla=dark.get()
            if nabla==1:
                resetbtn=Button(Bottoms,text='Reset',bd=5,bg='#181818',font='lucida 12 bold',fg='white',command=Reset,height=2,width=11)
                resetbtn.grid(row=0,column=3,rowspan=2,padx=10)
            else:
                resetbtn=Button(Bottoms,text='Reset',bd=5,bg='cadet blue',font='lucida 12 bold',command=Reset,height=2,width=11)
                resetbtn.grid(row=0,column=3,rowspan=2,padx=10)
    


    except Exception as e:
        raise ValueError('Oh No!')
        messagebox.showinfo('Password Generator','Some thing went wrong!\nPlease Try Again!')



    


    
def Reset():
    passtext.delete(0.0,END)
    muchtry.set('')
    lentry.set('')
    nabla2=dark.get()
    if nabla2==1:
            BtnGetpass=Button(Bottoms,text='Get Password',bd=5,bg='#181818',font='lucida 12 bold',fg='white',command=getpass,height=2)
            BtnGetpass.grid(row=0,column=3,rowspan=2,padx=10)

    else:    
        BtnGetpass=Button(Bottoms,text='Get Password',bd=5,bg='cadet blue',font='lucida 12 bold',command=getpass,height=2)
        BtnGetpass.grid(row=0,column=3,rowspan=2,padx=10)


#==========================Frames========================================

tops=Frame(root,bg='powder blue',relief=SUNKEN,bd=2)
tops.pack(side=TOP)

Bottoms=Frame(root,bg='powder blue',relief=SUNKEN,bd=10)
Bottoms.pack(side=TOP,pady=15)


lentry=StringVar()
muchtry=StringVar()

#============================lavel+Entry==================================
lbl_length=Label(Bottoms,text='Enter The Lenght:',font='lucida 12 bold',bg='powder blue')
lbl_length.grid(row=0,column=0,pady=10,padx=10)

lenght_entry=Entry(Bottoms,font='lucida 15 bold',textvariable=lentry)
lenght_entry.grid(row=0,column=1,padx=5)


lbl_much=Label(Bottoms,text='How Many Password:',font='arial 12 bold',bg='powder blue')
lbl_much.grid(row=1,column=0,pady=10)
much_entry=Entry(Bottoms,font='arial 15 bold',textvariable=muchtry)
much_entry.grid(row=1,column=1,)




#=====================Buttons==============================================

BtnGetpass=Button(Bottoms,text='Get Password',bd=5,bg='cadet blue',font='lucida 12 bold',command=getpass,height=2)
BtnGetpass.grid(row=0,column=3,rowspan=2,padx=10)
#=================================FileMenu===============================

mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_cascade(label='About',command=about)
m1.add_cascade(label='Dark Mode',command=darkon)
m1.add_cascade(label='Reset',command=Reset)
m1.add_cascade(label='Exit',command=exit)
mymenu.add_cascade(label='File',menu=m1)
root.config(menu=mymenu)


#======================================ScrollBar============================


scrollbar=Scrollbar(tops)
scrollbar.pack(side=RIGHT,fill=Y)
passtext=Text(tops,font='arial 12',fg='red',bd=5,yscrollcommand=scrollbar.set)
passtext.pack(padx=5,pady=5,fill=BOTH)
scrollbar.config(command=passtext.yview)

#-----------------xxxxxxxxxxxxxx-----------------xxxxxxxxxxxxxx------------------

root.mainloop()