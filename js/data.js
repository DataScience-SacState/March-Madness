var w = 500;
var h = 500;
var pad = 30;
var left_pad = 75;
var x_domain = 1;
var y_domain = 1.3;
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

var x = d3.scale.linear().domain([.4, x_domain]).range([left_pad, w-pad]),
    y = d3.scale.linear().domain([y_domain, .6]).range([pad, h-pad*2]);

// Create Axes

var xAxis = d3.svg.axis().scale(x).orient("bottom"),
    yAxis = d3.svg.axis().scale(y).orient("left");

/* PLOT DATA POINTS  */

var team1OffPlot;
var team1DefPlot;
var team1OffRegLine;
var team1DefRegLine;
var team2OffRegLine;
var team2DefRegLine;

var xAxisBar;
var yAxisBar;

function drawAxis() {
	yAxisBar = svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(0, " + (h - pad) + ")")
		.call(xAxis);
	
	xAxisBar = svg.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(" + (left_pad - pad) + ", 0)")
		.call(yAxis);
}
drawAxis();

function clearAxis() {
	xAxisBar.remove();
	yAxisBar.remove();
}

function clearPlot() {
	//svg.selectAll("*").remove();
	
	team1OffPlot.remove();
	team1DefPlot.remove();
	team1OffRegLine.remove();
	team1DefRegLine.remove();
	
}
function clearRegLines() {
	//svg.selectAll("*").remove();
	try {
	team1OffRegLine.remove();
	team1DefRegLine.remove();
	team2OffRegLine.remove();
	team2DefRegLine.remove();
	} catch (e) {}
}
//clearPlot();

function drawProjection(x1, y1, x2, y2) {
	team1DefRegLine = svg.append("line")
						.attr("x1", x(x1))
						.attr("y1", y(0))
						.attr("x2", x(x1))
						.attr("y2", y(y1))
						.attr("stroke", "blue")
						.attr("stroke-width", 1);
	team1OffRegLine = svg.append("line")
						.attr("x1", x(0))
						.attr("y1", y(y1))
						.attr("x2", x(x1))
						.attr("y2", y(y1))
						.attr("stroke", "blue")
						.attr("stroke-width", 1);

	team2DefRegLine = svg.append("line")
						.attr("x1", x(x2))
						.attr("y1", y(0))
						.attr("x2", x(x2))
						.attr("y2", y(y2))
						.attr("stroke", "green")
						.attr("stroke-width", 1);
	team2OffRegLine = svg.append("line")
						.attr("x1", x(0))
						.attr("y1", y(y2))
						.attr("x2", x(x2))
						.attr("y2", y(y2))
						.attr("stroke", "green")
						.attr("stroke-width", 1);
	
}

function createTeamVisual(data) {
	/*
	[
		{
			x:1, y:2
		},
		{
			x:3, y:6
		}
	]
	*/
	
	//for (team in data) {
		teamPlot = svg.selectAll("circles.off")
						.data(data)
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
	//}
}

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

//createScatterPlot(dummyData);




