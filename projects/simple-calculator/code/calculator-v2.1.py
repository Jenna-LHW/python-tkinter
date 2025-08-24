
from tkinter import *
root=Tk()

# window title
root.title("Simple Calculator")

def press_clear_btn():
    screen.delete(0,END) # Delete the entire screen

def press_btn(num):
    num_on_screen=screen.get() # Record what is already displayed
    screen.delete(0,END) # Erase what is on the screen
    screen.insert(0,str(num_on_screen) + str(num))  # Display what was on the screen and the new input number

def press_del_btn():
    num_on_screen=screen.get() #get what is on the screen
    screen.delete(0,END) # Delete what is on the screen
    num_on_screen=num_on_screen[:-1] # Slice the string; Remove the last character
    screen.insert(0,num_on_screen)  #Display it on the screen

def press_dot_btn():
    num_on_screen=screen.get() #get what is on the screen
    screen.delete(0,END) # Delete what is on the screen
    
    operators = ["+", "-", "×", "÷"]
    
    # Find the operator
    operator_pos = -1
    for i, char in enumerate(num_on_screen):
        if char in operators:
            operator_pos = i
            break  # Found it, stop looking
        
    # Split into two parts (Before and after operator)
    if operator_pos == -1:
        # No operator found, entire string is the current number(Only 1 number entered)
        current_number = num_on_screen
    else:
        # Everything after the operator is the current number
        current_number = num_on_screen[operator_pos + 1:]
    
    if "."  not in current_number:
        screen.insert(0, num_on_screen + ".") # Add the dot
    else: 
        screen.insert(0, num_on_screen) # There is already a dot on the screen, so action taken(no dot)

def add_btn():
    num_on_screen=screen.get()
    if num_on_screen != "":
        screen.delete(0,END) # Delete what is on the screen
        screen.insert(0, num_on_screen + "+") # Add the plus sign
        
def minus_btn():
    num_on_screen=screen.get()
    if num_on_screen != "":
        screen.delete(0,END) # Delete what is on the screen
        screen.insert(0, num_on_screen + "-") # Add the minus sign

def divide_btn():
    num_on_screen=screen.get()
    if num_on_screen != "":
        screen.delete(0,END) # Delete what is on the screen
        screen.insert(0, num_on_screen + "÷") # Add the divide sign

def multiply_btn():
    num_on_screen=screen.get()
    if num_on_screen != "":
        screen.delete(0,END) # Delete what is on the screen
        screen.insert(0, num_on_screen + "×") # Add the divide sign

def equal_btn():
    op_list = ["+", "-", "×", "÷"]
    num_on_screen = screen.get()
    
    for op in op_list:
        if op in num_on_screen:
            num1, num2 = num_on_screen.split(op)
            num1 = float(num1)
            num2 = float(num2)
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "×":
                result = num1 * num2
            elif op == "÷":
                if num2 == 0:
                    result = "Error"
                else:
                    result = num1 / num2
            else:
                result = "Error"
            
            screen.delete(0, "end")
            screen.insert(0, f"{num1} {op} {num2} = {result}")
            break  # Done, no need to check other ops


# Creating the widgets (Diplay screen and buttons)
screen=Entry(root,borderwidth=10)

button_clear=Button(root, text="C",width=5,height=2,command=press_clear_btn)
button_delete=Button(root, text="Del",width=10,height=2,command=press_del_btn)
button_division=Button(root, text="÷",width=5,height=2,command=divide_btn)

button_seven=Button(root, text="7",width=5,height=2,command=lambda:press_btn(7))
button_eight=Button(root, text="8",width=5,height=2,command=lambda:press_btn(8))
button_nine=Button(root, text="9",width=5,height=2,command=lambda:press_btn(9))
button_multiplication=Button(root, text="×",width=5,height=2,command=multiply_btn)

button_four=Button(root, text="4",width=5,height=2,command=lambda:press_btn(4))
button_five=Button(root, text="5",width=5,height=2,command=lambda:press_btn(5))
button_six=Button(root, text="6",width=5,height=2,command=lambda:press_btn(6))
button_minus=Button(root, text="-",width=5,height=2,command=minus_btn)

button_one=Button(root, text="1",width=5,height=2,command=lambda:press_btn(1))
button_two=Button(root, text="2",width=5,height=2,command=lambda:press_btn(2))
button_three=Button(root, text="3",width=5,height=2,command=lambda:press_btn(3))
button_plus=Button(root, text="+",width=5,height=2,command=add_btn)

button_zero=Button(root, text="0",width=5,height=2,command=lambda:press_btn(0))
button_dot=Button(root, text=".",width=5,height=2,command=press_dot_btn)
button_equal=Button(root, text="=",width=10,height=2,command=equal_btn)


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

