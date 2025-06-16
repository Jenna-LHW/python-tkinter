# Layout Management in Tkinter

## 📋 What You'll Learn

- [Geometry Manager Overview](#geometry-manager-overview)
- [Pack Geometry Manager](#pack-geometry-manager)
- [Grid Geometry Manager](#grid-geometry-manager)
- [Place Geometry Manager](#place-geometry-manager)
- [Choosing the Right Manager](#choosing-the-right-manager)

---
**Estimated Time:** 60 minutes  
**Prerequisites:** [Basic Widgets](02-basic-widgets.md) 

---

## Geometry Manager Overview
**Geometry Manager** control how widgets are arranged within their parents containers. Tkinter provides three managers, each with different strenghts.

### The Three Managers
| Manager | Best For | Complexity | Use Cases |
|---------|----------|------------|-----------|
| **Pack** | Simple linear layouts | Low | Toolbars, simple forms |
| **Grid** | Table-like layouts | Medium | Complex forms, calculators |
| **Place** | Absolute positioning | High | Custom positioning, overlays |

### Critical Rule: Don't Mix Managers 
```python
# NEVER do this in the same container
widget1.pack()
widget2.grid(row=0,coloumn=0) # will cause conflicts!

# Use one manager per container
frame1= Frame(root)
widget1.pack(in_=frame1) # pack inside frame1 

frame2 = Frame(root)
widger2.grid(row=0,column=0,in_frame=frame2) #grid inside Frame2
```

## Pack Geometry Manager
**Best for:** Simple, linear arrangements (vertical or horizontal)

### Basic Pack Usage
```python
from tkinter import *

root = Tk()
root.title("Pack Examples")
root.geometry("300x200")

# Default packing (top to bottom)
Label(root, text="First Widget", bg="lightblue").pack()
Label(root, text="Second Widget", bg="lightgreen").pack()
Label(root, text="Third Widget", bg="lightcoral").pack()

root.mainloop()
```

### Pack Sides and Direction
```python
from tkinter import *

root=Tk()
root.title("Pack sides")
root.geometry("400x300")

# Pack to different sides
Label(root, text="TOP", bg="red").pack(side=TOP, fill=X)
Label(root, text="BOTTOM", bg="blue").pack(side=BOTTOM, fill=X)  
Label(root, text="LEFT", bg="green").pack(side=LEFT, fill=Y)
Label(root, text="RIGHT", bg="yellow").pack(side=RIGHT, fill=Y)
Label(root, text="CENTER", bg="purple").pack(expand=True)

root.mainloop()
```

### Pack Options
| Option | Values | Purpose |
|--------|--------|---------|
| `side` | `TOP`, `BOTTOM`, `LEFT`, `RIGHT` | Which side to attach to |
| `fill` | `X`, `Y`, `BOTH`, `NONE` | How to expand |
| `expand` | `True`, `False` | Whether to use extra space |
| `padx` | Integer or `(left, right)` | External horizontal padding |
| `pady` | Integer or `(top, bottom)` | External vertical padding |
| `ipadx` | Integer | Internal horizontal padding |
| `ipady` | Integer | Internal vertical padding |
| `anchor` | `N`, `S`, `E`, `W`, `CENTER`, etc. | Position within allocated space |

## Practical Pack Examples

```python
from tkinter import *

root = Tk()
root.title("Pack Layouts")
root.geometry("400x300")

# Example 1: Toolbar layout
toolbar = Frame(root, bg="gray90", height=40)
toolbar.pack(side=TOP, fill=X)
toolbar.pack_propagate(False)  # Maintain height

Button(toolbar, text="New").pack(side=LEFT, padx=2, pady=5)
Button(toolbar, text="Open").pack(side=LEFT, padx=2, pady=5)
Button(toolbar, text="Save").pack(side=LEFT, padx=2, pady=5)
Button(toolbar, text="Exit").pack(side=RIGHT, padx=2, pady=5)

# Example 2: Status bar
status = Frame(root, bg="gray80", height=25)
status.pack(side=BOTTOM, fill=X)
status.pack_propagate(False)

Label(status, text="Ready", bg="gray80", anchor=W).pack(side=LEFT, padx=5)
Label(status, text="Line 1, Col 1", bg="gray80", anchor=E).pack(side=RIGHT, padx=5)

# Example 3: Main content area
content = Frame(root, bg="white")
content.pack(fill=BOTH, expand=True, padx=5, pady=5)

Label(content, text="Main Content Area", font=("Arial", 14)).pack(pady=20)

root.mainloop()
```

## Grid Geometry Manager
**Best for:** Table-like layouts, complex forms, calculators

### Basic Grid Usage
```Python
from tkinter import *

root=Tk()
root.title("Grid Examples")
root.geometry("300x200")

# simple grid layout
Label(root, text="Row 0, Col 0", bg="lightblue").grid(row=0, column=0)
Label(root, text="Row 0, Col 1", bg="lightgreen").grid(row=0, column=1)
Label(root, text="Row 1, Col 0", bg="lightcoral").grid(row=1, column=0)
Label(root, text="Row 1, Col 1", bg="lightyellow").grid(row=1, column=1)

root.mainloop()
```

### Grid Options 
| Option | Purpose | Example |
|--------|---------|---------|
| `row` | Row position (0-based) | `row=0` |
| `column` | Column position (0-based) | `column=1` |
| `rowspan` | Span multiple rows | `rowspan=2` |
| `columnspan` | Span multiple columns | `columnspan=3` |
| `sticky` | How to align in cell | `sticky="nsew"` |
| `padx` | External horizontal padding | `padx=5` |
| `pady` | External vertical padding | `pady=5` |
| `ipadx` | Internal horizontal padding | `ipadx=10` |
| `ipady` | Internal vertical padding | `ipady=5` |

## Advanced Grid Features
```python
from tkinter import *

root = Tk()
root.title("Advanced Grid")
root.geometry("400x300")

# Configure grid weights for resizing
root.columnconfigure(0, weight=1)  # Column 0 expands
root.columnconfigure(1, weight=2)  # Column 1 expands 2x more
root.rowconfigure(1, weight=1)     # Row 1 expands

# Header spanning multiple columns
Label(root, text="Header Spanning 3 Columns", bg="navy", fg="white", 
      font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3, 
                                       sticky="ew", padx=5, pady=5)

# Sidebar spanning multiple rows
Label(root, text="Sidebar\nSpanning\nRows", bg="lightgray", 
      justify=CENTER).grid(row=1, column=0, rowspan=2, 
                          sticky="nsew",padx=5,pady=5)

# Main content area
content_frame = Frame(root, bg="white", relief="sunken", borderwidth=2)
content_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", 
                   padx=5, pady=5)

Label(content_frame, text="Main Content", bg="white", 
      font=("Arial", 14)).pack(pady=20)

# Footer
Label(root, text="Footer Information", bg="gray", 
      fg="white").grid(row=2, column=1, columnspan=2, 
                       sticky="ew", padx=5, pady=5)

root.mainloop()
```

## Place Geometry Manager
**Best for:** Absolute positioning, overlays, custom layouts

### Basic Place Usage

```python
from tkinter import *

root = Tk()
root.title("Place Examples")
root.geometry("400x300")

# Absolute positioning
Label(root, text="Top Left", bg="red").place(x=10, y=10)
Label(root, text="Top Right", bg="green").place(x=300, y=10)
Label(root, text="Bottom Left", bg="blue").place(x=10, y=250)
Label(root, text="Bottom Right", bg="yellow").place(x=300, y=250)
Label(root, text="Center", bg="purple").place(x=200, y=150, anchor=CENTER)

root.mainloop()
```

### Place Options

| Option | Purpose | Values |
|--------|---------|--------|
| `x` | Absolute x position | Pixels from left |
| `y` | Absolute y position | Pixels from top |
| `relx` | Relative x position | 0.0 to 1.0 (percentage) |
| `rely` | Relative y position | 0.0 to 1.0 (percentage) |
| `width` | Absolute width | Pixels |
| `height` | Absolute height | Pixels |
| `relwidth` | Relative width | 0.0 to 1.0 (percentage) |
| `relheight` | Relative height | 0.0 to 1.0 (percentage) |
| `anchor` | Position anchor point | `N`, `S`, `E`, `W`, `CENTER`, etc. |

### Basic Positioning with Place
```python
from tkinter import *

root = Tk()
root.title("Relative Place")
root.geometry("400x300")
root.configure(bg="lightgray")

# Relative positioning (0.0 to 1.0)
Label(root, text="Top Left\n(0, 0)", bg="red").place(relx=0, rely=0, anchor=NW)
Label(root, text="Top Right\n(1, 0)", bg="green").place(relx=1, rely=0, anchor=NE)
Label(root, text="Bottom Left\n(0, 1)", bg="blue").place(relx=0, rely=1, anchor=SW)
Label(root, text="Bottom Right\n(1, 1)", bg="yellow").place(relx=1, rely=1, anchor=SE)
Label(root, text="Center\n(0.5, 0.5)", bg="purple", fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)

# Relative size
Label(root, text="50% Width", bg="orange").place(relx=0.25, rely=0.3, relwidth=0.5, height=30, anchor=NW)

root.mainloop()
```
### Overlay Example

```python
from tkinter import *

root = Tk()
root.title("Overlay Example")
root.geometry("400x300")

# Background content
main_frame = Frame(root, bg="lightblue")
main_frame.place(relwidth=1, relheight=1)

Label(main_frame, text="Main Content Area", font=("Arial", 16), 
      bg="lightblue").pack(pady=50)

Button(main_frame, text="Normal Button").pack(pady=10)
Entry(main_frame, width=30).pack(pady=10)

# Overlay dialog
overlay = Frame(root, bg="white", relief="raised", borderwidth=3)
overlay.place(relx=0.5, rely=0.5, width=250, height=150, anchor=CENTER)

Label(overlay, text="Overlay Dialog", font=("Arial", 14, "bold"), 
      bg="white").pack(pady=10)
Label(overlay, text="This is on top of other content", 
      bg="white", wraplength=200).pack(pady=5)

button_frame = Frame(overlay, bg="white")
button_frame.pack(pady=10)

Button(button_frame, text="OK", width=8).pack(side=LEFT, padx=5)
Button(button_frame, text="Cancel", width=8).pack(side=LEFT, padx=5)

root.mainloop()
```

## Choosing the Right Manager

### Decision Flowchart

![Decision Flowchart](/screenshoots/decision-flowchart.png)

### When to Use Each Manager

**Use Pack when:**
- Creating toolbars or status bars
- Making simple vertical or horizontal lists
- Building basic dialog boxes
- Working with a small number of widgets

**Use Grid when:**
- Creating forms with labels and inputs
- Building calculators or number pads
- Making table-like interfaces
- Need precise row/column alignment

**Use Place when:**
- Need exact pixel positioning
- Creating overlays or floating elements
- Building custom layouts
- Working with graphics or canvas elements

### Combining Managers
```python
from tkinter import *

root = Tk()
root.title("Combined Managers")
root.geometry("700x600")

# Main structure using Pack
header = Frame(root, bg="navy", height=50)
header.pack(side=TOP, fill=X)
header.pack_propagate(False)

content = Frame(root, bg="white")
content.pack(fill=BOTH, expand=True)

footer = Frame(root, bg="gray", height=30)
footer.pack(side=BOTTOM, fill=X)
footer.pack_propagate(False)

# Header uses Pack internally
Label(header, text="Application Title", fg="white", bg="navy", 
      font=("Arial", 16, "bold")).pack(pady=10)

# Content uses Grid internally
content.columnconfigure(1, weight=1)
content.rowconfigure(2, weight=1)

Label(content, text="Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Entry(content, width=30).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

Label(content, text="Email:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Entry(content, width=30).grid(row=1, column=1, sticky="ew", padx=10, pady=10)

# Text area with scrollbar using Pack in a frame
text_frame = Frame(content)
text_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

text_area = Text(text_frame, wrap=WORD)
scrollbar = Scrollbar(text_frame)

text_area.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=text_area.yview)

text_area.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Footer uses Pack
Label(footer, text="Status: Ready", bg="gray").pack(side=LEFT, padx=10)

# Floating help button using Place
help_btn = Button(content, text="?", font=("Arial", 12, "bold"), 
                  width=3, height=1, bg="lightblue")
help_btn.place(relx=0.99, rely=0.01, anchor=NE)

root.mainloop()
```
---

**Navigation:**  
[← Basic Widgets](02-basic-widgets.md) | [Next: Event Handling →](04-event-handling.md)

