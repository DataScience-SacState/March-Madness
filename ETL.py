#an ETL job to extract years >= 2014 for all databases in database.sqlite
import sqlite3 as sqlite
import pandas as pd


'''strings'''
#string variables for database and tables
sqlite_file = 'data/modified.sqlite'
regular_results = 'RegularSeasonDetailedResults' #hasDate
seasons = 'Seasons' #hasDate
teams  = 'Teams' #noDate
tourney_results = 'TourneyDetailedResults' #hasDate
tourney_seeds = 'TourneySeeds' #hasDate
tourney_slots = 'TourneySlots' #hasDate

'''connect'''
#connection
connExisting = sqlite.connect('data/database.sqlite')


'''transfer'''
#transfer teams

