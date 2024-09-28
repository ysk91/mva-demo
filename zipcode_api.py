import requests

class ZipcodeApi:

    def get(self):
        zipcode = input('Enter a zipcode: ')
        url = 'https://zipcloud.ibsnet.co.jp/api/search'
        payload = {'zipcode': zipcode}
        return requests.get(url, payload)
