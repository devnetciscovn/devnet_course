import requests

url = 'https://sandboxapicdc.cisco.com/api/aaaLogin.json'

body = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}

response1 = requests.post(url, json = body, verify = False)

url = 'https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json'

cookies = response1.cookies

response2 = requests.get(url, cookies = cookies, verify = False)
tenants = response2.json()["imdata"]
for tenant in tenants:
    print(tenant["fvTenant"]["attributes"]["name"])