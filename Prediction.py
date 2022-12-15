import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.figure(figsize=(20,10))
#Reading data from a csv file.
#data=pd.read_csv('Uganda_population.csv').tail()
data1=pd.read_csv("data.csv").head()
#data2=pd.read_csv("Uganda_popn.csv").head()


#Printing data.
def printdata(data):
    print("\nrows & columns: ",data.shape)
    #print("\nHead:\n",data.head())
    print("\nData:\n ",data)
#printdata(data1)

#sellecting x and y from the dataset.
x=data1['Years'].values
y=data1['TotalPopulation'].values
#print(x)
#print(y)

#mean of x and y
mean_x=np.mean(x)
mean_y=np.mean(y)
def printmean(mean1,mean2):    
    print("mean of x-label: ",mean1)
    print("mean of y-label: ",mean2)
printmean(mean_x,mean_y)

#total length of values
n=len(x)

#Using the formula to calculate b1 and b2
numer=0
denom=0
for i in range(n):
    numer += (x[i]-mean_x)*(y[i]-mean_y)
    denom += (x[i]-mean_x)**2
M=numer/denom
C=mean_y-(M*mean_x)

def print_grad_intercept(m,c):
    print("Gradient: ",m)
    print("Intercept: ",c)
print_grad_intercept(M,C)

#plotting valuesnd regration line
max_x=np.max(x)+6
min_x=np.min(x)+0

#calculating the line value x and y
x1=np.linspace(min_x,max_x,10)
y1 = C + M*x1

#plotting line
#title=plt.title("A graph of Years against  population in mellion")
def Linegraph(x,y,title):
    plt.plot(x,y, c='#58b970',label='Regration line')
    plt.scatter(x,y, c='#ef5423',label='scatter plot')
    plt.xlabel('Years')
    plt.ylabel('Population in melliom')
    plt.legend()
    title
    plt.grid(axis='both')
    plt.savefig('population.png')
    plt.show()
    
Linegraph(x1,y1,title)


#checking the correctness of the model

def Coefficient(p,q):
    ss_t=0
    ss_r=0
    for i in range(n):
        y_pred = ((p*x[i])+q)
        print(y_pred)
        ss_r += (y_pred-mean_y)**2
        ss_t += (y[i]-mean_y)**2
    
    #print(y_pred)

    print("\nTarget: ",y1)
    r2 =(ss_r/ss_t)
    print("\nCoeficient(R^2): ",r2)


Coefficient(M,C)
