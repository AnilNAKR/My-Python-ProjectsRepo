# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # The above data returns a data object
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# print(data.condition)

# highest = 0
# for i in data["temp"]:
#     if int(i) > highest:
#         highest = int(i)
# print(data[data.temp == highest])
#
# #-->Alternate method
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# How to create a dataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 50, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = squirrel_data["Primary Fur Color"]

color = {
    "Gray": 0,
    "Cinnamon": 0,
    "Black": 0
}

for col in fur_colors:
    if col == "Gray":
        color[col] += 1
    elif col == "Black":
        color[col] += 1
    elif col == "Cinnamon":
        color[col] += 1

final_colors = {
    "Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [color["Gray"], color["Cinnamon"], color['Black']]
}

colors_group = pd.DataFrame(final_colors)
# print(colors_group)
colors_group.to_csv("fur_color.csv")