from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.Utils import Utils


class Login:
    # login status cache
    isLogin = False

    @staticmethod
    def login():
        if CrawlConstants.NEED_LOGIN and not Login.isLogin and not Login.checkLogin():
            res = Utils.urlPost(CrawlConstants.LOGIN_PAGE, data=Login.buildPostData(),
                                headers=CrawlConstants.LOGIN_HEADERS, returnRaw=True)
            print(res.status, res.reason)

            Utils.saveCookie()
            Login.isLogin = Login.checkLogin()
            return Login.isLogin
        else:
            Login.isLogin = True
            return True

    # @staticmethod
    # def buildPostData():
    #     soupPage = Utils.urlGet(CrawlConstants.LOGIN_PAGE)
    #     assert (soupPage is not None)
    #     formHash = soupPage.select("form input[name=formhash]")
    #     assert (len(formHash) > 0)
    #     formHashValue = formHash[0]['value']
    #
    #     data = dict()
    #     data['formhash'] = formHashValue
    #     data['referer'] = "index.php"
    #     data['loginfield'] = "username"
    #     data['username'] = CrawlConstants.USERNAME
    #     data['password'] = CrawlConstants.PASSWORD
    #     data['loginsubmit'] = "true"
    #
    #     return data

    @staticmethod
    def buildPostData():
        soupPage = Utils.urlGet(CrawlConstants.LOGIN_PAGE)
        assert soupPage is not None

        pwKey = soupPage.select('input[type="password"]')[0]['name']
        vkValue = soupPage.select('input[name="vk"]')[0]['value']
        capId = soupPage.select('input[name="capId"]')[0]['value']
        captchaSrc = soupPage.select('form > div > img')[0]['src']
        print("captcha url=" + captchaSrc)

        captcha = input("Input your id plz:\n")

        data = dict()
        data['mobile'] = CrawlConstants.USERNAME
        data[pwKey] = CrawlConstants.PASSWORD
        data['capId'] = capId
        data['vk'] = vkValue
        data['backURL'] = "http%3A%2F%2Fweibo.cn%2F"
        data['code'] = captcha
        data['backTitle'] = "微博"
        data['submit'] = "登录"

        return data

    @staticmethod
    def checkLogin():
        content = Utils.getContent(Utils.urlGet(CrawlConstants.HOME_PAGE), CrawlConstants.LOGIN_INDICATOR_CSS)
        return content is not None and content == CrawlConstants.LOGIN_VERIFICATION_STR


if __name__ == "__main__":
    Login.login()
