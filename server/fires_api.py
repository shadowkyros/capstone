# encoding: utf-8
"""Provides the `Active Fires` API"""


# def haversine(lon1, lat1, lon2, lat2):
#     from math import radians, cos, sin, asin, sqrt, atan2, degrees
#     """
#     Calculate the great circle distance between two points
#     on the earth (specified in decimal degrees)
#     http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
#     """
#     # convert decimal degrees to radians
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
#     # haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * asin(sqrt(a))
#     r = 3956  # Radius of earth in miles. Use 6371 for kilometers
#     distance = c * r
#     bearing = atan2(sin(lon2 - lon1) * cos(lat2), cos(lat1) *
#                     sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1))
#     bearing = degrees(bearing)
#     bearing = (bearing + 360) % 360
#     return distance, bearing


def update_fires():
    # args = {
    #     "source": "..\static_data\ActiveFirePerimeters.kml",
    #     "output_file": "current.json",
    #     "output_dir": "..\output\\"
    # }
    args = {}
    AF = ActiveFires.ActiveFires(args)
    # AF.emitter(AF.parser(AF.get_kml("")))
    AF.emitter(AF.parser(AF.get_kml("")), '_ActiveFiresDict', True)


# def stationquery(dict_):
#     args = {}
#     AF = ActiveFires.ActiveFires(args)
#     firedict = AF.parser(AF.get_kml(""))
#     for i in range(len(firedict)):
#         print(firedict[i]['Fire Name'])


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from src import ActiveFires as ActiveFires
    else:
        from ..src import ActiveFires as ActiveFires


# Init.
update_fires()
# stationquery(update_fires())
# put the code here to get the stations and serve the info back to the user.
# look at `Tornado` to do this.  It's the defacto standard.
