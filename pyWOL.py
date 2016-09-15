import os
import wx
from wakeonlan import wol

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))
        self.CreateStatusBar() # Status bar at bottom of window

        # Set up the menu
        filemenu= wx.Menu()

        # About and exit button in menu
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the file menu to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the menu bar to the frame content.

        # Set event handlers
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)
          
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

app = wx.App(False)
frame = MainWindow(None, "Server Wake On LAN")
app.MainLoop()