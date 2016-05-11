import wx
from wx._core import Frame


class LoginPage(Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title, size=(800, 600))
