'''
        Working with GUIs and Tkinter
        
'''
from tkinter import *


root = Tk()
root.geometry('700x400')  # Set the size of the window

def draw_rectangle():
    #root2 = Tk()
    canvas = Canvas(root)  # Add the 'root' argument to the Canvas constructor
    canvas.pack()
    
    #draw a rectangle
    canvas.create_rectangle(10,10,110,110, outline='black', fill='white', width=2)
    
    root.mainloop()
    
def draw_circle():
    
    canvas = Canvas(root)  # Add the 'root' argument to the Canvas constructor
    canvas.pack()
    
    #draw a rectangle
    canvas.create_oval(10,10,110,110, outline='black', fill='white', width=2)
    
    root.mainloop()

def on_click(event):
    
    #draw a circle on the canvas
    canvas = Canvas(root)
    canvas.pack()
    
    canvas.create_oval(10,10,110,110, outline='black', fill='blue', width=2)
    
    
    
def draw_circle_centered():
    # first, create the root window.  Then get the center of the window and use that to draw the circle
    
      # Set the size of the window
    canvas = Canvas(root, width=600, height=200)  # Add the 'root' argument to the Canvas constructor
    canvas.pack()
    
    #finding the width and height of the window 
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()   
    
    center_x = width/2
    center_y = height/2
    
    #draw a circle centered in the window
    canvas.create_oval(width/2-50, height/2-50, width/2+50, height/2+50, outline='black', fill='white', width=2)
    
    root.mainloop()
    
def interactive_gui_with_buttons():
    
    
      # Set the size of the window
    canvas = Canvas(root, width=600, height=200)  # Add the 'root' argument to the Canvas constructor
    
    #set the title of the window
    root.title("Interactive GUI with Buttons")
    
    #create a label
    label = Label(root, text="Click the button to draw a circle")
    
    #create a button
    button = Button(root, text="Button")
    
    #pack the label, button and canvas
    label.pack()
    button.pack()
    canvas.pack()
    
    #listener and onEvent, onAction
    #bind the button to the draw_circle function
    button.bind("<Button-1>", on_click)
    
    root.mainloop()
    

if __name__ =="__main__":
    draw_rectangle()
    #draw_circle()
    #draw_circle_centered()
    #interactive_gui_with_buttons()