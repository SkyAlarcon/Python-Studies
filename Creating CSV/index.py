import csv

# with open("Analytics and Revenue by day from Apr_14_2023 to May_13_2023.csv", "r") as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         # print(row)
#         break

import pandas as pd

data = pd.read_csv("Analytics and Revenue by day from Apr_14_2023 to May_13_2023.csv")
# print(data)

# testFile = open("test.csv", "w")
# test = [{
#   "name": "Portal",
#   "appid": 400,
#   "playtime": 733,
#   "achieved": 15
#   }]
# testCol = ["name", "appid", "playtime", "achieved"]
# csv_file = "Games.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=testCol)
#         writer.writeheader()
#         for data in test:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")

# data = data = pd.read_csv("Games.csv")
# print(data)


import json

# Open file
file = open("users.json")

data = json.load(file)
# print(type(data))
# print(data)
users = open("test/users.csv", "w")
fields = ["telegramID", "steamID"]
csv_file = "test/users.csv"

try: 
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for line in data:
            writer.writerow(line)
except:
    pass

# for i in data["users"]:
#     print(i)
    # try:
    #     for i in data['']:
    #     with open(csv_file, 'w') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=fields)
    #         writer.writeheader()
    #         for i in data:
    #             writer.writerow(i)
    # except IOError:
    #     print("I/O error")

file.close()
# Close file

import os

dirPath = os.getcwd()
# print(dirPath)
print(os.listdir())

try:
    os.mkdir("test")
except:
    pass
print(os.listdir())

print(pd.read_csv("test/users.csv"))