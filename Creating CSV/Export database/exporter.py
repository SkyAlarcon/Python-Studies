import csv, pandas, json, os
from scripts import *
from pathlib import Path

path = Path("databasePy")
path.mkdir(parents = True, exist_ok = True)
path = Path("databasePy/usersGames")
path.mkdir(parents = True, exist_ok = True)


fileUsers = open("databaseJS/users.json")

dataUsers = json.load(fileUsers)
userPath = "databasePy/users.csv"
userFields = list(dataUsers[0].keys())

try:
    with open(userPath, "w") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = userFields)
        writer.writeheader()
        for row in dataUsers:
            writer.writerow(row)
except:
    pass

for userID in dataUsers:
    telegramID = userID["telegramID"]
    creationDate = getCreationDate(telegramID)
    deltaCreation15052023 = datesDelta(creationDate)
    deltaToday = datesDelta({"year": "2023", "month": "05", "day": "15"})
    for index in range (deltaCreation15052023, deltaToday, 1):
        date = getDate(index)
        path = Path(f"databaseJS/usersGames/{telegramID}/{date['year']}/{date['month']}/{date['day']}")
        daySavedJSON = open(f"{path}.json")
        dataDaySaved = json.load(daySavedJSON)
        path = Path(f"databasePy/usersGames/{telegramID}/{date['year']}/{date['month']}/{date['day']}")
        path.mkdir(parents = True, exist_ok = True)
        allGames = []
        for game in dataDaySaved:
            basicData = { "name":game["name"], "appid":game["appid"], "playtime":game["playtime"] }
            if "achievements" in game.keys():
                achievementsData = game["achievements"]
                gameAchievsPath = Path(f"{path}/{game['appid']}Achievements.csv")
                savingStatus = writeCSV(achievementsData, gameAchievsPath)
                basicData["achieved"] = game["achieved"]
                basicData["achievements"] = len(achievementsData)
            allGames += [basicData]
        gamePath = Path(f"{path}/games.csv")
        savingStatus = writeCSV(allGames, gamePath)
        daySavedJSON.close()
    else:
        print(f"{telegramID} done")

fileUsers.close()

# with open(userPath, "r") as file:

