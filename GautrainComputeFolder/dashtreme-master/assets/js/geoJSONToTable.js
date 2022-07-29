var golfdata = {
    "type": "FeatureCollection",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },

    "features": [
        {
            "type": "Feature",
            "properties": {
                "ename": "PGA Championship",
                "efdate": "10.08.2015",
                "etdate": "16.08.2016",
                "esportcat": "Golf",
                "elocnam": "Whistling Straits",
                "elocstree": "N8501 County Road LS",
                "ecity": "Sheboygan",
                "eloczip": "WI 53083",
                "elocland": "USA",
                "eclubnam": null,
                "elink": "http:\/\/www.pga.com\/pgachampionship\/",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-87.7351084, 43.8509493]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "ename": "Ryder Cup 2016",
                "efdate": "01.09.2016",
                "etdate": "02.10.2016",
                "esportcat": "Golf",
                "elocnam": "Hazeltine National Golf Course",
                "elocstree": "1900 Hazeltine Blvd",
                "ecity": "Chaska",
                "eloczip": "MN 55318",
                "elocland": "USA",
                "eclubnam": null,
                "elink": "http:\/\/www.rydercup.com\/",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-93.5908194, 44.833729]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "ename": "2015 Toshiba Classic",
                "efdate": "26.10.2015",
                "etdate": "01.11.2015",
                "esportcat": "Golf",
                "elocnam": "Newport Beach Country Club",
                "elocstree": "1600 East Coast Hwy",
                "ecity": "Newport Beach",
                "eloczip": "CA 92660",
                "elocland": "California, USA",
                "eclubnam": "Newport Beach Country Club",
                "elink": "http:\/\/www.toshibaclassic.com\/",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-117.8829118, 33.615317]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "ename": "HSBC Champions",
                "efdate": "04.11.2015",
                "etdate": "08.11.2015",
                "esportcat": "Golf",
                "elocnam": "Sheshan International Golf Club",
                "elocstree": "288 Linyin New Rd",
                "ecity": "Shanghai",
                "eloczip": null,
                "elocland": "China",
                "eclubnam": "Sheshan International Golf Club",
                "elink": "http:\/\/www.worldgolfchampionships.com\/hsbc-champions.html",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [121.22203, 31.104027]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "ename": "Cadillac Championship",
                "efdate": "02.03.2016",
                "etdate": "06.03.2016",
                "esportcat": "Golf",
                "elocnam": "Trump National Doral Miami",
                "elocstree": "4400 N.W. 87th Avenue",
                "ecity": "Miami",
                "eloczip": "FL 33178",
                "elocland": "USA",
                "eclubnam": "Trump National Doral Golf Club",
                "elink": "http:\/\/www.worldgolfchampionships.com\/cadillac-championship.html",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-80.3395621, 25.814003]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "ename": "Dell Match Play",
                "efdate": "23.03.2016",
                "etdate": "27.03.2016",
                "esportcat": "Golf",
                "elocnam": "Austin Country Club",
                "elocstree": "4408 Long Champ Dr",
                "ecity": "Austin",
                "eloczip": "TX 78746",
                "elocland": "USA",
                "eclubnam": "Austin Country Club",
                "elink": "http:\/\/www.worldgolfchampionships.com\/dell-match-play.html",
                "addrtype": "street_address",
                "addrlocat": "ROOFTOP"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-97.7975758, 30.3425085]
            }
        }
    ]
};

/*$(function () {
    function update() {
      map.removeLayer(layer)
      $.getJSON("index.geojson").done(function (data) {
        console.log(data);
        layer.addData(data)
        map.addLayer(layer)
      })
    }
    setInterval(update, 10000),
      update();
  });*/

window.onload = function() {
    $.getJSON("GautrainComputeFolder/dashtreme-master/index.geojson").done(function (data) {
        //console.log(data);
        document.getElementById("geojsoncontent").innerHTML = "<tr><th>busId</th><th>Azimuth</th>";
  
        golfdata.features.forEach(function(entry) {
            document.getElementById("geojsoncontent").innerHTML += "<tr><td>" + entry.properties.busId + "</td><td>" + entry.properties.Azimuth + "</td></tr>";
        });
      })
};