var w = 500;
var h = 500;
var pad = 30;
var left_pad = 75;
var dotR = 4;

//DATA?!?!?!?!?!

var dummyData = {

	team1: {
		name: "thefkinbest",
		offData: [
			{ x: 10, y: 10 },
			{ x: 20, y: 20 },
			{ x: 30, y: 30 }
		],
		defData: [
			{ x: 10, y: 30 },
			{ x: 20, y: 20 },
			{ x: 30, y: 10 }
		],
		offSlope: 1,
		offInt: 0,
		defSlope: -1,
		defInt: 40
	},
	team2: {
		name: "trash",
		offData: [
			{ x: 10, y: 15 },
			{ x: 20, y: 25 },
			{ x: 30, y: 35 }
		],
		defData: [
			{ x: 10, y: 35 },
			{ x: 20, y: 25 },
			{ x: 30, y: 15 }
		],
		offSlope: 1.5,
		offInt: 5,
		defSlope: -1.5,
		defInt: 45
	}
	
};

var svg = d3.select("#plot")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

var x = d3.scale.linear().domain([0, 40]).range([left_pad, w-pad]),
    y = d3.scale.linear().domain([40, 0]).range([pad, h-pad*2]);

var xAxis = d3.svg.axis().scale(x).orient("bottom"),
    yAxis = d3.svg.axis().scale(y).orient("left");

svg.append("g")
	.attr("class", "axis")
	.attr("transform", "translate(0, " + (h - pad) + ")")
	.call(xAxis);

svg.append("g")
	.attr("class", "axis")
	.attr("transform", "translate(" + (left_pad - pad) + ", 0)")
	.call(yAxis);

/* PLOT DATA POINTS  */

// Team 1 Offensive Data
svg.selectAll("#plot")
	.data(dummyData.team1.offData)
	.enter()
	.append("circle")
	.attr("fill", "blue")
	.attr("cx", function(d) { // Change for JSON
		return x(d.x)
	})
	.attr("cy", function(d) {
		return y(d.y)
	})
	.attr("r", dotR);

// Team 1 Defensive Data

svg.selectAll("#plot")
	.data(dummyData.team1.defData)
	.enter()
	.append("circle")
	.attr("fill", "green")
	.attr("cx", function(d) { // Change for JSON
		return x(d.x)
	})
	.attr("cy", function(d) {
		return y(d.y)	
	})
	.attr("r", dotR);

// Team 1 Offensive Regression Line
var team1 = dummyData.team1
console.log(team1);
var x_int = function(m,b) {
	if (m == 0 || b == 0) {
		return 0;
	}
	return -b/m;
};

svg.selectAll("#plot")
	.append("line")
	.attr("x1", x(0))
	.attr("y1", y(team1.offInt));
	.attr("x2", x(x_int(team1.offInt, team1.offSlope)))
	.attr("y2", y(0))
	.attr("stroke", "green")
	.attr("stroke-width", 1);


