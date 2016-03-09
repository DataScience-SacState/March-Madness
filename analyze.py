import pandas as pd
import sqlite3 as sqlite
import sklearn as sk

conn = sqlite.connect('data/database.sqlite')

''' quereies'''
#most winning teams in the last two years
mw2yr = "SELECT Wteam, COUNT(*)  AS wcount FROM RegularSeasonCompactResults WHERE Season >= 2014 GROUP BY Wteam ORDER BY wcount DESC;"
mw2yrDF = pd.read_sql_query(mw2yr,conn)

#avg winning score
avgWinScore = "SELECT Wteam, avg(Wscore) FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Wteam"
avgWinScoreDF = pd.read_sql_query(avgWinScore,conn)

#avg losing score
avgLossScore = "SELECT Lteam, avg(Lscore) FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Lteam"
avgLossScoreDF = pd.read_sql_query(avgLossScore,conn)

#joined scores
#rename
avgWinScoreDF = avgWinScoreDF.rename(columns={'Wteam':'Team'})
avgLossScoreDF = avgLossScoreDF.rename(columns={'Lteam':'Team'})
#merge
mergedWinLoss = avgWinScoreDF.merge(avgLossScoreDF,on="Team")

#Fieldgoal percentage

