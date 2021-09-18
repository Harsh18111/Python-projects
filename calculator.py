from tkinter import *

demo = Tk()
demo.title("calculator")
demo.config(bg="black")

#input box
e = Entry(demo, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#functions

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num)) 

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global op
    op = "add"

def button_minus():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global op
    op = "minus"

def button_multi():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global op
    op = "multi"

def button_div():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    global op
    op = "div"

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if op == "add":
        e.insert(0, f_num + int(second_number))
    elif op == "minus":
        e.insert(0, f_num - int(second_number))
    elif op == "multi":
        e.insert(0, f_num * int(second_number))
    elif op == "div":
        e.insert(0, f_num / int(second_number))
        



#button variables

btn_1 = Button(demo, text="1", padx=40, pady=20, bg="grey", command=lambda: button_click(1))
btn_2 = Button(demo, text="2", padx=40, pady=20, bg="grey", command=lambda: button_click(2))
btn_3 = Button(demo, text="3", padx=40, pady=20, bg="grey", command=lambda: button_click(3))
btn_4 = Button(demo, text="4", padx=40, pady=20, bg="grey", command=lambda: button_click(4))
btn_5 = Button(demo, text="5", padx=40, pady=20, bg="grey", command=lambda: button_click(5))
btn_6 = Button(demo, text="6", padx=40, pady=20, bg="grey", command=lambda: button_click(6))
btn_7 = Button(demo, text="7", padx=40, pady=20, bg="grey", command=lambda: button_click(7))
btn_8 = Button(demo, text="8", padx=40, pady=20, bg="grey", command=lambda: button_click(8))
btn_9 = Button(demo, text="9", padx=40, pady=20, bg="grey", command=lambda: button_click(9))
btn_0 = Button(demo, text="0", padx=40, pady=20, bg="grey", command=lambda: button_click(0))
btn_clear = Button(demo, text="Clear", padx=30, pady=20, bg="light grey", command=lambda: button_clear())
btn_equal = Button(demo, text="=", padx=40, pady=20, bg="light grey", command=lambda: button_equal())
btn_add = Button(demo, text="+", padx=40, pady=20, bg="orange", command=lambda: button_add())
btn_minus = Button(demo, text="-", padx=40, pady=20, bg="orange", command=lambda: button_minus())
btn_multi = Button(demo, text="x", padx=40, pady=20, bg="orange", command=lambda: button_multi())
btn_div = Button(demo, text="/", padx=40, pady=20, bg="orange", command=lambda: button_div())


#button alignment on screen

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

btn_clear.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_add.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multi.grid(row=3, column=3)
btn_div.grid(row=4, column=3)


demo.mainloop()