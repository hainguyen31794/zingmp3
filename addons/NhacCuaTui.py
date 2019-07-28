import requests
import xml.etree.ElementTree as ET
import json


LINK_EMBED = "https://www.nhaccuatui.com/mh/auto/"
LINK_EMBED_PL = "https://www.nhaccuatui.com/lh/auto/"
LINK_XHR = ""
KEYWORD = "https://www.nhaccuatui.com/embed_player/xml?html5=true&key"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
HEADERS = {"User-Agent" : user_agent}
LINK320 = ["<locationhq>", "</locationhq>"]
INFO = ["location", "locationHQ"]
cookies = {
    "JSESSIONID": "orccxe0xp8gju5fmmj4v7gha",
    "JSESSIONID": "orccxe0xp8gju5fmmj4v7gha",
    "NCTCRLS": "b5e9fe63cac80efad459bf21e543f07dd6231d590e34dd9b9c96064c6565c789fac97a9b9bc01259118e8520c8e9a7ebfaa6c1518837f4044b49de3488c1bee5b598509fcf15c55ee5f7f79cf390c9685521821432d08d8e503673f796411a26ce7fa3418d2a8a8b01ce74c7e7e48156af30ccec079265d594a1074f1397cd75629e43bb40e9d35c9f94acb2d4b8f625e44f35b5bb18c9a3d1769a39aad0fa451b42222c3b3cf534734cf181510f9f4733ef7931cf2d097437abf40ad93919efde7fdd8e00e5e1ecfdd458ef95049a5c414cb6971fff1e6e887393ed07b4716ab8892684132b6e34c976eeb22e63153d",
    "NCTNPLS": "d105f0707559ab6913385cf256056d7f",
    "NCT_AUTH_JWT": "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjUwMTE5NzUsImxvZ2luTWV0aG9kIjoiMyIsInVzZXJJZCI6IjMyMjIxNjA1IiwibmJmIjoxNTY0MTQ3OTc1LCJpYXQiOjE1NjQxNDc5NzUsImRldmljZUlkIjoiQjgzMUFBNTI1NjI1NEU2NjhGQzNCNUFGODNFQkZFQzIifQ.Ozn5iSNUhw0vSBF-bDKnqHsLxxn8e94E6YNsNLRLmF4",
    "NCT_BALLOON_INDEX": "True",
    "NCT_BALLOON_INDEX-hainguyen31794": "True",
    "NCT_ONOFF_ADV": "1",
    "autoPlayNext": "True",
    "fbm_414296278689656": "base_domain=.nhaccuatui.com",
    "isConfirm": "True" ,
    "nct_uuid": "B831AA5256254E668FC3B5AF83EBFEC2",
    "nctads_ck": "1bagb47diu0g01dpvaujq9iaz2_1564146199828",
    "qualityPlayerMp3": "high",
    "qualityPlayerVideo": "highest"
}

class NCT():
    def __init__(self, id, ispl = "false"):
        self.url = LINK_EMBED + id if not ispl else LINK_EMBED_PL + id
        self.link_mp3 = self.makeLinkMp3()

    def makeRequests(self, url):
        s = requests.session()
        res = s.get(url, cookies = cookies, headers = HEADERS)
        source = res.content.decode("utf-8")
        return source

    def makeLinkSource(self):
        try:
            source = self.makeRequests(self.url)
            index = source.rfind(KEYWORD)
            link_source = LINK_XHR + source[index: index +92]
            return link_source
        except:
            return False

    def makeLinkMp3(self):
        try:
            source = self.makeRequests(self.makeLinkSource())
            root = ET.fromstring(source)        
            data = ""
            for childs in root:
                datai = ""
                for child in childs:
                    if child.tag == "location": datai = child.text.strip() + "&#010;"
                    if child.tag == "locationHQ" and child.text is not None: datai = child.text.strip() + "&#010;"
                data += datai
            return data
        except:
            return "Khong the get link! :'("
        

    def __del__(self):
        print("HUY NCT THANH CONG")

if __name__ == "__main__":
    n = NCT("4mS3RM4QWrvb")
    print(n.link_mp3)