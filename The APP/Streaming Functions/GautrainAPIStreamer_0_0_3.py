import operator as op
import numpy as np
import pandas as pd
import geopandas as gpd
import json
import requests
import time
from pandas_geojson import to_geojson
from pandas_geojson import write_geojson
print("Packages have imported successfully")

def GauTrain_bus_data(north, south, east, west):
    """
    Get bus location data using the AfriGIS Gautrain API
    """
    L = []
    res = requests.get(f'https://saas.afrigis.co.za/rest/2/gautrain.mobileServer.getBusesByBoundingBoxServlet/myapisamples/6kECf6rlB8ajG5fCy-Gzhi07PNE/?north={north}&south={south}&east={east}&west={west}')
    L.append(res.json())

    CallDF = pd.DataFrame(L)
    ResultsDF = pd.DataFrame(CallDF['Result'])
    ResultsDF['Time Recorded'] = pd.Timestamp.now()
    BusPosDF = pd.DataFrame()
    BusPosDF['Bus Pos'] = ResultsDF['Result']
    gettermaN = BusPosDF["Bus Pos"][0].get("busPositions")

    BusTrackDF = pd.DataFrame(gettermaN, columns=["busId","currsegment","formattedLastModified","heading","lastModified","latitude","longitude","remainonsegment","routecode"])
    BusTrackDF = BusTrackDF.rename(columns={'heading':'Azimuth'})
    BusTrackDF = BusTrackDF.drop(columns=['currsegment','lastModified', 'remainonsegment', 'routecode'])
    BusTrackDF['response time'] = CallDF["ResponseTime"]
    BusTrackDF = BusTrackDF.fillna(value=BusTrackDF.iat[0,5])
    return BusTrackDF

map_north = -26.034
map_south = -26.049
map_east = 28.123
map_west = 28.116

# map_north = -25.583121
# map_south = -26.347813
# map_east = 28.647122
# map_west = 27.766627

Buslocs = GauTrain_bus_data(map_north, map_south, map_east, map_west)
print(Buslocs)


# REAL TIME LOCATION TRACKING FUNCTION
def bus_locate_call():
    """
    callback function 
    getting real-time location 
    """
    
    df = GauTrain_bus_data(map_north, map_south, map_east, map_west)
    timestmp = []
    for i in range(len(df.index)):
        timestmp.append(str(pd.Timestamp.now()))
    df['Timestamp'] =  timestmp
    df['GPS Last updated Date'] = df['formattedLastModified'].str[26:37]
    df['GPS Last updated Time'] = df['formattedLastModified'].str[37:]
    df = df.rename(columns={'response time':'API Response Time'})
    df = df.drop(columns=['formattedLastModified'])

    return df

#df = bus_locate_call()
#print(df)
#df.to_csv('API_call_outputs/seecols.csv', sep='\t', encoding='utf-8')
#REST_API_URL = "https://api.powerbi.com/beta/92454335-564e-4ccf-b0b0-24445b8c03f7/datasets/7e910e37-2fb8-444a-b75e-4905437084df/rows?key=23gQCnELqZV5kMeBxgIRVN0b2lNYQFBfNWAcbR7A6Q266HKCkVVqxB%2FVZz%2FA6pdQxKiJFHRCxARLh4OCrssPlA%3D%3D"

gjnum = 0
while(gjnum < 2):
    geo_json = to_geojson(df=bus_locate_call(), lat='latitude', lon='longitude', properties=['busId', 'Azimuth','latitude', 'longitude', 'API Response Time', 'Timestamp', 'GPS Last updated Date',  'GPS Last updated Time'])
    #data = bus_locate_call().to_json(orient='records')
    #data_json = bytes(data, encoding='utf-8')
    #print("JSON dataset", geo_json)

    # Post the data on the Power BI API
    #req = requests.post(REST_API_URL, data_json)

    #print(f"Dataset number {gjnum} posted to Power BI API.")

    #json_object = json.dumps(data_json, indent=4)

    #write_geojson(geo_json, filename='API_call_outputs/GeolocateAPICall0.html', indent=4)
    write_geojson(geo_json, filename='Endpoint/public/index.html', indent=4)

    print(f'Wrote dataset number {gjnum} to outputs.')
    gjnum = gjnum + 1
    print()
    time.sleep(10)