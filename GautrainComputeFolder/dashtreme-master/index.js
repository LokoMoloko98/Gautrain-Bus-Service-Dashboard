$(document).ready(function () {
	var ctx = document.getElementById("myChart").getContext("2d");

	var data = {
		labels: ["January", "February", "March", "April", "May", "June", "July"],
		datasets: [{
			backgroundColor: "rgba(255, 255, 255, 1.0)",
			borderColor: "rgba(255, 255, 255, 1.0)",
			pointRadius: "0",
			borderWidth: 1,
			data: [65, 59, 80, 81, 56, 55, 40]
		}]
	};

	var options = {
		animation: true,
		//Boolean - If we want to override with a hard coded scale
		scaleOverride: false,
		//** Required if scaleOverride is true **
		//Number - The number of steps in a hard coded scale
		scaleSteps: 10,
		//Number - The value jump in the hard coded scale
		scaleStepWidth: 10,
		//Number - The scale starting value
		scaleStartValue: 0,
		legend: {
			display: false,
			labels: {
			  fontColor: '#ddd',  
			  boxWidth:40
			}
		  },
		
		  scales: {
			xAxes: [{
			  ticks: {
				  beginAtZero:true,
				  fontColor: '#ddd'
			  },
			  gridLines: {
				display: true ,
				color: "rgba(221, 221, 221, 0.08)"
			  },
			}],
			 yAxes: [{
			  ticks: {
				  beginAtZero:true,
				  fontColor: '#ddd'
			  },
			  gridLines: {
				display: true ,
				color: "rgba(221, 221, 221, 0.08)"
			  },
			}]
		   }
		
	};

	var myLineChart = new Chart(ctx, {
		type: "line",
		data: data,
	});

	setInterval(function () {
		setData(data.datasets[0].data);
		setLabels(data.labels);

		var myLineChart = new Chart(ctx, { type: "line", data: data, });
	}, 4000);

	function setLabels(labels) {
		var nextMonthIndex = months.indexOf(labels[labels.length - 1]) + 1;
		var nextMonthName = months[nextMonthIndex] != undefined ? months[nextMonthIndex] : "January";
		labels.push(nextMonthName);
		labels.shift();
	}

	function setData(data) {
		data.push(Math.floor(Math.random() * 100) + 1);
		data.shift();
	}

	function convertMonthNameToNumber(monthName) {
		var myDate = new Date(monthName + " 1, 2016");
		var monthDigit = myDate.getMonth();
		return isNaN(monthDigit) ? 0 : (monthDigit + 1);
	}

	var months = ["January", "February", "March", "April", "May", "June",
		"July", "August", "September", "October", "November", "December"
	];

});