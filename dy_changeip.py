import requests
import json

myip = requests.get("http://ifconfig.me").content.decode("UTF-8")
dnsname='sub.example.com'
dw = requests.get("https://api.cloudflare.com/client/v4/zones/{zoneid}/dns_records",headers={"Authorization": "Bearer token", "Content-Type": "application/json"}).content.decode("UTF-8")
for dns in json.loads(dw)['result']:
    if dnsname in dns['name']:
        if dns['content']!=myip:
            requests.put("https://api.cloudflare.com/client/v4/zones/{zoneid}/dns_records/"+dns['id'],headers={"Authorization": "Bearer token", "Content-Type": "application/json"}
                         ,json={"type":"A","name":dnsname,"content":myip})

