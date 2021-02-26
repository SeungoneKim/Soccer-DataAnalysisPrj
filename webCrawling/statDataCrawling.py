# statDataCrawling.py
# Yonsei Computer Science
# 2018147550 Seungone Kim
'''
 This .py code is implemented to perform Web Crawling to get the data needed for the project, and export it in a CSV file.
 Using the Selenium module, it opens the a remote controlled Chrome tab with webdriver.
 Then with the functions implemented in Selenium module, it scratches data and saves in a list.
 Then with the pandas module, it changes the whole data into DataFrame and then exports into a CSV File.
 Particularly this .py code gets data about the player's data from 5 leagues in 3 seasons, making 15 CSV Files.
 The CSV Files are already made and included in data folder.
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from pathlib import Path
from globals import idxToLeague, idxToSeason, idxToColumnTitle

driver = webdriver.Chrome("/Users/louisdebroglie/vscode_workspace/python_projects/python/project_2018147550/webCrawling/chromedriver")

# 1~3(past to present) general : age, appearances, minutes played, goals, assists, yellow cards, red cards, mom, avg rating
# 4~6(past to present) scoring : goal P90, non-penalty goal p90
# 7~9(past to present) shooting : shots, shots on target, shot accuracy
# 10~12(past to present) creation : big chances created, completed dribbles, crosses
# 13~15(past to present) passing : passes P90, passes completed %
# 16~18(past to present) disruption : touches, intercept
# 19~21(past to present) defending : tackles won %, aerials won %, duels won %
# 22~24(past to present) goalkeeping : clean sheets, saves made P90, penalty saves

# Information needed to get StatsData
# Premier League
urlPremierLeague = ['https://www.footballcritic.com/premier-league/season-2017-2018/player-stats/all/2/13294',
                    'https://www.footballcritic.com/premier-league/season-2018-2019/player-stats/all/2/16336', 'https://www.footballcritic.com/premier-league/season-2019-2020/player-stats/all/2/21558']

# La Liga
urlLaLiga = ['https://www.footballcritic.com/primera-division/season-2017-2018/player-stats/all/6/13478',
             'https://www.footballcritic.com/primera-division/season-2018-2019/player-stats/all/6/17112', 'https://www.footballcritic.com/primera-division/season-2019-2020/player-stats/all/6/22435']

# BundesLiga
urlBundesLiga = ['https://www.footballcritic.com/bundesliga/season-2017-2018/player-stats/all/3/13293',
                 'https://www.footballcritic.com/bundesliga/season-2018-2019/player-stats/all/3/16295', 'https://www.footballcritic.com/bundesliga/season-2019-2020/player-stats/all/3/21557']

# SerieA
urlSerieA = ['https://www.footballcritic.com/serie-a/season-2017-2018/player-stats/all/8/13348',
             'https://www.footballcritic.com/serie-a/season-2018-2019/player-stats/all/8/17845', 'https://www.footballcritic.com/serie-a/season-2019-2020/player-stats/all/8/22436']

# Ligue One
urlLigueOne = ['https://www.footballcritic.com/ligue-1/season-2017-2018/player-stats/all/4/13295',
               'https://www.footballcritic.com/ligue-1/season-2018-2019/player-stats/all/4/16810', 'https://www.footballcritic.com/ligue-1/season-2019-2020/player-stats/all/4/21586']

urlData = [urlPremierLeague, urlLaLiga, urlBundesLiga, urlSerieA, urlLigueOne]

rangePremierLeague = [21, 20, 21]
rangeLaLiga = [23, 22, 23]
rangeBundesLiga = [20, 19, 20]
rangeSerieA = [22, 22, 23]
rangeLigueOne = [22, 22, 22]

rangeData = [rangePremierLeague, rangeLaLiga,
             rangeBundesLiga, rangeSerieA, rangeLigueOne]

# Performing Web Crawling to get StatsData
for url in range(5):
    for season in range(3):
        players_data = []

        # Opening the remoted tab with get()
        driver.get(urlData[url][season])
        input()

        # mostly use find_elemnts_by_tag_name() method
        # finding the <tr> tag in HTML code
        for pageidx in range(rangeData[url][season]):
            tr_list = driver.find_elements_by_tag_name("tr")
            for tr in tr_list:
                # saving player's stats in player[] list (This list contains information of each individual player and will be appended to players_data later on)
                player = []
                tds = tr.find_elements_by_tag_name("td")
                skip = False
                for idx, td in enumerate(tds):
                    if idx in [0, 3]:
                        player.append(td.text)
                        print(td.text)
                print(player)
                if skip or len(player) < 2:
                    continue
                
                # looking for additional information
                crs = tr.find_elements_by_class_name("cr")
                print("CR", len(crs))
                for cr in crs:
                    if cr.get_attribute("textContent") == "":
                        continue
                    print("cr-", cr.get_attribute("textContent"))
                    player.append(cr.get_attribute("textContent"))
                
                # gettting nationality and team information : will later be used to compare with the data made from valueDataCrawling.py
                nat_and_team = []
                for idx, td in enumerate(tds):
                    if idx in [1, 2]:
                        print("data srt", td.get_attribute("data-sort"))
                        nat_and_team.append(td.get_attribute("data-sort"))
                player = [player[0]] + nat_and_team + player[1:]
                print(player)

                # appending player to players_data
                players_data.append(player)

                print("-"*10)

            # going to next page
            try:
                next_page = driver.find_element_by_xpath(
                    '//*[@id="DataTables_Table_0_next"]')
                driver.execute_script("arguments[0].click();", next_page)
                time.sleep(10)

            except Exception:
                pass

        # preprocessing the players_data
        preprocessed_players_data = []
        for i in range(len(players_data)):
            tmpplayer = []
            for colidx in idxToColumnTitle.keys():
                try:
                    tmpplayer.append(players_data[i][colidx])
                except IndexError:
                    pass

            preprocessed_players_data.append(tmpplayer)

        # generating a DataFrame with the preprocessed_players_data
        df = pd.DataFrame(data=preprocessed_players_data, index=[i for i in range(len(
            preprocessed_players_data))], columns=[idxToColumnTitle[member] for member in idxToColumnTitle])
        print("This is also done #################")

        # making csv file with the generated DataFrame
        filename = idxToLeague[url]+idxToSeason[season]+".csv"
        df.to_csv(filename, mode='w')
