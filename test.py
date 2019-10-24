import requests
import json

rsp = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
rsp.encoding = "UTF-8"

with open("1.dat", "w", encoding="UTF-8") as fp:
  dick = json.loads(rsp.content.decode("UTF-8").split('\n')[0])
  json.dump(dick, fp, indent=4, ensure_ascii=False)
