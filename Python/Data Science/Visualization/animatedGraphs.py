import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

df = pd.read_csv(url, sep=',', header='infer')

df_interest = df.loc[df['Country/Region'].isin(['United Kingdom', 'US', 'Italy', 'Germany']) & df['Province/State'].isnull()]
for item in df_interest.index:
    newIndex = df.iloc[item, 1]
    df_interest.rename(index={item:newIndex}, inplace=True)

df_interest = df_interest.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1)
df1 = df_interest.transpose() # alternate between the rows and the columns
df1 = df1.loc[(df1 != 0).any(1)] # for each series in our dataframe, append the dataframe by the series with atleast one item greater than zero. this is to avoid plotting graphs of zero values
df1.index = pd.to_datetime(df1.index) # convert arguments to datetime

# plotting the graphs
# graph 1: Animated line graph
color = ['coral', 'aqua', 'orange', 'crimson']
fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor") #rotate the x-axis values
plt.subplots_adjust(bottom = 0.2, top = 0.9) #ensuring the dates (on the x-axis) fit in the screen
plt.xlabel('No of Deaths')
plt.ylabel('Dates')
# setting up the curve function
def buildOurCoolChart(i=int): # i is the no of loops
    plt.legend(df1.columns)
    p = plt.plot(df1[:i].index, df1[:i].values) #note it only returns the dataset, up to the point i
    for i in range(0,4):
        p[i].set_color(color[i]) #set the colour of each curve

animator = ani.FuncAnimation(fig, buildOurCoolChart, interval = 100)

# graph 2: Animated pie graph
fig, axes = plt.subplots(figsize=(10,5))
explode=[0.01,0.01,0.01,0.01] #pop out each slice from the pie

def getMePie(i):
    def absolute_value(val): #turn % back to a number
        a  = np.round(val/100.*df1.head(i).max().sum(), 0)
        return int(a)
    axes.clear()
    plot = df1.head(i).max().plot.pie(y=df1.columns,autopct=absolute_value, label='',explode = explode, shadow = True)
    plot.set_title('Total Number of Deaths\n' + str(df1.index[min( i, len(df1.index)-1 )].strftime('%y-%m-%d')), fontsize=12)

animator = ani.FuncAnimation(fig, getMePie, interval = 200)

# graph 3: Animated bar graph
fig = plt.figure()
bar = ''
def buildmebarchart(i=int):
    iv = min(i, len(df1.index)-1) #the loop iterates an extra one time, which causes the dataframes to go out of bounds. This was the easiest (most lazy) way to solve this :)
    objects = df1.max().index
    y_pos = np.arange(len(objects))
    performance = df1.iloc[[iv]].values.tolist()[0]
    if bar == 'vertical':
        plt.bar(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Deaths')
        plt.xlabel('Countries')
        plt.title('Deaths per Country \n' + str(df1.index[iv].strftime('%y-%m-%d')))
    else:
        plt.barh(y_pos, performance, align='center', color=['red', 'green', 'blue', 'orange'])
        plt.yticks(y_pos, objects)
        plt.xlabel('Deaths')
        plt.ylabel('Countries')
animator = ani.FuncAnimation(fig, buildmebarchart, interval=100)

plt.show()
