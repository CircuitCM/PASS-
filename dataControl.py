'''
ESSENTIAL FILE CONTAINING ALL DATA PROCESSING FUNCTIONS

'''
# General Python Imports
#from RFCmodel import Models
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

#-----------FUNCTION: cleanTrain()-----------#
def filter_train_dat(df1): # PARAM: pandas DataFrame
    #   *Code Outline:
    #       1. Filter - Use the 'bodypart' column as a key to filter out any data rows that don't explicitly inform shot outcomes
    #       2. Drop - Use the .drop function to remove any data columns that don't explicitly inform shot outcomes,
    #                  and subsequently create two separate data sets.
    #           2a. Data Analysis: include descriptive features along with explicit shot data.
    #           2b. Goal Predictions: only include explicitly informative features and labels (i.e. remove all qualitative data)

    #   Code Execution:
    #   1. Filter
    train = df1[pd.notnull(df1['bodypart'])]

    #   2. Drop
    trainOG = train.drop(['id_odsp', 'id_event', 'sort_order', 'text', 'player_out', 'player_in'], axis=1)  # 2a
    train = trainOG.drop(['event_type', 'event_type2', 'player2', 'event_team', 'opponent', 'player', 'time', 'side'], axis=1)  # 2b
    train = train.dropna()
    return train, trainOG

def filter_split(dat):
    dat_features = dat.drop('is_goal', axis=1)
    dat_labels = dat[["is_goal"]]

    # Print Features and Labels shape to ensure accuracy
    #print('Training Features Shape:', train_features.shape)
    #print('Training Labels Shape:', train_labels.shape)
    return dat_features, dat_labels


def filter_test_dat(df)->(pd.DataFrame,pd.DataFrame):
    test1 = df[
        ["ID", "Event_team", "Player", "playerno", "Shot_place", "Shot_outcome", "Location", "Body_Part", "assist_method", "Situation",
         "fastbreak", "is_goal", "x", "y"]]
    test = df[
        ["Shot_place", "Shot_outcome", "is_goal", "Location", "Body_Part", "assist_method", "Situation",
         "fastbreak"]]
    return test1, test


#-----------FUNCTION: teamConv()-----------#
#   Desc: Convert team names to binary for easier use during subsequent analysis
#         - Occidental = 1
#         - Opponent = 0
def teamConv(test): # PARAM: pandas DataFrame

    test['Event_team'] = np.where(test['Event_team'] == 'Occidental', 1, 0)

    return test

#-----------FUNCTION: teamSort()-----------#
#   Desc: Sort and separate the dataframe to only include Occidental College shot data
def teamSort(df): # PARAM: pandas DataFrame
    df = df.loc[df['Event_team'] == 'Occidental']
    return df


#-----------FUNCTION: split()-----------#
#   Desc: Separate Training and Test set labels and features
def split(train, test): # PARAM: 
    # Separate Training Set Labels and Features
    #       global train_features
    #       global train_labels
    #       global test_features
    #       global test_labels

    train_features = train.drop('is_goal', axis=1)
    train_labels = train[["is_goal"]]

    # Separate Test Set Labels and Features
    test_features = test.drop('is_goal', axis=1)
    test_labels = test[['is_goal']]

    # Print Features and Labels shape to ensure accuracy
    print('Training Features Shape:', train_features.shape)
    print('Training Labels Shape:', train_labels.shape)
    print('Testing Features Shape:', test_features.shape)
    print('Testing Labels Shape:', test_labels.shape)
    return train_features, train_labels, test_features, test_labels

#-----------FUNCTION: rfc()-----------#
#   Desc: Run the RandomForest Classifier based on input training and testing sets
def rfc(train_features, train_labels): # PARAM: labels and features for training/test sets

    #   1. Create a Random Forest Regressor
    clf = RandomForestRegressor(n_estimators=1000)

    #   2. Train the model
    clf.fit(train_features, train_labels.values.ravel())
    #labels_pred = clf.predict(test_features)
    #labels_pred = labels_pred.round(2)
    #print("Classifier Predictions:")
    #print(labels_pred)
    #print(labels_pred.shape)

    # 3. Check Accuracy using actual and predicted values

    # Model Accuracy, how often is the classifier correct?

    #print("Accuracy:", metrics.accuracy_score(test_labels, labels_pred))
    return clf

def predict(rf:RandomForestRegressor,test_features):
    labels_pred = rf.predict(test_features)
    labels_pred = labels_pred.round(8)
    return labels_pred


