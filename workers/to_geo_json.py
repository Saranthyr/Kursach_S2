def convert(text):
    geo = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "summary": {
                            "lengthInMeters":int(text['routes'][0]['summary']['lengthInMeters']),
                            "travelTimeInSeconds":int(text['routes'][0]['summary']['travelTimeInSeconds']),
                            "trafficDelayInSeconds":int(text['routes'][0]['summary']['trafficDelayInSeconds']),
                            "trafficLengthInMeters":int(text['routes'][0]['summary']['trafficLengthInMeters']),
                            "departureTime":text['routes'][0]['summary']['departureTime'],
                            "arrivalTime":text['routes'][0]['summary']['arrivalTime']
                        },
                        "sections": [
                                {
                                    "startPointIndex":int(text['routes'][0]['sections'][0]['startPointIndex']),
                                    "endPointIndex":int(text['routes'][0]['sections'][0]['endPointIndex']),
                                    "sectionType":text['routes'][0]['sections'][0]['sectionType'],
                                    "travelMode":text['routes'][0]['sections'][0]['travelMode']
                                }
                        ],
                        "segmentSummary": [
                            {
                                "lengthInMeters": int(text['routes'][0]['legs'][0]['summary']['lengthInMeters']),
                                "travelTimeInSeconds": int(text['routes'][0]['legs'][0]['summary']['travelTimeInSeconds']),
                                "trafficDelayInSeconds": int(text['routes'][0]['legs'][0]['summary']['trafficDelayInSeconds']),
                                "trafficLengthInMeters": int(text['routes'][0]['legs'][0]['summary']['trafficLengthInMeters']),
                                "departureTime": text['routes'][0]['legs'][0]['summary']['departureTime'],
                                "arrivalTime": text['routes'][0]['legs'][0]['summary']['arrivalTime']
                            }
                        ],
                    },
                    "geometry":{
                        "coordinates":[[float(i['longitude']), float(i['latitude'])]
                                       for i in text['routes'][0]['legs'][0]['points']],
                        "type": "LineString"
                    }
                },
            ]
        }
    return geo
