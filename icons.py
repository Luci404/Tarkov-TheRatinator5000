import json
import requests
import os.path

with open("data.json", 'r') as file:
    data = file.read()

obj = json.loads(data)

for item in obj:
    uid = item["uid"]
    iconPath = item["iconPath"]
    path = "icons/" + uid + ".png"
    print("UID: " + uid + " | Icon path: " + iconPath)
    if os.path.isfile(path) or iconPath == "":
        continue
    response = requests.get(iconPath)
    if (response.status_code == 200):
        try:
            with open(path, "wb") as file:
                file.write(response.content)
        except:
            print("Error: Failed to write image!")
    else:
        print("Error: Failed to download image!")