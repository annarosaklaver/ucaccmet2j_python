import json

#import the json data to a variable precipitation
with open("precipitation.json") as file:
    precipitation = json.load(file)

#create a list of just the Seattle measurements
seattle_precipitation = []
for measurement in precipitation:
    if measurement["station"] == "GHCND:US1WAKG0038":
        seattle_precipitation.append(measurement)

print(seattle_precipitation)
