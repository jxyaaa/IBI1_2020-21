import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/jiang/Desktop")

covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:12:2,:])
#make it between 0 and 10

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

world_new_cases=covid_data.loc[world_data,"new_cases"]
mean = np.mean(world_new_cases)
#calculate the mean
median = np.median(world_new_cases)
#calculate the median
print('the mean of new cases is:',world_new_cases.mean())
print('the median new cases is:',world_new_cases.median())
plt.boxplot(world_new_cases)
#draw a boxplot
plt.xlabel(" new cases")
plt.ylabel("number")
plt.title(" the distribution of new cases")
plt.show()

world_dates=covid_data.loc[world_data,"date"]
world_new_deaths=covid_data.loc[world_data,"new_deaths"]
#store the data

plt.plot(world_dates,world_new_cases,'b-',label = "world new cases")
plt.plot(world_dates,world_new_deaths,'r-',label = "world new deaths")
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title(" new cases and new deaths")
plt.legend()
plt.show()


#question.txt
S=[]
for i in range(0,7996):
    if covid_data.iloc[i,1] == "Spain":
        S.append(True)
    else:
        S.append(False)
print(covid_data.loc[S,"total_cases"])
print(covid_data.loc[S,"new_cases"])

total_cases=covid_data.loc[S,"total_cases"]
new_cases=covid_data.loc[S,"new_cases"]
Spain_dates=covid_data.loc[S,"date"]

plt.plot(Spain_dates,total_cases,'b+',label = "Spain total cases")
plt.plot(Spain_dates,new_cases,'r+',label = "Spain new cases")
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4], rotation=-90)
plt.xlabel("date")
plt.ylabel("number")
plt.title(" new cases and new deaths")
plt.legend()
plt.show()
#plot total cases and new cases in Spain
