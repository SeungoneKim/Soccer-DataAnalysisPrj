==================================================================================CONTENTS==================================================================================

1. SoccerPlayerAnalysis

This directory is a module containing all the data and source code needed for the project.

1-1)
The 'data' directory consists of 15+5 CSV files.
The 15 CSV files contained in 'playerStats' are sourced from  https://www.footballcritic.com/
The 5 CSV files contained in 'valueData' are sourced from  https://www.transfermarkt.com/
The data was web crawled using Selenium module with the code in 'webCrawling' directory.

1-2)
The 'src' directory consists of 4 .py files.
'algorithms.py' has 6 functions included. These functions are used in the Statisical Analysis of the project.
'classHierarchy.py' has 1 class implemented. This class is used in setup.py to make up the DataBase data structure needed when gathering and preprocessing the player data.
'globalInfo.py' has 4 lists, 6 dictionaries, and 4 sets included. These contain information that will be used when iterating through the data in 'algorithms.py' and 'setup.py'.
'setup.py' has 8 functions included. These functions are used when making up the datastructure 'Database' and 'SoccerPlayerdata'. It includes functions that preprocess data.

1-3) 
The 'test.py' is the user interface of the project.
It is imported in 'main.py' and then demonstrates the project in CLI.
It asks for the absolute path of the directory.

PLEASE READ THIS PART,
CAUTION : PLEASE MAKE SURE YOU ENTERED THE ABSOLUTE PATH OF 'project_2018147550'


2. WebCrawling

2-1)
'statDataCrawling.py' is a .py file that performs Web Crawling from https://www.footballcritic.com/

It generates 15 CSV files from 5 leagues in 3 seasons. This code was already executed and the CSV files were moved to 'data' directory in SoccerPlayerAnalysis.

2-2)
'valueDataCrawling.py' is a .py file that performs Web Crawling from https://www.transfermarkt.com/

It generates 5 CSV files from 5 leagues. This code was already executed and the CSV files were moved to 'data' directory in SoccerPlayerAnalysis.


3. main.py

This .py file is going to be executed during the demonstration of CSI2100-01.

It uses the module 'SoccerPlayerAnalysis'.

Specifically, it imports SoccerPlayerAnalysis.test which has the user interface code included.

4. README.txt

It is this textfile.


==================================================================================INSTALL==================================================================================

1. SoccerPlayerAnalysis

These are the list of libraries and moudles contained in SoccerPlayerAnalysis,
Please use,

pip3 install 

to download the modules that are not downloaded in your environment.

###############################################################################
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor 
import math
###############################################################################

2. webCrawling

These are the list of libraries and moudles contained in SoccerPlayerAnalysis,
Please use,

pip3 install 

to download the modules that are not downloaded in your environment.

###############################################################################
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
###############################################################################


Also, you to execute the code statDataCrawling.py and valueDataCrawling.py, you need to have a Chrome driver downloaded and included in your directory.

1) Please go to  https://chromedriver.chromium.org
2) Download the chrome driver that matches your operating system and your chrome version.
3) PLEASE EXECUTE THE CHROME DRIVER YOU DOWNLOADED AT LEAST ONCE.
4) Move the chrome driver into the webCrawling directory.
5) In statDataCrawling.py and valueDataCrawling.py, change the absolute path of the Chrome driver.

PLEASE READ THIS PART,
Because of these reasons, I found that executing statDataCrawling.py and valueDataCrawling.py are not applicable with the whole project.
It does not matter much because we just need the 15+5 CSV files made with this code.
However to show what I have done for the project, I included the code anyways.

==================================================================================HOW TO USE==================================================================================

Please do not change the positions of any directory or file.

PLEASE EXECUTE main.py to see the results of the project.

PLEASE type in the correct ABSOLUTE PATH of 'project_2018147550' inside your computer when executing main.py

Please check you did all the INSTALLS you need to do. (List of modules or libraires used are listed above in INSTALLS.)

When you execute statDataCrawling.py and valueDataCrawling.py to see how the Web Crawling was performed, please check the INSTALLS above.