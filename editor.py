import wx
import wx.lib.dialogs
import wx.stc as stc
import os

# fonts for editor
faces = {
    'times' : 'Times New Roman',
    'hel' : 'Arial',
    'mono' : 'Courier New',
    'size' : 10,
    'size2' : 12,
    'size3' : 14
}

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''
        self.filename = ''
        self.leftMarginWidth = 25

        wx.Frame.__init__(self, parent, title=title, size=(800, 600))




        self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | wx.TE_WORDWRAP)

        self.control.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.control.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        #not showing white space
        self.control.SetViewWhiteSpace(False)
        self.control.SetMargins(5,0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1, self.leftMarginWidth)


        #this is for the status bar
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((220,220, 220))

        #creating the menubar
        #File menu
        fileMenu = wx.Menu()

        menuNew = fileMenu.Append(wx.ID_NEW, "&New", "Create new file")
        menuOpen = fileMenu.Append(wx.ID_OPEN, "&Open", "Open a file")
        fileMenu.AppendSeparator()
        menuSave = fileMenu.Append(wx.ID_SAVE, "&Save", "Save file")
        menuSaveAs = fileMenu.Append(wx.ID_SAVEAS, "Save &As", "Save file as")
        fileMenu.AppendSeparator()
        menuClose = fileMenu.Append(wx.ID_EXIT, "&Quit", "Quit application")


        #Edit Menu
        editMenu = wx.Menu()

        menuUndo = editMenu.Append(wx.ID_UNDO, "&Undo", "Undo previous action")
        menuRedo = editMenu.Append(wx.ID_REDO, "&Redo", "Redo previous action")
        editMenu.AppendSeparator()
        menuCopy = editMenu.Append(wx.ID_COPY, "&Copy", "Copy selected item")
        menuCut = editMenu.Append(wx.ID_CUT, "C&ut", "Cut selected item")
        menuPaste = editMenu.Append(wx.ID_PASTE, "&Paste", "Paste selected item")
        menuSelectAll = editMenu.Append(wx.ID_SELECTALL, "&Select All", "Select entire document")

        #Help Menu
        helpMenu = wx.Menu()

        menuAbout = helpMenu.Append(wx.ID_ABOUT, "&About", "About this application")

        #showing menu
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(editMenu, "&Edit")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        self.SetBackgroundColour('black')

        #binding functions
        self.Bind(wx.EVT_MENU, self.new, menuNew)
        self.Bind(wx.EVT_MENU, self.open, menuOpen)
        self.Bind(wx.EVT_MENU, self.save, menuSave)
        self.Bind(wx.EVT_MENU, self.saveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.quit, menuClose)
        self.Bind(wx.EVT_MENU, self.undo, menuUndo)
        self.Bind(wx.EVT_MENU, self.redo, menuRedo)
        self.Bind(wx.EVT_MENU, self.selectAll, menuSelectAll)
        self.Bind(wx.EVT_MENU, self.copy, menuCopy)
        self.Bind(wx.EVT_MENU, self.cut, menuCut)
        self.Bind(wx.EVT_MENU, self.paste, menuPaste)
        self.Bind(wx.EVT_MENU, self.about, menuAbout)

        self.control.Bind(wx.EVT_KEY_UP, self.UpdateLineCol)

        self.Show()

        self.UpdateLineCol(self)

    #All menu functions
    def new(self, event):
        self.fileName = ''
        self.control.SetValue("")

    def open(self, event):
        dialogBox = wx.FileDialog(self, "Choose a file to open", self.dirname, "", "*.*", wx.FD_OPEN)
        if(dialogBox.ShowModal()==wx.ID_OK):
            self.filename = dialogBox.GetFilename()
            self.dirname = dialogBox.GetDirectory()
            openedFile = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(openedFile.read())
            openedFile.close()
        dialogBox.Destroy()

    def save(self, event):
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            #save vs save as
            try:
                dialogBox = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if(dialogBox.ShowModal() == wx.ID_OK):
                    self.filename = dialogBox.GetFilename()
                    self.dirname = dialogBox.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dialogBox.Destroy()
            except:
                pass

    def saveAs(self, event):
        try:
            dialogBox = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if(dialogBox.ShowModal() == wx.ID_OK):
                self.filename = dialogBox.GetFilename()
                self.dirname = dialogBox.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.control.GetValue())
                f.close()
            dialogBox.Destroy()
        except:
            pass

    def quit(self, event):
        self.Close(True)

    def UpdateLineCol(self, event):
        line = self.control.GetCurrentLine() + 1 #1 so that it starts counting from 1
        col = self.control.GetColumn(self.control.GetCurrentPos())
        posDisplay = "Line %s, Column %s" %(line, col)
        self.StatusBar.SetStatusText(posDisplay, 0)

    #Now the edit functions
    def undo(self, event):
        self.control.Undo()

    def redo(self, event):
        self.control.Redo()

    def selectAll(self, event):
        self.control.SelectAll()

    def copy(self, event):
        self.control.Copy()

    def cut(self, event):
        self.control.Cut()

    def paste(self, event):
        self.control.Paste()

    #About menu
    def about(self, event):
        dialogBox = wx.lib.dialogs.ScrolledMessageDialog(self,
                                                         "This application is created by Sauhard Pant as "
                                                         "a side project. You can view the source code for "
                                                         "this project on my github page (AvidRP/Editor)."
                                                         "This isn't a completely done project, so there are "
                                                         "more features to come!",
                                                         "About this Text Editor", size=(400, 400))
        dialogBox.ShowModal()
        dialogBox.Destroy()

app = wx.App()
frame = MainWindow(None, 'Text Editor')
app.MainLoop()
