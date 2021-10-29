#==CORONA INFO SCRAPPER
from bs4 import BeautifulSoup #Don't Forget To Install bs4 first
import requests, json

dunia = "https://www.worldometers.info/coronavirus/"
heads = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
reqs = requests.get(dunia, headers = heads)
datas = BeautifulSoup(reqs.content , "lxml")
datax = datas.findAll("div", {"id": "maincounter-wrap"})
res = ""
for x in datax:
    res += str(x)
kasusx = res.split('<span>')[0].split("</span>")[0].split(">")[5]
sembuhx = res.split('<span>')[2].split("</span>")[0]
matix = res.split('<span>')[1].split("</span>")[0]
result = {
    "result":{
        "dunia": {
            "positif": kasusx, 
            "sembuh": sembuhx, 
            "meninggal": matix
        }
     }
}
print(str(json.dumps(result,indent=4)))
