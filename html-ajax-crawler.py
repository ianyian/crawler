import json
import urllib.request as req
url = "https://medium.com/_/api/home-feed"
request = req.Request(url,
                      headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                               })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

data = data.replace("])}while(1);</x>", "")
data = json.loads(data)

posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])
