from os import name
from numpy.core.getlimits import _fr1
import pandas as pd
import numpy as np

# pandas series
top_epl_teams = pd.Series(['Chelsea', 'Mancity', 'Liverpool', 'Man-u', 'Arsenal', 'Tottenham'])
top_epl_teams.name = 'The top teams in the English Premier League'
top_epl_teams
top_epl_teams.dtype 
top_epl_teams.values 
type(top_epl_teams.values)
top_epl_teams[0]

# we can explicitly assign indexes to our list items
top_epl_teams.index = [
    'Fourth',
    'First',
    'Third',
    'Second',
    'Ninth',  
    'Seventh'
]
top_epl_teams['First']

# creating pandas series
top_epl_teams = pd.Series(['Chelsea', 'Mancity', 'Liverpool', 'Man-u', 'Arsenal', 'Tottenham'])

f1_rankings_2021 = pd.Series({
    'Verstappen': "First",
    'Hamilton': 'Second',
    'Lando': 'Third',
    'Perez': 'Fourth',
    'Leclerc': 'Fifth'
}, name='F1 drivers and their standings 2021')

f1_rankings_2020 = pd.Series(
    ['Third','Sixth','First','Fourth','Fifth'],
    index=['Verstappen','Lando', 
    'Hamilton', 
    'Perez',
    'Leclerc'],name='F1 drivers and their standings 2020')

f1_rankings_2019 = pd.Series(f1_rankings_2020, index=['Vettel', 'Albon', 'Hamilton', 'Verstappen', 'Leclerc'], name='search for F1 drivers and their standings 2020')

# indexing

f1_rankings_2020['Verstappen']
f1_rankings_2020.iloc[0]
f1_rankings_2020[['Verstappen', 'Hamilton']]
f1_rankings_2020['Verstappen':'Hamilton'] # the upper limit(Hamilton) of the range is included

# conditional selection(boolean arrays)
g7_pop = pd.Series([87, 67, 345, 34, 56, 127, 67])
g7_pop.index = ['United Kingdom', 'Germany', 'United States', 'Canada', 'Italy', 'Japan', 'France']
g7_pop
g7_pop.mean()
g7_pop.std()
g7_pop>70
g7_pop[g7_pop>70]
g7_pop[g7_pop>g7_pop.mean()]

# modifying series
# by index
g7_pop['Canada'] = 42.4
# by sequencial
g7_pop.iloc[0] = 93.32
# by conditions
g7_pop[g7_pop<70] = 93.32

