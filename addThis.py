
#teams is the df with all the team ids and the mean
#skills. This for loop probably wont work. but close
#enough
for row in teams:
	rowId = row[0]
	rowOff = row[1]
	rowDef = row[2]
	print "{"
	print rowId+":{"
	print rowOff
	print rowDef
	print "games : ["
	#need to make these df's for regressionline
	theirRegress = pd.DataFrame(columns=("theirOff","theirScore"))
	ourRegress = pd.DataFrame(columns=("theirDef","ourScore"))
	#figure this for loop out
	for game in RegularSeasonDetailedResults[where WId == rowId]:
		#get the row in teams that has the other teams id
		oppOff = teams[game.LId][1]
		oppDef = teams[game.LId][2]
		ourScore = game.Wscore
		theirScore = game.Lscore
		#making these to append to end of the others
		tempTheir = pd.DataFrame([[oppOff,theirScore]],columns =("theirOff","theirScore"))
		tempOur = pd.DataFrame([[oppDef,ourScore]],columns =("theirOff","theirScore"))
		#appending
		theirRegress.append(tempTheir)
		ourRegress.append(tempOur)

		#back to print json. this might not be how to make an array in jsons
		#but fuck you
		print '{'
		print "oppOff : " + oppOff
		print "oppDef : " + oppDef
		print "ourScore: " + ourScore
		print "theirScore" + theirScore
		print "}"
	#do this same thing again but for when our id lost
	for game in RegularSeasonDetailedResults[where LId == rowId]:
		#get the row in teams that has the other teams id
		oppOff = teams[game.WId][1]
		oppDef = teams[game.WId][2]
		ourScore = game.Wscore
		theirScore = game.Lscore
		#making these to append to end of the others
		tempTheir = pd.DataFrame([[oppOff,theirScore]],columns =("theirOff","theirScore"))
		tempOur = pd.DataFrame([[oppDef,ourScore]],columns =("theirOff","theirScore"))
		#appending
		theirRegress.append(tempTheir)
		ourRegress.append(tempOur)

		#back to print json. this might not be how to make an array in jsons
		#but fuck you
		print '{'
		print "oppOff : " + oppOff
		print "oppDef : " + oppDef
		print "ourScore: " + ourScore
		print "theirScore" + theirScore
		print "}"
	print "]"

	#theres a function in some scipy i guess.
	#find it. im going to bed.
	#it find the regression line coeffecients
	#given two vars.
	#so call that function twice.
	#once with the columns of ourRegress,
	#another with columns of theirRegress

	print "theirLine : {intercept:theirLine.intercept, slope: theirLine.slope}"
	print "ourLine : {intercept:ourLine.intercept, slope: ourLine.slope}"
	print "}"

	#that should be detailed enough
	#pass this things output to a file
	#and give it to matt
	#and also fix offensiveScore somehow

'''
{
	"1101":{
		"offensiveSkill" : "5"
		"defensiveSkill" : "5"
			"games" : {
				{
					"oppOff" : "6"
					"oppDef" : "7"
					"ourScore" : "56"
					"theirScore" : "70"
				}
				{
					"oppOff" : "6"
					"oppDef" : "7"
					"ourScore" : "56"
					"theirScore" : "70"
				}
				{
					"oppOff" : "6"
					"oppDef" : "7"
					"ourScore" : "56"
					"theirScore" : "70"
				}
			}
		"theirLine" : {"interc":1,"slope":2}
		"ourLine" :  {"interc":1,"slope":2}
	}
}
'''	


