# valueDataCrawling.py
# Yonsei Computer Science
# 2018147550 Seungone Kim
'''
 This .py code is implemented to perform Web Crawling to get the data needed for the project, and export it in a CSV file.
 Using the Selenium module, it opens the a remote controlled Chrome tab with webdriver.
 Then with the functions implemented in Selenium module, it scratches data and saves in a list.
 Then with the pandas module, it changes the whole data into DataFrame and then exports into a CSV File.
 Particularly this .py code gets data about the player's estimated Value from transfermarkt.com, from 5 leagues in Europe.
 The CSV Files are already made and included in data folder.
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
even_data = []
odd_data = []
driver = webdriver.Chrome("/Users/louisdebroglie/vscode_workspace/python_projects/python/project_2018147550/webCrawling/chromedriver")

# information needed to get valueData
url_bundesLiga = "https://www.transfermarkt.com/spieler-statistik/marktwertAenderungen/marktwertetop/?plus=0&galerie=0&position=alle&spielerposition_id=0&spieler_land_id=0&verein_land_id=&wettbewerb_id=L1&alter=16+-+45&filtern_nach_alter=16%3B45&minAlter=16&maxAlter=45&minMarktwert=100.000&maxMarktwert=180.000.000&yt0=Show"
url_premierLeague = "https://www.transfermarkt.com/spieler-statistik/marktwertAenderungen/marktwertetop/?plus=0&galerie=0&position=alle&spielerposition_id=0&spieler_land_id=0&verein_land_id=&wettbewerb_id=GB1&alter=16+-+45&filtern_nach_alter=16%3B45&minAlter=16&maxAlter=45&minMarktwert=100.000&maxMarktwert=180.000.000&yt0=Show"
url_serieA = "https://www.transfermarkt.com/spieler-statistik/marktwertAenderungen/marktwertetop/?plus=0&galerie=0&position=alle&spielerposition_id=0&spieler_land_id=0&verein_land_id=&wettbewerb_id=IT1&alter=16+-+45&filtern_nach_alter=16%3B45&minAlter=16&maxAlter=45&minMarktwert=100.000&maxMarktwert=180.000.000&yt0=Show"
url_ligueOne = "https://www.transfermarkt.com/spieler-statistik/marktwertAenderungen/marktwertetop/?plus=0&galerie=0&position=alle&spielerposition_id=0&spieler_land_id=0&verein_land_id=&wettbewerb_id=FR1&alter=16+-+45&filtern_nach_alter=16%3B45&minAlter=16&maxAlter=45&minMarktwert=100.000&maxMarktwert=180.000.000&yt0=Show"
url_laLiga = "https://www.transfermarkt.com/spieler-statistik/marktwertAenderungen/marktwertetop/?plus=0&galerie=0&position=alle&spielerposition_id=0&spieler_land_id=0&verein_land_id=&wettbewerb_id=ES1&alter=16+-+45&filtern_nach_alter=16%3B45&minAlter=16&maxAlter=45&minMarktwert=100.000&maxMarktwert=180.000.000&yt0=Show"
range_bundesLiga = 9
range_primerLeague = 6
range_serieA = 8
range_ligueOne = 7
range_laLiga = 8

# Using url_bundesLiga to fill playerinfobundesLiga.csv
# Opening the remoted tab with get()
driver.get(url_bundesLiga)
for i in range(range_bundesLiga):
    pages = driver.find_elements_by_class_name("page")
    next_page = pages[i].find_element_by_tag_name("a")
    next_page.click()
    time.sleep(4)
    # finding the even class to get player's information
    even = driver.find_elements_by_class_name("even")
    for e in even:
        p_data = e.text.split()
        # preprocessing the name information (Length of name differs)
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = e.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = e.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = e.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to even_data list.
        even_data.append(p_data)
    # finding the odd class to get player's information
    odd = driver.find_elements_by_class_name("odd")
    for o in odd:
        p_data = o.text.split()
        # preprocessing the name information (Length of name differs)
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = o.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = o.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = o.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to odd_data list.
        odd_data.append(p_data)
    time.sleep(4)

# This is the list that we will append the player information saved in odd_data and even_data
total_data = []
for i in range(len(odd_data)): # odd_data and even_data have the same length
    try:
        if len(odd_data[i]) > 7:
            print(odd_data[i])
            overflow = ""
            for j in range(len(odd_data[i][6:])):
                overflow += odd_data[i][6+j]
            odd_data[i] = odd_data[i][0:6] + [overflow]
        if len(even_data[i]) > 7:
            print(even_data[i])
            overflow = ""
            for j in range(len(even_data[i][6:])):
                overflow += even_data[i][6+j]
            even_data[i] = even_data[i][0:6] + [overflow]
        # appending the data
        total_data.append(odd_data[i])
        total_data.append(even_data[i])
    except IndexError:
        pass

# generating a DataFrame using the total_data
df = pd.DataFrame(data=total_data, index=[i for i in range(len(total_data))], columns=[
                  "name", "position", "age", "value", "changed", "nat", "club"])
# generating a CSV file using the dataframe
df.to_csv("playerinfobundesLiga.csv")

# initializing the even_data and odd_data to get player info from the next league
even_data = []
odd_data = []

# Using url_primerLeague to fill playerinfoPrimerLeague.csv
# Opening the remoted tab with get()
driver.get(url_premierLeague)
for i in range(range_primerLeague):
    pages = driver.find_elements_by_class_name("page")
    next_page = pages[i].find_element_by_tag_name("a")
    next_page.click()
    time.sleep(4)
    # finding the even class to get player's information
    even = driver.find_elements_by_class_name("even")
    for e in even:
        p_data = e.text.split()
        # preprocessing the name information (Length of name differs)
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = e.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = e.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = e.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to even_data list.
        even_data.append(p_data)
    # finding the odd class to get player's information
    odd = driver.find_elements_by_class_name("odd")
    for o in odd:
        p_data = o.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = o.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = o.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = o.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to odd_data list.
        odd_data.append(p_data)

    time.sleep(4)
# This is the list that we will append the player information saved in odd_data and even_data
total_data = []
for i in range(len(odd_data)): # odd_data and even_data have the same length
    try:
        if len(odd_data[i]) > 7:
            print(odd_data[i])
            overflow = ""
            for j in range(len(odd_data[i][6:])):
                overflow += odd_data[i][6+j]
            odd_data[i] = odd_data[i][0:6] + [overflow]
        if len(even_data[i]) > 7:
            print(even_data[i])
            overflow = ""
            for j in range(len(even_data[i][6:])):
                overflow += even_data[i][6+j]
            even_data[i] = even_data[i][0:6] + [overflow]
        # appending the data
        total_data.append(odd_data[i])
        total_data.append(even_data[i])
    except IndexError:
        pass
# generating a DataFrame using the total_data
df = pd.DataFrame(data=total_data, index=[i for i in range(len(total_data))], columns=[
                  "name", "position", "age", "value", "changed", "nat", "club"])
# generating a CSV file using the dataframe
df.to_csv("playerinfopremierLeague.csv")

# initializing the even_data and odd_data to get player info from the next league
even_data = []
odd_data = []


# Using url_serieA to fill playerinfoSerieA.csv
# Opening the remoted tab with get()
driver.get(url_serieA)
for i in range(range_serieA):
    pages = driver.find_elements_by_class_name("page")
    next_page = pages[i].find_element_by_tag_name("a")
    next_page.click()
    time.sleep(4)
    # finding the even class to get player's information
    even = driver.find_elements_by_class_name("even")
    for e in even:
        p_data = e.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = e.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = e.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = e.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to even_data list.
        even_data.append(p_data)
    # finding the odd class to get player's information
    odd = driver.find_elements_by_class_name("odd")
    for o in odd:
        p_data = o.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = o.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = o.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = o.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        # saving information of each player to odd_data list.
        odd_data.append(p_data)
    time.sleep(4)

# This is the list that we will append the player information saved in odd_data and even_data
total_data = []
for i in range(len(odd_data)): # odd_data and even_data have the same length
    try:
        if len(odd_data[i]) > 7:
            print(odd_data[i])
            overflow = ""
            for j in range(len(odd_data[i][6:])):
                overflow += odd_data[i][6+j]
            odd_data[i] = odd_data[i][0:6] + [overflow]
        if len(even_data[i]) > 7:
            print(even_data[i])
            overflow = ""
            for j in range(len(even_data[i][6:])):
                overflow += even_data[i][6+j]
            even_data[i] = even_data[i][0:6] + [overflow]
        # appending the data
        total_data.append(odd_data[i])
        total_data.append(even_data[i])
    except IndexError:
        pass
# generating a DataFrame using the total_data
df = pd.DataFrame(data=total_data, index=[i for i in range(len(total_data))], columns=[
                  "name", "position", "age", "value", "changed", "nat", "club"])
# generating a CSV file using the dataframe
df.to_csv("playerinfoSerieA.csv")

# initializing the even_data and odd_data to get player info from the next league
even_data = []
odd_data = []


# Using url_ligueOne to fill playerinfoLigueOne.csv
# Opening the remoted tab with get()
driver.get(url_ligueOne)
for i in range(range_ligueOne):
    pages = driver.find_elements_by_class_name("page")
    next_page = pages[i].find_element_by_tag_name("a")
    next_page.click()
    time.sleep(4)
    # finding the even class to get player's information
    even = driver.find_elements_by_class_name("even")
    for e in even:
        p_data = e.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = e.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = e.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = e.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to even_data list.
        even_data.append(p_data)
    # finding the odd class to get player's information
    odd = driver.find_elements_by_class_name("odd")
    for o in odd:
        p_data = o.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = o.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = o.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = o.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to odd_data list.
        odd_data.append(p_data)
    time.sleep(4)

# This is the list that we will append the player information saved in odd_data and even_data
total_data = []
for i in range(len(odd_data)):
    try:
        if len(odd_data[i]) > 7:
            print(odd_data[i])
            overflow = ""
            for j in range(len(odd_data[i][6:])):
                overflow += odd_data[i][6+j]
            odd_data[i] = odd_data[i][0:6] + [overflow]
        if len(even_data[i]) > 7:
            print(even_data[i])
            overflow = ""
            for j in range(len(even_data[i][6:])):
                overflow += even_data[i][6+j]
            even_data[i] = even_data[i][0:6] + [overflow]
        # appending the data
        total_data.append(odd_data[i])
        total_data.append(even_data[i])
    except IndexError:
        pass
# generating a DataFrame using the total_data
df = pd.DataFrame(data=total_data, index=[i for i in range(len(total_data))], columns=[
                  "name", "position", "age", "value", "changed", "nat", "club"])
# generating a CSV file using the dataframe
df.to_csv("playerinfoLigueOne.csv")

# initializing the even_data and odd_data to get player info from the next league
even_data = []
odd_data = []


# Using url_laLiga to fill playerinfolaLiga.csv
# Opening the remoted tab with get()
driver.get(url_laLiga)
for i in range(range_laLiga):
    pages = driver.find_elements_by_class_name("page")
    next_page = pages[i].find_element_by_tag_name("a")
    next_page.click()
    time.sleep(4)
    # finding the even class to get player's information
    even = driver.find_elements_by_class_name("even")
    for e in even:
        p_data = e.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = e.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = e.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = e.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to even_data list.
        even_data.append(p_data)
    # finding the odd class to get player's information
    odd = driver.find_elements_by_class_name("odd")
    for o in odd:
        p_data = o.text.split()
        p_data = [p_data[0]+p_data[1]] + p_data[2:]
        if len(p_data) == 6:
            p_data = [p_data[0]] + [p_data[1]+p_data[2]] + p_data[3:]
        c = o.find_element_by_class_name("flaggenrahmen")
        p_data.append(c.get_property("title"))
        try:
            t = o.find_element_by_class_name(
                "vereinprofil_tooltip.tooltipstered")
        except NoSuchElementException:
            t = o.find_element_by_class_name("vereinprofil_tooltip")
        t = t.find_element_by_tag_name("img")
        p_data.append(t.get_property("alt"))
        print(p_data)
        # saving information of each player to odd_data list.
        odd_data.append(p_data)
    time.sleep(4)

# This is the list that we will append the player information saved in odd_data and even_data
total_data = []
for i in range(len(odd_data)):
    try:
        if len(odd_data[i]) > 7:
            print(odd_data[i])
            overflow = ""
            for j in range(len(odd_data[i][6:])):
                overflow += odd_data[i][6+j]
            odd_data[i] = odd_data[i][0:6] + [overflow]
        if len(even_data[i]) > 7:
            print(even_data[i])
            overflow = ""
            for j in range(len(even_data[i][6:])):
                overflow += even_data[i][6+j]
            even_data[i] = even_data[i][0:6] + [overflow]
        # appending the data
        total_data.append(odd_data[i])
        total_data.append(even_data[i])
    except IndexError:
        pass
# generating a DataFrame using the total_data
df = pd.DataFrame(data=total_data, index=[i for i in range(len(total_data))], columns=[
                  "name", "position", "age", "value", "changed", "nat", "club"])
# generating a CSV file using the dataframe
df.to_csv("playerinfoLaLiga.csv")
