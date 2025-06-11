> We are going to learn about Graphical User Interface (GUI). We are going to use **Tkinter**, which is a module that comes built-in in Python that allows us to built GUI.  
# Import Tkinter
>There are two ways that we can import the TKinter module:  
>> Method 1:
>> ```python
>> from tkinter import *
>> ```  
>
>> Method 2:   
>> ```python
>> import tkinter as tk
>>```
> So you might be thinking when to use method 1 and method 2. Well....let me explain!
>> **Method 1**: 
>> This imports **all** the classes and functions from the *tkinter* module into your namespace.  
>> Pros:
>> - Shorter code
>> - Easier to read for beginners  
>> 
>> Cons:
>> - Can potentially cause name clashes if you're working with multiple libraries that have overlapping names
>
>> **Method 2**: 
>> This imports the *tkinter* module and gives it the alias *tk*.  You then need to reference widgets and functions using the *tk* prefix, like *tk.Button*, *tk.Label*, *tk.Tk()*, etc.
>> Pros:
>> - Makes the code cleaner and avoids name conflicts 
>> - Standard and widely recommended style, especially for large programs.  
>> 
>> Cons:
>> - Slightly longer code due to the *tk* prefix.
> 
# Creating a window
>As I am still a beginner, I will be using *Method 1*.
> ```python
> from tkinter import *
> root = Tk()
> root.mainloop()
> ```
>> By *convention* the main window in Tkinter, is called *root*. But you can use any other name.  
>> The **mainloop()** ensures the main window remains visible on the screen.  
>> Typically, in Tkinter program, we place the call to the **mainloop()** method as the **last statmement** after creating the widgets
> 
# Adding some label widget
> Now we want our window to have some texts. So we need to create a  *label* widget.
> **There are always 2 steps to create a widget.**
>> Step 1: Create the widget!
>> ```python
>> myLabel = Label(root,text="Hello World!")
>> ```
>
>> Step 2: Display the widget on our window!  
>> 
>> We have different ways of *putting things on the screen* using Tkinter  
>> The first one we are going to look at is **pack()**
>>```python
>> myLabel.pack()
>>```
> Complete code:
> ```python
> from tkinter import *
> root = Tk()
> myLabel = Label(root,text="Hello World!")
> myLabel.pack()
> root.mainloop()
>```
> Congratulation!! You created your very first window with a *label* widget:  
> ![First window with Hello World label](/screenshoots/01-first-window.png)  
>
> **Positioning with the Grid system**  
> The grid system is another way of *putting things on the screen*. 
> ```python
> from tkinter import *
> root = Tk()
> MyLabel1 = Label(root,text="Hello!")  
> MyLabel2 = Label(root,text="My name is John")
>
> MyLabel1.grid(row=0,column=0)
> MyLabel2.grid(row=1,column=0)
>
> root.mainloop()
> ```
>> We just need to specify the row and column we want the label widget to be in.  
>> It always starts with row 0 and column 0  
>
>  ![Two labels arranged vertically using grid](/screenshoots/02-grid-vertical.png)  
> We can now *play* with the row and column to see how it works  
> For example here we have 
>```python 
> MyLabel1.grid(row=0,column=0)
> MyLabel2.grid(row=1,column=1)
>```  
> ![Labels positioned diagonally in grid system](/screenshoots/03-grid-diagonal.png)
> 
# Creating a button widget 
> Like I said to create a widget we have two steps:
> 1. Create the widget
> 2. Display it on the screen
> ```python
> from tkinter import *
> root=Tk()
> myButton=Button(root,text="Click Me!")
> myButton.pack()
> root.mainloop()
>```  
> And here you go:  
> ![Simple Click Me button](/screenshoots/04-basics-button.png)  
>  
> We can also change the size of the button
> ```python
> from tkinter import *
> root=Tk()
> myButton=Button(root,text="Click Me!",padx=50,pady=5)
> myButton.pack()
> root.mainloop()
>```
> ![Button with padding applied](/screenshoots/05-button-with-padding.png)  
> As you can see the button is bigger now!  
> ***padx*** is for the horizontal length (The x-axis) and ***pady*** is for the vertical length (The y-axis).  
>  
> We can also specify the state of the button. For example,  
>```python
> from tkinter import *
> root=Tk()
> myButton=Button(root,text="Click Me!",state=DISABLED,padx=50,pady=5)
> myButton.pack()
> root.mainloop()
> ```  
> ![Disabled button shown in gray](/screenshoots/06-disabled-button.png)
>> As you can see we cannot click on the button. It has been disable  
> 
> Now, we need the button to actually *do something*  
> What we do is actually create a function. Like any function in Python.  
> ```python
> from tkinter import *
> root=Tk()
>  
>  def myClick():
>    myLabel = Label(root, text="Button Clicked!!")
>    myLabel.pack()
> 
> myButton=Button(root,text="Click Me!",command=myClick, padx=50,pady=5)
> myButton.pack()
> root.mainloop()
> ```
>**Pay close attenttion to this:**    
>```python
> myButton=Button(root,text="Click Me!",command=myClick, padx=50,pady=5)
> ```  
> 
> *myClick* does not have any parenthesis, "(" or ")"   
> 
> Before I clicked:  
> ![Button before being clicked](/screenshoots/07-button-before-click.png)
> 
> After I clicked:  
> ![Button after click showing new label](/screenshoots/08-button-after-click.png)
> 
> We can also **change the colour of the button**; the *foreground* and the *background*
> ```python
> from tkinter import *
> root=Tk()
>  
>  def myClick():
>    myLabel = Label(root, text="Button Clicked!!", fg="blue")
>    myLabel.pack()
> 
> myButton=Button(root,text="Click Me!",command=myClick, fg="white", bg="red", padx=50,pady=5)
> myButton.pack()
> root.mainloop()
> ```
> ![Button with red background and white text](/screenshoots/09-colored-button.png)
> 
# Creating input fields
> This is the code:
>```python
> from tkinter import *
> root=Tk()
>
> e= Entry(root)
> e.pack()
>
> def myClick():
>   myLabel = Label(root, text="Button Clicked!!",fg="blue")
>   myLabel.pack()
>
>myButton=Button(root,text="Click Me!",command=myClick,fg="white", bg="red", padx=50,pady=5)
>myButton.pack()
>root.mainloop()
>```
> 
> And this is how it's going to look:  
> ![Entry field with button example](/screenshoots/10-input-field-example.png)  
> 
> Now, we can play around with what we have learn.  
> Here is mine:  
> ```python
>from tkinter import *
>root=Tk()
>
>def clicked():
>    myLabel=Label(root, text="Hello " + box.get() + "!")
>    myLabel.pack()
>
>fLine= Label(root,text="Enter Your Name: ")
>fLine.pack()
>
>box=Entry(root)
>box.pack()
>
>button=Button(root,text="Enter", command=clicked)
>button.pack()
>
>root.mainloop()
>```  
>
> ![Final name input demonstration](/screenshoots/11-name-input-demo.png)
> 
