# Basic Widgets in Tkinter

## 📋 What You'll Learn

- [Widget Overview](#widget-overview)
- [Label Widget](#label-widget)
- [Button Widget](#button-widget)
- [Entry Widget](#entry-widget)
- [Text Widget](#text-widget)
- [Frame Widget](#frame-widget)
- [Widget Styling and Configuration](#widget-styling-and-configuration)
- [Practical Examples](#practical-example)

---

**⏱️ Estimated Time:** 45 minutes  
**🎯 Prerequisites:** [Getting Started with Tkinter](01-getting-started.md) 

---

## Widget Overview
**Widgets** are the building blocks of your GUI - buttons, text fields, labels and other interactive elements that users see and interact with.  


### Widget Hierarchy
In Tkinter, the widget hierarchy refers to the parent-child relationship between widgets. Widgets are organized in a tree-like structure, where each widget can have a parent (except the root widget) and may also have child widgets. This hierarchy determines how widgets are displayed and managed within the application.

```python
Root Window (Tk)
├── Frame (container)
│   ├── Label (display text)
│   ├── Button (clickable)
│   └── Entry (text input)
└── Another Frame
    └── Text (multi-line text)
```

### Common Widget Properties

Every widget shares these fundamental properties:

| Property | Purpose | Example |
|----------|---------|---------|
| `text` | Display text | `text="Click Me"` |
| `font` | Text styling | `font=("Arial", 12, "bold")` |
| `bg` / `background` | Background color | `bg="lightblue"` |
| `fg` / `foreground` | Text color | `fg="black"` |
| `width` | Widget width | `width=20` |
| `height` | Widget height | `height=3` |
| `state` | Enable/disable | `state="disabled"` |

### Widget Creation Pattern (Reminder)

```python
# Step 1: Create the widget
widget = WidgetType(parent, configuration_options)

# Step 2: Display the widget
widget.pack()  # or .grid() or .place()
```

It can also be written as:

```python
widgetType(parent, configuration_options).pack()
```

## Label Widget
**Purpose:** Display Text or Image (Non-interactive)  

### Basic Label Creation
```python
from tkinter import *

root=Tk()

simple_label=Label(root,text="Hello")
simple_label.pack()

root.mainloop()
```

### Label Configuration Options
```python
from tkinter import *

root=Tk()
root.geometry("400x300")
root.config(bg="White")

#Basic Label
basic=Label(root,text="Basic")
basic.pack()

#styled Label
styled=Label(
    root,
    text="Styled Label",
    font=('Arial', 16, "bold"),
    fg="blue",
    bg="yellow"
)
styled.pack(pady=5)

#Multi-lined Label
multiline=Label(
    root,
    text="This is a\nmulti line\n label",
    justify="center",
    bg="lightgray"
)
multiline.pack(pady=5)

# Label with custom dimensions
sized = Label(
    root,
    text="Custom dimesion Label",
    width=20,  
    height=3,  
    bg="lightgreen",
    relief="raised",  
    borderwidth=2
)
sized.pack(pady=5)

root.mainloop()
```

## Button Widget
**Purpose:** Interactive widget that responds to clicks

### Basic Button Creation
```python
from tkinter import *

root=Tk()

button=Button(root,text="Click Here!")
button.pack(pady=10)

root.mainloop()
```

### Button With Actions
```python
from tkinter import *

def fn_click():
     label=Label(root,text="Button Clicked!")
     label.pack()
     
root=Tk()

button=Button(
    root,
    text="Click Here!",
    command=fn_click
)
button.pack(pady=10)

root.mainloop()
```

### Advanced Button Examples
```python
from tkinter import *

#Functions of the buttons
def increment():
    global counter #Global variable counter
    counter+=1
    counter_var.set(f"Count: {counter}")

def decrement():
    global counter
    counter-=1
    counter_var.set(f"Count: {counter}")
    
def reset():
    global counter
    counter=0
    counter_var.set(f"Count: {counter}")

# Main Screen
root=Tk()
root.geometry("400x400")

# Counter 
counter= 0
counter_var=StringVar()
counter_var.set(f"Count: {counter}")

counter_label=Label(root,textvariable=counter_var, font=("Arial", 14))
counter_label.pack(pady=10)

# Button creation and display
Button(root,text="Increment (+)", command=increment, bg="lightgreen", width=15).pack(pady=5)
Button(root,text="Decrement (-)", command=decrement, bg="lightcoral", width=15).pack(pady=5)
Button(root,text="Reset", command=reset, bg="lightblue", width=15).pack(pady=5)

root.mainloop()
```python
from tkinter import *

root = Tk()
root.title("Button States")

def toggle_button():
    if normal_btn["state"] == "normal":
        normal_btn.configure(state="disabled", text="Disabled",bg="pink")
    else:
        normal_btn.configure(state="normal", text="Enabled",bg="lightgreen")

# Normal button
normal_btn = Button(root, text="Enabled", bg="lightgreen")
normal_btn.pack(pady=10)

# Toggle button
toggle_btn = Button(root, text="Toggle Above Button", command=toggle_button)
toggle_btn.pack(pady=5)

# Disabled button
disabled_btn = Button(root, text="Always Disabled", state="disabled")
disabled_btn.pack(pady=10)

root.mainloop()
```

###  More Label/Button Styling Options

| Option | Values | Purpose |
|--------|--------|---------|
| `justify` | `"left"`, `"center"`, `"right"` | Text alignment |
| `anchor` | `"n"`, `"s"`, `"e"`, `"w"`, `"center"` | Position within widget |
| `relief` | `"flat"`, `"raised"`, `"sunken"`, `"groove"`, `"ridge"` | Border style |
| `borderwidth` | Integer | Border thickness |
| `wraplength` | Integer (pixels) | Text wrapping width |

## Entry Widget
**Purpose:** Single-line text input field

### Basic Entry Creation
```python
from tkinter import *

root = Tk()
root.title("Entry Examples")

# Simple entry field
entry = Entry(root)
entry.pack(pady=10)

# Get text from entry
def get_text():
    Label(root,text="User entered:"+ entry.get()).pack()

Button(root, text="Get Text", command=get_text).pack(pady=5)

root.mainloop()
``` 

### Entry with Labels and Validation
```python
from tkinter import *

root = Tk()
root.title("User Form")
root.geometry("300x300")

# Name entry
Label(root, text="Name:").pack(pady=(10,0))
name_entry = Entry(root, width=30)
name_entry.pack(pady=5)

# Email entry
Label(root, text="Email:").pack(pady=(10,0))
email_entry = Entry(root, width=30)
email_entry.pack(pady=5)

# Password entry (hidden text)
Label(root, text="Password:").pack(pady=(10,0))
password_entry = Entry(root, width=30, show="*")  # Hide characters
password_entry.pack(pady=5)

# Result display
result_var = StringVar()
result_label = Label(root, textvariable=result_var, wraplength=250, justify="left")
result_label.pack(pady=10)

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if name and email and password:
        result_var.set(f"Welcome {name}!\nEmail: {email}\nPassword: {'*' * len(password)}")
    else: #Not all fields are filled
        result_var.set("Please fill in all fields!")

def clear_form():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    result_var.set("")

# Buttons
Button(root, text="Submit", command=submit_form, 
       bg="lightgreen").pack(pady=5)
Button(root, text="Clear", command=clear_form, 
       bg="lightcoral").pack(pady=2)

root.mainloop()
```

### Entry Methods and Properties

| Method/Property | Purpose | Example |
|-----------------|---------|---------|
| `.get()` | Get current text | `text = entry.get()` |
| `.insert(index, text)` | Insert text at position | `entry.insert(0, "Hello")` |
| `.delete(start, end)` | Delete text range | `entry.delete(0, END)` |
| `show` | Hide characters | `show="*"` for passwords |
| `state` | Enable/disable | `state="readonly"` |
| `width` | Field width in characters | `width=25` |

### Advanced Entry Features
```python
from tkinter import *

root = Tk()
root.title("Advanced Entry Features")

# --------- Placeholder Entry ---------

# Function that runs when the Entry gains focus (clicked into)
def on_focus_in(event):
    # If the current text is the placeholder, clear it and set text color to black
    if placeholder_entry.get() == "Enter your name...":
        placeholder_entry.delete(0, END)
        placeholder_entry.configure(fg="black")

# Function that runs when the Entry loses focus (clicked away)
def on_focus_out(event):
    # If the input is empty, reinsert the placeholder and set text color to gray
    if placeholder_entry.get() == "":
        placeholder_entry.insert(0, "Enter your name...")
        placeholder_entry.configure(fg="gray")

# Create the placeholder Entry
placeholder_entry = Entry(root, width=30, fg="gray")  # Start with gray text
placeholder_entry.insert(0, "Enter your name...")     # Insert placeholder text
# Bind focus events to change behavior based on focus
placeholder_entry.bind("<FocusIn>", on_focus_in)
placeholder_entry.bind("<FocusOut>", on_focus_out)
placeholder_entry.pack(pady=10)  # Add some vertical padding

# --------- Number-Only Entry ---------

# Validation function that only allows digits
def validate_number(char):
    return char.isdigit()

# Register the validation function with tkinter and specify it should receive typed characters (%S)
vcmd = (root.register(validate_number), '%S')

# Create an Entry that validates input on each keypress
number_entry = Entry(root, width=30, validate='key', validatecommand=vcmd)
Label(root, text="Numbers only:").pack(pady=(10,0))  # Label for the number-only entry
number_entry.pack(pady=5)

# --------- Read-Only Entry ---------

# Create an Entry that cannot be edited
readonly_entry = Entry(root, width=30, state="readonly")
readonly_entry.pack(pady=10)

# Insert text into read-only field (must temporarily set it to "normal")
readonly_entry.configure(state="normal")         # Enable editing temporarily
readonly_entry.insert(0, "Read-only text")       # Insert fixed text
readonly_entry.configure(state="readonly")       # Set it back to read-only


root.mainloop()  
```

## Text Widget
**Purpose:** Multi-line input and display

### Basic Text Widget
```python
from tkinter import *

root = Tk()
root.title("Text Widget Example")

# Multi-line text area
text_area = Text(root, width=50, height=5)
text_area.pack(pady=10)

# Insert some initial text
text_area.insert("1.0", "This is a multi-line text widget.\nYou can type here...")

def get_all_text():
    content = text_area.get("1.0", END)
    Label(root,text="Text content: ", justify="left",fg="red").pack()
    Label(root,text=content).pack()

Button(root, text="Get All Text", command=get_all_text).pack(pady=5)

root.mainloop()
```

### Text widget with scrollbar
```python
from tkinter import *

root = Tk()
root.title("Text with Scrollbar")
root.geometry("500x200")

# Create frame to hold text and scrollbar
text_frame = Frame(root)
text_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

# Create text widget
text_area = Text(text_frame, width=50, height=15, wrap=WORD)

# Create scrollbar
scrollbar = Scrollbar(text_frame)

# Configure scrollbar
text_area.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=text_area.yview)

# Pack text and scrollbar
text_area.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Add sample text
sample_text = """This is a long text that demonstrates scrolling.
You can add as much text as you want here.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

text_area.insert("1.0", sample_text)

root.mainloop()
```

### Text Widget Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `.insert(index, text)` | Insert text at position | `text.insert("1.0", "Hello")` |
| `.get(start, end)` | Get text range | `text.get("1.0", END)` |
| `.delete(start, end)` | Delete text range | `text.delete("1.0", "2.0")` |
| `.see(index)` | Scroll to position | `text.see("end")` |

**Index Format:** `"line.character"` (e.g., `"1.0"` = line 1, character 0)

## Frame Widget
**Purpose:** Container to organise and group other widgets

### Basic Frame Usage
```python
from tkinter import *

root = Tk()
root.title("Frame Examples")
root.geometry("400x300")

# Create frames for organization
top_frame = Frame(root, bg="lightblue", height=100)
top_frame.pack(fill=X, pady=5)

bottom_frame = Frame(root, bg="lightgreen", height=100)
bottom_frame.pack(fill=X, pady=5)

# Add widgets to frames
Label(top_frame, text="Top Frame Content", bg="lightblue").pack(pady=20)
Label(bottom_frame, text="Bottom Frame Content", bg="lightgreen").pack(pady=20)

root.mainloop()
```

### Practical Frame Organisation
```python
from tkinter import *

root = Tk()
root.title("Organized Layout")
root.geometry("400x300")

# Header frame
header_frame = Frame(root, bg="navy", height=60)
header_frame.pack(fill=X)
header_frame.pack_propagate(False)  # Maintain fixed height

Label(header_frame, text="My Application",font=("Arial", 18, "bold"), fg="white", bg="navy").pack(pady=15)

# Main content frame
content_frame = Frame(root, bg="white")
content_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Left sidebar
left_frame = Frame(content_frame, bg="lightgray", width=100)
left_frame.pack(side=LEFT, fill=Y, padx=(0,10))
left_frame.pack_propagate(False)

# Right content area
right_frame = Frame(content_frame, bg="white")
right_frame.pack(side=LEFT, fill=BOTH, expand=True)

# Add content to frames
Label(left_frame, text="Menu", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)
Button(left_frame, text="Option 1", width=10).pack(pady=2)
Button(left_frame, text="Option 2", width=10).pack(pady=2)
Button(left_frame, text="Option 3", width=10).pack(pady=2)

Label(right_frame, text="Main Content Area", font=("Arial", 14)).pack(pady=20)
Text(right_frame, height=10).pack(fill=BOTH, expand=True)

root.mainloop()
```

## Widget Styling and Configuration
### Colour Scheme
```python
from tkinter import *

root = Tk()
root.title("Color Schemes")

# Light theme
light_frame = Frame(root, bg="#f0f0f0")
light_frame.pack(fill=X, pady=5)

Label(light_frame, text="Light Theme", bg="#f0f0f0", 
      font=("Arial", 12, "bold")).pack(pady=5)
Button(light_frame, text="Light Button", bg="white", 
       fg="black", relief="flat").pack(pady=2)

# Dark theme
dark_frame = Frame(root, bg="#2b2b2b")
dark_frame.pack(fill=X, pady=5)

Label(dark_frame, text="Dark Theme", bg="#2b2b2b", 
      fg="white", font=("Arial", 12, "bold")).pack(pady=5)
Button(dark_frame, text="Dark Button", bg="#404040", 
       fg="white", relief="flat").pack(pady=2)

root.mainloop()
```

### Common Color Values

| Color Name | Hex Code | RGB |
|------------|----------|-----|
| `"white"` | `"#FFFFFF"` | `(255, 255, 255)` |
| `"black"` | `"#000000"` | `(0, 0, 0)` |
| `"red"` | `"#FF0000"` | `(255, 0, 0)` |
| `"green"` | `"#008000"` | `(0, 128, 0)` |
| `"blue"` | `"#0000FF"` | `(0, 0, 255)` |
| `"lightgray"` | `"#D3D3D3"` | `(211, 211, 211)` |

## Practical Example
**User Registration Form**
```python
from tkinter import *

root = Tk()
root.title("User Registration")
root.geometry("400x500")

# Title
Label(root, text="User Registration", font=("Arial", 18, "bold")).pack(pady=10)

# Form frame
form_frame = Frame(root)
form_frame.pack(pady=20)

# Form fields
fields = ["First Name", "Last Name", "Email", "Phone", "Password"]
entries = {}

for i, field in enumerate(fields):
    Label(form_frame, text=f"{field}:", anchor="w").grid(row=i, column=0,sticky="w", pady=5)
    
    if field == "Password":
        entry = Entry(form_frame, width=30, show="*")
    else:
        entry = Entry(form_frame, width=30)
    
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[field] = entry

# Gender selection
Label(form_frame, text="Gender:", anchor="w").grid(row=len(fields), column=0, sticky="w", pady=5)

gender_var = StringVar()
gender_frame = Frame(form_frame)
gender_frame.grid(row=len(fields), column=1, sticky="w", pady=5)

Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side=LEFT)
Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side=LEFT)

# Result display
result_text = Text(root, height=8, width=50)
result_text.pack(pady=20)

def submit_form():
    result_text.delete("1.0", END)
    result_text.insert("1.0", "Registration Details:\n" + "="*30 + "\n")
    
    for field, entry in entries.items():
        value = entry.get()
        if field == "Password":
            value = "*" * len(value)
        result_text.insert(END, f"{field}: {value}\n")
    
    result_text.insert(END, f"Gender: {gender_var.get()}\n")

def clear_form():
    for entry in entries.values():
        entry.delete(0, END)
    gender_var.set("")
    result_text.delete("1.0", END)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

Button(button_frame, text="Submit", command=submit_form, bg="lightgreen", width=10).pack(side=LEFT, padx=5)
Button(button_frame, text="Clear", command=clear_form, bg="lightcoral", width=10).pack(side=LEFT, padx=5)

root.mainloop()
```

---

**Navigation:**  
[← Getting Started](01-getting-started.md) | [Next: Layout Management →](03-layout-management.md)
