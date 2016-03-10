#an ETL job to extract years >= 2014 for all databases in database.sqlite
import sqlite3 as sqlite

#string variables for database and tables
sqlite_file = 'data/modified.sqlite'
regular_detailed = 'RegularSeasonDetailedResults'
seasons = 'Seasons'
teams  = 'Teams'

connExisting = sqlite.connect('data/database.sqlite')
connNew = sqlite.connect(sqlite_file)


