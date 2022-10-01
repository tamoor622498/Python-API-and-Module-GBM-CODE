import requests
import cheapShark
import pantryID
import json

url = "https://getpantry.cloud/apiv1/pantry/"+pantryID.key+"/basket/hackUMBC"

payload = json.dumps(cheapShark.getDeals())

#response = requests.post(url, data=payload)
#print(response.text)

res = requests.get(url)
print(res.text)