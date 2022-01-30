from back.db_conn import connection
import math


earth_rad = 6371
coordinates = []

distances = []

unavailable = {"при", "ГБОУ", "Школа", "школа", "ГОУ", "СОШ", "Колледж",
               "инст", "лиц", "гимн", "гуп", "гбпоу", "оао",
               "концерн", "сотруд", "комбинат", "КП", "академ",
               "общеж", "шк"}


def degr_to_rad(degrees):
    return degrees * math.pi/180


def coordinates_pool(tablename, net):
    conn = connection()
    cursor = conn.cursor()
    q = 'select latitude, longitude, name, address, phone, seats_count from ' +\
        tablename + ' where net_status = ' + str(net) + ' order by id asc'
    cursor.execute(q)
    for record in cursor.fetchall():
        if (tablename == "stolovaja" or tablename == "bufet") and (net == False):
            if any(item.lower() in record[2].lower() for item in unavailable):
                continue
            else:
                coordinates.append([record[0], record[1], record[2], record[3], record[4], record[5]])
        else:
            coordinates.append([record[0], record[1], record[2], record[3], record[4], record[5]])
    cursor.close()
    conn.close()


def create_coordinates_pool(table, net):
    coordinates_pool(str(table), net)


def check_distance(latitude, longitude, table, net):
    create_coordinates_pool(table, net)
    for coords in coordinates:
        delta_lat = degr_to_rad(latitude - coords[0])
        delta_long = degr_to_rad(longitude - coords[1])
        lat1 = degr_to_rad(coords[0])
        lat2 = degr_to_rad(latitude)
        a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.sin(delta_long/2) * math.sin(delta_long/2)\
            * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distances.append([earth_rad*c, coords[0], coords[1], coords[2], coords[3], coords[4], coords[5]])


def nearest (latitude, longitude, table, net, mode):
    check_distance(latitude, longitude, table, net)
    closest = 5
    closest_coords = []
    if mode == "pedestrian":
        max_distance = 2.5
    else:
        max_distance = 5
    for i in range(len(distances)):
        if distances[i][0] < max_distance:
            if distances[i][0] < closest:
                closest = distances[i][0]
                closest_coords = [distances[i][1],
                                  distances[i][2],
                                  distances[i][3],
                                  distances[i][4],
                                  distances[i][5],
                                  distances[i][6]]
    distances.clear()
    coordinates.clear()
    return closest_coords
