import requests

url = "https://zipcloud.ibsnet.co.jp/api/search"


def get(zipcode):
    payload = {"zipcode": zipcode}
    return requests.get(url, payload)
