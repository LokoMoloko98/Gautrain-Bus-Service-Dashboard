import latency from './latency.json' assert {type: 'json'};

console.log(latency.features);
var time = Object.values(latency.features)
console.log(time[0].properties.API_Response_Time)

$(function () {
	"use strict";

	// chart 1

	// var ctx = document.getElementById('chart1').getContext('2d');

	// var myChart = new Chart(ctx, {
	// 	type: 'line',
	// 	data: {
	// 		labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
	// 		datasets: [{
	// 			label: 'New Visitor',
	// 			data: [3, 3, 8, 5, 7, 4, 6, 4, 6, 3],
	// 			backgroundColor: '#fff',
	// 			borderColor: "transparent",
	// 			pointRadius: "0",
	// 			borderWidth: 3
	// 		}, {
	// 			label: 'Old Visitor',
	// 			data: [7, 5, 14, 7, 12, 6, 10, 6, 11, 5],
	// 			backgroundColor: "rgba(255, 255, 255, 0.25)",
	// 			borderColor: "transparent",
	// 			pointRadius: "0",
	// 			borderWidth: 1
	// 		}]
	// 	},
	// 	options: {
	// 		maintainAspectRatio: false,
	// 		legend: {
	// 			display: false,
	// 			labels: {
	// 				fontColor: '#ddd',
	// 				boxWidth: 40
	// 			}
	// 		},
	// 		tooltips: {
	// 			displayColors: false
	// 		},
	// 		scales: {
	// 			xAxes: [{
	// 				ticks: {
	// 					beginAtZero: true,
	// 					fontColor: '#ddd'
	// 				},
	// 				gridLines: {
	// 					display: true,
	// 					color: "rgba(221, 221, 221, 0.08)"
	// 				},
	// 			}],
	// 			yAxes: [{
	// 				ticks: {
	// 					beginAtZero: true,
	// 					fontColor: '#ddd'
	// 				},
	// 				gridLines: {
	// 					display: true,
	// 					color: "rgba(221, 221, 221, 0.08)"
	// 				},
	// 			}]
	// 		}

	// 	}
	// });


	// chart 2

	// var ctx = document.getElementById("chart2").getContext('2d');
	// var myChart = new Chart(ctx, {
	// 	type: 'doughnut',
	// 	data: {
	// 		labels: ["Direct", "Affiliate", "E-mail", "Other"],
	// 		datasets: [{
	// 			backgroundColor: [
	// 				"#ffffff",
	// 				"rgba(255, 255, 255, 0.70)",
	// 				"rgba(255, 255, 255, 0.50)",
	// 				"rgba(255, 255, 255, 0.20)"
	// 			],
	// 			data: [5856, 2602, 1802, 1105],
	// 			borderWidth: [0, 0, 0, 0]
	// 		}]
	// 	},
	// 	options: {
	// 		maintainAspectRatio: false,
	// 		legend: {
	// 			position: "bottom",
	// 			display: false,
	// 			labels: {
	// 				fontColor: '#ddd',
	// 				boxWidth: 15
	// 			}
	// 		}
	// 		,
	// 		tooltips: {
	// 			displayColors: false
	// 		}
	// 	}
	// });

	// chart 3 (GAUGE)

	// var randomValue = function (data) {
	// 	return Math.round(Math.max.apply(null, data) * Math.random());
	// };

	// /*var API_latency_value = latency.features.map(function(e) {
	// 	return e.properties.API_Response_Time[0];
	// 	Object.values(
	// });*/

	

	// var data = [2.5, 5.0, 7.5, 10];
	// //var value = randomValue(data);
	// var value = time[0].properties.API_Response_Time;
	
	// var config = {
	// 	type: 'gauge',
	// 	data: {
	// 		labels: ['Low Latency Range', 'Acceptable Latency Range', 'High Latency Range', 'Very High Latency Range'],
	// 		datasets: [{
	// 			data: data,
	// 			value: value,
	// 			backgroundColor: ['green', 'yellow', 'orange', 'red'],
	// 			borderWidth: 2
	// 		}]
	// 	},
	// 	options: {
	// 		responsive: true,
	// 		title: {
	// 			display: false,
	// 			text: 'Gauge chart with datalabels plugin displaying labels'
	// 		},
	// 		layout: {
	// 			padding: {
	// 				bottom: 30
	// 			}
	// 		},
	// 		needle: {
	// 			// Needle circle radius as the percentage of the chart area width
	// 			radiusPercentage: 2,
	// 			// Needle width as the percentage of the chart area width
	// 			widthPercentage: 3.2,
	// 			// Needle length as the percentage of the interval between inner radius (0%) and outer radius (100%) of the arc
	// 			lengthPercentage: 80,
	// 			// The color of the needle
	// 			color: 'rgba(0, 0, 0, 1)'
	// 		},
	// 		valueLabel: {
	// 			display: true,
	// 		},
	// 		plugins: {
	// 			datalabels: {
	// 				display: true,
	// 				formatter: function (value, context) {
	// 					return context.chart.data.labels[context.dataIndex];
	// 				},
	// 				//color: function (context) {
	// 				//  return context.dataset.backgroundColor;
	// 				//},
	// 				color: 'rgba(0, 0, 0, 1.0)',
	// 				//color: 'rgba(255, 255, 255, 1.0)',
	// 				backgroundColor: null,
	// 				font: {
	// 					size: 10,
	// 					weight: 'bold'
	// 				}
	// 			}
	// 		}
	// 	}
	// };
	// window.onload = function() {
	// var ctx = document.getElementById('gaugechart').getContext('2d');
	// var myGauge = new Chart(ctx, config);
	
	
	// var update  = function () {
	// 			   config.data.datasets.forEach(function(dataset) {
	// 				var API_latency_value = time[0].properties.API_Response_Time;
	// 				dataset.value = API_latency_value
	// 				//dataset.value = randomValue(dataset.data);
	// 				});
	// 				myGauge.update();
	// 			}
	// 	setInterval(update, 5000),
	// 	update();
	// };
                
    // time.forEach(function(entry) {
    //     document.getElementById("jsoncontent").innerHTML += "<tr><td>" + entry.properties.busId + "</td><td>" + entry.properties.GPSLastupdatedDate + "</td><td>" + entry.properties.GPSLastupdatedTime + "</td><td>" + entry.properties.Timestamp + "</td><td>" + entry.properties.API_Response_Time + "</td><td>" + entry.properties.latitude + "</td><td>" + entry.properties.longitude + "</td></tr>";
    // });

});