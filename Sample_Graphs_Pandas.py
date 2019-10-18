#Import python packages
import pandas as pd
import os

#Set current working directory to fails data folder
os.chdir('C:/Users/12407/Desktop/Education/Projects/Graphs/')

#Import graphing data
df_sample = pd.read_csv('C:/Users/12407/Desktop/Education/Projects/Graphs/Sample_Data.csv')

#Pandas plot
print('Current Working Directory' , os.getcwd())
df_sample.set_index('Year', inplace=True)
pd_plot = df_sample.groupby('Type')['Price'].plot(legend=True)
fig = pd_plot.get_figure()
fig.savefig("output_pd.png")