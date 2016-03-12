import pandas as pd
import sqlite3 as sqlite
import matplotlib as mp
import numpy as np
import sklearn as sk
import scipy.stats as st
import json

conn = sqlite.connect('data/database.sqlite')

result = {}

#get the offensive data
def getData(teamId):
    teamId = str(teamId)
    
    owinningScript = "SELECT Wteam AS team, Wscore AS score, (CAST (Wfgm AS FLOAT))/(CAST(Wfga AS FLOAT)) as fgp,(CAST (Wfgm3 AS FLOAT))/(CAST(Wfga3 AS FLOAT)) as tpp, (CAST (Wftm AS FLOAT))/(CAST(Wfta AS FLOAT)) as ftp, Wor as ofr FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    owinningDf = pd.read_sql_query(owinningScript, conn, params = (teamId, ))
    
    olosingScript ="SELECT Lteam AS team, Lscore AS score, (CAST (Lfgm AS FLOAT))/(CAST(Lfga AS FLOAT)) as fgp,(CAST (Lfgm3 AS FLOAT))/(CAST(Lfga3 AS FLOAT)) as tpp, (CAST (Lftm AS FLOAT))/(CAST(Lfta AS FLOAT)) as ftp, Lor as ofr FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam =?)"
    olosingDf = pd.read_sql_query(olosingScript, conn, params = (teamId, ))
    
    oteamDf = owinningDf.append(olosingDf)
    
    o = oteamDf.apply(genOffScore,axis=1)
    
    omean = o.mean(axis=0) 
    #print(omean)

    dwinningScript = "SELECT Wteam as team, Lscore as oppscore, Lto as oppto, Wdr as dr, Wstl as stl, Wblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    dwinningDf = pd.read_sql_query(dwinningScript, conn, params = (teamId, ))
    
    dlosingScript = "SELECT Lteam as team, Wscore as oppscore, Wto as oppto, Ldr as dr, Lstl as stl, Lblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam = ?)"
    dlosingDf = pd.read_sql_query(dlosingScript, conn, params = (teamId, ))
    
    dteamDf = dwinningDf.append(dlosingDf)
    
    d = dteamDf.apply(genDefScore,axis=1)
    dmean = d.mean(axis=0)

    od = pd.concat([o,d],axis=1)
    
    #return(omean,dmean)
    #print(od)
    return(od)

#process the data
def genOffScore(row):
    ppg = row[1]
    fgp = (row[2]) * .65
    tpp = (row[3]) * .20
    ftp = (row[4]) * .1
    ofr = (row[5]) * .05
    oScore = fgp + tpp + ftp + ofr
    #return ppg,oScore
    return oScore

def getDefData(teamId):
    teamId = str(teamId)
    
    winningScript = "SELECT Wteam as team, Lscore as oppscore, Lto as oppto, Wdr as dr, Wstl as stl, Wblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    winningDf = pd.read_sql_query(winningScript, conn, params = (teamId, ))
    
    losingScript = "SELECT Lteam as team, Wscore as oppscore, Wto as oppto, Ldr as dr, Lstl as stl, Lblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam = ?)"
    losingDf = pd.read_sql_query(losingScript, conn, params = (teamId, ))
    
    teamDf = winningDf.append(losingDf)

def genDefScore(row):
    MEAN = 68.56
    GIVEN_SD = 9.83
    MAX_TO = 25
    MAX_DR = 48
    MAX_ST = 15
    MAX_BLK = 13
    team = row[0]
    ppg = row[1]
    sppg  = (int(row[1]) - MEAN)/GIVEN_SD
    xppg = 1-(st.norm.cdf(sppg))*.6
    to  = (row[2])/MAX_TO * .20
    dr  = (row[3])/MAX_DR * .1
    stl  = (row[4])/MAX_ST * .05
    blk = (row[5])/MAX_BLK*.05     
    dScore = xppg + to + dr + stl + blk
    return dScore

def getTeams():
    script = "SELECT DISTINCT(Wteam) FROM RegularSeasonDetailedResults WHERE Season >= 2014;"
    a = pd.read_sql_query(script,conn)
    b = a.iloc[:,0]
    b = b.tolist()
    return b
'''
def generateDF():
    teams = (getTeams())
    teamsdf = pd.DataFrame(columns =('id', 'offSkill', 'defSkill'))
    '''
    for a in teams:
        foo = getData(a)
        adf = pd.DataFrame([[a,foo[0],foo[1]]],columns=('id', 'offSkill', 'defSkill'))
        teamsdf = teamsdf.append(adf)
    #a = teamsdf.reset_index().to_json(orient='id')
    
    print(teamsdf)
    #return a
    #return teamsdf
    '''
    myD = {}
    for a in teams:
        foo = getData(a)
        myD[a] = foo
'''
#teams is the df with all the team ids and the mean
#skills. This for loop probably wont work. but close
#enough

def generateDF():
    teams = (getTeams())
    teamsdf = pd.DataFrame(columns =('id', 'offSkill', 'defSkill'))
    
    for a in teams:
       foo = getData(a)
       adf = pd.DataFrame([[a,foo[0],foo[1]]],columns=('id', 'offSkill', 'defSkill'))
       teamsdf = teamsdf.append(adf)
    
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

a = (generateDF())
'''
with open('data.txt', 'w') as outfile:
    json.dump(a, outfile)
'''
