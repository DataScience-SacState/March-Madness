import pandas as pd
import sqlite3 as sqlite
import sklearn as sk

conn = sqlite.connect('data/database.sqlite')

''' 

quereies

'''

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
avgWinScoreDFConverted = avgWinScoreDF.rename(columns={'Wteam':'Team'})
avgLossScoreDFConverted = avgLossScoreDF.rename(columns={'Lteam':'Team'})
#merge
mergedWinLossScore = avgWinScoreDFConverted.merge(avgLossScoreDFConverted,on="Team")
print(mergedWinLossScore)

'''Offensive stats'''
#field goals
#win
avgWinFGP = "SELECT Wteam,AVG((CAST(Wfgm AS FLOAT))/(CAST (Wfga AS FLOAT))) AS  Wfgp FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Wteam ORDER BY Wteam ASC;"
avgLossFGP = "SELECT Lteam,AVG((CAST(Lfgm AS FLOAT))/(CAST (Lfga AS FLOAT))) AS Lfgp FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Lteam ORDER BY Lteam ASC;"

#loss
avgWinFGPDF = pd.read_sql_query(avgWinFGP,conn)
avgLossFGPDF = pd.read_sql_query(avgLossFGP,conn)

#rename
avgWinFGPDFConverted = avgWinFGPDF.rename(columns={'Wteam':'Team'})
avgLossFGPDFConverted = avgLossFGPDF.rename(columns={'Lteam':'Team'})
#merge
mergeWinLossFGP = avgWinFGPDFConverted.merge(avgLossFGPDFConverted, on="Team")

#3 pointer
#win
avgWin3P = "SELECT Wteam,AVG((CAST(Wfgm3 AS FLOAT))/(CAST (Wfga3 AS FLOAT))) AS  Wfgp3 FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Wteam ORDER BY Wteam ASC;"
avgLoss3P = "SELECT Lteam,AVG((CAST(Lfgm3 AS FLOAT))/(CAST (Lfga3 AS FLOAT))) AS Lfgp3 FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Lteam ORDER BY Lteam ASC;"

#dataframe
avgWin3PDF = pd.read_sql_query(avgWin3P,conn)
avgLoss3PDF = pd.read_sql_query(avgLoss3P,conn)

#rename
avgWin3PDFConverted = avgWin3PDF.rename(columns={'Wteam':'Team'})
avgLoss3PDFConverted = avgLoss3PDF.rename(columns={'Lteam':'Team'})

#merge
mergeWinLoss3P = avgWin3PDFConverted.merge(avgLoss3PDFConverted, on="Team")
print(mergeWinLoss3P)

#freethrow
#sql strings
avgWinFTP = "SELECT Wteam,AVG((CAST(Wftm AS FLOAT))/(CAST (Wfta AS FLOAT))) AS  Wft FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Wteam ORDER BY Wteam ASC;"
avgLossFTP = "SELECT Lteam,AVG((CAST(Lftm AS FLOAT))/(CAST (Lfta AS FLOAT))) AS  Lft FROM RegularSeasonDetailedResults WHERE Season >= 2014 GROUP BY Lteam ORDER BY Lteam ASC;"

#dataframe
avgWinFTPDF = pd.read_sql_query(avgWinFTP,conn)
avgLossFTPDF = pd.read_sql_query(avgLossFTP,conn)

#rename
avgWinFTPDFConverted = avgWinFTPDF.rename(columns={'Wteam':'Team'})
avgLossFTPDFConverted = avgLossFTPDF.rename(columns={'Lteam':'Team'})

#merge
mergeWinLossFTP = avgWinFTPDFConverted.merge(avgLossFTPDFConverted, on="Team")
#print(mergeWinLossFTP)




#print(avgWinFTPDF)



