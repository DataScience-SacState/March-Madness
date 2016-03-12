var w = 500;
var h = 500;
var pad = 20;
var left_pad = 100;

//DATA?!?!?!?!?!

var svg = d3.select("#plot")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

var x = d3.scale.linear().domain([0, 23]).range([left_pad, w-pad]),
    y = d3.scale.linear().domain([6, 0]).range([pad, h-pad*2]);

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

svg.selectAll("#root")
	.data(dataset)
	.enter()
	.append("offSkill")
	.attr("cx", function(d) { // Change for JSON
		return d[0];
	})
	.attr("cy", function(d) {
		return d[1];
	})
	.attr("r", 5);

/*var dummyDate = {

	team1: "thefkinbest",
	team2: "trash",
	team1OffData: {
		{ x: 10, y: 10 },
		{ x: 20, y: 20 },
		{ x: 30, y: 30 }
	},
	team1DefData: {
		{ x: 10, y: 30 },
		{ x: 20, y: 20 },
		{ x: 30, y: 10 }
	},
	team2OffData: {
		{ x: 10, y: 15 },
		{ x: 20, y: 25 },
		{ x: 30, y: 35 }
	},
	team2DefData: {
		{ x: 10, y: 35 },
		{ x: 20, y: 25 },
		{ x: 30, y: 15 }
	},

	team1OffSlope: 1,
	team1OffIntercept: 0, 

	team1DefSlope: -1,
	team1DefIntercept: 40, 

	team2OffSlope: 1.5,
	team2OffIntercept: 5,
	
	team2DefSlope: -1.5,
	team2DefIntercept: 45
	
};*/
