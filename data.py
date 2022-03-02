import requests
import json
import typing
import time

class ItemInfoStruct:
    uid: str = ""
    name: str = "Name"
    shortName: str = "Short Name"
    price: float = 0.0
    traderPrice: float = 0.0
    traderName: str = "Trader Name"
    slots: int = 0
    iconPath: str = ""

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

itemInfoStructs: typing.List["ItemInfoStruct"] = []
response = requests.get("https://tarkov-market.com/api/v1/items/all?x-api-key=" + API_KEY)
if (response.status_code == 200):
    for data in response.json():
        print(data["name"])
        itemInfoStruct: ItemInfoStruct = ItemInfoStruct()
        itemInfoStruct.uid = data["uid"]
        itemInfoStruct.name = data["name"]
        itemInfoStruct.shortName = data["shortName"]
        itemInfoStruct.price = data["price"]
        itemInfoStruct.traderPrice = data["traderPrice"]
        itemInfoStruct.traderName = data["traderName"]
        itemInfoStruct.slots = data["slots"]
        itemInfoStruct.iconPath = data["icon"]
        itemInfoStructs.append(itemInfoStruct)
else:
    print("Error: Request failed, status code: " + str(response.status_code))

def dumper(obj):
    return obj.__dict__

jsonString = json.dumps(itemInfoStructs, default=dumper, indent=2)

with open("data.json", 'w') as file:
    file.write(jsonString)