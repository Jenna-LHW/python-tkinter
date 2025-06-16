# Getting Started with Tkinter

## 📋 What You'll Learn

- [Understanding Tkinter](#understanding-tkinter)
- [Import Methods and Best Practices](#import-methods)
- [Creating Your First Window](#creating-your-first-window)
- [Essential Concepts](#essential-concepts)

---  
**⏱️ Estimated Time:** 30 minutes  
**🎯 Prerequisites:** Basic Python knowledge  

---  

## Understanding Tkinter
Tkinter is Python's standard GUI toolkit that allows you to create desktop applications with windows, buttons, menus and other graphical elements.

**Why choose Tkinter?**
- **Pre-installed:** Comes with Python by default
- **Cross-platform:** Works on Winodows, macOS and Linux

---

## Import Methods
There are two primary ways to import Tkinter, each with distinct advantages:

### Method 1: 
```python
from tkinter import *
```

**Pros:**
- Cleaner, more readable code
- Direct access to all components
- Beginner-friendly syntax
- Less typing

```python
#Example
from tkinter import *

root=Tk()                       #Direct access
label=Label(root,text="Hi")     # No prefix needed 
button=button(root,text="Click!")
```  

**Cons:**
- Can conflict with other imported modules that have overlapping names

### Method 2:
```python
import tkinter as tk
```

**Pros:**
- Clean namespace management
- No naming conflicts
- Industry standard approach

```python
import tkinter as tk

root=tk.Tk()                        #Explicit prefix
label=tk.Label(root,text="Hi")
button=tk.button(root,text="Click!")
```

**Cons:**
- Requires ```tk.``` prefix for everything (*More typing*)  

### Recommendation
- **Learning/Small Projects:** Use method 1  
- **Large projects:** Use method 2

> **In this tutorial, we will be using Method 1**

## Verification
Before we continue, verify if Tkinter is available

```python
# Test if Tkniter is properly installed
try:
    import tkinter
    print("Tkinter is available!")
    print(f"Version: {tkinter.TkVersion}")

except ImportError:
    print("Tkinter is not available")
```

---

## Creating Your First Window
Every Tkinter application starts with a main window.

```python
from tkinter import *

root=Tk()

root.mainloop()
```

**Understanding the code**
```python
from tkinter import *   #Import all Tkinter components

root=Tk()               #Create the main window object
                        # By convention the main window is called 'root'

root.mainloop()         #Start the event loop
                        # Keeps the window responsive to user actions
                        # MUST be the last line
```

## Adding Basic Customisation
```python
from tkinter import *

# Create and configure main window
root=Tk()
root.title("My First Window")   # Set window title
root.geometry("300x400")        # Set size of window (width X height)
root.configure(bg="lightblue")  # Set backgorund(bg) colour to lightblue

# Set minimum and maximum size of window
root.minsize(300,200)           # Minimum size width, height
root.maxsize(800,600)           # Maximum size width. height

# Start the event loop
root.mainloop()
```
## Window configuration Options

| Method | Purpose | Syntax | Example |
|--------|---------|---------|---------|
| `title()` | Set window title | `.title("Title")` | `root.title("Calculator")` |
| `geometry()` | Set size and position | `.geometry("widthxheight±xoffset±yoffset")`  Note:  **Window size** – widthxheight. **Window position** – X and Y distance from the top-left corner of the screen| `root.geometry("400x300+100+50")` |
| `configure()` | Set properties | `.configure()` – comes from older versions of Tk()  `.config()` – is just a shorter alias and is more commonly used for convenience.  `.Config()`, can be used on any widget to change settings that you may have applied earlier, or haven’t applied yet. | `root.configure(bg="white")` |
| `minsize()` | Set minimum size | `.minsize(width,height)` | `root.minsize(300, 200)` |
| `maxsize()` | Set maximum size | `.maxsize(width, height)` | `root.maxsize(800, 600)` |
| `resizable()` | Control resize ability | `.resizable(height=None, width=None)`  Arguments to be passed: **Positive integer or True** - to make window resizable. **0 or False** - to make window non-resizable | `root.resizable(True, True)`  `root.resizable(0, 0)` |
---

## Essential Concepts
### The Root Window

- **Purpose:** Main container for the entire application
- **Convention:** Usally named `root` or `app`

### The Event Loop
```python
root.mainloop()
```

**What it does:**
- Keeps the window visible and responsive
- Processes user interactions
- Updates the display when needed
- Runs continously until the window is closed

**Important Rules**
- Must the ***last line** in your program
- Only call it once per application
- Everything else must be set up before calling `mainloop()`


### Widget Creation 
Every widget in Tkinter follows 2 steps:
```python
#Step 1: Create the widget
Widget = widgetType(parent, options...)

#Step 2: Display the widget 
widget.pack() 
```
---

**Navigation:**  
[← Back to Notes Index](README.md) | [Next: Basic Widgets →](02-basic-widgets.md)
