import requests
import sys

filename = str(sys.argv[1]) 

imgdata = {"upload": open(filename, "rb")}
url = "http://uploads.im/api"

result = requests.post(url, files=imgdata)

data = result.json()
print data
print data["data"]["img_url"]


