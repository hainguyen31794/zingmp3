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
cookies = {}
with open("d:/Project/dl-playlist-nhac/addons/nct.json") as f:
    cookies = json.load(f)

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