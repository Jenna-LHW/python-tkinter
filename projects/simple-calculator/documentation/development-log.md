
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
[Calculator Code](/code/calculator-v1.py)

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

- Why it happened: The gaps between the buttons were caused by the *padx=10, pady=10* parameters in the grid condfiguration. These parameters add 10 pixels of padding around each button, which I misuderstood for width and height. I thought these specifies the width and heigth of the buttons

### Thoughts & Reflections
Read **well** documentations. Don't just assume things!
  
 

<!--## Day2: [Date]
**Time Spent:** [hours/minites]
**Phase:** 

### What I Worked On Today
- [main tasks]

### Code Progress
```python
# code I wrote today
```

### What I Learned
- [what I learned]

### Problems I Encountered
1. Problem: [described the issue]
- what I tried: [Attempts to solve it]
- Solution: [how I fixed it/ still working on it]
- Why it happened: [root cause]
  
### Screenshots

-->
