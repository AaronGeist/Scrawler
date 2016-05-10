from wx.core import wx

from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.PageLoader import PageLoader
from src.core.crawl.PageParser import PageParser
from src.core.crawl.Utils import Utils


class Viewer(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent=parent, title=title, size=(800, 600))

        self.panel = wx.Panel(self, -1)
        self.leftWindow = wx.ScrolledWindow(self.panel, -1, )
        self.leftWindow.SetScrollRate(10, 10)
        self.leftWindow.SetScrollbar(0, 1, 1000, 1500)
        self.leftWindow.SetBackgroundColour("grey")

        self.rightWindow = wx.ScrolledWindow(self.panel, -1)
        self.rightWindow.SetScrollRate(10, 10)
        self.rightWindow.SetScrollbar(0, 1, 1000, 1500)
        self.rightWindow.SetBackgroundColour("yellow")

        topSizer = wx.BoxSizer()
        # second param indicates the % of total space
        topSizer.Add(self.leftWindow, 1, wx.EXPAND | wx.ALL, 5)
        topSizer.Add(self.rightWindow, 2, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(topSizer)

        self.currentPageNum = 1
        self.textCtrl = wx.TextCtrl(self.leftWindow, value=str(self.currentPageNum))
        loadBtn = wx.Button(self.leftWindow, label='Go', size=(40, 20))
        self.Bind(wx.EVT_BUTTON, lambda evt, param="curr": self.onParseTopPage(evt, param), loadBtn)
        prevBtn = wx.Button(self.leftWindow, label='<', size=(30, 20))
        self.Bind(wx.EVT_BUTTON, lambda evt, param="prev": self.onParseTopPage(evt, param), prevBtn)
        nextBtn = wx.Button(self.leftWindow, label='>', size=(30, 20))
        self.Bind(wx.EVT_BUTTON, lambda evt, param="next": self.onParseTopPage(evt, param), nextBtn)

        navigationSizer = wx.BoxSizer()
        navigationSizer.Add(self.textCtrl, 0, flag=wx.LEFT | wx.RIGHT, border=3)
        navigationSizer.Add(loadBtn, 0, flag=wx.LEFT | wx.RIGHT, border=1)
        navigationSizer.Add(prevBtn, 0, flag=wx.LEFT, border=4)
        navigationSizer.Add(nextBtn, 0, flag=wx.RIGHT, border=3)

        self.titleSizer = wx.BoxSizer(wx.VERTICAL)
        self.leftSizer = wx.BoxSizer(wx.VERTICAL)
        self.leftSizer.AddSpacer(5)
        self.leftSizer.Add(navigationSizer, 0, flag=wx.ALL, border=1)
        self.leftSizer.AddSpacer(5)
        self.leftSizer.Add(self.titleSizer)
        self.leftWindow.SetSizer(self.leftSizer)

        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        self.rightWindow.SetSizer(self.rightSizer)

        # msg subscriber
        Utils.subscribe(self.displayTopPage, "topPage")
        Utils.subscribe(self.displaySubPage, "parseSubPage")

    def onParseTopPage(self, evt, cmd):
        if cmd == "curr":
            self.currentPageNum = int(self.textCtrl.GetValue())
        elif cmd == "next":
            self.currentPageNum += 1
        elif cmd == "prev":
            self.currentPageNum -= 1
        else:
            return
        self.textCtrl.SetValue(str(self.currentPageNum))
        url = CrawlConstants.HOME_PAGE + CrawlConstants.HOME_PAGE_BROWSER + str(self.currentPageNum)
        pageParser = PageParser()
        pageParser.parseTopPage(url, async=True)

    def onLoadSubPage(self, evt, page):
        evt.GetEventObject().SetBackgroundColour("red")
        pageParser = PageParser()
        pageParser.parseSubPage(page.url, async=True)

    # msg handler
    def displayTopPage(self, msg):
        self.titleSizer.Clear(delete_windows=True)
        subPageList = msg
        for subPage in subPageList:
            btn = wx.Button(self.leftWindow, label=subPage.title)
            # use lambda to pass object to handler
            self.Bind(wx.EVT_BUTTON, lambda evt, p=subPage: self.onLoadSubPage(evt, p), btn)
            self.titleSizer.Add(btn)
        self.titleSizer.Fit(self.leftWindow)
        self.leftWindow.Fit()
        self.panel.Layout()

    # msg handler
    def displaySubPage(self, msg):
        self.rightSizer.Clear(delete_windows=True)
        page = msg
        print("Image len " + str(len(page.imgSrcList)))
        # load subPage
        pageLoader = PageLoader()
        imageList = pageLoader.load(page)
        print("Finish loading images " + str(len(imageList)))
        for image in imageList:
            try:
                imageObj = wx.Image(image.location, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                self.rightSizer.Add(wx.StaticBitmap(self.rightWindow, -1, imageObj), proportion=0, flag=wx.ALL,
                                    border=5)
            except Exception:
                print("Cannot display location=" + image.location)

        self.rightSizer.Fit(self.rightWindow)
        self.rightWindow.Fit()
        self.panel.Layout()
