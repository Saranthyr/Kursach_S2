import timeit
from back.db_conn import connection
import math


earth_rad = 6371
coordinates = []

distances = []


def degr_to_rad(degrees):
    return degrees * math.pi/180


def coordinates_pool(tablename):
    conn = connection()
    cursor = conn.cursor()
    q = 'select latitude, longitude from ' + tablename + ' order by id asc'
    cursor.execute(q)
    for record in cursor.fetchall():
        coordinates.append([record[0], record[1]])


def create_coordinates_pool():
    coordinates_pool('bar_net')


def check_distance(latitude, longitude):
    start = timeit.default_timer()
    create_coordinates_pool()
    for coords in coordinates:
        delta_lat = degr_to_rad(latitude - coords[0])
        delta_long = degr_to_rad(longitude - coords[1])
        lat1 = degr_to_rad(coords[0])
        lat2 = degr_to_rad(latitude)
        a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.sin(delta_long/2) * math.sin(delta_long/2)\
            * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distances.append([earth_rad*c, coords[0], coords[1]])
    finish = timeit.default_timer()
    print("Time elapsed: " + str(finish - start))


def nearest (latitude, longitude):
    check_distance(latitude, longitude)
    closest = 5
    closest_coords = []
    for i in range(len(distances)):
        if distances[i][0] < 2.5:
            if distances[i][0] < closest:
                closest = distances[i][0]
                closest_coords = [distances[i][1], distances[i][2]]
    return closest_coords
