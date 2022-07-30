import myJson from './data.json' assert {type: 'json'};

console.log(myJson.features);
console.log(myJson.features.busId);
console.log(myJson.features.TimeStamp);

window.onload = function() {
        
    document.getElementById("jsoncontent").innerHTML = "<tr><th>Bus ID</th><th>Bus GPS Last Updated Date</th><th>Bus GPS Last Updated Time</th><th>Dashboard Last Updated Time</th><th>API Call Response Time</th><th>Bus Latitude</th><th>Bus Longitude</th>";
                
    myJson.features.forEach(function(entry) {
        document.getElementById("jsoncontent").innerHTML += "<tr><td>" + entry.properties.busId + "</td><td>" + entry.properties.GPSLastupdatedDate + "</td><td>" + entry.properties.GPSLastupdatedTime + "</td><td>" + entry.properties.Timestamp + "</td><td>" + entry.properties.API_Response_Time + "</td><td>" + entry.properties.latitude + "</td><td>" + entry.properties.longitude + "</td></tr>";
    });
  };