import wx
import wx.lib.dialogs
import wx.stc as stc

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
        self.leftMarginWidth = 25

        window = wx.Frame.__init__(self, parent, title=title, size=(800, 600))

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
        helpMenu.AppendSeparator()
        menuCode = helpMenu.Append(wx.ID_ANY, "&See Code", "View this application's source code")

        #showing menu
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(editMenu, "&Edit")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        self.SetBackgroundColour('black')

        #color = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND)
        #self.SetBackgroundColour(color)

        self.Show()


app = wx.App()
frame = MainWindow(None, 'Text Editor')
app.MainLoop()
