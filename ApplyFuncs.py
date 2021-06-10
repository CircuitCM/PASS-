import pandas as pd

from dataControl import filter_train_dat, filter_split, rfc, filter_test_dat, predict, teamSort
from perfMeasures import goalPerf, shotData, bodyPart, playerSeasonEval, gamePerfPlayer, gk_defStats, gamePerf
from sklearn.ensemble import RandomForestRegressor
import os
import joblib


def _set_regressor(reg:RandomForestRegressor):
    global freg
    freg=reg


def _get_regressor()-> RandomForestRegressor:
    global freg
    if freg is None:
        freg = joblib.load(os.getcwd()+'/Model Data/rf_model.joblib')
    return freg


def train_from(src:str):
    # source can be anything pandas load_csv accepts, file dir or http
    traindat = pd.read_csv(src)
    train, trainOG = filter_train_dat(traindat)
    train_features, train_labels = filter_split(train)
    save_frame = pd.DataFrame()
    save_frame['train_features']=[train_features]
    save_frame['train_labels']=[train_labels]
    rf = rfc(train_features,train_labels)
    global freg
    freg = rf
    #save model to disk, can be reloaded every time new server restarts
    joblib.dump(rf, os.getcwd()+'/Model Data/rf_model.joblib',compress=3)


def results_from(src:str):
    #source can be anything pandas load_csv accepts
    oxyplayerdata = pd.read_csv(src)
    test1, test = filter_test_dat(oxyplayerdata)
    test1:pd.DataFrame=test1
    test_features, test_labels = filter_split(test)
    labels_pred = predict(_get_regressor(),test_features)
    test1['xG'] = labels_pred
    #---- all this crap really needs to be abstracted
    #alter to specify desired team, or assume there are only desired team stats
    specs = teamSort(test1)
    aG, xG, avgAG, avgXG, Performance, avgPerformance, aGconvR, xGconvR, shots, shotsoT, shotsp90, shotsoTp90 = goalPerf(specs)
    realGoals, expGoals, shotLocation = shotData(specs)
    rightFoot, leftFoot, head = bodyPart(specs)
    playerSeasonE = playerSeasonEval(specs)
    perGameStats_Team, OppGameStats = gamePerf(test1)

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
    PGS, IDs = gamePerfPlayer(specs)
    gk_season = gk_defStats(test1)
    wd = os.getcwd()
    test1.to_csv(wd+'/Model Data/Results/TeamData.csv')
    seasonStats.to_csv(wd+'/Model Data/Results/seasonStats.csv')
    playerSeasonE.to_csv(wd+'/Model Data/Results/playerSeasonEval.csv')
    perGameStats_Team.to_csv(wd+'/Model Data/Results/perGameStats_Team.csv')
    OppGameStats.to_csv(wd+'/Model Data/Results/OppGameStats.csv')
    PGS.to_csv(wd+'/Model Data/Results/PGS.csv')
    gk_season.to_csv(wd+'/Model Data/Results/gk_season.csv')
    #I will save all these to seperate csvs for now, allowing them to be loaded as needed into the website, can be changed later




