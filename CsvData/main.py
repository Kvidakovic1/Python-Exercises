import pandas
black = 0
cinnamon = 0
gray = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"].tolist()
print(fur_color)

for color in fur_color:
    if color == "Black":
        black += 1
    if color == "Cinnamon":
        cinnamon += 1
    if color == "Gray":
        gray +=1

print(f"There is {black} black squirrels")
print(f"There is {gray} gray squirrels")
print(f"There is {cinnamon} cinnamon squirrels")


data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],

    "Count" : [gray, cinnamon, black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

