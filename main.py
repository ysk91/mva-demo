from zipcode_api import ZipcodeApi

zipcode_api = ZipcodeApi()
address = zipcode_api.get().json()

print(address)