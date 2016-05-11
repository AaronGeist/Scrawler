class CrawlConstants:
    # header
    DEFAULT_HEADER = [(
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36")]

    IMGAGE_HEADER = [("Content-Type", "image/jpeg"), ("Server", "cloudflare-nginx")]

    # html tag attributes
    ATTR_HREF = 'href'
    ATTR_SRC = 'src'

    COOKIE_FILE = "ck.txt"

    # path
    FOLDER_IMAGE = "image"


    # url
    # BASE_URL = "http://174.127.195.176/bbs/"
    # HOME_PAGE = BASE_URL + "forum-318-1.html"
    # LOGIN_PAGE = BASE_URL + "logging.php?action=login"
    # TOP_PAGE_LINK_CSS = "table tbody tr th.new span > a"
    # SUB_PAGE_IMG_CSS = 'a[href*="imagetwist"] > img[src*="imagetwist"]'
    # USERNAME = ""
    # PASSWORD = ""

    # BASE_URL = "http://www.guokr.com/"
    # HOME_PAGE = BASE_URL + "group/31/"
    # LOGIN_PAGE = ""
    # HOME_PAGE_BROWSER = "?page="
    # TOP_PAGE_LINK_CSS = "ul#postList > li a.title-link"
    # SUB_PAGE_IMG_CSS = "ul.cmts-list > li a > img"

    BASE_URL = "http://weibo.cn/"
    HOME_PAGE = BASE_URL
    LOGIN_PAGE = "http://login.weibo.cn/login/?rand=1640789743&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%E5%BE%AE%E5%8D%9A&vt=4&revalid=2&ns=1"
    LOGIN_HEADERS = [
                ("User-Agent",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"),
                ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
                ("Accept-Language", "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2"),
                ("Content-Type", "application/x-www-form-urlencoded"),
                ("Host", "login.weibo.cn"),
                ("Origin", "http://login.weibo.cn"),
                ("DNT", "1"),
                ("Upgrade-Insecure-Requests", "1"),
                ("Referer",
                 "http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=4")
            ]

    NEED_LOGIN = True
    LOGIN_INDICATOR_CSS = "div.u > div.ut"
    LOGIN_VERIFICATION_STR = "奏乐爱做俯卧飞鸟"
    USERNAME = ""
    PASSWORD = ""

