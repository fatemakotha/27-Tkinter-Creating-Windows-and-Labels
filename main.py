import tkinter

my_window = tkinter.Tk() #created a window
my_window.title("My First GUI prog") #changes the title of the window
my_window.minsize(width=500, height=300) #changes the size of the window

#Creating a LABEL:

my_label = tkinter.Label(text="I am a Label")
my_label.pack() #pust the label at the center of screen





my_window.mainloop() #will keep the window open. This is a loop lie: while True. HAS TO BE AT THE END OF THE PROGRAM **