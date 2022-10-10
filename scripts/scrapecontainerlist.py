import urllib.request
import sys
from bs4 import BeautifulSoup

def download():
    weburl = urllib.request.urlopen("https://awesome-docker.netlify.app/")

    if weburl.getcode()==200:
        content = weburl.read()
        print(content)
    else:
        print("Failed to get the content")


def getItems(fileaddr):
    with open(fileaddr, "r") as f:
        c = f.read()
        soup = BeautifulSoup(c, "html.parser")
        items = soup.find_all('li')
        for it in items:
            fl = it.find_all('a')
            if len(fl)>0 and fl[0].get("href").startswith("https://github.com"):
                print(fl[0].get("href"), ", ", fl[0].get_text())
        #print(soup.prettify())
        # all_hrefs = [a.get('href') for a in soup.find_all('a')]
    return

if __name__ == "__main__":
    if sys.argv[1] == "download":
        download()
    elif sys.argv[1] == "items":
        getItems(sys.argv[2])
    else:
        print("Unknown commandline parameters. Use download or itesm")