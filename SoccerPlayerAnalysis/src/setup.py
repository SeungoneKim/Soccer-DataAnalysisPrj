from SoccerPlayerAnalysis.src.classHierarchy import Player
from SoccerPlayerAnalysis.src.globalInfo import *
import math

'''
# setting path
path = 'C:\VSCode_Workspace\DataAnalysis'
specificPath1 = "\data\ValueData"
specificPath2 = "\data\playerStats\\"
'''

# lists that will save stat data and will be used to compare in MakeDataBase() later on
bundesLigaPlayerStats=[]
premierLeaguePlayerStats=[]
laLigaPlayerStats=[]
serieAPlayerStats=[]
ligueOnePlayerStats=[]
PlayerStats=[bundesLigaPlayerStats,premierLeaguePlayerStats,laLigaPlayerStats,serieAPlayerStats,ligueOnePlayerStats]

# setting up playerStats : will be used later when making DataBase
def StatsFileProcess(path,specificPath2):
    for leagueidx in range(5):
        for seasonidx in range(3):
            PlayerStats[leagueidx].append([])
            playerStatsDataPath = path+specificPath2+idxToLeague[leagueidx]+idxToSeason[seasonidx]+".csv"
            playerStatsData = open(playerStatsDataPath,'r',encoding='UTF-8')
            for row in playerStatsData:
                PlayerStats[leagueidx][seasonidx].append(row.rstrip('\n'))


# setting up DataBase
def MakeDataBase(path,specificPath1,specificPath2):
    
    # this is important data : OBJECT THAT WILL BE RETURNED IN THE END OF THE FUNCTION
    DataBase={}

    StatsFileProcess(path,specificPath2)
    for idx in range(5):
        valueDataPath= path+specificPath1+'/playerinfo'+idxToLeague[idx]+'.csv'
        valuedata = open(valueDataPath,'r',encoding='UTF-8')
        key= firstkey[idx]
        for playerrow in valuedata:
            #print(key)
            if key == firstkey[idx]:
                key += 1
                continue

            player = playerrow.rstrip('\n').split(',')

            #print(player)

            for leagueidx in range(5):
                for seasonidx in range(3):
                    #print(key,leagueidx,seasonidx)
                    #print(player[1])

                    #print(key,leagueidx,seasonidx)
                    for iprow in PlayerStats[leagueidx][seasonidx]:
                        ip = iprow.split(',')
                        flg=False
                        for numbers in ip:
                            if numbers=='-':
                                flg=True
                                break
                        if flg is True:
                            continue
                        #print(ip)
                        #print(player[1].replace(" ","").replace("-","").lower().strip(),'###########', ip[1].replace(" ","").replace("-","").lower().strip(),'###########',idxToLeague[leagueidx],idxToSeason[seasonidx],'###########',valueDataPath)
                        
                        # Comparing the name, nationality and age to see if they are identical player
                        if (player[1].replace(" ","").lower().strip()== ip[1].replace(" ","").lower().strip()) and (player[6].replace(" ","").lower().strip()== ip[3].replace(" ","").lower().strip()) and ((int)(player[3])==(int)(ip[4])):
                            #print(key,"###",player[1].replace(" ","").replace("-","").lower().strip(),'###########', ip[1].replace(" ","").replace("-","").lower().strip(),'###########',idxToLeague[leagueidx],idxToSeason[seasonidx],'###########',valueDataPath,"###################",idxToLeague[leagueidx],idxToSeason[seasonidx])
                            #print(player)
                            #print(ip)
                            if key not in DataBase:
                                
                                DataBase[key]= Player(player[1],player[2],player[4],player[7],player[6],player[3])
                            #print(ip)
                            DataBase[key].addSeason(ip)
            
            #print(DataBase[player[0]])
            key = key+1
    deleteList=[]
    for itemt in DataBase:
        if len(DataBase[itemt].data)==0:
            deleteList.append(itemt)
        else:
            num= len(DataBase[itemt].data)
            flg=False
            for ss in range(num):
                if len(DataBase[itemt].data[ss])!=len(DataBase[itemt].data[0]):
                    flg=True
                    break
            if flg is True:
                deleteList.append(itemt)
            else:
                DataBase[itemt].makeAvgData()
        #print(itemt.getName(),end='')
        #print(itemt.getEstimatedValue(),end='')
        #print(itemt.getCurrentClub(),end='')
        #print(itemt.getNationality(),end='')
        #print(itemt.getAge(),end='')
        
        #print(itemt.avgdata)
    for idx in deleteList:
        del(DataBase[idx])

    return DataBase
    

def changeEstimatedValue(num):
    answ=0
    if num[-1]=='m':
        val= float(num[1:-1])
        answ= val*1000000
    else:
        val= float(num[1:-3])
        answ= val*1000
    return answ
    

def MakeSoccerData(DataBase):
    # dictionary that will be returned later on
    SoccerData= {}
    # name
    name=[]
    for player in DataBase.values():
        name.append(player.getName())
    SoccerData['name']=name
    # Estimated Value
    estimatedValue=[]
    for player in DataBase.values():
        estimatedValue.append(changeEstimatedValue(player.getEstimatedValue()))
    SoccerData['estimatedValue']=estimatedValue
    # Current Club
    currentClub=[]
    for player in DataBase.values():
        currentClub.append(player.getCurrentClub())
    SoccerData['currentClub']=currentClub
    # Nationality
    nationality=[]
    for player in DataBase.values():
        nationality.append(player.getNationality())
    SoccerData['nationality']=nationality
    # Age
    age=[]
    for player in DataBase.values():
        age.append(int(player.getAge()))
    SoccerData['age']=age
    # Other PlayerStats Data
    idx=5 # starting from playing time
    for item in ColumnListforSoccerData.values():

        SoccerData[item]=[]
        percentagevalueFlg=False
    
        if (DataBase[217].getInfoFromAvgData(idx))[-1]=='%':
            percentagevalueFlg=True

        for player in DataBase.values():
            if (player.getInfoFromAvgData(idx)=='-') or (player.getInfoFromAvgData(idx)==''):
                SoccerData[item].append(0.0)
            elif percentagevalueFlg is False:
                SoccerData[item].append(float(player.getInfoFromAvgData(idx)))
            else:
                val= player.getInfoFromAvgData(idx)
                val2 = val[:-1]
                SoccerData[item].append(float(val2))
        
        idx += 1
    
    return SoccerData

def MakeStrikerSoccerData(DataBase):
    # dictionary that will be returned later on
    StrikerSoccerData= {}
    # name
    name=[]
    for player in DataBase.values():
        if player.getPosition() in StrikerPositions:
            name.append(player.getName())
    StrikerSoccerData['name']=name
    # Estimated Value
    estimatedValue=[]
    for player in DataBase.values():
        if player.getPosition() in StrikerPositions:
            estimatedValue.append(changeEstimatedValue(player.getEstimatedValue()))
    StrikerSoccerData['estimatedValue']=estimatedValue
    # Current Club
    currentClub=[]
    for player in DataBase.values():
        if player.getPosition() in StrikerPositions:
            currentClub.append(player.getCurrentClub())
    StrikerSoccerData['currentClub']=currentClub
    # Nationality
    nationality=[]
    for player in DataBase.values():
        if player.getPosition() in StrikerPositions:
            nationality.append(player.getNationality())
    StrikerSoccerData['nationality']=nationality
    # Age
    age=[]
    for player in DataBase.values():
        if player.getPosition() in StrikerPositions:
            age.append(int(player.getAge()))
    StrikerSoccerData['age']=age
    # Other PlayerStats Data
    
    for itemidx in ColumnsforStriker.keys():
        StrikerSoccerData[ColumnsforStriker[itemidx]]=[]
        percentagevalueFlg=False
    
        if (DataBase[217].getInfoFromAvgData(itemidx+5))[-1]=='%':
            percentagevalueFlg=True

        for player in DataBase.values():
            if player.getPosition() in StrikerPositions:
                if (player.getInfoFromAvgData(itemidx+5)=='-') or (player.getInfoFromAvgData(itemidx+5)==''):
                    StrikerSoccerData[ColumnsforStriker[itemidx]].append(0.0)
                elif percentagevalueFlg is False:
                    StrikerSoccerData[ColumnsforStriker[itemidx]].append(float(player.getInfoFromAvgData(itemidx+5)))
                else:
                    val= player.getInfoFromAvgData(itemidx+5)
                    val2 = val[:-1]
                    StrikerSoccerData[ColumnsforStriker[itemidx]].append(float(val2))
        
        
    
    return StrikerSoccerData

def MakeMidfielderSoccerData(DataBase):
    # dictionary that will be returned later on
    MidfielderSoccerData= {}
    # name
    name=[]
    for player in DataBase.values():
        if player.getPosition() in MidfielderPositions:
            name.append(player.getName())
    MidfielderSoccerData['name']=name
    # Estimated Value
    estimatedValue=[]
    for player in DataBase.values():
        if player.getPosition() in MidfielderPositions:
            estimatedValue.append(changeEstimatedValue(player.getEstimatedValue()))
    MidfielderSoccerData['estimatedValue']=estimatedValue
    # Current Club
    currentClub=[]
    for player in DataBase.values():
        if player.getPosition() in MidfielderPositions:
            currentClub.append(player.getCurrentClub())
    MidfielderSoccerData['currentClub']=currentClub
    # Nationality
    nationality=[]
    for player in DataBase.values():
        if player.getPosition() in MidfielderPositions:
            nationality.append(player.getNationality())
    MidfielderSoccerData['nationality']=nationality
    # Age
    age=[]
    for player in DataBase.values():
        if player.getPosition() in MidfielderPositions:
            age.append(int(player.getAge()))
    MidfielderSoccerData['age']=age
    # Other PlayerStats Data
    
    for itemidx in ColumnsforMidfielder.keys():

        MidfielderSoccerData[ColumnsforMidfielder[itemidx]]=[]
        percentagevalueFlg=False
    
        if (DataBase[217].getInfoFromAvgData(itemidx+5))[-1]=='%':
            percentagevalueFlg=True

        for player in DataBase.values():
            if player.getPosition() in MidfielderPositions:
                if (player.getInfoFromAvgData(itemidx+5)=='-') or (player.getInfoFromAvgData(itemidx+5)==''):
                    MidfielderSoccerData[ColumnsforMidfielder[itemidx]].append(0.0)
                elif percentagevalueFlg is False:
                    MidfielderSoccerData[ColumnsforMidfielder[itemidx]].append(float(player.getInfoFromAvgData(itemidx+5)))
                else:
                    val= player.getInfoFromAvgData(itemidx+5)
                    val2 = val[:-1]
                    MidfielderSoccerData[ColumnsforMidfielder[itemidx]].append(float(val2))
        
        
    
    return MidfielderSoccerData

def MakeDefenderSoccerData(DataBase):
    # dictionary that will be returned later on
    DefenderSoccerData= {}
    # name
    name=[]
    for player in DataBase.values():
        if player.getPosition() in DefenderPositions:
            name.append(player.getName())
    DefenderSoccerData['name']=name
    # Estimated Value
    estimatedValue=[]
    for player in DataBase.values():
        if player.getPosition() in DefenderPositions:
            estimatedValue.append(changeEstimatedValue(player.getEstimatedValue()))
    DefenderSoccerData['estimatedValue']=estimatedValue
    # Current Club
    currentClub=[]
    for player in DataBase.values():
        if player.getPosition() in DefenderPositions:
            currentClub.append(player.getCurrentClub())
    DefenderSoccerData['currentClub']=currentClub
    # Nationality
    nationality=[]
    for player in DataBase.values():
        if player.getPosition() in DefenderPositions:
            nationality.append(player.getNationality())
    DefenderSoccerData['nationality']=nationality
    # Age
    age=[]
    for player in DataBase.values():
        if player.getPosition() in DefenderPositions:
            age.append(int(player.getAge()))
    DefenderSoccerData['age']=age
    # Other PlayerStats Data
    
    for itemidx in ColumnsforDefender.keys():

        DefenderSoccerData[ColumnsforDefender[itemidx]]=[]
        percentagevalueFlg=False
    
        if (DataBase[217].getInfoFromAvgData(itemidx+5))[-1]=='%':
            percentagevalueFlg=True

        for player in DataBase.values():
            if player.getPosition() in DefenderPositions:
                if (player.getInfoFromAvgData(itemidx+5)=='-') or (player.getInfoFromAvgData(itemidx+5)==''):
                    DefenderSoccerData[ColumnsforDefender[itemidx]].append(0.0)
                elif percentagevalueFlg is False:
                    DefenderSoccerData[ColumnsforDefender[itemidx]].append(float(player.getInfoFromAvgData(itemidx+5)))
                else:
                    val= player.getInfoFromAvgData(itemidx+5)
                    val2 = val[:-1]
                    DefenderSoccerData[ColumnsforDefender[itemidx]].append(float(val2))

    return DefenderSoccerData


def MakeGoalkeeperSoccerData(DataBase):
    # dictionary that will be returned later on
    GoalkeeperSoccerData= {}
    # name
    name=[]
    for player in DataBase.values():
        if player.getPosition() in GoalkeeperPositions:
            name.append(player.getName())
    GoalkeeperSoccerData['name']=name
    # Estimated Value
    estimatedValue=[]
    for player in DataBase.values():
        if player.getPosition() in GoalkeeperPositions:
            estimatedValue.append(changeEstimatedValue(player.getEstimatedValue()))
    GoalkeeperSoccerData['estimatedValue']=estimatedValue
    # Current Club
    currentClub=[]
    for player in DataBase.values():
        if player.getPosition() in GoalkeeperPositions:
            currentClub.append(player.getCurrentClub())
    GoalkeeperSoccerData['currentClub']=currentClub
    # Nationality
    nationality=[]
    for player in DataBase.values():
        if player.getPosition() in GoalkeeperPositions:
            nationality.append(player.getNationality())
    GoalkeeperSoccerData['nationality']=nationality
    # Age
    age=[]
    for player in DataBase.values():
        if player.getPosition() in GoalkeeperPositions:
            age.append(int(player.getAge()))
    GoalkeeperSoccerData['age']=age
    # Other PlayerStats Data
    
    for itemidx in ColumnsforGoalkeeper.keys():

        GoalkeeperSoccerData[ColumnsforGoalkeeper[itemidx]]=[]
        percentagevalueFlg=False
    
        if (DataBase[217].getInfoFromAvgData(itemidx+5))[-1]=='%':
            percentagevalueFlg=True

        for player in DataBase.values():
            if player.getPosition() in GoalkeeperPositions:
                if (player.getInfoFromAvgData(itemidx+5)=='-') or (player.getInfoFromAvgData(itemidx+5)==''):
                    GoalkeeperSoccerData[ColumnsforGoalkeeper[itemidx]].append(0.0)
                elif percentagevalueFlg is False:
                    GoalkeeperSoccerData[ColumnsforGoalkeeper[itemidx]].append(float(player.getInfoFromAvgData(itemidx+5)))
                else:
                    val= player.getInfoFromAvgData(itemidx+5)
                    val2 = val[:-1]
                    GoalkeeperSoccerData[ColumnsforGoalkeeper[itemidx]].append(float(val2))
        
        
    
    return GoalkeeperSoccerData


   
 