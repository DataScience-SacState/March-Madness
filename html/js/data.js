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
		defInt: 40,

	},
	team2: {
		offScore: 1, 
		defScore: 1
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
var team1Off = svg.selectAll("#plot")
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

var team1Def = svg.selectAll("#plot")
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

// Team 2 Offensive Data
// var team2Off = svg.selectAll("#plot")
// 	.data(dummyData.team2.offData)
// 	.enter()
// 	.append("circle")
// 	.attr("fill", "purple")
// 	.attr("cx", function(d) { // Change for JSON
// 		return x(d.x)
// 	})
// 	.attr("cy", function(d) {
// 		return y(d.y)
// 	})
// 	.attr("r", dotR);

// // Team 2 Defensive Data

// var team2Def = svg.selectAll("#plot")
// 	.data(dummyData.team2.defData)
// 	.enter()
// 	.append("circle")
// 	.attr("fill", "orange")
// 	.attr("cx", function(d) { // Change for JSON
// 		return x(d.x)
// 	})
// 	.attr("cy", function(d) {
// 		return y(d.y)	
// 	})
// 	.attr("r", dotR);


// Team 1 Offensive Regression Line

var x_int = function(m,b) {	return -b/m };

var team1 = dummyData.team1;

svg.append("line")
	.attr("x1", x(0))
	.attr("y1", y(team1.offInt))
	.attr("x2", x(40))
	.attr("y2", y(40*team1.offSlope + team1.offInt))
	.attr("stroke", "green")
	.attr("stroke-width", 1);


