import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("user_data.csv")
print(df, "\n")

lab1_completed_count = len(df)
print("Number of people who completed Lab 1: ", lab1_completed_count, "\n")

elmo_supporters = df.loc[df["sesame"] == "elmo", "username"]
result = "People who support elmo: "
for name in elmo_supporters:
	result += name + " "

elmo_support_count = len(elmo_supporters)
print(result)
print("Total", elmo_support_count, "\n")

cookie_monster_night_owl = df.loc[(df["sesame"] == "cookie monster") & (df["sleep"] == "night owl"), "username"]
result = "People who support cookie monster and are night owls: "
for name in cookie_monster_night_owl:
	result += name + " "

cookie_monster_night_owl_count = len(cookie_monster_night_owl)
print(result)
print("Total", cookie_monster_night_owl_count, "\n")

not_elmo_not_rock_morning_birds = df.loc[(df["sesame"] != "elmo") & (df["rps"] != "rock") & (df["sleep"] == "morning birds"), "username"]
result = "People who do not support elmo, are not night owls, and are morning birds: "
for name in not_elmo_not_rock_morning_birds:
	result += name + " "

not_elmo_not_rock_morning_birds_count = len(not_elmo_not_rock_morning_birds)
print(result)
print("Total", not_elmo_not_rock_morning_birds_count)

gdf = pd.DataFrame([
	("Completed Lab 1", lab1_completed_count),
	("Elmo", elmo_support_count),
	("Cookie Monster & Night Owls", cookie_monster_night_owl_count),
	("Not Elmo, Not Night Owl, & Morning Bird", not_elmo_not_rock_morning_birds_count)
	], columns=["Category", "Student Count"])
sns.barplot(x="Category", y="Student Count", data = gdf)
plt.show()