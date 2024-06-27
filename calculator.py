from tkinter import * 

root=Tk()
root.title("Calculator")
root.geometry("465x484")
root.config(bg="light blue")

expression = ""
def show(value):
    global expression
    expression+=value
    label_result.config(text=expression)

def clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)  
    

label_result= Label(root,width=25,height=2,text="",font=("arial",30),bg="pink")
label_result.pack()

Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="blue",command=lambda : clear()).place(x=1,y=97)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("/")).place(x=120,y=97)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("%")).place(x=240,y=97)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("*")).place(x=350,y=97)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("7")).place(x=1,y=176)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("8")).place(x=120,y=176)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("9")).place(x=240,y=176)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("-")).place(x=350,y=176)


Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("4")).place(x=1,y=255)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("5")).place(x=120,y=255)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("6")).place(x=240,y=255)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("+")).place(x=350,y=255)


Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("1")).place(x=1,y=334)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("2")).place(x=120,y=334)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("3")).place(x=240,y=334)


Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show(".")).place(x=1,y=413)
Button(root,text="0",width=10,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : show("0")).place(x=120,y=413)

Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="green",command=lambda : calculate()).place(x=350,y=334)


root.mainloop()

