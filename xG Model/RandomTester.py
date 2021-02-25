# General Python Imports
import os
import warnings
import sklearn 
import numpy as np
#warnings.simplefilter(action='ignore', category=FutureWarning)

import time
import matplotlib.pyplot as plt
import seaborn as sns

# Data Manipulation and Machine Learning Imports
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from dataControl import cleanTrain, cleanTest, teamConv, split, rfc, teamSort
from perfMeasures import goalPerf, playerSeasonEval, shotData, bodyPart, gamePerf, gamePerfPlayer, gk_defStats

# Google Sheets Imports
import gspread
import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets 

gc = pygsheets.authorize(service_file= 'andrabi-analytics.json')
#Oxy = 'https://docs.google.com/spreadsheets/d/1JV_ikgD0xG8IvW-MU8P1XhRQ73CoLmFB81LxU347jQY/export?format=csv&gid=0' # read in training data from Google spreadsheet
#Oxy = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSUi7dv_9At8t7pN9UX0J1V_-jfvUJ-SShjKII-GLS2BsUKbDgYHn_-YO9_lt2-onCJ-3ug1XLhvwXI/pub?gid=0&single=true&output=csv'
#Oxy = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSUi7dv_9At8t7pN9UX0J1V_-jfvUJ-SShjKII-GLS2BsUKbDgYHn_-YO9_lt2-onCJ-3ug1XLhvwXI/pub?output=csv' # read in xG data from Google spreadsheet
oxyplayerdata = pd.read_csv('xG.csv')

specs = teamSort(oxyplayerdata)
#print("---SPEcS---")
#print(specs)
# Calculate Season Goal performance Stats
#aG, xG, avgAG, avgXG, Performance, avgPerformance, aGconvR, xGconvR, shots, shotsoT, shotsp90, shotsoTp90 = goalPerf(specs)

#ealGoals, expGoals, shotLocation = shotData(specs)


#rightFoot, leftFoot, head = bodyPart(specs)

#playerSeasonEval = playerSeasonEval(specs)
#print(playerSeasonEval)
#print(oxyplayerdata)
xG = specs['xG']
xG = sum(xG)
print(xG)


playerStats, Check = gamePerfPlayer(specs)
PGS, Opp = gamePerf(oxyplayerdata)
print("team perGame Stats")
print(PGS)
print("player perGame Stats")
print(playerStats.shape[0])
print(playerStats)

'''
sh = gc.open('xG Stats')

wks5 = sh[5]
wks5.set_dataframe(gk_season, (1,1))
#wks4.set_dataframe(IDs, 'A1')
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'andrabi-analytics.json', scope)
gc = gspread.authorize(credentials)

spreadsheet_key = '1JV_ikgD0xG8IvW-MU8P1XhRQ73CoLmFB81LxU347jQY'
wks_name = 'Master'
'''

