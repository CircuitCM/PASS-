'''
Main Project File: Running MoBot xG model and reading prediction into a Google spreadsheet

'''
# General Python Imports
import os
import sklearn 
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Data Manipulation and Machine Learning Imports
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from dataControl import cleanTrain, cleanTest, teamConv, split, rfc, teamSort
from perfMeasures import goalPerf, playerSeasonEval, shotData, bodyPart, gamePerf, gamePerfPlayer, gk_defStats
# Google Sheets API Imports
import gspread
import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets 

#* Fetch raw shot data from local and online source
gc = pygsheets.authorize(service_file= 'andrabi-analytics.json')

# Access online data set
Oxy = 'https://docs.google.com/spreadsheets/d/1wg8Alyl0kBnbQEkOGUDW-j5EGvfEGaGP2woXwHHL_88/export?format=csv&gid=0' # read in training data from Google spreadsheet

# Access locally stored data set
Euro = pd.read_csv('events.csv') # read-in .csv file

oxyplayerdata = pd.read_csv(Oxy) # read-in .csv file


# Print statement to indicate no errors in loading data from online source
print("Running... MoBot Expected Goals Model")
print("")

#*-----------------------------------------------------*#
#*               --Main Code Execution--               *#
#*-----------------------------------------------------*#


#* 1. Quality Control
#   *1a. clean training and testing data
#   *1b. confirm that resulting dataframes are of the correcct dimensions by checking their shapes

train, trainOG = cleanTrain(Euro) # clean training data set
print(train.shape) # check shape

test1, test = cleanTest(oxyplayerdata) # clean test data set
print(test.shape) # check shape

OxyData = test1 # clean data set for later use
print(OxyData.shape) #check shape


#* 2. Model Execution
#   *2a. split the data into training and test sets
#   *2b. run MoBot on training and test input

train_features, train_labels, test_features, test_labels = split(train, test) # 2a


labels_pred = rfc(train_features, train_labels, test_features, test_labels) # 2b

#* 3. DataFrame Preparation
#   *3a. Add prediction data to previously cleaned dataframe
#   *3b. Create a separate, duplicate dataframe for additional performance analysis
#       *3b.1. Sort and separate dataframe to only include Occidental College shot information
#   *3c. 

OxyData['xG'] = labels_pred # 3a

# Sort and separate dataframe to only include Occidental shot information

specs = teamSort(OxyData)

# Sort and separate dataframe to only include Occidental shot information
#specs = teamSort(specs)

# Calculate Season Goal performance Stats
aG, xG, avgAG, avgXG, Performance, avgPerformance, aGconvR, xGconvR, shots, shotsoT, shotsp90, shotsoTp90 = goalPerf(specs)

# Extract total aG, xG, and location for every shot
realGoals, expGoals, shotLocation = shotData(specs)

# Extract total instances for each body part (i.e. figure out how much each one was used across the season)
rightFoot, leftFoot, head = bodyPart(specs)


# Extract player performance stats for the entire season
playerSeasonEval = playerSeasonEval(specs)

# Calculate team stats on p90 basis
perGameStats_Team, OppGameStats= gamePerf(OxyData)

# Create dataframe consisting of season goal performance stats
seasonStats = pd.DataFrame()

seasonStats['aG'] = [aG]
seasonStats['xG'] = [xG]
seasonStats['aGp90'] = [avgAG]
seasonStats['xGp90'] = [avgXG]
seasonStats['Performance'] = [Performance]
seasonStats['avgPerformance'] = [avgPerformance]
seasonStats['aGconv_rate'] = [aGconvR]
seasonStats['xGconv_rate'] = [xGconvR]
seasonStats['Total_Shots'] = [shots]
seasonStats['Shots_on_Target'] = [shotsoT]
seasonStats['shotsp90'] = [shotsp90]
seasonStats['shotsoTp90'] = [shotsoTp90]


# Calculate player stats on a p90 basis
PGS, IDs = gamePerfPlayer(specs)

# Calculate GK stats on a seasonal basis
gk_season = gk_defStats(OxyData)
#print(PGS)

# 4. Upload prediction data to Google Sheets
#   *4a. Access xG Stats Google Spreadsheet
#   *4b. Declare and initialize each individual worksheet within xG Stats Google Spreadsheet
#   *4b. Update xG Stats 
#   *4c.


# Access Google Spreadsheet
sh = gc.open('xG Stats')

#--Declare and initialize variables for each individual worksheet within Google Spreadsheet--#

wks = sh[0] # First worksheet: raw_xG 

wks1 = sh[1] # Second worksheet: Season_team

wks2 = sh[2] # Third worksheet: Season-player

wks3 = sh[3] # Fourth worksheet: Game_team

wks4 = sh[4] # Fifth worksheet: Game_player

wks5 = sh[5] # Sixth worksheet: Season_GK

wks10 = sh[9] # Tenth worksheet: Opposition Seasonal Stats

#--Update Google Spreadsheet(s) according to input parameters--#

wks.set_dataframe(OxyData, (1,1)) # Update the entire spreadsheet with OxyData dataframe (raw xG data)

wks1.set_dataframe(seasonStats, (1,1)) # Update the entire spreadsheet with seasonStats dataframe (team's seasonal performance)

wks2.set_dataframe(playerSeasonEval, 'E1') # Update the spreadsheet starting from Cell 'E1' with playerSeasonEval (players' seasonal performance)

wks3.set_dataframe(perGameStats_Team, (1, 1)) # Update the entire spreadsheet with perGameStats_Team dataframe (team's performance per game for '19-20 season)

wks10.set_dataframe(OppGameStats, (1, 1)) # Update the entire spreadsheet with OppGameStats dataframe (opposition's performance per game for '19-20 season)


wks4.set_dataframe(PGS, (1,1))

wks5.set_dataframe(gk_season, (1,1))


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('andrabi-analytics.json', scope)
    
gc = gspread.authorize(credentials)

spreadsheet_key = '1JV_ikgD0xG8IvW-MU8P1XhRQ73CoLmFB81LxU347jQY'

wks_name = 'Master'

print("---HELLO---")
d2g.upload(OxyData, spreadsheet_key, wks_name, credentials=credentials, row_names=True)
