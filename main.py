from dotenv import load_dotenv
import urllib.request, json, os

load_dotenv()

try:
    url = "https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-tp/beta/v1/TripUpdates"

    hdr = {
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': os.environ['PRIMARY_KEY'],
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print(response.read())
except Exception as e:
    print(e)
