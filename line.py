import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))

data=pd.read_csv("UgandaPopulation.csv")
data1=pd.read_csv("data.csv")
data2=pd.read_csv("Uganda_popn.csv")

def printdata(data):
    #print(data.head())
    print(data)
#printdata(data1) 
   
years=data['Years'].values
population=data['Total_Population'].values 
#print(population)
year=data1['Years'].values
popln=data1['TotalPopulation'].values

year1=data2['Year'].values
popn=data2['Population'].values 
#pop=popln.sort(reverse=True)
def selecteddata(col1,col2):
    print('\n\nYears: ',col1)
    print('population: ',col2)
#selecteddata(years,population)
    
#t=plt.title("A line graph showing Uganda population growth between 1960 to 2015")    
def populationxy(x,y):
    plt.plot(x,y,'r-o',label='popln_dataset1')
    #plt.plot(x,z,'b-o',label='popln_dataset2')
    plt.legend()
    plt.savefig('UG_population.png')
    plt.show()

populationxy(years,population)
populationxy(year,popln)
populationxy(year1,popn)