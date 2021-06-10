'''
    FUNCTIONS FOR CALCULATING AND EXTRACTING PERFORMANCE INFORMATION
'''
# Functions for calculating performance measures
import pandas as pd
import sklearn as sk
from dataControl import teamConv, teamSort

def goalPerf(df):
    
    realGoals = df['is_goal']
    aG = realGoals[realGoals == 1].value_counts()
    aG = sum(aG)


    expGoals = df['xG']
    xG = sum(expGoals)
    xG = round(xG, 2)
    
 
    out = df['ID'].nunique()
    out = int(out)

# If the player or team hasn't registered any shots for the entire season (e.g. Goalkeeper or benchwarmer) set all return variables = 0
    if df.shape[0] == 0:
        xG = 0 
        aG = 0
        avgAG = 0
        avgXG = 0
        shotsp90 = 0
        shotsoTp90 = 0
        Performance = 0
        avgPerformance = 0
        xGconvR = 0
        aGconvR = 0
        shots = 0
        onTarget = 0

# If player or team has registered 0 xG for the entire season
    elif xG == 0:
        avgAG = round((aG/out),2)

        avgXG = 0

        Performance = round((aG - xG),2)

        avgPerformance = (avgAG - avgXG)

        xGconvR = 0

        shots = df.shape[0]
        aGconvR = round((aG/shots), 2)

        # Calculate total shots and shots on target for the entire season and per90
        totalShots = df.shape[0]

        array = [1, 4]
        outcome = df.loc[df['Shot_outcome'].isin(array)]
            
        onTarget = outcome.shape[0]

        # Shots/on target p90
        shotsp90 = round((totalShots/out), 2)
        shotsoTp90 = round((onTarget/out), 2)

# Team or player has registered at least 1 xG for the entire season
    else:
        avgAG = round((aG/out),2)

        avgXG = round((xG/out),2)

        Performance = round((aG - xG),2)

        avgPerformance = (avgAG - avgXG)

        xGconvR = round((aG/xG),2)

        shots = df.shape[0]
        aGconvR = round((aG/shots), 2)

        # Calculate total shots and shots on target for the entire season and per90
        totalShots = df.shape[0]

        array = [1, 4]
        outcome = df.loc[df['Shot_outcome'].isin(array)]
            
        onTarget = outcome.shape[0]
        # Shots/on target p90
        shotsp90 = round((totalShots/out), 2)
        shotsoTp90 = round((onTarget/out), 2)




    return aG, xG, avgAG, avgXG, Performance, avgPerformance, aGconvR, xGconvR, shots, onTarget, shotsp90, shotsoTp90

# Return each instance of aG and xG for the entire season (as opposed to integer summation)
def shotData(df):
    
    aG = df.loc[df['is_goal'] == 1]
    
    xG = df['xG']

    shotLocation = df['Location']
    return aG, xG, shotLocation

#
def bodyPart(df):
    rightFoot = pd.DataFrame(df.loc[df['Body_Part'] == 1])
    rightFoot = rightFoot['Body_Part']

    leftFoot = pd.DataFrame(df.loc[df['Body_Part'] == 2])
    leftFoot = leftFoot['Body_Part']

    head = df.loc[df['Body_Part'] == 3]
    head = head['Body_Part']

    return rightFoot, leftFoot, head


#*----FUNCTION: playerSeasonEval(df)----#
#*   Desc: accepts pandas dataframe input
#*   Execution:
#       *1. Sort the Occidental DataFrame based on each player's name.
#       *2. Split into 28 separate dataframes (one for each player).
#       *3. call goalPerf() and perform seasonal performance evaluation for each player (goalkeepers included).
#           *3a. Returns 12 variables for each player (Note: inefficient approach)
#       *4. Add each player's return as a new row in a dataframe
#       *4. Return the 336 variables for use in the main script

def playerSeasonEval(df):
    BHarding = pd.DataFrame(df.loc[df['Player'] == 'Ben Harding'])
    BH1, BH2, BH3, BH4, BH5, BH6, BH7, BH8, BH9, BH10, BH11, BH12 = goalPerf(BHarding)

    JGitin = pd.DataFrame(df.loc[df['Player'] == 'Jacob Gitin'])
    JG1, JG2, JG3, JG4, JG5, JG6, JG7, JG8, JG9, JG10, JG11, JG12 = goalPerf(JGitin)

    SDrazan = pd.DataFrame(df.loc[df['Player'] == 'Scott Drazan'])
    SD1, SD2, SD3, SD4, SD5, SD6, SD7, SD8, SD9, SD10, SD11, SD12 = goalPerf(SDrazan)

    RMccabe = pd.DataFrame(df.loc[df['Player'] == 'Riley Mccabe'])
    RM1, RM2, RM3, RM4, RM5, RM6, RM7, RM8, RM9, RM10, RM11, RM12 = goalPerf(RMccabe)    

    SShearer = pd.DataFrame(df.loc[df['Player'] == 'Spencer Shearer'])
    SS1, SS2, SS3, SS4, SS5, SS6, SS7, SS8, SS9, SS10, SS11, SS12 = goalPerf(SShearer)

    RWilson = pd.DataFrame(df.loc[df['Player'] == 'Ryan Wilson'])
    RW1, RW2, RW3, RW4, RW5, RW6, RW7, RW8, RW9, RW10, RW11, RW12 = goalPerf(RWilson)

    DPaine = pd.DataFrame(df.loc[df['Player'] == 'David Paine'])
    DP1, DP2, DP3, DP4, DP5, DP6, DP7, DP8, DP9, DP10, DP11, DP12 = goalPerf(DPaine)

    NEble = pd.DataFrame(df.loc[df['Player'] == 'Nicolas Eble'])
    NE1, NE2, NE3, NE4, NE5, NE6, NE7, NE8, NE9, NE10, NE11, NE12 = goalPerf(NEble)

    MTeplitz = pd.DataFrame(df.loc[df['Player'] == 'Matthew Teplitz'])
    MT1, MT2, MT3, MT4, MT5, MT6, MT7, MT8, MT9, MT10, MT11, MT12 = goalPerf(MTeplitz)

    BSimon = pd.DataFrame(df.loc[df['Player'] == 'Ben Simon'])
    BS1, BS2, BS3, BS4, BS5, BS6, BS7, BS8, BS9, BS10, BS11, BS12 = goalPerf(MTeplitz)

    MBlumenfeld = pd.DataFrame(df.loc[df['Player'] == 'Marcus Blumenfeld'])
    MB1, MB2, MB3, MB4, MB5, MB6, MB7, MB8, MB9, MB10, MB11, MB12 = goalPerf(MBlumenfeld)

    JBrannon = pd.DataFrame(df.loc[df['Player'] == 'Jasper Brannon'])
    JB1, JB2, JB3, JB4, JB5, JB6, JB7, JB8, JB9, JB10, JB11, JB12 = goalPerf(JBrannon)

    MAnzalone = pd.DataFrame(df.loc[df['Player'] == 'Matthew Anzalone'])
    MA1, MA2, MA3, MA4, MA5, MA6, MA7, MA8, MA9, MA10, MA11, MA12 = goalPerf(MAnzalone)

    SKim = pd.DataFrame(df.loc[df['Player'] == 'Sean Kim'])
    SK1, SK2, SK3, SK4, SK5, SK6, SK7, SK8, SK9, SK10, SK11, SK12 = goalPerf(SKim)

    JMeeker = pd.DataFrame(df.loc[df['Player'] == 'Jack Meeker'])
    JM1, JM2, JM3, JM4, JM5, JM6, JM7, JM8, JM9, JM10, JM11, JM12 = goalPerf(JMeeker)

    AParedes = pd.DataFrame(df.loc[df['Player'] == 'Adrian Paredes'])
    AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10, AP11, AP12 = goalPerf(AParedes)    
    LMyers = pd.DataFrame(df.loc[df['Player'] == 'Logan Myers'])
    LM1, LM2, LM3, LM4, LM5, LM6, LM7, LM8, LM9, LM10, LM11, LM12 = goalPerf(LMyers)

    TWray = pd.DataFrame(df.loc[df['Player'] == 'Tyler Wray'])
    TW1, TW2, TW3, TW4, TW5, TW6, TW7, TW8, TW9, TW10, TW11, TW12 = goalPerf(TWray)

    JFoster = pd.DataFrame(df.loc[df['Player'] == 'Jake Foster'])
    JF1, JF2, JF3, JF4, JF5, JF6, JF7, JF8, JF9, JF10, JF11, JF12 = goalPerf(JFoster)

    JSchwartz = pd.DataFrame(df.loc[df['Player'] == 'Joey Schwartz'])
    JS1, JS2, JS3, JS4, JS5, JS6, JS7, JS8, JS9, JS10, JS11, JS12 = goalPerf(JSchwartz)

    JHenry = pd.DataFrame(df.loc[df['Player'] == 'Jazz Henry'])
    JH1, JH2, JH3, JH4, JH5, JH6, JH7, JH8, JH9, JH10, JH11, JH12 = goalPerf(JHenry)

    TJarvis = pd.DataFrame(df.loc[df['Player'] == 'Teagan Jarvis'])
    TJ1, TJ2, TJ3, TJ4, TJ5, TJ6, TJ7, TJ8, TJ9, TJ10, TJ11, TJ12 = goalPerf(TJarvis)

    THernandez = pd.DataFrame(df.loc[df['Player'] == 'Tye Hernandez'])
    TH1, TH2, TH3, TH4, TH5, TH6, TH7, TH8, TH9, TH10, TH11, TH12 = goalPerf(THernandez)

    MRobertson = pd.DataFrame(df.loc[df['Player'] == 'Miles Robertson'])
    MR1, MR2, MR3, MR4, MR5, MR6, MR7, MR8, MR9, MR10, MR11, MR12 = goalPerf(MRobertson)    

    CJordening = pd.DataFrame(df.loc[df['Player'] == 'Caleb Jordening'])
    CJ1, CJ2, CJ3, CJ4, CJ5, CJ6, CJ7, CJ8, CJ9, CJ10, CJ11, CJ12 = goalPerf(CJordening)

    NStreitz = pd.DataFrame(df.loc[df['Player'] == 'Neython Streitz'])
    NS1, NS2, NS3, NS4, NS5, NS6, NS7, NS8, NS9, NS10, NS11, NS12 = goalPerf(NStreitz)

    BTucker = pd.DataFrame(df.loc[df['Player'] == 'Ben Tucker'])
    BT1, BT2, BT3, BT4, BT5, BT6, BT7, BT8, BT9, BT10, BT11, BT12 = goalPerf(BTucker)

    LHaas = pd.DataFrame(df.loc[df['Player'] == 'Luke Haas'])
    LH1, LH2, LH3, LH4, LH5, LH6, LH7, LH8, LH9, LH10, LH11, LH12 = goalPerf(LHaas)

    EDacosta = pd.DataFrame(df.loc[df['Player'] == 'Eric Dacosta'])
    ED1, ED2, ED3, ED4, ED5, ED6, ED7, ED8, ED9, ED10, ED11, ED12 = goalPerf(EDacosta)
    df = pd.DataFrame()

    df['Player'] = ['Ben Harding', 'Jacob Gitin', 'Scott Drazan', 'Riley Mccabe', 'Spencer Shearer', 'Ryan Wilson', 'David Paine', 'Nicolas Eble', 'Matthew Teplitz', 'Ben Simon', 'Marcus Blumenfeld', 'Jasper Brannon', 'Matthew Anzalone', 'Sean Kim', 'Jack Meeker', 'Adrian Paredes', 'Logan Myers', 'Tyler Wray', 'Jake Foster', 'Joey Schwartz', 'Jazz Henry', 'Teagan Jarvis', 'Tye Hernandez', 'Miles Robertson', 'Caleb Jordening', 'Neython Streitz', 'Ben Tucker', 'Luke Haas', 'Eric Dacosta']
    df['playerno'] = ['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '27', '30', '31']
    df['position'] = ['GK', 'GK', 'GK', 'D', 'M', 'M',	'D', 'M', 'F', 'M',	'F', 'M', 'D', 'F', 'D', 'M', 'M', 'F',	'M', 'M', 'F', 'F',	'M', 'D', 'F', 'D',	'D', 'GK', 'D']
    df['year'] = ['FY', 'So', 'Jr', 'Sr', 'So', 'Sr', 'Jr', 'Jr', 'Jr', 'Sr', 'Jr', 'So', 'So', 'Jr', 'Jr', 'So', 'FY', 'Sr', 'So', 'FY', 'FY', 'So', 'FY', 'Sr', 'FY', 'FY', 'Jr', 'Sr', 'FY']
    df['aG'] = [BH1, JG1, SD1, RM1, SS1, RW1, DP1, NE1, MT1, BS1, MB1, JB1, MA1, SK1, JM1, AP1, LM1, TW1, JF1, JS1, JH1, TJ1, TH1, MR1, CJ1, NS1, BT1, LH1, ED1] 
    df['xG'] = [BH2, JG2, SD2, RM2, SS2, RW2, DP2, NE2, MT2, BS2, MB2, JB2, MA2, SK2, JM2, AP2, LM2, TW2, JF2, JS2, JH2, TJ2, TH2, MR2, CJ2, NS2, BT2, LH2, ED2] 
    df['aGp90'] = [BH3, JG3, SD3, RM3, SS3, RW3, DP3, NE3, MT3, BS3, MB3, JB3, MA3, SK3, JM3, AP3, LM3, TW3, JF3, JS3, JH3, TJ3, TH3, MR3, CJ3, NS3, BT3, LH3, ED3]
    df['xgp90'] = [BH4, JG4, SD4, RM4, SS4, RW4, DP4, NE4, MT4, BS4, MB4, JB4, MA4, SK4, JM4, AP4, LM4, TW4, JF4, JS4, JH4, TJ4, TH4, MR4, CJ4, NS4, BT4, LH4, ED4]
    df['Perf'] = [BH5, JG5, SD5, RM5, SS5, RW5, DP5, NE5, MT5, BS5, MB5, JB5, MA5, SK5, JM5, AP5, LM5, TW5, JF5, JS5, JH5, TJ5, TH5, MR5, CJ5, NS5, BT5, LH5, ED5]
    df['Perfp90'] = [BH6, JG6, SD6, RM6, SS6, RW6, DP6, NE6, MT6, BS6, MB6, JB6, MA6, SK6, JM6, AP6, LM6, TW6, JF6, JS6, JH6, TJ6, TH6, MR6, CJ6, NS6, BT6, LH6, ED6]
    df['aGconvR'] = [BH7, JG7, SD7, RM7, SS7, RW7, DP7, NE7, MT7, BS7, MB7, JB7, MA7, SK7, JM7, AP7, LM7, TW7, JF7, JS7, JH7, TJ7, TH7, MR7, CJ7, NS7, BT7, LH7, ED7]
    df['xGconvR'] = [BH8, JG8, SD8, RM8, SS8, RW8, DP8, NE8, MT8, BS8, MB8, JB8, MA8, SK8, JM8, AP8, LM8, TW8, JF8, JS8, JH8, TJ8, TH8, MR8, CJ8, NS8, BT8, LH8, ED8]
    df['Total_Shots'] = [BH9, JG9, SD9, RM9, SS9, RW9, DP9, NE9, MT9, BS9, MB9, JB9, MA9, SK9, JM9, AP9, LM9, TW9, JF9, JS9, JH9, TJ9, TH9, MR9, CJ9, NS9, BT9, LH9, ED9]
    df['Shots_on_Target'] = [BH10, JG10, SD10, RM10, SS10, RW10, DP10, NE10, MT10, BS10, MB10, JB10, MA10, SK10, JM10, AP10, LM10, TW10, JF10, JS10, JH10, TJ10, TH10, MR10, CJ10, NS10, BT10, LH10, ED10]
    df['shotsp90'] = [BH11, JG11, SD11, RM11, SS11, RW11, DP11, NE11, MT11, BS11, MB11, JB11, MA11, SK11, JM11, AP11, LM11, TW11, JF11, JS11, JH11, TJ11, TH11, MR11, CJ11, NS11, BT11, LH11, ED11]
    df['shotsoTp90'] = [BH12, JG12, SD12, RM12, SS12, RW12, DP12, NE12, MT12, BS12, MB12, JB12, MA12, SK12, JM12, AP12, LM12, TW12, JF12, JS12, JH12, TJ12, TH12, MR12, CJ12, NS12, BT12, LH12, ED12]

    return df

#This function performs xG analysis on each recorded game (16 total),
#%   by splitting up the shot data based on its game ID (e.g. all events 
#%   from the fourth game have an ID of 4).
#%

#*-----------FUNCTION: gamePerf(df)-----------*#
#*   Desc: perform xG analysis for each recorded game (16 ToW)
#*   Execution:
#       *1. Sort the Occidental DataFrame based on each player's name.
#       *2. Split shot data based on game ID
#       *3. call goalPerf() and perform seasonal performance evaluation for each player (goalkeepers included).
#           *3a. Returns 12 variables for each player (Note: inefficient approach)
#       *4. Add each player's return as a new row in a dataframe
#       *4. Return the 336 variables for use in the main script

def gamePerf(df):
    
    print("TEAM CHECK")
    print(df)
    numGames = df['ID'].nunique()


    PGS = pd.DataFrame()
    OppPGS = pd.DataFrame()
    for i in range(1, numGames+1):
        # Split up based on game ID (i.e. each individual game)
        xP = 0
        aP = 0
        perGameStats = pd.DataFrame()
        OppGameStats = pd.DataFrame()

        gameID = i
        OxyGoals = pd.DataFrame(df.loc[df['ID'] == i])
        OppGoals = pd.DataFrame(df.loc[df['ID'] == i])

        OxyGoals = pd.DataFrame(OxyGoals.loc[df['Event_team'] == 'Occidental'])
        OppGoals = pd.DataFrame(OppGoals.loc[df['Event_team'] != 'Occidental'])

        print("---Oxy Goals Check---")
        print(OxyGoals)

        print("---OPP GOALS CHECK---")
        print(OppGoals)

        # Occidental College xG and aG calculations
        RG = OxyGoals['is_goal']
        aG = sum(i for i in RG if i == 1) 
        XG = OxyGoals['xG']
        xG = sum(i for i in XG if i != 0)
        
        aGconvR = round(aG/OxyGoals.shape[0], 2)
        chanceQ = round(xG/OxyGoals.shape[0], 2)

        OxyShots = OxyGoals.shape[0]
        array = [1, 4]
        OxyShotsonTarget = OxyGoals.loc[OxyGoals['Shot_outcome'].isin(array)]
        OxyShotsonTarget = OxyShotsonTarget.shape[0]


        # Opposition xG and aG Calculations
        OppRG = OppGoals['is_goal']
        OppaG = sum(i for i in OppRG if i == 1)
        ExG = OppGoals['xG']
        OppxG = sum(i for i in ExG if i != 0)
        if OppGoals.shape[0] == 0:
            OppaGConvR = 0
            OppchanceQ = 0
            OppShots = 0
            OppShotsonTarget = 0
        else:
            OppaGconvR = round(OppaG/OppGoals.shape[0], 2)
            OppchanceQ = round(OppxG/OppGoals.shape[0], 2)

            OppShots = OppGoals.shape[0]
            OppShotsonTarget = OppGoals.loc[OppGoals['Shot_outcome'].isin(array)]
            OppShotsonTarget = OppShotsonTarget.shape[0]


        # Calculationg Expected and Actual outcomes individual matches
        xPerformance = (xG - OppxG)
        aPerformance = (aG - OppaG)
       
        perGameStats['ID'] = [gameID]
        perGameStats['aG'] = [aG]
        perGameStats['xG'] = [xG]
        perGameStats['Shots'] = [OxyShots]
        perGameStats['SoT'] = [OxyShotsonTarget]
        perGameStats['convR'] = [aGconvR]
        perGameStats['CQ'] = [chanceQ]
        
        OppGameStats['ID'] = [gameID]
        OppGameStats['aG'] = [OppaG]
        OppGameStats['xG'] = [OppxG]
        OppGameStats['Shots'] = [OppShots]
        OppGameStats['SoT'] = [OppShotsonTarget]
        OppGameStats['convR'] = [OppaGconvR]
        OppGameStats['CQ'] = [OppchanceQ]

        if aG > OppaG:
            aP += 3
            perGameStats['aP'] = [aP]
            if xG > OppxG:
                xP += 3
                perGameStats['xP'] = [xP]
            elif xG < OppxG:
                xP += 0
                perGameStats['xP'] = [xP]
            else:
                xP += 1
                perGameStats['xP'] = [xP]
        elif aG < OppaG:
            aP += 0
            perGameStats['aP'] = [aP]
            if xG > OppxG:
                xP += 3
                perGameStats['xP'] = [xP]
            elif xG < OppxG:
                xP += 0
                perGameStats['xP'] = [xP]
            else:
                xP += 1
                perGameStats['xP'] = [xP]
        else:
            aP += 1
            perGameStats['aP'] = [aP]
            if xG > OppxG:
                xP += 3
                perGameStats['xP'] = [xP]
            elif xG < OppxG:
                xP += 0
                perGameStats['xP'] = [xP]
            else:
                xP += 1
                perGameStats['xP'] = [xP]
                                    
        PGS = PGS.append(perGameStats)
        OppPGS = OppPGS.append(OppGameStats)
        print("---PGS CHECK---")
        print(PGS)
    return PGS, OppPGS


def playerStatsCalc(df):
    RG = df['is_goal']
    aG = sum(i for i in RG if i == 1) 
    XG = df['xG']
    xG = sum(i for i in XG if i != 0)

    totalShots = df.shape[0]

    array = [1, 4]
    outcome = df.loc[df['Shot_outcome'].isin(array)]
            
    onTarget = outcome.shape[0]

    if aG > xG:
        perf = "Overperformed"
    elif aG < xG:
        perf = "Underperformed"
    else:
        perf = "On Par"    

    return aG, xG, totalShots, onTarget, perf


def gamePerfPlayer(df):
    print(df)
    df = df.loc[df['Event_team'] == 'Occidental']
    print("---HELLLLLLOOOOOO---")
    print(df)
    numGames = df['ID'].nunique()
    
    print(numGames)
    PGS = pd.DataFrame()
    Check = pd.DataFrame()
    for i in range(1, numGames+1):
        playerStats = pd.DataFrame()
        checker = pd.DataFrame()

        Games = pd.DataFrame(df.loc[df['ID'] == i])

        gameID = i
        print("gameID: ", gameID)

        BHarding = pd.DataFrame(Games.loc[df['Player'] == 'Ben Harding'])
        BH1, BH2, BH3, BH4, BH5 = playerStatsCalc(BHarding)

        JGitin = pd.DataFrame(Games.loc[df['Player'] == 'Jacob Gitin'])
        JG1, JG2, JG3, JG4, JG5 = playerStatsCalc(JGitin)

        SDrazan = pd.DataFrame(Games.loc[df['Player'] == 'Scott Drazan'])
        SD1, SD2, SD3, SD4, SD5 = playerStatsCalc(SDrazan)

        RMccabe = pd.DataFrame(Games.loc[df['Player'] == 'Riley Mccabe'])
        RM1, RM2, RM3, RM4, RM5 = playerStatsCalc(RMccabe)    

        SShearer = pd.DataFrame(Games.loc[df['Player'] == 'Spencer Shearer'])
        SS1, SS2, SS3, SS4, SS5 = playerStatsCalc(SShearer)

        RWilson = pd.DataFrame(Games.loc[df['Player'] == 'Ryan Wilson'])
        RW1, RW2, RW3, RW4, RW5, = playerStatsCalc(RWilson)

        DPaine = pd.DataFrame(Games.loc[df['Player'] == 'David Paine'])
        DP1, DP2, DP3, DP4, DP5 = playerStatsCalc(DPaine)

        NEble = pd.DataFrame(Games.loc[df['Player'] == 'Nicolas Eble'])
        NE1, NE2, NE3, NE4, NE5 = playerStatsCalc(NEble)

        MTeplitz = pd.DataFrame(Games.loc[df['Player'] == 'Matthew Teplitz'])
        MT1, MT2, MT3, MT4, MT5 = playerStatsCalc(MTeplitz)

        BSimon = pd.DataFrame(Games.loc[df['Player'] == 'Ben Simon'])
        BS1, BS2, BS3, BS4, BS5 = playerStatsCalc(MTeplitz)

        MBlumenfeld = pd.DataFrame(Games.loc[df['Player'] == 'Marcus Blumenfeld'])
        MB1, MB2, MB3, MB4, MB5 = playerStatsCalc(MBlumenfeld)

        JBrannon = pd.DataFrame(Games.loc[df['Player'] == 'Jasper Brannon'])
        JB1, JB2, JB3, JB4, JB5 = playerStatsCalc(JBrannon)

        MAnzalone = pd.DataFrame(Games.loc[df['Player'] == 'Matthew Anzalone'])
        MA1, MA2, MA3, MA4, MA5 = playerStatsCalc(MAnzalone)

        SKim = pd.DataFrame(Games.loc[df['Player'] == 'Sean Kim'])
        SK1, SK2, SK3, SK4, SK5 = playerStatsCalc(SKim)

        JMeeker = pd.DataFrame(Games.loc[df['Player'] == 'Jack Meeker'])
        JM1, JM2, JM3, JM4, JM5 = playerStatsCalc(JMeeker)

        AParedes = pd.DataFrame(Games.loc[df['Player'] == 'Adrian Paredes'])
        AP1, AP2, AP3, AP4, AP5 = playerStatsCalc(AParedes)    

        LMyers = pd.DataFrame(Games.loc[df['Player'] == 'Logan Myers'])
        LM1, LM2, LM3, LM4, LM5 = playerStatsCalc(LMyers)

        TWray = pd.DataFrame(Games.loc[df['Player'] == 'Tyler Wray'])
        TW1, TW2, TW3, TW4, TW5 = playerStatsCalc(TWray)

        JFoster = pd.DataFrame(Games.loc[df['Player'] == 'Jake Foster'])
        JF1, JF2, JF3, JF4, JF5 = playerStatsCalc(JFoster)

        JSchwartz = pd.DataFrame(Games.loc[df['Player'] == 'Joey Schwartz'])
        JS1, JS2, JS3, JS4, JS5 = playerStatsCalc(JSchwartz)

        JHenry = pd.DataFrame(Games.loc[df['Player'] == 'Jazz Henry'])
        JH1, JH2, JH3, JH4, JH5 = playerStatsCalc(JHenry)

        TJarvis = pd.DataFrame(Games.loc[df['Player'] == 'Teagan Jarvis'])
        TJ1, TJ2, TJ3, TJ4, TJ5= playerStatsCalc(TJarvis)

        THernandez = pd.DataFrame(Games.loc[df['Player'] == 'Tye Hernandez'])
        TH1, TH2, TH3, TH4, TH5 = playerStatsCalc(THernandez)

        MRobertson = pd.DataFrame(Games.loc[df['Player'] == 'Miles Robertson'])
        MR1, MR2, MR3, MR4, MR5 = playerStatsCalc(MRobertson)    

        CJordening = pd.DataFrame(Games.loc[df['Player'] == 'Caleb Jordening'])
        CJ1, CJ2, CJ3, CJ4, CJ5 = playerStatsCalc(CJordening)

        NStreitz = pd.DataFrame(Games.loc[df['Player'] == 'Neython Streitz'])
        NS1, NS2, NS3, NS4, NS5 = playerStatsCalc(NStreitz)

        BTucker = pd.DataFrame(Games.loc[df['Player'] == 'Ben Tucker'])
        BT1, BT2, BT3, BT4, BT5 = playerStatsCalc(BTucker)

        LHaas = pd.DataFrame(Games.loc[df['Player'] == 'Luke Haas'])
        LH1, LH2, LH3, LH4, LH5 = playerStatsCalc(LHaas)

        EDacosta = pd.DataFrame(Games.loc[df['Player'] == 'Eric Dacosta'])
        ED1, ED2, ED3, ED4, ED5 = playerStatsCalc(EDacosta)

        checker['ID'] = [gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID,]
        checker ['Player'] = ['Ben Harding', 'Jacob Gitin', 'Scott Drazan', 'Riley Mccabe', 'Spencer Shearer', 'Ryan Wilson', 'David Paine', 'Nicolas Eble', 'Matthew Teplitz', 'Ben Simon', 'Marcus Blumenfeld', 'Jasper Brannon', 'Matthew Anzalone', 'Sean Kim', 'Jack Meeker', 'Adrian Paredes', 'Logan Myers', 'Tyler Wray', 'Jake Foster', 'Joey Schwartz', 'Jazz Henry', 'Teagan Jarvis', 'Tye Hernandez', 'Miles Robertson', 'Caleb Jordening', 'Neython Streitz', 'Ben Tucker', 'Luke Haas', 'Eric Dacosta']
        
        
        playerStats['ID'] = [gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID, gameID,]
        playerStats['Player'] = ['Ben Harding', 'Jacob Gitin', 'Scott Drazan', 'Riley Mccabe', 'Spencer Shearer', 'Ryan Wilson', 'David Paine', 'Nicolas Eble', 'Matthew Teplitz', 'Ben Simon', 'Marcus Blumenfeld', 'Jasper Brannon', 'Matthew Anzalone', 'Sean Kim', 'Jack Meeker', 'Adrian Paredes', 'Logan Myers', 'Tyler Wray', 'Jake Foster', 'Joey Schwartz', 'Jazz Henry', 'Teagan Jarvis', 'Tye Hernandez', 'Miles Robertson', 'Caleb Jordening', 'Neython Streitz', 'Ben Tucker', 'Luke Haas', 'Eric Dacosta']
        playerStats['playerno'] = ['0', '00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '27', '30', '31']
        playerStats['position'] = ['GK', 'GK', 'GK', 'D', 'M', 'M',	'D', 'M', 'F', 'M',	'F', 'M', 'D', 'F', 'D', 'M', 'M', 'F',	'M', 'M', 'F', 'F',	'M', 'D', 'F', 'D',	'D', 'GK', 'D']
        playerStats['year'] = ['FY', 'So', 'Jr', 'Sr', 'So', 'Sr', 'Jr', 'Jr', 'Jr', 'Sr', 'Jr', 'So', 'So', 'Jr', 'Jr', 'So', 'FY', 'Sr', 'So', 'FY', 'FY', 'So', 'FY', 'Sr', 'FY', 'FY', 'Jr', 'Sr', 'FY']
        playerStats['aG'] = [BH1, JG1, SD1, RM1, SS1, RW1, DP1, NE1, MT1, BS1, MB1, JB1, MA1, SK1, JM1, AP1, LM1, TW1, JF1, JS1, JH1, TJ1, TH1, MR1, CJ1, NS1, BT1, LH1, ED1] 
        playerStats['xG'] = [BH2, JG2, SD2, RM2, SS2, RW2, DP2, NE2, MT2, BS2, MB2, JB2, MA2, SK2, JM2, AP2, LM2, TW2, JF2, JS2, JH2, TJ2, TH2, MR2, CJ2, NS2, BT2, LH2, ED2] 
        playerStats['Total_Shots'] = [BH3, JG3, SD3, RM3, SS3, RW3, DP3, NE3, MT3, BS3, MB3, JB3, MA3, SK3, JM3, AP3, LM3, TW3, JF3, JS3, JH3, TJ3, TH3, MR3, CJ3, NS3, BT3, LH3, ED3]
        playerStats['Shots_on_Target'] = [BH4, JG4, SD4, RM4, SS4, RW4, DP4, NE4, MT4, BS4, MB4, JB4, MA4, SK4, JM4, AP4, LM4, TW4, JF4, JS4, JH4, TJ4, TH4, MR4, CJ4, NS4, BT4, LH4, ED4]
        playerStats['Performance'] = [BH5, JG5, SD5, RM5, SS5, RW5, DP5, NE5, MT5, BS5, MB5, JB5, MA5, SK5, JM5, AP5, LM5, TW5, JF5, JS5, JH5, TJ5, TH5, MR5, CJ5, NS5, BT5, LH5, ED5]


        print("---Stats Check---")
        print(playerStats)
        print("-----------------")
        print("")
        Check = Check.append(checker)
        PGS = PGS.append(playerStats)

    return PGS, Check

#-----------FUNCTION: gk_defStats()-----------#
def gk_defStats(df):
    # Filter the DataFrame to only include opposition statistics (i.e. teams other than Occidental)
    OppStats = pd.DataFrame(df.loc[df['Event_team'] != 'Occidental'])


    # Take and store the sum of total xG conceded for the season
    AG = OppStats['is_goal']
    OppaG = sum(AG)
    
    # Take and store the sum of total xG conceded for the season
    XG = OppStats['xG']
    OppxG = sum(XG)

    # Calculate and store the total number of shots conceded
    oppShots = OppStats.shape[0]

    
    array = [1, 4]
    outcome = OppStats.loc[OppStats['Shot_outcome'].isin(array)]
            
    onTarget = outcome.shape[0]

    # Calculate true defensive rating: ratio of xG conceded to shots conceded
    defPerf = 10 * (1 - (OppxG/oppShots))
    defPerf = round(defPerf,2)
    print("defPerf:", defPerf)

    # Calcuate goalkeeper save rating (out 0f 10): ratio of goals conceded to shots conceded
    gkRate = 10 * (1- (OppaG/onTarget))
    gkRate = round(gkRate,2)
    print("gKSR: ", gkRate)

    # Calculate true goalkeeper rating: ratio of xG conceded to goals conceded
    gkPerf = round((OppaG - OppxG),2) 
    
    # Assign True Performance 
    if gkPerf > 0:
        perf = "Underperformed"

    elif gkPerf < 0: 
        perf = "Overperformed"

    else:
        perf = "On Par"    

    # Store all output in Pandas dataframe, to be uploaded to xG Stats spreadsheet
    gk_season = pd.DataFrame()

    gk_season['defPerf'] = [defPerf]
    gk_season['gkRate'] = [gkRate]
    gk_season['gkPerf'] = [gkPerf]
    gk_season['shotCon'] = [oppShots]
    gk_season['shotConOT'] = [onTarget]
    gk_season['OppaG'] = [OppaG]
    gk_season['OppxG'] = [OppxG]
    gk_season['Performance'] = [perf]

    return gk_season





