import requests

LINK_EMBED = "https://zingmp3.vn/embed/song/"
LINK_XHR = "https://mp3.zing.vn/xhr"
KEYWORD = "/media/get-source?type=audio&key="
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
headers = {"User-Agent" : user_agent}
class Zing():
    def __init__(self, id):
        self.url = LINK_EMBED + id
        self.link_mp3 = self.makeRequests()

    def makeRequests(self):
        s = requests.session()
        res = s.get(self.url, headers = headers)
        source_data = res.content.decode("utf-8")
        index = source_data.rfind(KEYWORD)
        link_source = LINK_XHR + source_data[index: index +66]
        return link_source

    def __del__(self):
        print("HUY ZingMp3 THANH CONG")

if __name__ == "__main__":
    z = Zing("ZWADZBB9");
    print(z.link_mp3)
        
        
