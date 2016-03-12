import pandas as pd
import sqlite3 as sqlite
import matplotlib as mp
import numpy as np
import sklearn as sk

conn = sqlite.connect('data/database.sqlite')

#get the offensive data
def getOffData(teamId):
    teamId = str(teamId)
    #print(teamId)
    winningScript = "SELECT Wteam AS team, Wscore AS score, (CAST (Wfgm AS FLOAT))/(CAST(Wfga AS FLOAT)) as fgp,(CAST (Wfgm3 AS FLOAT))/(CAST(Wfga3 AS FLOAT)) as tpp, (CAST (Wftm AS FLOAT))/(CAST(Wfta AS FLOAT)) as ftp, Wor as ofr FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    #winningDf = conn.execute(winningScript, teamId)
    winningDf = pd.read_sql_query(winningScript, conn, params = (teamId, ))
    losingScript ="SELECT Lteam AS team, Lscore AS score, (CAST (Lfgm AS FLOAT))/(CAST(Lfga AS FLOAT)) as fgp,(CAST (Lfgm3 AS FLOAT))/(CAST(Lfga3 AS FLOAT)) as tpp, (CAST (Lftm AS FLOAT))/(CAST(Lfta AS FLOAT)) as ftp, Lor as ofr FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam =?)"
    losingDf = pd.read_sql_query(losingScript, conn, params = (teamId, ))
    
    teamDf = winningDf.append(losingDf)
    #print(teamDf)
    
    teamDf.apply(genOffScore,axis=1)

#process the data
def genOffScore(row):
    #score = fgp * .65 + tpp * .2 + ftp *.1 + ofr*.05
    fgp = (row[2]) * .65
    tpp = (row[3]) * .20
    ftp = (row[4]) * .1
    ofr = (row[5]) * .05
    score = fgp + tpp + ftp + ofr
    print(score)



getOffData(1181)
#same script, except when they lose
