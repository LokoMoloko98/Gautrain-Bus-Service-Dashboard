import numpy as np
import pandas as pd
import geopandas as gpd
import json
import requests
import time
from pandas_geojson import to_geojson
from pandas_geojson import write_geojson
import sys
from point import *
from pyproj import crs
print("Packages have imported successfully")


class PQuadTreeNode():
    def __init__(self, point, nw = None, ne = None, se = None, sw = None):
        self.point = point
        self.nw = nw
        self.ne = ne
        self.se = se
        self.sw = sw

def __repr__(self):
    return point.__repr__(self.point)

def is_leaf(self):
    return self.nw==None and self.ne==None and \
    self.se==None and self.sw==None

def search_pqtree(q, p, is_find_only=True):
    if q is None:
        return
    if q.point==p and is_find_only:
        return q
    dx,dy=0,0
    if p.x>q.point.x:
        dx=1
    if p.y>q.point.y:
        dy=1
    qnum = dx+dy*2
    child = [q.sw, q.se, q.nw, q.ne][qnum]
    if child is None:
        if not is_find_only:
            return q
        else: # q is not the point and no more to search for
            return
    return search_pqtree(child, p, is_find_only)

def insert_pqtree(q, p):
    n = search_pqtree(q, p, False)
    node = PQuadTreeNode(point=p)
    if p.x<n.point.x and p.y<n.point.y:
        n.sw = node
    elif p.x<n.point.x and p.y>=n.point.y:
        n.nw = node
    elif p.x>=n.point.x and p.y<n.point.y:
        n.se = node
    else:
        n.ne = node

def pointquadtree(data):
    root = PQuadTreeNode(point = data[0])
    for p in data[1:]:
        insert_pqtree(root, p)
    return root


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
#print(Buslocs)


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
    df = df.rename(columns={'response time':'API Response Time'})
    df = df.drop(columns=['formattedLastModified'])

    return df

#df = bus_locate_call()
#print(df)


if __name__ == '__main__':
    data1 = []
    pointsmetadata = []
    data = bus_locate_call()
    data.to_csv('out.csv', index=False)
    for i in range(len(data)):
        data1.append([data.iloc[i,2], data.iloc[i,3], data.iloc[i,0]])
    points = []
    for d in data1:
        points.append(Point(d[0], d[1], d[2]))
    for p in range(len(points)):
        print(points[p], points[p].get_busID())
    
    # #insertions
    print("Inserting Points...")
    tick_insertion = time.perf_counter()
    q = pointquadtree(points) #THE ACTUAL INSERTION CALL
    tock_insertion = time.perf_counter()
    print("Insertion Procss Done.")
    insertiontime = f"{tock_insertion - tick_insertion:0.10f} seconds"
    print("Insertion time =", insertiontime)
    print()

    lons = []
    lats = []

    #retrieval 
    print("Retrieving All Points...")
    tick_retrieval = time.perf_counter()
    for p in points:
        if search_pqtree(q, p) is None:
            print("None") #THE ACTUAL QUERY CALL
        else:
            print(search_pqtree(q, p).point, search_pqtree(q, p).point.get_busID())
        #lons.append(float(__repr__(search_pqtree(q, p))[1:14]))
        #lats.append(float(__repr__(search_pqtree(q, p))[16:30]))
    tock_retrieval = time.perf_counter()
    print("All Points Retrieved.")
    retrievalime = f"{tock_retrieval - tick_retrieval:0.10f} seconds"
    print("Retrieval time =", retrievalime)
    print()


    # gjnum = 0
    # while(True):
    #     geo_json = to_geojson(df=bus_locate_call(), lat='latitude', lon='longitude', properties=['busId', 'Azimuth','latitude', 'longitude', 'API Response Time', 'Timestamp', 'GPSLastupdatedDate',  'GPSLastupdatedTime'])
    #     #data = bus_locate_call().to_json(orient='records')


    #     #write_geojson(geo_json, filename='API_call_outputs/GeolocateAPICall0.html', indent=4)
    #     write_geojson(geo_json, filename='GautrainComputeFolder/dashtreme-master/index.geojson', indent=4)

    #     print(f'Wrote dataset number {gjnum} to outputs.')
    #     gjnum = gjnum + 1
    #     print()
    #     time.sleep(10)

