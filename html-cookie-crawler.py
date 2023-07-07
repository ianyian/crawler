import urllib.request as req


def getData(url):
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": ""
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    print("****************** page#" +
          str(count) + "***************************")
    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count += 1
