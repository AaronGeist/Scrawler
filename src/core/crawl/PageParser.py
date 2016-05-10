import uuid
from concurrent.futures import ThreadPoolExecutor

import wx

from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.Login import Login
from src.core.crawl.Utils import Utils
from src.core.model.Page import Page


class PageParser:
    def parseSubPage(self, subPageUrl, async=True):
        print("Start parsing subPage " + subPageUrl)

        if async:
            ThreadPoolExecutor(1).submit(self.doParseSubPage, subPageUrl)
        else:
            self.doParseSubPage(subPageUrl)
        print("Finish parsing subPage " + subPageUrl)

    def doParseSubPage(self, subPageUrl):

        if not Login.login():
            assert "Fail to login"

        page = Page()

        try:
            page.url = subPageUrl
            page.uniqueID = str(uuid.uuid5(uuid.NAMESPACE_URL, page.url))
            subPage = Utils.urlGet(subPageUrl)

            # imgList = Utils.getAttrList(subPage, 'img[src*="imgroom"]', CrawlConstants.ATTR_SRC)
            # page.imgSrcList.extend(imgList)

            # imgList = Utils.getAttrList(subPage, 'img[src*="imgur"]', CrawlConstants.ATTR_SRC)
            # page.imgSrcList.extend(imgList)

            imgList = Utils.getAttrList(subPage, CrawlConstants.SUB_PAGE_IMG_CSS, CrawlConstants.ATTR_SRC)
            if imgList is None or len(imgList) == 0:
                print("Cannot find image in " + subPageUrl)
                return page
            page.imgSrcList.extend(list(set(imgList)))
        except Exception as e:
            print("Exception: " + str(e))

        wx.CallAfter(Utils.publish, "parseSubPage", page)


    def parseTopPage(self, topPageUrl, async=True):
        print("Start parsing topPage " + topPageUrl)

        if async:
            ThreadPoolExecutor(1).submit(self.doParseTopPage, topPageUrl)
        else:
            self.doParseTopPage(topPageUrl)

        print("Finish parsing topPage " + topPageUrl)

    def doParseTopPage(self, topPageUrl):
        if not Login.login():
            assert "Fail to login"

        soupPage = Utils.urlGet(topPageUrl)
        soupLinkList = soupPage.select(CrawlConstants.TOP_PAGE_LINK_CSS)
        assert soupLinkList is not None and len(soupLinkList) > 0

        subPageList = list()
        # filter some links
        print("Find subLink " + str(len(soupLinkList)))
        for soupLink in soupLinkList:
            if len(soupLink.contents[0]) < 5:
                continue
            if soupLink.has_attr("style"):
                continue

            subPage = Page()
            subPageUrl = soupLink[CrawlConstants.ATTR_HREF]
            if "http" not in subPageUrl:
                subPageUrl = CrawlConstants.BASE_URL + subPageUrl
            subPageTitle = soupLink.contents[0]

            print("Find link " + subPageUrl + " " + subPageTitle)
            subPage.url = subPageUrl
            subPage.title = subPageTitle
            subPageList.append(subPage)

        wx.CallAfter(Utils.publish, "topPage", subPageList)


if __name__ == "__main__":
    parser = PageParser()
    f = parser.parseTopPage(CrawlConstants.HOME_PAGE, async=True)

    res = Utils.getFutureResult(f)

    for page in res:
        print("find " + page.url + " " + page.title)
