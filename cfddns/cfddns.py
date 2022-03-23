import requests
import json
import logging
import os
from systemd.journal import JournalHandler
import miniupnpc
from decouple import config

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

log = logging.getLogger(__name__)
log.addHandler(JournalHandler())

key = config('API_KEY')
email = config('API_EMAIL')
cf_endpoint = config('API')
zone_id = config('ZONE')
record_id = config('RECORD')

# get WAN ip address
u = miniupnpc.UPnP()
u.discoverdelay = 200
u.discover()
u.selectigd()
wan_ip = u.externalipaddress()

api_headers = {"X-Auth-Key": key, "X-Auth-Email": email}
payload = {"type": "A"}
result = requests.get(
    f"{cf_endpoint}zones/{zone_id}/dns_records/{record_id}", headers=api_headers
)
parsed = result.json()
print(f"Current A Record: {parsed['result']['content']}")

if wan_ip != parsed["result"]["content"]:
    result = requests.patch(
        f"{cf_endpoint}zones/{zone_id}/dns_records/{record_id}",
        json={"content": wan_ip},
        headers=api_headers,
    )
    log.info(f"Current host IP {parsed['result']['content']} for {parsed['result']['name']} is out of date. WAN IP address of {u.externalipaddress()} updated.")
else:
    log.info(f"Current host IP {parsed['result']['content']} for {parsed['result']['name']} is up to date. No changes made.")