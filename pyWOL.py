import os
import wx
from wakeonlan import wol

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        
        # Initialize and draw "frame" (window)
        wx.Frame.__init__(self, parent, title=title, size=(415,200))
        
        # Status bar at bottom of window
        self.CreateStatusBar()
        
        # Declare IP Address
        self.iptag = wx.StaticText(self, label="Server IP: ", pos=(20, 30))
        self.ipAddress=wx.TextCtrl(self,-1,'192.168.1.113',pos=(140,25), size =(100,20))
        self.ipAddress.SetToolTipString("IP Address of targeted NIC")
        
        # Declare MAC address
        self.mactag = wx.StaticText(self, label="Server MAC Address: ", pos=(20, 50))
        self.macAddress=wx.TextCtrl(self,-1,'FF:FF:FF:FF:FF',pos=(140,45), size =(100,20))
        self.macAddress.SetToolTipString("MAC Address of targeted NIC")        
        
        # Declare subnet
        self.subnettag = wx.StaticText(self, label="Subnet Mask: ", pos=(20, 70))
        self.subnetAddress = wx.TextCtrl(self,-1,'255.255.255.255',pos=(140,65), size =(100,20))
        self.subnetAddress.SetToolTipString("This is usually 255.255.255.255")

        # Declare port
        self.porttag = wx.StaticText(self, label="Port: ", pos=(20, 90))
        self.Port = wx.TextCtrl(self,-1,'9',pos=(140,85), size =(45,20))
        self.Port.SetToolTipString("This is usually 9")
        
        
        # Button to send packets
        self.wake = wx.Button(self, label="WAKE", pos=(300, 85))
        self.wake.Bind(wx.EVT_BUTTON, self.wakeClick)
                       
        #Draw the window ("frame")
        self.Show()

        # Set up the menu
        filemenu= wx.Menu()

        # About and exit button in menu
        menuExit = filemenu.Append(wx.ID_EXIT,"Exit"," Terminate the program")

        # Create menu at top
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the file menu to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the menu bar to the frame content.

        # Set event handlers
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Render the frame data
        self.Show(True)
        

    # Click the button and it sends a magic packet to defined host
    def wakeClick(self,e):
        
        ip = "'"+self.ipAddress.GetValue()+"'"". "
        mac = "'"+self.macAddress.GetValue()+"'"". "
        p = "'"+ self.Port.GetValue()+"'"
               
        wol.send_magic_packet(mac, ip, p)
                        
        #wol.send_magic_packet(self.macAddress.GetValue(), ip_address=self.ipAddress.GetValue(), port=self.Port.GetValue())
        
        dlg = wx.MessageDialog(self, "Magic packet sent", "WOL Operation Complete", wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
          
    # Kill the app
    def OnExit(self,e):
        self.Close(True)
        
app = wx.App(False)
frame = MainWindow(None, "Server Wake On LAN")
app.MainLoop()