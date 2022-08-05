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
    df['GPSLastupdatedDate'] = df['formattedLastModified'].str[26:37]
    df['GPSLastupdatedTime'] = df['formattedLastModified'].str[37:]
    df = df.rename(columns={'response time':'API_Response_Time'})
    df = df.drop(columns=['formattedLastModified'])

    return df

#df = bus_locate_call()
#print(df)
#df.to_csv('API_call_outputs/seecols.csv', sep='\t', encoding='utf-8')

gjnum = 0
while(True):
    geo_json = to_geojson(df=bus_locate_call(), lat='latitude', lon='longitude', properties=['busId', 'Azimuth','latitude', 'longitude', 'API_Response_Time', 'Timestamp', 'GPSLastupdatedDate',  'GPSLastupdatedTime'])
    #data = bus_locate_call().to_json(orient='records')


    #write_geojson(geo_json, filename='API_call_outputs/GeolocateAPICall0.html', indent=4)
    #write_geojson(geo_json, filename='GautrainComputeFolder/dashtreme-master/data.json', indent=4)
    write_geojson(geo_json, filename='GautrainComputeFolder/dashtreme-master/data.geojson', indent=4)
    write_geojson(geo_json, filename='GautrainComputeFolder/dashtreme-master/latency.json', indent=4)

    print(f'Wrote dataset number {gjnum} to outputs.')
    gjnum = gjnum + 1
    print()
    time.sleep(5)
