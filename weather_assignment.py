import json
from csv import DictReader

# create a dictionary of stations by station id
with open('stations.csv') as file:
    reader = DictReader(file)
    stations = list(reader)
stations_by_id = {}
for station in stations:
    stations_by_id[station["Station"]] = {}
    stations_by_id[station["Station"]] = station
stations = stations_by_id

#import the json data to a variable precipitation
with open("precipitation.json") as file:
    precipitation = json.load(file)

#create a list of just the Seattle measurements
seattle_precipitation = []
for measurement in precipitation:
    if measurement["station"] == "GHCND:US1WAKG0038":
        seattle_precipitation.append(measurement)

# print(seattle_precipitation)

#calculate total monthly precipitaion
total_precipitation_1 = 0
total_precipitation_2 = 0
total_precipitation_3 = 0
total_precipitation_4 = 0
total_precipitation_5 = 0
total_precipitation_6 = 0
total_precipitation_7 = 0
total_precipitation_8 = 0
total_precipitation_9 = 0
total_precipitation_10 = 0
total_precipitation_11 = 0
total_precipitation_12 = 0
for measurement in seattle_precipitation:
    if measurement["date"].startswith("2010-01") == True:
        total_precipitation_1 = total_precipitation_1 + measurement["value"]
    elif measurement["date"].startswith("2010-02") == True:
        total_precipitation_2 = total_precipitation_2 + measurement["value"]
    elif measurement["date"].startswith("2010-03") == True:
        total_precipitation_3 = total_precipitation_3 + measurement["value"]
    elif measurement["date"].startswith("2010-04") == True:
        total_precipitation_4 = total_precipitation_4 + measurement["value"]
    elif measurement["date"].startswith("2010-05") == True:
        total_precipitation_5 = total_precipitation_5 + measurement["value"]
    elif measurement["date"].startswith("2010-06") == True:
        total_precipitation_6 = total_precipitation_6 + measurement["value"]
    elif measurement["date"].startswith("2010-07") == True:
        total_precipitation_7 = total_precipitation_7 + measurement["value"]
    elif measurement["date"].startswith("2010-08") == True:
        total_precipitation_8 = total_precipitation_8 + measurement["value"]
    elif measurement["date"].startswith("2010-09") == True:
        total_precipitation_9 = total_precipitation_9 + measurement["value"]
    elif measurement["date"].startswith("2010-10") == True:
        total_precipitation_10 = total_precipitation_10 + measurement["value"]
    elif measurement["date"].startswith("2010-11") == True:
        total_precipitation_11 = total_precipitation_11 + measurement["value"]
    elif measurement["date"].startswith("2010-12") == True:
        total_precipitation_12 = total_precipitation_12 + measurement["value"]

total_monthly_precipitation = [total_precipitation_1,total_precipitation_2,total_precipitation_3,total_precipitation_4,total_precipitation_5,total_precipitation_6,total_precipitation_7,total_precipitation_8,total_precipitation_9, total_precipitation_10, total_precipitation_11, total_precipitation_12]

# print(total_monthly_precipitation)

#calculate total yearly precipitation
total_yearly_precipitation = 0
for value in total_monthly_precipitation:
    total_yearly_precipitation = total_yearly_precipitation + value

#calculate relative monthly precipitation
relative_monthly_precipitation = []
for value in total_monthly_precipitation:
    relative_monthly_precipitation.append(value/total_yearly_precipitation)

print(relative_monthly_precipitation)


results = {
    "Seattle" : {
        "station": "GHCND:US1WAKG0038",
        "state" : "WA",
        "total_monthly_precipitation" : total_monthly_precipitation,
        "total_yearly_precipitation" : total_yearly_precipitation,
        "relative_monthly_precipitation" : relative_monthly_precipitation
    }
}

with open("results.json", 'w') as file:
    json.dump(results, file, indent=4)
