import os

from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.ImageLoader import ImageLoader
from src.core.crawl.Utils import Utils
from src.core.model.Image import Image


class PageLoader:
    def load(self, page):
        print("Loading page " + page.url)

        # create folder for images
        folder = os.path.join(Utils.rootPath(), CrawlConstants.FOLDER_IMAGE, page.uniqueID)
        Utils.createFolder(folder)
        return self.doLoad(page, folder)

    def doLoad(self, page, folder):
        # fill image in queue
        for imgSrc in page.imgSrcList:
            image = Image()
            image.src = imgSrc
            print("img src = " + imgSrc)
            image.location = folder + "/" + Utils.parseImageName(imgSrc)
            print("img location = " + image.location)
            page.imageList.append(image)

        # start load image
        imageLoader = ImageLoader()
        return imageLoader.load(page.imageList)


if __name__ == "__main__":
    pass
