from tkinter import*
from tkinter import messagebox


# Self
# def processOK():
#     print("I am OK")
    
# def processCancel():
#     messagebox.showinfo("Cancel Message","This is cancel")

# window=Tk()
# window.geometry("200x300")
# label_1=Label(window,text="Python window programming")
# label_1.pack()
# b1=Button(window,text="OK",bg="Yellow",command=processOK).pack(side=TOP)
# b2=Button(window,text="Cancel",bg="Green",command=processCancel).pack(side=TOP)
# window.mainloop()



# Task 1
root=Tk()
frame=Frame(root)
frame.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text='Red',fg='red').pack(side=LEFT)
greenbutton=Button(frame,text='Brown',fg='brown').pack(side=LEFT)
blueButton=Button(frame,text='Blue',fg='blue').pack(side=LEFT)
blackButton=Button(bottomframe,text='Black',fg='black').pack(side=BOTTOM)
root.mainloop()



# Task 2
root=Tk()
b=0

for r in range(5):
    for c in range(5):
        btn=Button(
            root,
            text=str(b),
            fg='white',
            bg='black',
            activebackground='green',
            activeforeground='blue',
            width=6,
            height=2,
            borderwidth=2,
            relief="raised",
            font=('Arial',10,'bold')
        )
        
        btn.grid(row=r,column=c)
        b=b+1
    
root.mainloop()



# Task 3
class Test:
    def __init__(self):
        top=Tk()
        L1=Label(top,text='Physics')
        L1.place(x=10,y=10)
        E1=Entry(top,bd=5).place(x=60,y=10)
        L2=Label(top,text='Maths').place(x=10,y=50)
        E2=Entry(top,bd=5).place(x=60,y=50)
        L3=Label(top,text="Total").place(x=10,y=150)
        E3=Entry(top,bd=5).place(x=60,y=150)
        B=Button(top,text='Add').place(x=100,y=100)
        top.geometry('250x250')
        top.mainloop()
        
Test()