A simple Python3 script to update a zone A record using the Cloudflare API

Requires the following non-standard Python3 modules.

* miniupnpc - Used to get WAN IP address from local IGD (probably your router)
* python-decouple - Used to manage config.ini to keep authentication credentials out of the main script.

Script will query local network to find an IGD using UPnP, and if found will grab the external IP address. Next, it will check your specific zone at Cloudflare to verify if the domain ip needs to be updated.