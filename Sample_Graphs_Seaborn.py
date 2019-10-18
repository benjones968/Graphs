#Import python packages
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns

#Set current working directory to fails data folder
#print('Current Working Directory' , os.getcwd())
os.chdir('C:/Users/12407/Desktop/Education/Projects/Graphs')
#print('New Working Directory' , os.getcwd())

#Import graphing data
df_sample = pd.read_csv('C:/Users/12407/Desktop/Education/Projects/Graphs/Sample_Data.csv')

#Matplotlib plot
#df = df_sample[df_sample['Type']=='Platinum']
#plt.plot( 'Year', 'Price', data=df, color='blue', linewidth=2, label="Platinum")
#df = df_sample[df_sample['Type']=='Palladium']
#plt.plot( 'Year', 'Price', data=df, color='red', linewidth=2, label="Palladium")
#df = df_sample[df_sample['Type']=='Rhodium']
#plt.plot( 'Year', 'Price', data=df, color='yellow', linewidth=2, label="Rhodium")
#plt.legend()

#Seaborn plot
sns_plot = sns.lineplot(x="Year", y="Price", hue="Type", data=df_sample)
fig = sns_plot.get_figure()
fig.savefig("output.png")
