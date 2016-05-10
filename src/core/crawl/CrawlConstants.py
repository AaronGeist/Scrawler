class CrawlConstants:
    # header
    DEFAULT_HEADER = [(
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36")]

    IMGAGE_HEADER = [("Content-Type", "image/jpeg"), ("Server", "cloudflare-nginx")]

    # html tag attributes
    ATTR_HREF = 'href'
    ATTR_SRC = 'src'

    FOLDER_IMAGE = ""

    COOKIE_FILE = "ck.txt"

    USERNAME = ""
    PASSWORD = ""

    # url
    # BASE_URL = "http://174.127.195.176/bbs/"
    # HOME_PAGE = BASE_URL + "forum-318-1.html"
    # LOGIN_PAGE = BASE_URL + "logging.php?action=login"
    # TOP_PAGE_LINK_CSS = "table tbody tr th.new span > a"
    # SUB_PAGE_IMG_CSS = 'a[href*="imagetwist"] > img[src*="imagetwist"]'
    BASE_URL = "http://www.guokr.com/"
    HOME_PAGE = BASE_URL + "group/31/"
    HOME_PAGE_BROWSER = "?page="
    TOP_PAGE_LINK_CSS = "ul#postList > li a.title-link"
    SUB_PAGE_IMG_CSS = "ul.cmts-list > li a > img"

    # path
    IMAGE_FOLDER = "image"

    NEED_LOGIN = False
