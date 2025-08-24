
# Simple Calculator - Development Log
**Status:** In Progress

## Day 1: 12 June 2025
**Time Spent:** 1 Hour  
**Phase:** Basic Layout

### What I Worked On Today
- Creating the window 
- Add buttons (Numbers and Operations)
- Create a display area

### Code Progress
[Calculator Code version 1](../code/calculator-v1.py)

### What I Learned
- How to use the grid system
- *Discovered* grid padding

### Problems I Encountered
#### 1. Problem: Layout Issues with Button Grid
- Description: Calculator buttons were not positioning correctly when using a grid layout system. Unwanted gaps appeared.    
![Problem-1](/screenshoots/Problem-1.png)  

- Solution: Remove the padding parameters in the grid placement and set consistent button dimentsions:
```python
# Original (with gaps):
button_clear=Button(root, text="C")
button_clear.grid(row=1,column=0,padx=10,pady=10)

# Fixed (no gaps):
button_clear=Button(root, text="C",width=5,height=2)
button_clear.grid(row=1,column=0)
```  
![Solution-1](/screenshoots/Solution-1.png)  

- Why it happened: The gaps between the buttons were caused by the 'padx=10, pady=10* parameters in the grid condfiguration. These parameters add 10 pixels of padding around each button, which I misuderstood for width and height. I thought these specifies the width and heigth of the buttons

### Thoughts & Reflections
Always read documentation **carefully** - don't just assume how things work! This mistake taught me the importance of understanding each parameter's actual purpose before implementing it. The confusion between padding and dimensions led me to redo my notes and organize them more systematically.
  
## Day 2: 17 June 2025
**Time Spent:** 45 Minutes  
**Phase:** Basic Functionality

### What I Worked On Today
- Implement number input
- Add the decimal point operation
- Add the delete and clear functionality

### Code Progress
```python
...
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
    if "."  not in num_on_screen:
        screen.insert(0, num_on_screen + ".") # Add the dot
    else: 
        screen.insert(0, num_on_screen) # There is already a dot on the screen, so action taken(no dot)
...
```

### What I Learned
- How to make buttons respond to clicks using the `command` option in Tkinter. 
- How to use the `lambda` function to pass arguments to button commands.
- How to display button input on the screen using the `Entry` widget and methods like `.get()`, `.insert()`, and `.delete()`.

### Problems I Encountered
1. Problem: Numbers appeared backwards
- Description: When trying to enter a number like 102, the digits appeared in reverse order (e.g., 201). Each digit I clicked was being added to the start of the existing number instead of the end.
- Solution: Erase what was already on the screen, then re-display it and concatenate it with the new number entered

```python
# Original Code, showing number backwards
def press_btn(num):
    screen.insert(0,num)

button_seven=Button(root, text="7",width=5,height=2,command=lambda:press_btn(7))
# I did the same the other number buttons

# Fixed 
def press_btn(num):
    num_on_screen=screen.get() # Record what is already displayed
    screen.delete(0,END) # Erase what is on the screen
    screen.insert(0,str(num_on_screen) + str(num))  # Display what was on the screen and the new input number

button_seven=Button(root, text="7",width=5,height=2,command=lambda:press_btn(7))
# I did the same the other number buttons
```

I have found another solution which is more efficient:  
```python
def press_btn(num):
    screen.insert(END,str(num))
```

- Why it happened: Basically what happened is that I *told* Tkinter `screen.insert(0,num)` which means "Insert `num` at position `0` on the screen." So every time a number is pressed, it is inserted at the beggining (index=0)
  
### Thoughts & Reflections
While working with Tkinter, I realized how important it is to apply what we have learned before. For example, I used **slicing** in my code today; a concept that I first learned when working with list/string.   

Another takeaway is that in coding, there are usually multiple ways to solve a problem. Sometimes we take longer route (like I did first) and then later discover a simpler, more efficient solution.  That's part of the learning process and what matters most is the understanding and reaching the solution.

## Day 3: 22 June 2025
**Time Spent:** 30 Minutes  
**Phase:** Calculator Logic

### What I Worked On Today
- Implementing arithmetic operation

### Code Progress
[Calculator Code Version 2](../code/calculator-v2.py)

### What I Learned
- How to implement operator-based expression 
- Managing user input as string and converting them for calculation

### Problems I Encountered
1. Problem: Logic behind equal sign button
- Description: I struggled with figuring out how to process the entered expression, especially splitting it correctly and handling the operators.
  
### Thoughts & Reflections
It feel rewarding to see the progress I have made with the calculator sp far. Next, I will focus on thorough testing and improving the visual to make the app more user-friendly and polished. 

## Day 5: 24 August 2025
**Time Spent:** 30 Minutes  
**Phase:** Calculator Logic

### What I Worked On Today
- Some small errors when performing calculations( It was not allowing the second "dot operation" example 7.1 + 9.3, in the 9.3)

### Code Progress
[Calculator Code Version 2](../code/calculator-v2.1.py)


