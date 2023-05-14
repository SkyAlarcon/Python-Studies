import csv, pandas, json, os, moment
import scripts as auto

try:
    os.mkdir("databasePy")
except:
    pass


fileUsers = open("databaseJS/users.json")

dataUsers = json.load(fileUsers)
print(dataUsers)
userPath = "databasePy/users.csv"
userFields = ["telegramID", "steamID"]

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
    gamesPath = f"databaseJS/usersGames/{telegramID}"
    yearsList = os.listdir(gamesPath)
    gamesPath = f"databaseJS/usersGames/{telegramID}/{yearsList[0]}"
    monthsList = os.listdir(gamesPath)
    gamesPath = f"databaseJS/usersGames/{telegramID}/{yearsList[0]}/{monthsList[0]}"
    daysList = os.listdir(gamesPath)
    dayNumber = daysList[0].split(".")
    creationDate = {"year": yearsList[0], "month": monthsList[0], "day": dayNumber[0]}
    auto.getDay(creationDate)
    # print(creationDate)


fileUsers.close()

# with open(userPath, "r") as file:

