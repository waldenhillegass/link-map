from dataclasses import dataclass
import json
import time
from typing import List
import requests


@dataclass
class Train():
    id: str
    direction: str
    next_station_index: int
    next_station: str
    time_until: str
    leg_total: str

    def __str__(self):
        return f"""id: {self.id}
direction: {self.direction}
next_station: {self.next_station}
next_station_index: {self.next_station_index}
time_until: {self.time_until}
total_leg_time: {self.leg_total}"""



class TrainGetter():
    def __init__(self) -> None:
        pass

    def station_id_to_name(self, id, api_dict):
        for station in api_dict["data"]["references"]["stops"]:
            if id == station["id"]:
                return station["name"]

    def station_name_to_index(self, name):
        m = {"Angle Lake" : 0,
             "SeaTac/Airport": 1,
             "Tukwila Int'l Blvd": 2,
             "Rainier Beach": 3,
             "Othello": 4,
             "Columbia City": 5,
             "Mount Baker": 6,
             "Beacon Hill": 7,
             "SODO": 8,
             "Stadium": 9,
             "Int'l Dist/Chinatown": 10,
             "Pioneer Square": 11,
             "Symphony": 12,
             "Westlake": 13,
             "Capitol Hill": 14,
             "Univ of Washington": 15,
             "U District": 16,
             "Roosevelt": 17,
             "Northgate": 18,
             "Shoreline South/148th": 19,
             "Shoreline North/185th": 20,
             "Mountlake Terrace": 21,
             "Lynnwood City Center": 22
            }
        return m[name]
    
    def get_direction(self, trip_id, api_dict):
        for trip in api_dict["data"]["references"]["trips"]:
            if trip["id"] == trip_id:
                if trip["directionId"] == "0":
                    return "S"
                else:
                    return "N"
        raise ValueError(f"Trip id {trip_id} not found")

    def get_next_station(self, trip_dict, api_dict):
        next_stop_id = trip_dict["status"]["nextStop"]
        name = self.station_id_to_name(next_stop_id, api_dict)
        index = self.station_name_to_index(name)
        return name, index
    
    def get_trains(self, json_str) -> List[Train]:
        api_dict = json.loads(json_str)
        out = []
        for trip in api_dict["data"]["list"]:
            t = self.process_train(trip, api_dict)
            out.append(t)
            print(t)
            print("")
            print("")
        return out


    def get_leg_time(self, trip_dict):
        next_stop_id = trip_dict["status"]["nextStop"]
        for i, stop in enumerate(trip_dict["schedule"]["stopTimes"]):
            if stop["stopId"] == next_stop_id:
                if i == 0:
                    return 0
                return stop["arrivalTime"] - trip_dict["schedule"]["stopTimes"][i - 1]["departureTime"]
    
        
    def process_train(self, trip_dict, api_dict):
        next_station_name, next_station_index = self.get_next_station(trip_dict, api_dict)
        now = time.time()
        updated = trip_dict["status"]["lastUpdateTime"] / 1000
        staleness = now - updated
        time_to_next_stop = max(trip_dict["status"]["nextStopTimeOffset"] - staleness, 0)

        trip_id = trip_dict["tripId"]

        return Train(
            id=trip_id,
            direction=self.get_direction(trip_id, api_dict),
            next_station_index=next_station_index,
            next_station=next_station_name,
            time_until=time_to_next_stop,
            leg_total=self.get_leg_time(trip_dict)
        )




