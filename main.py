from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import urllib.request, json, os

load_dotenv()

trip_updates = 'https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-tp/beta/v1/TripUpdates'
vehicle_positions = 'https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-vp/beta/v1/VehiclePositions'

headers = {
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': os.environ['PRIMARY_KEY'],
}

req = urllib.request.Request(vehicle_positions, headers=headers)

with urllib.request.urlopen(req) as response:
    data = response.read()

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(data)

# print('GTFS version:', feed.header.gtfs_realtime_version)
# print('Timestamp:', feed.header.timestamp)

# for entity in feed.entity:
#     if entity.trip_update:
#         trip = entity.trip_update.trip
#         print('Trip ID:', trip.trip_id)

feed_dict = MessageToDict(feed)
print(json.dumps(feed_dict, indent=2))
