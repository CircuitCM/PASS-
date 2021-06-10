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
from perfMeasures import goalPerf, playerSeasonEval, shotData, bodyPart, gamePerf, gamePerfPlayer

# Google Sheets Imports
import gspread
import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets 

gc = pygsheets.authorize(service_file= 'andrabi-analytics.json')
Oxy = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSUi7dv_9At8t7pN9UX0J1V_-jfvUJ-SShjKII-GLS2BsUKbDgYHn_-YO9_lt2-onCJ-3ug1XLhvwXI/pub?output=csv' # read in xG data from Google spreadsheet
oxyplayerdata = pd.read_csv(Oxy)


oxySpecs = teamSort(oxyplayerdata)

seasonStats = playerSeasonEval(oxySpecs)
df = oxySpecs

# Create soccer pitch graphic
def pitch_creator(size=(10,10)):
    with plt.style.context('bmh'):
        fig = plt.figure()
        plt.axis([-1, 27, -1, 27])
        plt.grid(False)


        plt.plot([0, 0], [0, 25], color='black')
        plt.plot([0, 25], [25, 25], color="black")
        plt.plot([25, 25], [25, 0], color='black')
        plt.plot([0, 25], [0, 0], color='black')
        
         # penalty area
        plt.plot([9, 9], [25, 22], color='black')
        plt.plot([9, 16], [22, 22], color = 'black')
        plt.plot([16, 16], [25, 22], color = 'black')

        #18-yard box
        plt.plot([4, 4], [25, 16], color = 'black')
        plt.plot([4, 21], [16, 16], color = 'black')
        plt.plot([21, 21], [25, 16], color = 'black')

        # right goal posts
        plt.plot([11, 11], [25, 24.5], color='black')
        plt.plot([11, 14], [24.5, 24.5], color='black')
        plt.plot([14, 14], [24.5, 25], color='black')

        centreCircle = plt.Circle((60, 40), 10, color='black', fill=False)
        ax = plt.gca()
        ax.add_patch(centreCircle)
        ax.set_facecolor('green')


        

# Create HeatMap

#plotting all data
plt1 = pitch_creator()
#Tidy Axes
plt.axis('off')

sns.kdeplot(df["x"],df["y"], shade=True,n_levels=50)
plt.ylim(0, 25)
plt.xlim(0, 25)

plt.title("Shot Location Heat Map", size = 18)
plt.legend(loc='upper right')
plt.savefig('Season Shot Map.png')
plt.show()

# basic plot
p1=sns.regplot(data=df, x="x", y="y", fit_reg=False, marker="o", color="skyblue", scatter_kws={'s':400})
  