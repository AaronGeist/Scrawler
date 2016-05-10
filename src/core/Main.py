from wx.core import wx

from src.core.view.Viewer import Viewer

app = wx.App(False)
frame = Viewer(None, "Deathpool")
frame.Show(True)

app.MainLoop()
