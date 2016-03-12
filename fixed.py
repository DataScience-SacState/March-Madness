import pandas as pd
import sqlite3 as sqlite
import matplotlib as mp
import numpy as np
import sklearn as sk
import scipy.stats as st

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
    
    oteamDf.apply(genOffScore,axis=1)
    
    dwinningScript = "SELECT Wteam as team, Lscore as oppscore, Lto as oppto, Wdr as dr, Wstl as stl, Wblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    dwinningDf = pd.read_sql_query(dwinningScript, conn, params = (teamId, ))
    
    dlosingScript = "SELECT Lteam as team, Wscore as oppscore, Wto as oppto, Ldr as dr, Lstl as stl, Lblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam = ?)"
    dlosingDf = pd.read_sql_query(dlosingScript, conn, params = (teamId, ))
    
    dteamDf = dwinningDf.append(dlosingDf)
    a = dteamDf.apply(genDefScore,axis=1)
    print(a)

#process the data
def genOffScore(row):
    #score = fgp * .65 + tpp * .2 + ftp *.1 + ofr*.05
    fgp = (row[2]) * .65
    tpp = (row[3]) * .20
    ftp = (row[4]) * .1
    ofr = (row[5]) * .05
    oScore = fgp + tpp + ftp + ofr
    return oScore

def getDefData(teamId):
    teamId = str(teamId)
    
    winningScript = "SELECT Wteam as team, Lscore as oppscore, Lto as oppto, Wdr as dr, Wstl as stl, Wblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Wteam = ?)"
    winningDf = pd.read_sql_query(winningScript, conn, params = (teamId, ))
    
    losingScript = "SELECT Lteam as team, Wscore as oppscore, Wto as oppto, Ldr as dr, Lstl as stl, Lblk as blk FROM RegularSeasonDetailedResults WHERE Season >= 2014 AND (Lteam = ?)"
    losingDf = pd.read_sql_query(losingScript, conn, params = (teamId, ))
    
    teamDf = winningDf.append(losingDf)
    teamDf.apply(genDefScore,axis=1)

def genDefScore(row):
    #print(row)
    MEAN = 68.56
    GIVEN_SD = 9.83
    MAX_TO = 25
    MAX_DR = 48
    MAX_ST = 15
    MAX_BLK = 13

    team = row[0]
    ppg  = (int(row[1]) - MEAN)/GIVEN_SD
    xppg = 1-(st.norm.cdf(ppg))*.6
    
    to  = (row[2])/MAX_TO * .20
    dr  = (row[3])/MAX_DR * .1
    stl  = (row[4])/MAX_ST * .05
    blk = (row[5])/MAX_BLK*.05 
    
    dScore = xppg + to + dr + stl + blk
    return dScore
getData(1101)


