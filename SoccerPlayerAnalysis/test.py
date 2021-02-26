import SoccerPlayerAnalysis.src.setup as setup
from SoccerPlayerAnalysis.src.algorithms import *
import SoccerPlayerAnalysis.src.classHierarchy as classHierarchy
import SoccerPlayerAnalysis.src.globalInfo as globalInfo

def performAnalysis():
    print('##########################################')
    print()
    print('Welcome to Soccer Player Analysis Project.')
    print()
    print('##########################################')
    print()
    print('This project is built to answer the question of,')
    print('"Is the number of goals and assists the most important aspect that determines the estimated value of a soccer player?"')
    print()
    print('The data used in this project was Web Crawled from https://www.footballcritic.com and https://www.transfermarkt.com')
    print()
    print('The copyright of all the code in this project belongs to Seungone Kim')
    print('Yonsei University Computer Science 2018147550')
    print()
    print('###################################################################')
    print('Please type in the absolute path of this folder, "project_2018147550" inside your computer.')
    print()
    print('Example of absolute path : "/Users/louisdebroglie/vscode_workspace/python_projects/python/project_2018147550"')
    print('Please be cautious with typing your absolute path. PLEASE CHECK "/" are typed correctly and not included after 2018147550')
    print()
    path = input('The relative path is : ')
    specificPath1 = "/SoccerPlayerAnalysis/data/ValueData"
    specificPath2 = "/SoccerPlayerAnalysis/data/playerStats/"
    specificPath3 = "/SoccerPlayerAnalysis/src/"
    print()
    print('WARNING : We assume you wrote the correct relative path. If not, please end the program and restart please.')
    print('###################################################################')
    # Building a databse and soccerdata that will be used through out the program
    print('Building database...')
    print('This may take a few seconds. Please wait.')
    database= setup.MakeDataBase(path,specificPath1,specificPath2)
    soccerdata= setup.MakeSoccerData(database)
    soccerstrikerdata= setup.MakeStrikerSoccerData(database)
    soccermidfielderdata= setup.MakeMidfielderSoccerData(database)
    soccerdefenderdata= setup.MakeDefenderSoccerData(database)
    soccergoalkeeperdata= setup.MakeGoalkeeperSoccerData(database)

    # Global variable and list that will determine whether to terminate program and check if the user input if valid.
    endflg=False
    available_options_group=['a','b','c','d','e','q']
    available_options_task=['1','2','3','4','5','6','q']

    while endflg is False:
        print('###################################################################')
        print('Please choose the group of players you wish to Analysis.(Case Sensitive)')
        print()
        print('Press "a" to analyze all players in data.')
        print('Press "b" to specifically analyze Strikers.')
        print('Press "c" to specifically analyze Midfielders.')
        print('Press "d" to specifically analyze Defenders.')
        print('Press "e" to specifically analyze Goalkeepers.')
        print('Press "q" if you wish to end the program.')
        print()
        print('ALARM : You may later on choose another group.')
        print()
        grouptoAnalyze = input('Your input is : ')
        while True:
            if grouptoAnalyze not in available_options_group:
                print('###################################################################')
                print('MisType detected. Please Type again.')
                print()
                grouptoAnalyze = input('Your input is : ')
                print()
                continue
            else:
                break
        if grouptoAnalyze=='q':
            print('End of program.')
            endflg=True
            break
        print('###################################################################')
        print('Press the following number on the prompt to perform a certain task.(Case Sensitive)')
        print()
        print('Press "1" to see the Analysis results of "What is the most important aspect of the group I choosed?"')
        print('Press "2" to see the Analysis results of "How strong relationship does a certain independent variable have with the dependent variable?"')
        print('Press "3" to see the Figure explaining "How strong relationship a certain independent variable has with the dependent variable"')
        print('Press "4" to see the relationship between dependent variables of the group you choosed.')
        print('Press "5" to see the Analysis results of "How strong relationship does all of the independent variable have with the dependent variable?"')
        print('Press "6" to see the difference between the group you choosed and the other groups.')
        print('Press "q" if you wish to end the program.')
        print()
        print('ALARM : You may later on choose another group.')
        print()
        task_number= input('Your input is : ')
        print()
        print('###################################################################')
        while True:
            if task_number not in available_options_task:
                print('###################################################################')
                print('Mistype detected. Please Type again.')
                print()
                task_number= input('Your input is : ')
                print()
                continue
            else:
                break
        if task_number=='q':
            print('End of program.')
            endflg=True
            break
        print()
        print()
        
        # Performing FindDominantVariable() from algorithms.py
        if task_number=='1':
            print('###################################################################')
            print()
            if grouptoAnalyze=='a':
                FindDominantVariable(soccerdata,globalInfo.ColumnListforSoccerData,'estimatedValue')
            elif grouptoAnalyze=='b':
                FindDominantVariable(soccerstrikerdata,globalInfo.ColumnsforStriker,'estimatedValue')
            elif grouptoAnalyze=='c':
                FindDominantVariable(soccermidfielderdata,globalInfo.ColumnsforMidfielder,'estimatedValue')
            elif grouptoAnalyze=='d':
                FindDominantVariable(soccerdefenderdata,globalInfo.ColumnsforDefender,'estimatedValue')
            else: # grouptoAnalyze=='e'
                FindDominantVariable(soccergoalkeeperdata,globalInfo.ColumnsforGoalkeeper,'estimatedValue')
            print()
            print('###################################################################')
            print()
        # Performing SingleVariableLinearRegression from algorithms.py
        elif task_number=='2':
            print('The following is a list of independent variables you may use.')
            if grouptoAnalyze=='a':
                for idx in globalInfo.ColumnListforSoccerData:
                    print(globalInfo.ColumnListforSoccerData[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnListforSoccerData.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                print('###################################################################')
                print()
                SingleVariableLinearRegression(soccerdata,'estimatedValue',independentVariable,True)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='b':
                for idx in globalInfo.ColumnsforStriker:
                    print(globalInfo.ColumnsforStriker[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforStriker.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                print('###################################################################')
                print()
                SingleVariableLinearRegression(soccerstrikerdata,'estimatedValue',independentVariable,True)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='c':
                for idx in globalInfo.ColumnsforMidfielder:
                    print(globalInfo.ColumnsforMidfielder[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforMidfielder.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                print('###################################################################')
                print()
                SingleVariableLinearRegression(soccermidfielderdata,'estimatedValue',independentVariable,True)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='d':
                for idx in globalInfo.ColumnsforDefender:
                    print(globalInfo.ColumnsforDefender[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforDefender.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                print('###################################################################')
                print()
                SingleVariableLinearRegression(soccerdefenderdata,'estimatedValue',independentVariable,True)
                print()
                print('###################################################################')
                print()
            else: # grouptoAnalyze=='e'
                for idx in globalInfo.ColumnsforGoalkeeper:
                    print(globalInfo.ColumnsforGoalkeeper[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforGoalkeeper.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                print('###################################################################')
                print()
                SingleVariableLinearRegression(soccergoalkeeperdata,'estimatedValue',independentVariable,True)
                print()
                print('###################################################################')
                print()

        # Performing showFigure() from algorithms.py
        elif task_number=='3':
            print('The following is a list of independent variables you may use.')
            if grouptoAnalyze=='a':
                for idx in globalInfo.ColumnListforSoccerData:
                    print(globalInfo.ColumnListforSoccerData[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnListforSoccerData.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                showFigure(soccerdata,'estimatedValue',independentVariable)
            elif grouptoAnalyze=='b':
                for idx in globalInfo.ColumnsforStriker:
                    print(globalInfo.ColumnsforStriker[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforStriker.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                showFigure(soccerstrikerdata,'estimatedValue',independentVariable)
            elif grouptoAnalyze=='c':
                for idx in globalInfo.ColumnsforMidfielder:
                    print(globalInfo.ColumnsforMidfielder[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforMidfielder.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                showFigure(soccermidfielderdata,'estimatedValue',independentVariable)
            elif grouptoAnalyze=='d':
                for idx in globalInfo.ColumnsforDefender:
                    print(globalInfo.ColumnsforDefender[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforDefender.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                showFigure(soccerdefenderdata,'estimatedValue',independentVariable)
            else: # grouptoAnalyze=='e'
                for idx in globalInfo.ColumnsforGoalkeeper:
                    print(globalInfo.ColumnsforGoalkeeper[idx])
                print()
                independentVariable = input('Your input is : ')
                while True:
                    if independentVariable not in globalInfo.ColumnsforGoalkeeper.values():
                        print('Mistype detected. Please Type again.')
                        independentVariable = input('Your input is : ')
                        continue
                    else:
                        break
                showFigure(soccergoalkeeperdata,'estimatedValue',independentVariable)
        
        # Performing showColinearity() in algorithms.py
        elif task_number=='4':
            print('The following is a list of independent variables used to check the colinearity.')
            if grouptoAnalyze=='a':
                for idx in globalInfo.ColumnListforSoccerData:
                    print(globalInfo.ColumnListforSoccerData[idx])
                showColinearity(soccerdata,globalInfo.ColumnListforSoccerData)
            elif grouptoAnalyze=='b':
                for idx in globalInfo.ColumnsforStriker:
                    print(globalInfo.ColumnsforStriker[idx])
                showColinearity(soccerstrikerdata,globalInfo.ColumnsforStriker)
            elif grouptoAnalyze=='c':
                for idx in globalInfo.ColumnsforMidfielder:
                    print(globalInfo.ColumnsforMidfielder[idx])
                showColinearity(soccermidfielderdata,globalInfo.ColumnsforMidfielder)
            elif grouptoAnalyze=='d':
                for idx in globalInfo.ColumnsforDefender:
                    print(globalInfo.ColumnsforDefender[idx])
                showColinearity(soccerdefenderdata,globalInfo.ColumnsforDefender)
            else: # grouptoAnalyze=='e'
                for idx in globalInfo.ColumnsforGoalkeeper:
                    print(globalInfo.ColumnsforGoalkeeper[idx])
                showColinearity(soccergoalkeeperdata,globalInfo.ColumnsforGoalkeeper)
        
        # Performing MultiVariateLinearRegression() in algorithms.py
        elif task_number=='5':
            print('The following is a list of independent variables used in the analysis.')
            if grouptoAnalyze=='a':
                for idx in globalInfo.ColumnListforSoccerData:
                    print(globalInfo.ColumnListforSoccerData[idx])
                print('###################################################################')
                print()
                MultiVariateLinearRegression(soccerdata,'estimatedValue',globalInfo.ColumnListforSoccerData)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='b':
                for idx in globalInfo.ColumnsforStriker:
                    print(globalInfo.ColumnsforStriker[idx])
                print('###################################################################')
                print()
                MultiVariateLinearRegression(soccerstrikerdata,'estimatedValue',globalInfo.ColumnsforStriker)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='c':
                for idx in globalInfo.ColumnsforMidfielder:
                    print(globalInfo.ColumnsforMidfielder[idx])
                print('###################################################################')
                print()
                MultiVariateLinearRegression(soccermidfielderdata,'estimatedValue',globalInfo.ColumnsforMidfielder)
                print()
                print('###################################################################')
                print()
            elif grouptoAnalyze=='d':
                for idx in globalInfo.ColumnsforDefender:
                    print(globalInfo.ColumnsforDefender[idx])
                print('###################################################################')
                print()
                MultiVariateLinearRegression(soccerdefenderdata,'estimatedValue',globalInfo.ColumnsforDefender)
                print()
                print('###################################################################')
                print()
            else: # grouptoAnalyze=='e'
                for idx in globalInfo.ColumnsforGoalkeeper:
                    print(globalInfo.ColumnsforGoalkeeper[idx])
                print('###################################################################')
                print()
                MultiVariateLinearRegression(soccergoalkeeperdata,'estimatedValue',globalInfo.ColumnsforGoalkeeper)
                print()
                print('###################################################################')
                print()
        
        # Performing FindDominantVariable() among all groups
        else: # task_number=='6':
            print('##########################################################################')
            print('This is result of all groups of players')
            print()
            FindDominantVariable(soccerdata,globalInfo.ColumnListforSoccerData,'estimatedValue')
            print()
            print()
            MultiVariateLinearRegression(soccerdata,'estimatedValue',globalInfo.ColumnListforSoccerData)
            print()
            print('##########################################################################')
            print('This is result of strikers')
            print()
            FindDominantVariable(soccerstrikerdata,globalInfo.ColumnsforStriker,'estimatedValue')
            print()
            print()
            MultiVariateLinearRegression(soccerstrikerdata,'estimatedValue',globalInfo.ColumnsforStriker)
            print()
            print('##########################################################################')
            print('This is result of midfielders')
            print()
            FindDominantVariable(soccermidfielderdata,globalInfo.ColumnsforMidfielder,'estimatedValue')
            print()
            print()
            MultiVariateLinearRegression(soccermidfielderdata,'estimatedValue',globalInfo.ColumnsforMidfielder)
            print()
            print('##########################################################################')
            print('This is result of defenders')
            print()
            FindDominantVariable(soccerdefenderdata,globalInfo.ColumnsforDefender,'estimatedValue')
            print()
            print()
            MultiVariateLinearRegression(soccerdefenderdata,'estimatedValue',globalInfo.ColumnsforDefender)
            print()
            print('##########################################################################')
            print('This is result of goalkeepers')
            print()
            FindDominantVariable(soccergoalkeeperdata,globalInfo.ColumnsforGoalkeeper,'estimatedValue')
            print()
            print()
            MultiVariateLinearRegression(soccergoalkeeperdata,'estimatedValue',globalInfo.ColumnsforGoalkeeper)
            print()
            print('##########################################################################')

    print()
    print('##########################################')
    print()
    print('Thank you for using Soccer Player Analysis Project.')
    print()
    print('##########################################')