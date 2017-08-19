from Tkinter import *
from tkFileDialog import *
from tkMessageBox import showerror

fileName = None

def newFile():
    global fileName
    fileName = "New Untitled File"
    #empty the file from 0 row and 0 column to the end of file to make new file
    Text.delete(0.0, END)

def saveAs():
    #w for write for built in asksaveasfile
    f = asksaveasfile(mode = 'w', defaultextension = '.txt')
    t = Text.get(0.0, END)
    #try catch to get rid of white space at the end of file when saved
    try:
        f.write(t.rstrip())
    except:
        showerror(title = "error", message = "Something went wrong. Unable to save file...")

def saveFile():
    global fileName
    #storting the entire file contents in a var
    t = Text.get(0.0, END)
    f = open(fileName, 'w')
    f.write(t)
    f.close()

def openFile():
    f = askopenfile(mode = 'r')
    t = f.read()
    #editor needs to be empty
    Text.delete(0.0, END)
    Text.insert(0.0, t)


#Working on the obj itself
root = Tk()

root.title("Hackable Text Editor")
root.minsize(width=600, height = 600)
root.maxsize(width = 600, height = 600)

#so it fills up entire window
text = Text(root, width = 600, height = 600)
#need to actually display the text box
text.pack()

#working on the menu bar itself
menuBar = Menu(root)
fileMenu = Menu(menuBar)
fileMenu.add_command(label="New", command = newFile)
fileMenu.add_command(label="Open", command = openFile)
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_command(label="Save As", command = saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command = root.quit)
menuBar.add_cascade(label="File", menu =fileMenu)

root.config(menu=menuBar)
root.mainloop()
