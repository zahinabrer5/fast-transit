from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import json, requests, os

load_dotenv()

trip_updates = 'https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-tp/beta/v1/TripUpdates'
vehicle_positions = 'https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-vp/beta/v1/VehiclePositions'


def get_json(url):
    headers = {
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': os.environ['PRIMARY_KEY'],
    }

    resp = requests.get(url, headers=headers).content

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(resp)

    # print('GTFS version:', feed.header.gtfs_realtime_version)
    # print('Timestamp:', feed.header.timestamp)

    # for entity in feed.entity:
    #     if entity.trip_update:
    #         trip = entity.trip_update.trip
    #         print('Trip ID:', trip.trip_id)

    feed_dict = MessageToDict(feed)
    return json.dumps(feed_dict, indent=2)


print(get_json(trip_updates))

""" Plan:
1. use geolocation to find nearest bus stop, or let user choose manually
2. let user choose from a list of buses headed for the stop
3. show the estimated time remaining for the bus to arrive at the stop
"""
