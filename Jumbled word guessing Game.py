import tkinter
from tkinter import *
import random
from tkinter import messagebox

words=[]
ans=[]

r=open("words.txt",'r',encoding='UTF-8')

data=r.readlines()

for i in data:
    space=i.index(" ")
    words.append(i[0:space])
    ans.append(i[space+1:-1])

#print(words)
#print(ans)

r.close()

num = random.randrange(0,10,1)

def reset():
    global num
    num = random.randrange(0,10,1)
    lbl.config(text=words[num])
    el.delete(0,END)


def checkans():
    var = el.get()
    print("CHECCCKK")
    if var == ans[num]:
        print("CORRECT!")
        messagebox.showinfo("Success","THIS IS A CORRECT ANSWER !!")
        reset()
    else:
        print("WRONG!",var,ans[num])
        messagebox.showerror("Fail","THIS IS A WRONG ANSWER !!")
        el.delete(0,END)



root = tkinter.Tk()
root.geometry("350x380+400+300")
root.title("First Game")
root.configure(background="#7CEC9F")

lbl = Label(
    root,
    text = words[num],
    font = ("Verdana",18),
    bg = "#43BE31",
    fg = "#2C3335",
)
lbl.pack(pady=35,ipadx=30)

checkbox = StringVar()

el = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = checkbox,
)

el.pack(pady=5,ipadx=5,ipady=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    fg = "#2C3335",
    command = checkans,
).pack(pady=40)

btnreset = Button(
    root,
    text="Reset",
    font=("Comic sans ms", 16),
    width=16,
    fg="#2C3335",
    command = reset,
).pack()


root.mainloop()