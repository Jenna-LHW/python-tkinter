from tkinter import *
root=Tk()

# window title
root.title("Simple Calculator")

# Creating the widgets (Diplay screen and buttons)
screen=Entry(root,borderwidth=10)

button_clear=Button(root, text="C",width=5,height=2)
button_delete=Button(root, text="Del",width=10,height=2)
button_division=Button(root, text="÷",width=5,height=2)

button_seven=Button(root, text="7",width=5,height=2)
button_eight=Button(root, text="8",width=5,height=2)
button_nine=Button(root, text="9",width=5,height=2)
button_multiplication=Button(root, text="×",width=5,height=2)

button_four=Button(root, text="4",width=5,height=2)
button_five=Button(root, text="5",width=5,height=2)
button_six=Button(root, text="6",width=5,height=2)
button_minus=Button(root, text="-",width=5,height=2)

button_one=Button(root, text="1",width=5,height=2)
button_two=Button(root, text="2",width=5,height=2)
button_three=Button(root, text="3",width=5,height=2)
button_plus=Button(root, text="+",width=5,height=2)

button_zero=Button(root, text="0",width=5,height=2)
button_dot=Button(root, text=".",width=5,height=2)
button_equal=Button(root, text="=",width=10,height=2)


# Displaying the widgets
screen.grid(row=0,column=0,columnspan="4")

button_clear.grid(row=1,column=0)
button_delete.grid(row=1,column=1,columnspan="2")
button_division.grid(row=1,column=3)

button_seven.grid(row=2,column=0)
button_eight.grid(row=2,column=1)
button_nine.grid(row=2,column=2)
button_multiplication.grid(row=2,column=3)

button_four.grid(row=3,column=0)
button_five.grid(row=3,column=1)
button_six.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

button_one.grid(row=4,column=0)
button_two.grid(row=4,column=1)
button_three.grid(row=4,column=2)
button_plus.grid(row=4,column=3)

button_zero.grid(row=5,column=0)
button_dot.grid(row=5,column=1)
button_equal.grid(row=5,column=2,columnspan="2")


root.mainloop()
