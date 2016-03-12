var w = 500;
var h = 500;
var pad = 30;
var left_pad = 75;
var x_domain = 40;
var y_domain = 40;
var dot_rad = 4;

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

var entries = d3.entries(dummyData)
console.log(entries);

// Create SVG

var svg = d3.select("#plot")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

// Create Scale

var x = d3.scale.linear().domain([0, x_domain]).range([left_pad, w-pad]),
    y = d3.scale.linear().domain([y_domain, 0]).range([pad, h-pad*2]);

// Create Axes

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

var team1OffPlot;
var team1DefPlot;
var team1OffRegLine;
var team1DefRegLine;

var createScatterPlot = function(data) {
	var team1 = data.team1;
	var team2 = data.team2;

	team1OffPlot = svg.selectAll("circles.off")
						.data(team1.offData)
						.enter()
						.append("circle")
						.attr("class", "off")
						.attr("fill", "blue")
						.attr("cx", function(d) { // Change for JSON
							return x(d.x)
						})
						.attr("cy", function(d) {
							return y(d.y)
						})
						.attr("r", dot_rad);

	team1DefPlot = svg.selectAll("circles.def")
						.data(team1.defData)
						.enter()
						.append("circle")
						.attr("class", "def")
						.attr("fill", "green")
						.attr("cx", function(d) { // Change for JSON
							return x(d.x)
						})
						.attr("cy", function(d) {
							return y(d.y)	
						})
						.attr("r", dot_rad);

	team1OffRegLine = svg.append("line")
						.attr("x1", x(0))
						.attr("y1", y(team1.offInt))
						.attr("x2", x(40))
						.attr("y2", y(40*team1.offSlope + team1.offInt))
						.attr("stroke", "blue")
						.attr("stroke-width", 1);

	team1DefRegLine = svg.append("line")
						.attr("x1", x(0))
						.attr("y1", y(team1.defInt))
						.attr("x2", x(40))
						.attr("y2", y(40*team1.defSlope + team1.defInt))
						.attr("stroke", "green")
						.attr("stroke-width", 1);
};

createScatterPlot(dummyData);




