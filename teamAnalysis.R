#eat the data from the csv's
RegularSeasonCompactResults <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/RegularSeasonCompactResults.csv")
RegularSeasonDetailedResults <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/RegularSeasonDetailedResults.csv")
SampleSubmission <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/SampleSubmission.csv")
Seasons <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/Seasons.csv")
Teams <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/Teams.csv")
TourneyCompactResults <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/TourneyCompactResults.csv")
TourneyDetailedResults <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/TourneyDetailedResults.csv")
TourneySeeds <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/TourneySeeds.csv")
TourneySlots <- read.csv("~/Documents/dataScienceClub/march-machine-learning-mania-2016-v1/MarchMadness/data/TourneySlots.csv")

#Successfully eaten all the csv's. f databases, download more ram

#cut out previous years
RegularSeasonCompactResults <- RegularSeasonCompactResults[which(RegularSeasonCompactResults$Season >= 2010),]


#make a function to find the mean score for a team
meanScored <- function(teamID){
  mean(c(RegularSeasonCompactResults$Wscore[which(RegularSeasonCompactResults$Wteam==as.integer(teamID))]
       , RegularSeasonCompactResults$Lscore[which(RegularSeasonCompactResults$Lteam==as.integer(teamID))]))
}
# call meanScored for every team and make the result a new column in Teams
RegularSeasonCompactResults$WmeanScored  <- sapply(RegularSeasonCompactResults$Wteam,meanScored)
RegularSeasonCompactResults$LmeanScored  <- sapply(RegularSeasonCompactResults$Lteam,meanScored)

#make a function to find the mean points scored on for a team
meanScoredOn <- function(teamID){
  mean(c(RegularSeasonCompactResults$Wscore[which(RegularSeasonCompactResults$Lteam==as.integer(teamID))]
         , RegularSeasonCompactResults$Lscore[which(RegularSeasonCompactResults$Wteam==as.integer(teamID))]))
}
# call meanScoredOn for every team make the result a new column in RegularSeasonCompactResults
RegularSeasonCompactResults$WmeanScoredOn  <- sapply(RegularSeasonCompactResults$Wteam,meanScoredOn)
RegularSeasonCompactResults$LmeanScoredOn  <- sapply(RegularSeasonCompactResults$Lteam,meanScoredOn)

#make a function to find the offensiveSkill of a team
#honestly dont know if i can even explain this process
findOffensiveSkill <- function(teamID){
  mean(c(RegularSeasonCompactResults$Wscore[which(RegularSeasonCompactResults$Wteam==teamID)]
       - RegularSeasonCompactResults$LmeanScoredOn[which(RegularSeasonCompactResults$Wteam==teamID)]
       , RegularSeasonCompactResults$Lscore[which(RegularSeasonCompactResults$Lteam==teamID)]
       - RegularSeasonCompactResults$WmeanScoredOn[which(RegularSeasonCompactResults$Lteam==teamID)]))
}

findDefensiveSkill <- function(teamID){
  mean(c(-RegularSeasonCompactResults$WmeanScored[which(RegularSeasonCompactResults$Lteam==teamID)]
       + RegularSeasonCompactResults$Wscore[which(RegularSeasonCompactResults$Lteam==teamID)]
       , -RegularSeasonCompactResults$LmeanScored[which(RegularSeasonCompactResults$Wteam==teamID)]
       + RegularSeasonCompactResults$Lscore[which(RegularSeasonCompactResults$Wteam==teamID)]))
}

#add offensiveSkill and defensiveSkill columns to RegularSeasonCompactResults
RegularSeasonCompactResults$WoffensiveSkill <- sapply(RegularSeasonCompactResults$Wteam,findOffensiveSkill)
RegularSeasonCompactResults$WdefensiveSkill <- sapply(RegularSeasonCompactResults$Wteam,findDefensiveSkill)
RegularSeasonCompactResults$LoffensiveSkill <- sapply(RegularSeasonCompactResults$Lteam,findOffensiveSkill)
RegularSeasonCompactResults$LdefensiveSkill <- sapply(RegularSeasonCompactResults$Lteam,findDefensiveSkill)



