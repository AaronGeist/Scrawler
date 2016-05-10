from src.core.crawl.CrawlConstants import CrawlConstants
from src.core.crawl.Utils import Utils


class Login:
    # login status cache
    isLogin = False

    @staticmethod
    def login():
        if CrawlConstants.NEED_LOGIN and not Login.isLogin and not Login.checkLogin():
            res = Utils.urlPost(CrawlConstants.LOGIN_PAGE, data=Login.buildPostData(), returnRaw=True)
            print(res.status, res.reason)
            Utils.saveCookie()
            Login.isLogin = Login.checkLogin()
            return Login.isLogin
        else:
            Login.isLogin = True
            return True

    @staticmethod
    def buildPostData():
        soupPage = Utils.urlGet(CrawlConstants.LOGIN_PAGE)
        assert (soupPage is not None)
        formHash = soupPage.select("form input[name=formhash]")
        assert (len(formHash) > 0)
        formHashValue = formHash[0]['value']

        data = dict()
        data['formhash'] = formHashValue
        data['referer'] = "index.php"
        data['loginfield'] = "username"
        data['username'] = CrawlConstants.USERNAME
        data['password'] = CrawlConstants.PASSWORD
        data['loginsubmit'] = "true"

        return data

    @staticmethod
    def checkLogin():
        content = Utils.getContent(Utils.urlGet(CrawlConstants.HOME_PAGE), "div#menu ul li cite a")
        return content is not None and content == CrawlConstants.USERNAME


if __name__ == "__main__":
    Login.login()
    Login.login()
