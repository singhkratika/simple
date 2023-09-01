from tkinter import*
def add():
 a=int(n1.get())
 b=int(n2.get())
 c=a+b
 res.config(text=str(c))
def sub():
 a=int(n1.get())
 b=int(n2.get())
 c=a-b
 res.config(text=str(c))
def mul():
 a=int(n1.get())
 b=int(n2.get())
 c=a*b
 res.config(text=str(c))
def div():
 a=int(n1.get())
 b=int(n2.get())
 c=a/b
 res.config(text=str(c))
root=Tk()
root.title("simple calculator")
root.geometry("500x400+500+200")

lbl=Label(root,text="simple calculator",fg="blue",font=("Arial 20 bold"))
lbl.place(x=150,y=20)
lbl1=Label(root,text="enter first no:",fg="black",font=("Arial 15 bold"))
lbl1.place(x=40,y=60)
n1=Entry(root,font=("Arial 15"))
n1.place(x=200,y=60)
lbl2=Label(root,text="enter second no:",fg="black",font=("Arial 15 bold"))
lbl2.place(x=40,y=100)
n2=Entry(root,font=("Arial 15"))
n2.place(x=210,y=100)
res=Label(root,text="enter result:",fg="black",font=("Arial 15 bold"))
res.place(x=40,y=200)
btnadd=Button(root,text="ADD",font=("Arial 15"),fg="blue",command=add)
btnadd.place(x=40,y=250)
btnsub=Button(root,text="sub",font=("Arial 15"),fg="blue",command=sub)
btnsub.place(x=40,y=300)
btnmul=Button(root,text="MUL",font=("Arial 15"),fg="blue",command=mul)
btnmul.place(x=40,y=350)
btndiv=Button(root,text="DIV",font=("Arial 15"),fg="blue",command=div)
btndiv.place(x=40,y=400)

root.mainloop()

