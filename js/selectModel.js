var teamNames;
var teamData;

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "data/Teams.csv",
        dataType: "text",
        success: function(data) {teamNames(data);}
    });
    $.ajax({
        type: "GET",
        url: "data/some.json",
        dataType: "text",
        success: function(data) {teamData = JSON.parse(data); plotAll();}
    });
     
    $("#submitButton").on("click", function(e) { 
         e.preventDefault();
         updatePlot();
    })
    
  /*  teamData = $.getJSON( "data/some.json" );
    console.log(teamData);
    plotAll(); */
});

function teamNames(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];
    
    teamNames = [];
    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j=0; j<headers.length; j++) {
                tarr.push(headers[j]+":"+data[j]);
            }
            
            teamNames.push({"id":data[0], "name":data[1]});
            
            lines.push(tarr);
        }
    }
    
    populateTeams(teamNames);
}

function populateTeams(teamNames) {
    // alert(teamNames[0].name);
    for (var i = 0; i < teamNames.length; i++)
        $(".teamInput select").append("<option value=\"" + teamNames[i].id + "\" >" + teamNames[i].name + "</option>");
}

function plotAll() {
    var data = [];
    
    console.log(teamData);
    for (var i = 0; i < 351; i++) {
    	data.push({ "x":teamData["defSkill"][i], "y":teamData["offSkill"][i] });
    }

    createTeamVisual(data);
}
//clearPlot();
//plotAll();

function updatePlot() {
    clearRegLines();

    var a = $("#selectA");
    var aId = a[0].options[a[0].selectedIndex].value;
    var aRow;
    var b = $("#selectB");
    var bId = b[0].options[b[0].selectedIndex].value;
    var bRow;
    
    console.log(teamData);
    for (var i = 0; i < 351; i++) {
    	teamId = teamData["id"][i];
    	if (teamId == aId)
    		aRow = i;
    	if (teamId == bId)
    		bRow = i;
    }
    
    var x1 = teamData["defSkill"][aRow];
    var y1 = teamData["offSkill"][aRow];
    var x2 = teamData["defSkill"][bRow];
    var y2 = teamData["offSkill"][bRow];
    
    drawProjection(x1, y1, x2, y2);
    
    
    /*
    teamData = {
    "1101":{
    	"offensiveSkill":5,
    	"defensiveSkill":5,
    	"games":[
    		{
    			"oppOff":6,
    			"oppDef":7,
    			"ourScore":20,
    			"theirScore":60
    		}	
    	],
    	"theirLine":{"interc":0,"slope":2},
    	"ourLine":{"interc":0,"slope":1}
    }}//*/

    /*
    var offData = [];
    for (game in teamData[aId].games) {
        offData.push({ "x":teamData[aId].oppOff, "y":teamData[aId].theirScore });
    }

    var defData = [];
    for (game in teamData[aId]) {
        defData.push({ "x":teamData[aId].oppDef, "y":teamData[aId].ourScore });
    }

    var data = {
        team1: {
            "offData": offData,
            "defData": defData,
            "offSlope": teamData[aId].ourLine.slope,
            "offInt": teamData[aId].ourLine.interc,
            "defSlope": teamData[aId].theirLine.slope,
            "defInt": teamData[aId].theirLine.interc
        },
        team2:{
            offScore: 10,
            defScore: 20
        }
    }
    
    console.log(data);
    
    createScatterPlot(data);

    console.log("Plotting Projections");
    var projX1 = data.team2.offScore;
    var projY1 = (data.team1.offSlope * projX1) + data.team1.offInt;
    var projX2 = data.team2.defScore;
    var projY2 = (data.team1.defSlope * projX2) + data.team1.defInt;
    
    console.log(projY1 + " : " + projY2);
    
    drawProjection(projX1, projY1, projX2, projY2);
    
    /*
    */      
}
