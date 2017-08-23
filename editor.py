from Tkinter import *
#for saving purposes
import tkFileDialog
import tkMessageBox


#All functions
def newFile():
    answer = tkMessageBox.askquestion(title="Save file", message="Do you want to save this file?")
    #if yes first save then delete all
    if(answer == True):
        saveFile()
    deleteAllOption()

def openFile():
    newFile()
    file = tkFileDialog.askopenfile()
    text.insert(INSERT, file.read())

def saveFile():
    filePath = tkFileDialog.asksaveasfilename()
    writeFile = open(filePath, mode='w')
    writeFile.write(text.get(0.0, END).rstrip())

def closeFile():
    saveFile()
    root.quit()

def selectAllOption():
    #SELect all
    text.tag_add(SEL, "0.0", END)

def deleteAllOption():
    text.delete(0.0, END)

def cutOption():
    #need to clear pre cut stuff
    root.clipboard_clear()
    root.clipboard_append(string=text.selection_get())
    #delete first to last character
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

#same as cut without the deletion
def copyOption():
    root.clipboard_clear()
    root.clipboard_append(string=text.selection_get())

def pasteOption():
    text.insert(INSERT, root.clipboard_get())

def deleteOption():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

#window object
root = Tk()

root.title("Untitled")
#window size
root.minsize(width=400, height=400)

#setting up textBox
#highlightthickness to get rid of border
#for some reason undo function won't work unless set to trueasdf
text= Text(root, width=400, height=400, font=("Arial"), bd =5, highlightthickness=0, undo=True)

#so it takes up full screen when size is increased
text.pack(fill=BOTH)


#DROPDOWNS
menu = Menu(root)
root.config(menu=menu)

#File Menu
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New...", command=newFile)
fileMenu.add_command(label="Open...", command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label="Save...", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close..", command=closeFile)

#Edit Menu
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=text.edit_undo)
editMenu.add_command(label="Redo", command=text.edit_redo)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=cutOption)
editMenu.add_command(label="Copy", command=copyOption)
editMenu.add_command(label="Paste", command=pasteOption)
editMenu.add_command(label="Select All", command=selectAllOption)
editMenu.add_separator()
editMenu.add_command(label="Delete", command=deleteOption)

#keep the editor running
root.mainloop()


