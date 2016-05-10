import os

from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.ParallelTemplate import ParallelTemplate
from src.core.crawl.Utils import Utils
from src.core.model.Image import Image


class ImageLoader:
    def load(self, imageList):
        template = ParallelTemplate(5)
        return template.run(self.doLoad, imageList)

    def doLoad(self, image):
        if os.path.isfile(image.location):
            print(">>>>>>> skip loading image: " + image.src)
        else:
            print(">>>>>>> start loading image: " + image.src)
            Utils.downloadImage(image.src, image.location, headers=CrawlConstants.IMGAGE_HEADER)
        return image


if __name__ == "__main__":
    iQueue = list()
    for i in range(10):
        image = Image()
        image.src = "http://www.dpfile.com/s/c/app/main/index-header/i/sprite.122340b14b6d989d8548edb59bd3a93c.png"
        image.location = str(i) + ".png"
        iQueue.append(image)

    loader = ImageLoader()
    res = loader.load(iQueue)
    print("res=" + str(len(res)))
