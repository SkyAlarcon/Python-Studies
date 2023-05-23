import os, pathlib, csv
import arrow as moment

def formatDate (dateDict: dict):
    '''
    (dict) -> str

    Recieves a date as a dict and returns a formatted str DD-MM-YYYY
    '''
    dateStr = dateDict["year"] + "-" + dateDict["month"] + "-" + dateDict["day"]
    return dateStr

def getDate (daysForward = 0):
    '''
    ([int]) -> dict

    Recieves how many days, from today, in the future the day is (negative if it's in the past)
    and returns day's date as a dict
    '''
    date = {
        "day": moment.now().shift(days = daysForward).format("DD"),
        "month": moment.now().shift(days = daysForward).format("MM"),
        "year": moment.now().shift(days = daysForward).format("YYYY")
    }
    return date

def getCreationDate (telegramID: str):
    '''
    (str) -> dict
    
    Recieves a telegramID and returns the date of creation of the user as a dict
    '''
    gamesPath = f"databaseJS/usersGames/{telegramID}"
    yearsList = os.listdir(gamesPath)
    gamesPath = f"databaseJS/usersGames/{telegramID}/{yearsList[0]}"
    monthsList = os.listdir(gamesPath)
    gamesPath = f"databaseJS/usersGames/{telegramID}/{yearsList[0]}/{monthsList[0]}"
    daysList = os.listdir(gamesPath)
    dayNumber = daysList[0].split(".")
    creationDate = {"year": yearsList[0],
                    "month": monthsList[0],
                    "day": dayNumber[0]
                    }
    return creationDate

def datesDelta (dateStart: dict, dateFinish = getDate()):
    '''
    (dict, [dict]) -> int

    Recieves a dict with a start date and a finish date and calculates their delta

    If no finish date is set, it will use today as reference
    '''
    start = moment.get(formatDate(dateStart))
    finish = moment.get(formatDate(dateFinish))
    delta = (start - finish).days
    return delta

def removeDictTag(dict, tags):
    newDict = {value: dict[value] for value in dict if value not in tags}
    return newDict

def filterDictTag(dict, tags):
    newDict = {value: dict[value] for value in dict if value in tags}
    return newDict

def writeCSV(toSave: list, path: pathlib.WindowsPath):
    status = "pending"
    try:
        with open(f"{path}", "w") as csvFile:
            fields = toSave[0].keys()
            writer = csv.DictWriter(csvFile, fieldnames = fields)
            writer.writeheader()
            for row in toSave:
                writer.writerow(row)
        status = "saved"
    except Exception as e:
        status = "error"
    return status