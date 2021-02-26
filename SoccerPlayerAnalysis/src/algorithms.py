import SoccerPlayerAnalysis.src.setup as setup
import SoccerPlayerAnalysis.src.globalInfo as globalInfo
from SoccerPlayerAnalysis.src.classHierarchy import Player
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor 
import math

def generateDataFrame(SoccerData):
        colList=[]
        
        for items in SoccerData.keys():
            colList.append(items)

        df= pd.DataFrame(SoccerData,columns=colList)
        return df

def showFigure(SoccerData,dependentVariable,independentVariable):
        df = generateDataFrame(SoccerData)

        ax = sns.regplot(x=independentVariable,y=dependentVariable,data=df,scatter_kws={"color":"black"},line_kws={"color":"red"})
        plt.title('Relationship between '+independentVariable+' and '+dependentVariable, color='red')
        plt.xlabel(independentVariable,fontsize=12)
        plt.ylabel(dependentVariable,fontsize=12)
        plt.grid(True)
        plt.show()

def SingleVariableLinearRegression(SoccerData,dependentVariable,independentVariable,showSummary):

    df = generateDataFrame(SoccerData)
    df = df.drop(["name","currentClub","nationality"],axis=1)
    df = df[np.isfinite(df).all(1)]

    target= df[[independentVariable]]
    x_data_pre= df[[dependentVariable]]

    x_data = sm.add_constant(x_data_pre,has_constant="add")

    model= sm.OLS(target.astype(np.float64), x_data.astype(np.float64))
    fitted_model= model.fit()

    if showSummary is True:
        print(fitted_model.summary())

    return fitted_model.rsquared_adj

def FindDominantVariable(SoccerData,dependentVariables,independentVariable):
    Adj_Rsquared_values={}
    for item in dependentVariables.values():
        
        Adj_Rsquared_values[item]= SingleVariableLinearRegression(SoccerData,item,independentVariable,False)
    
    Adj_Rsquared_values_view = [(value,key) for key,value in Adj_Rsquared_values.items()]
    Adj_Rsquared_values_view.sort(reverse=True)
    print("independent variable and it's Adjusted R-Squared Value is, (in order)")
    for value,key in Adj_Rsquared_values_view:
        print(key,":",value)
    
def showColinearity(SoccerData,dependentVariables):
    df = generateDataFrame(SoccerData)

    dependentVariablesList = []
    for item in dependentVariables.values():
        dependentVariablesList.append(item)

    x_data = df[dependentVariablesList]
    x_data = sm.add_constant(x_data, has_constant= "add")
    
    print(x_data.corr())

    cmap = sns.light_palette("darkgray", as_cmap = True)  
    sns.heatmap(x_data.corr(), annot = True, cmap = cmap)
    plt.show()


def MultiVariateLinearRegression(SoccerData,dependentVariable,independentVariables):
    df = generateDataFrame(SoccerData)
    df = df.drop(["name","currentClub","nationality"],axis=1)
    df = df[np.isfinite(df).all(1)]

    x_data_colList=[]
    if type(independentVariables) is list:
        x_data_colList= independentVariables
    elif type(independentVariables) is dict:
        for element in independentVariables.values():
            x_data_colList.append(element)

    y_data_colList=[dependentVariable]
    
    x_data= df[x_data_colList]
    x_data.head()
    x_data = sm.add_constant(x_data, has_constant="add")
    
    y_data= df[y_data_colList]
    y_data.head()
    
    # OLS Statistical Test
    multimodel = sm.OLS(y_data,x_data)
    fitted_multimodel = multimodel.fit()
    print_fitted_multimodel = fitted_multimodel.summary()
    print(print_fitted_multimodel)
