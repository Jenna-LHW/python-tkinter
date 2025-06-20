# Event Handling

## 📋 What You'll Learn
- [Basic Event Concepts](#basic-event-concepts)
- [Command Parameter](#command-parameter)
- [Bind Method](#bind-method)
- [Common Event Types](#common-event-types)
- [Event Object](#event-object)
- [Mouse Events](#mouse-events)
- [Keyboard Events](#keyboard-events)
- [Window Events](#window-events)
- [Lambda Functions in Event Handling](#lambda-functions-in-event-handling)
- [Practical Examples](#practical-examples)

---
**Estimated Time:** 45 Minutes  
**Prerequisities:** [Layout Management](03-layout-management.md)

---

## Basic Event Concepts
In Tkinter, events are things that happen during the execution of your program - user clicks, key presses, window resizing, etc. Event handling is the process of defining what should happen when these events occur.

There are two main ways to handle events in TKinter:
1. **Command parameter** - for simple widget-specific events
2. **Bind method** - for more complex event handling

## Command Parameter
The simplest way to handle events is using the `command` parameter available in many widgets.

```python
from tkinter import *

root=Tk()
root.title("Command Example")
root.geometry("200x100")

def click():
    label.config(text="Button clicked!")
    label.pack()

Button(root,text="Click Me!",command=click).pack()
label=Label(root,text="Waiting for click ...")
label.pack()

root.mainloop()
```
**Widgets that support command parameter:**
- Button
- Checkbutton
- Radiobutton
- Menubutton
- Scale

## Bind Method
The `bind()` method is more flexible and can handle a wider variety of events.

### Syntax
```ptyhon
widget.bind(event,handler)
```

### Basic bind example:
```python
from tkinter import *

def on_enter(event):
    button.config(bg="lightblue")

def on_leave(event):
    button.config(bg="SystemButtonFace")

root=Tk()
root.geometry("200x100")

button=Button(root,text="Hover over me")
button.pack(pady=20)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
```

## Common Event Types

| Event String | Description |
|--------------|-------------|
| `<Button-1>` | Left mouse button click |
| `<Button-2>` | Middle mouse button click |
| `<Button-3>` | Right mouse button click |
| `<Double-Button-1>` | Left mouse button double-click |
| `<ButtonRelease-1>` | Left mouse button release |
| `<Motion>` | Mouse movement |
| `<Enter>` | Mouse enters widget area |
| `<Leave>` | Mouse leaves widget area |
| `<Key>` | Any key press |
| `<KeyPress-a>` | Specific key press (letter 'a') |
| `<KeyRelease>` | Any key release |
| `<Return>` | Enter key |
| `<Space>` | Spacebar |
| `<BackSpace>` | Backspace key |
| `<Delete>` | Delete key |
| `<Up>`, `<Down>`, `<Left>`, `<Right>` | Arrow keys |
| `<F1>`, `<F2>`, etc. | Function keys |
| `<Control-c>` | Ctrl+C combination |
| `<Alt-F4>` | Alt+F4 combination |
| `<FocusIn>` | Widget gains focus |
| `<FocusOut>` | Widget loses focus |
| `<Configure>` | Widget is resized or moved |  

## Event Object

When an event occurs, Tkinter creates an event object that contains information about the event. This object is passed to your event handler function.

### Common Event Object Attributes:

| Attribute | Description |
|-----------|-------------|
| `event.x`, `event.y` | Mouse coordinates relative to widget |
| `event.x_root`, `event.y_root` | Mouse coordinates relative to screen |
| `event.char` | Character typed (for key events) |
| `event.keysym` | Key symbol (for key events) |
| `event.keycode` | Numeric key code |
| `event.num` | Button number (for mouse events) |
| `event.width`, `event.height` | Widget dimensions (for configure events) |
| `event.widget` | Widget that triggered the event |

### Example using event attributes:
```python
from tkinter import *

root = Tk()
root.title("Event Object Example")

info_label = Label(root, text="Event information will appear here")
info_label.pack(pady=10)

def show_event_info(event):
    info_text = f"Event: {event.type}\n"
    info_text += f"Coordinates: ({event.x}, {event.y})\n"
    info_text += f"Widget: {event.widget.winfo_class()}"
    info_label.config(text=info_text)

canvas = Canvas(root, width=300, height=200, bg="lightgray")
canvas.bind("<Button-1>", show_event_info)
canvas.bind("<Motion>", show_event_info)
canvas.pack(pady=10)

root.mainloop()

```

## Mouse Events
### Complete mouse event example:
```python
from tkinter import *

root = Tk()
root.title("Mouse Events")

status_label = Label(root, text="Mouse events will be shown here")
status_label.pack(pady=10)

def left_click(event):
    status_label.config(text=f"Left click at ({event.x}, {event.y})")

def right_click(event):
    status_label.config(text=f"Right click at ({event.x}, {event.y})")

def double_click(event):
    status_label.config(text=f"Double click at ({event.x}, {event.y})")

def mouse_enter(event):
    event.widget.config(bg="lightblue")
    status_label.config(text="Mouse entered the area")

def mouse_leave(event):
    event.widget.config(bg="lightgray")
    status_label.config(text="Mouse left the area")

def mouse_motion(event):
    status_label.config(text=f"Mouse at ({event.x}, {event.y})")

canvas = Canvas(root, width=300, height=200, bg="lightgray")
canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
canvas.bind("<Double-Button-1>", double_click)
canvas.bind("<Enter>", mouse_enter)
canvas.bind("<Leave>", mouse_leave)
canvas.bind("<Motion>", mouse_motion)
canvas.pack(pady=10)

root.mainloop()
```

## Keyboard Events

### Key press handling:
```python
from tkinter import *

root = Tk()
root.title("Keyboard Events")
root.focus_set()  # Make sure the window can receive key events

output_text = Text(root, width=50, height=10)
output_text.pack(pady=10)

def key_pressed(event):
    output_text.insert(END, f"Key pressed: {event.keysym} (char: {event.char})\n")
    output_text.see(END)  # Scroll to bottom

def special_keys(event):
    if event.keysym == "Return":
        output_text.insert(END, "Enter key pressed!\n")
    elif event.keysym == "BackSpace":
        output_text.insert(END, "Backspace pressed!\n")
    elif event.keysym == "Delete":
        output_text.insert(END, "Delete pressed!\n")
    output_text.see(END)

def ctrl_combination(event):
    output_text.insert(END, f"Ctrl+{event.keysym} pressed!\n")
    output_text.see(END)

# Bind to root window to capture all key events
root.bind("<Key>", key_pressed)
root.bind("<Return>", special_keys)
root.bind("<BackSpace>", special_keys)
root.bind("<Delete>", special_keys)
root.bind("<Control-c>", ctrl_combination)
root.bind("<Control-v>", ctrl_combination)

instruction_label = Label(root, text="Click here and press any keys")
instruction_label.pack(pady=5)

root.mainloop()
```

## Window Events

### Window-related events:
```python
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Window Events")

status_label = Label(root, text="Window event information")
status_label.pack(pady=10)

def window_configured(event):
    if event.widget == root:  # Only track root window changes
        status_label.config(text=f"Window resized to: {event.width}x{event.height}")

def window_focus_in(event):
    if event.widget == root:
        status_label.config(text="Window gained focus")
        root.config(bg="lightblue")

def window_focus_out(event):
    if event.widget == root:
        status_label.config(text="Window lost focus")
        root.config(bg="lightgray")

def window_closing():
    result = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if result:
        root.destroy()

root.bind("<Configure>", window_configured)
root.bind("<FocusIn>", window_focus_in)
root.bind("<FocusOut>", window_focus_out)
root.protocol("WM_DELETE_WINDOW", window_closing)  # Window close button

root.mainloop()
```
## Lambda Functions in Event Handling

Lambda functions are useful for passing arguments to event handlers or for simple operations.

```python
from tkinter import *

root =  Tk()
root.title("Lambda Functions")

result_label =  Label(root, text="Click a button")
result_label.pack(pady=10)

# Using lambda to pass arguments
def button_clicked(button_name):
    result_label.config(text=f"{button_name} was clicked!")

button1 =  Button(root, text="Button 1", 
                   command=lambda: button_clicked("Button 1"))
button1.pack(pady=5)

button2 =  Button(root, text="Button 2", 
                   command=lambda: button_clicked("Button 2"))
button2.pack(pady=5)

# Lambda for simple operations
counter = 0
counter_label =  Label(root, text=f"Counter: {counter}")
counter_label.pack(pady=10)

def update_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Counter: {counter}")

increment_button =  Button(root, text="Increment", 
                           command=lambda: update_counter())
increment_button.pack(pady=5)

root.mainloop()
```

## Practical Examples
### Example 1: Simple Drawing Application
```python
from tkinter import *

root = Tk()
root.title("Simple Drawing App")

canvas = Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Variables to track drawing
drawing = False
last_x = 0
last_y = 0

def start_drawing(event):
    global drawing, last_x, last_y
    drawing = True
    last_x = event.x
    last_y = event.y

def draw(event):
    global drawing, last_x, last_y
    if drawing:
        canvas.create_line(last_x, last_y, event.x, event.y, width=2)
        last_x = event.x
        last_y = event.y

def stop_drawing(event):
    global drawing
    drawing = False

def clear_canvas():
    canvas.delete("all")

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=5)

root.mainloop()
```
### Example 2: Form with validation

```python
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Interactive Form")

# Create form fields
Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Age:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
age_entry = Entry(root, width=30)
age_entry.grid(row=2, column=1, padx=5, pady=5)

# Status label
status_label = Label(root, text="Fill out the form", fg="blue")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

def validate_name(event):
    name = name_entry.get()
    if len(name) < 2:
        status_label.config(text="Name must be at least 2 characters", fg="red")
    else:
        status_label.config(text="Name looks good", fg="green")

def validate_email(event):
    email = email_entry.get()
    if "@" not in email or "." not in email:
        status_label.config(text="Please enter a valid email", fg="red")
    else:
        status_label.config(text="Email looks good", fg="green")

def validate_age(event):
    try:
        age = int(age_entry.get())
        if age < 0 or age > 120:
            status_label.config(text="Please enter a valid age (0-120)", fg="red")
        else:
            status_label.config(text="Age looks good", fg="green")
    except ValueError:
        status_label.config(text="Age must be a number", fg="red")

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    try:
        age = int(age_entry.get())
        if len(name) >= 2 and "@" in email and "." in email and 0 <= age <= 120:
            messagebox.showinfo("Success", f"Form submitted!\nName: {name}\nEmail: {email}\nAge: {age}")
        else:
            messagebox.showerror("Error", "Please fix the form errors before submitting")
    except ValueError:
        messagebox.showerror("Error", "Please fix the form errors before submitting")

# Bind validation events
name_entry.bind("<KeyRelease>", validate_name)
email_entry.bind("<KeyRelease>", validate_email)
age_entry.bind("<KeyRelease>", validate_age)

# Submit button
submit_button = Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Allow Enter key to submit form
root.bind("<Return>", lambda event: submit_form())

root.mainloop()
```
---

**Navigation:**  
[← Layout Managenment](03-layout-managment.md) 
