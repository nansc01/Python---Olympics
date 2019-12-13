import pandas as pd

df = pd.read_csv("athlete_events(1).csv")
print("step 0: \n==========================")
print("There are " + str(len(df)) + " records in the dataset.")

df.Medal = df.Medal.fillna("None")
print("\nStep 1:\n============================")
print("There are " + str(len(df[df.Medal != "None"])) + " in the dataset with medals.")

# Step 2:  Report the top 3 sports in olympics that has the tallest, shortest, heaviest and lightest (on average) athletes
df1 = df.groupby("Sport")["Height"].mean().nlargest(3)
df2 = df.groupby("Sport")["Height"].mean().nsmallest(3)
df3 = df.groupby("Sport")["Weight"].mean().nlargest(3)
df4 = df.groupby("Sport")["Weight"].mean().nsmallest(3)

print("\nStep 2:\n===========================")
print("Tallest: \n", df1, "\n\nShortest: \n", df2, "\n\nHeaviest: \n", df3, "\n\nlightest: \n", df4)

#Step 3: For winter olympics only, report the team with most Gold medals year by year
print("\nStep 3")
print("========================")
a = df[df.Season == "Winter"]
years1 = a.groupby("Year").mean().reset_index()["Year"].tolist()

for year in years1:
    gg = a[(a.Year == year) & (a.Medal == "Gold")].groupby("Team")["Medal"].count().nlargest(1).reset_index()
    print(str(year) + " " + gg["Team"][0])
    

#Step 4:​ For each sport, report which team dominates it -- team with most medals.  
print("\nStep 4")
print("========================")
sports = df.groupby("Sport").count().reset_index()["Sport"].tolist()

for sport in sports:
    ss = df[df.Sport == sport].groupby("Team")["Medal"].count().nlargest(1).reset_index()
    print(sport + ": " + ss["Team"][0] + " with " + str(ss['Medal'][0]) + " Medals.")
    
print("\nStep 5")
print("========================")
b = df[df.Season == "Summer"]
years2 = b.groupby("Year").count().reset_index()["Year"].tolist()

datarates = []

for year in years2:
    f = b[b.Year == year]
    datarates.append(len(f[f.Sex == "F"]) / len(f))
    
import matplotlib.pyplot as plt
plt.plot(years2,datarates)
plt.show()


#Step 6: Create a graph displaying average athlete age year by year
print("\nStep 6")
print("========================")

years = df.groupby("Year").count().reset_index()["Year"].tolist()
ages = df.groupby("Year")["Age"].mean().tolist()
plt.plot(years,ages)
plt.show()

print("\nStep 7")
print("========================")

c= df[df.Year == 2016]
compete_rates = []
for sport in sports:
    cc = c[c.Sport == sport]
    if (len(cc) == 0):
        continue
    rate = len(cc[cc.Medal != "None"]) / len(cc)
    compete_rates.append({"Sports" : sport, "Rate" : rate})
    
compete_rates = sorted(compete_rates, key = lambda x: x["Rate"], reverse = True)
print("We recommend: ")

print(compete_rates[0]["Sports"])
print(compete_rates[1]["Sports"])
print(compete_rates[2]["Sports"])











