from sys import argv
from requests import get
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutor

disable_warnings()
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


def sendDetectionRequest(url, urlId):
    try:
        url = url.strip()
        print("[{}] GET {}".format(urlId, url))
        get(url, verify=False, proxies=proxies, timeout=10)
    except Exception as e:
        print(e)
        pass


threads = []
urlId = 0
urlFile = open(argv[1], "r", encoding="utf-8")
urlList = urlFile.readlines()
with ThreadPoolExecutor(max_workers=15) as executor:
    for url in urlList:
        urlId += 1
        threads.append(executor.submit(sendDetectionRequest, url, urlId))
