import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/jiang/Desktop")

covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:12:2,:])

L=[]
for i in range(0,7996):
    if covid_data.iloc[i,1] == "Afghanistan":
        L.append(True)
    else:
        L.append(False)
print(covid_data.loc[L,"total_cases"])

world_data = []
for i in range(0,7996):
    if covid_data.iloc[i,1] == "World":
        world_data.append(True)
    else:
        world_data.append(False)
print(covid_data.loc[world_data,"total_cases"])

world_new_cases=covid_data.iloc[world_data,"new_cases"]
print('the mean of new cases is:',world_new_cases.mean())
print('the median new cases is:',world_new_cases.median())
plt.boxplot(world_new_cases)
plt.xlabel(" new cases")
plt.ylabel("number")
plt.title(" the distribution of new cases")
plt.show()

plt.plot(world_dates,world_new_cases,'b+',label = "world new cases")
plt.plot(world_dates,world_new_deaths,'r+',label = "world new deaths")
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title(" new cases and new deaths")
plt.legend()
plt.show()
