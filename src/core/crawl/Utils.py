import http.cookiejar
import os
import re
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from src.core.crawl.CrawlConstants import CrawlConstants
from wx.lib.pubsub.pub import getDefaultPublisher


class Utils:
    cookie = None

    @staticmethod
    def saveCookie():
        assert (Utils.cookie is not None)
        Utils.cookie.save(CrawlConstants.COOKIE_FILE, ignore_discard=True, ignore_expires=True)

    @staticmethod
    def loadCookie():
        try:
            Utils.cookie = http.cookiejar.MozillaCookieJar()
            Utils.cookie.load(CrawlConstants.COOKIE_FILE, ignore_discard=True, ignore_expires=True)
        except Exception:
            print("Create new cookie")

        assert (Utils.cookie is not None)
        return Utils.cookie

    @staticmethod
    def createOpener(headers=None):
        if headers is None:
            headers = CrawlConstants.DEFAULT_HEADER

        try:
            cookiProcessor = urllib.request.HTTPCookieProcessor(Utils.loadCookie())
            opener = urllib.request.build_opener(cookiProcessor)
            opener.addheaders = headers
            return opener
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def urlGet(url, opener=None, headers=None, returnRaw=False):
        if (opener is None):
            opener = Utils.createOpener(headers)

        try:
            response = opener.open(url)
            if returnRaw:
                return response
            else:
                return BeautifulSoup(response.read(), 'html.parser')
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def urlPost(url, opener=None, data=None, returnRaw=False):
        if (opener is None):
            opener = Utils.createOpener()

        try:
            encodeData = urllib.parse.urlencode(data).encode("utf-8")
            response = opener.open(url, data=encodeData)
            if returnRaw:
                return response
            else:
                return BeautifulSoup(response.read(), 'html.parser')
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def getAttrList(soupObj, matchExp, attr):
        assert (soupObj is not None)
        assert (matchExp is not None)

        itemTagList = soupObj.select(matchExp)

        attrList = list()
        for itemTag in itemTagList:
            attrList.append(itemTag[attr])

        return attrList

    @staticmethod
    def getContent(soupObj, matchExp, index=0):
        assert (soupObj is not None)
        assert (matchExp is not None)

        itemList = soupObj.select(matchExp)
        if itemList is None or len(itemList) <= 0:
            return None
        else:
            return itemList[0].contents[index]

    @staticmethod
    def downloadImage(url, targetFilePath, headers=None):
        print("Downloading " + url)
        res = Utils.urlGet(url, returnRaw=True)
        assert (res is not None)

        try:
            f = open(targetFilePath, "wb")
            f.write(res.read())
            f.close()
        except Exception as e:
            print("Cannot write file: " + targetFilePath, e)

    @staticmethod
    def parseImageName(url):
        assert (url is not None)

        if (url.endswith("png") or url.endswith("jgp") or url.endswith("gif")):
            subUrl = url.split("/")
            return subUrl[len(subUrl) - 1]
        else:
            res = re.findall("/([^/]*?\.(jpg|png|gif))", url)
            if len(res) > 0:
                return res[0][0]
            print("Cannot parser image name")
            return "NA.jpg"

    @staticmethod
    def createFolder(path):
        if not os.path.isdir(path):
            os.makedirs(path)

    @staticmethod
    def getFutureResult(future):
        try:
            return future.result()
        except Exception as e:
            print("Exception get future result: " + str(e))

        return None

    @staticmethod
    def publish(topic, msg):
        getDefaultPublisher().sendMessage(topic, msg=msg)

    @staticmethod
    def subscribe(func, topic):
        getDefaultPublisher().subscribe(func, topic)

    @staticmethod
    def rootPath():
        return os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    # Utils.createFolder("test/aabb")
    print(Utils.parseImageName(
        "http://www.dpfile.com/s/c/app/main/index-header/i/sprite.122340b14b6d989d8548edb59bd3a93c.png"))

    src = "http://3.im.guokr.com/XA_vKZBSgzF0ji3YluzlDi4PzupT_vV0xLyfsyQLVSKgAAAAoAAAAEpQ.jpg?imageView2/1/w/48/h/48"
    print(Utils.parseImageName(src))

    print(Utils.rootPath())