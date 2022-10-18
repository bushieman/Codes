from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
x = np.arange(-10, 11)

#% Matplotlib
## plotting properties
## method 1:
## matplotlib Global API
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1) # rows, columns, panel selected
plt.title('Cool Graphs1')
plt.text(x=30, y=50, s='mytext')
plt.xlabel('X')
plt.ylabel('X Squared')
plt.plot(x, x**2) # x,y
plt.plot(x, (x**2) * -1, linestyle='dashed')
plt.plot([0,0], [-100, 100], linestyle='dashdot')
plt.legend(['X^2', '-X^2','Vertical Line']) # key
plt.subplot(1, 2, 2) 
plt.title('Cool Graphs2')
plt.xlabel('X')
plt.ylabel('X Squared')
plt.plot(x, x**2 , linestyle='dotted')
plt.plot(x, (x**2) * -1, linestyle='solid')
plt.plot([0,0], [-100, 100], color='orange')
plt.legend(['X^2', '-X^2','Vertical Line'])

## saving a figure
plt.savefig('hist.png')

## method 2:
## OOP interface
## single axes
fig, axes = plt.subplots(figsize=(10,5))
axes.set_title('Cool Graphs')
axes.set_xlabel('X')
axes.set_ylabel('X Squared')
axes.plot(x, (x**2), '-oc',linewidth=3, markersize=6, label='X^2')
axes.plot(x, (x**2) * -1, color='coral', linewidth=6, label='-X^2')
axes.plot([0,0], [-100, 100], color='orange', linewidth=3,label='Vertical Line')
axes.legend()
## multiple axes
plot_items = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
fig, (ax1, ax2) = plot_items
ax1.set_title('Cool Graphs1')
ax2.set_title('Cool Graphs2')
ax1.set_xlabel('X')
ax1.set_ylabel('X Squared')
ax2.set_xlabel('X')
ax2.set_ylabel('X Squared')
ax1.plot(x, (x**2), color='aqua', linewidth=3, marker='o', markersize=6, label='X^2')
ax1.plot(x, (x**2) * -1, color='coral', linestyle=':',linewidth=6, label='-X^2')
ax1.plot([0,0], [-100, 100], color='orange', linewidth=3,label='Vertical Line')
ax2.plot(x, (x**2), color='aqua', linewidth=3, marker='o', markersize=6, label='X^2')
ax2.plot(x, (x**2) * -1, color='coral', linewidth=6, label='-X^2')
ax2.plot([0,0], [-100, 100], color='orange', linestyle='--', linewidth=3,label='Vertical Line')
ax1.legend()
ax2.legend()

## cool matplotlib arguments - they are positional arguments hence should come before keyword arguments
## '-og' - straight line marker 'o' color green
## '--c' - dashes cyan
## '-.b' - dash dot blue
## ':r' - dotted red

## the subplot2grid command 
plt.figure(figsize=(16,8))
ax1 = plt.subplot2grid((4,4), (0,0), rowspan=2)
ax2 = plt.subplot2grid((4,4), (0,1), rowspan=2)
ax2 = plt.subplot2grid((4,4), (2,0), colspan=2,rowspan=2)
ax4 = plt.subplot2grid((4,4), (0,2), rowspan=4, colspan=2)

## scatter plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (np.random.rand(N) * 20)**2
## single axes
plt.figure(figsize=(14,7))
plt.title('Cool Dot Graph')
plt.xlabel('random x')
plt.ylabel('random y')
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
plt.colorbar()

## multiple axes
fig = plt.figure(figsize=(14,7))
ax1 = fig.add_subplot(1,2,1)
plt.title('Cool Dot Graph1')
plt.xlabel('random x')
plt.ylabel('random y')
plt.scatter(x, y, s=area, c=colors, alpha=0.4, cmap='Pastel1')
plt.colorbar()
ax2 = fig.add_subplot(1,2,2)
plt.title('Cool Dot Graph2')
plt.xlabel('random x')
plt.ylabel('random y')
plt.scatter(x, y, s=area, c=colors, alpha=0.4, cmap='Pastel2')
plt.colorbar()

##  histograms
values = np.random.randn(100)
plt.subplots(figsize=(14,7))
plt.hist(values, bins=100, alpha=0.9, histtype='bar', color='steelblue', edgecolor='green' )
plt.xlim(xmin=-5, xmax=5)

##  kernel density estimation
values = np.random.randn(100)
values2 = np.linspace(min(values)-10, max(values)+10, 100)
density = stats.kde.gaussian_kde(values)
plt.subplots(figsize=(14,6))
plt.plot(values2, density(values2), color='coral')
plt.fill_between(values2, 0, density(values2), alpha=0.5, color='coral')
plt.xlim(xmin=-5, xmax=5)

## combine plots
values = np.random.randn(100)
values2 = np.linspace(min(values)-10, max(values)+10, 100)
density = stats.kde.gaussian_kde(values)
plt.subplots(figsize=(14,6))
plt.hist(values, bins=100, histtype='bar', alpha=0.6, color='steelblue', edgecolor='green', density=1)
plt.plot(values2, density(values2), color='coral')
plt.xlim(xmin=-5, xmax=5)

## bar plots
y = np.random.rand(1,5)[0]
y2 = np.random.rand(1,5)[0]
plt.figure(figsize=(14,6))
plt.bar(np.arange(1,6), y, width=0.5, color='cyan')

## stacked bar plots
y = np.random.rand(1,5)[0]
y2 = np.random.rand(1,5)[0]
plt.figure(figsize=(14,6))
plt.bar(np.arange(1,6), y, width=0.5, color='#00b894', label='label y')
plt.bar(np.arange(1,6), y2, width=0.5, color='#e17055', label='label y2', bottom=y)
plt.legend()

## boxplots and outlier detection
values = np.concatenate([np.random.randn(10), np.array([10, 15, -10, -15])])
plt.figure(figsize=(14,6))
plt.hist(values)
plt.figure(figsize=(14,6))
plt.boxplot(values)

plt.show()

#% Seaborn

import seaborn as sns
sns.set(style="ticks", color_codes=True, font_scale=1.5) # this should be always at the top before plotting
color = sns.color_palette()

## Loading datasets from git
flights = sns.load_dataset('flights')

## train dataset
train = pd.read_csv('./data/housing/train.csv')
##  relplot
sns.relplot(x='passengers', y='month', hue='year', data=flights) # scatter graph by default
# parameters = {
#     kind: 'line', 'violin', 'scatter', 'strip', 'swarm', 'boxen'
#     palette: 'YlOrRd', 'Spectral
# }

## categorical data with catplot
sns.catplot(x='passengers', y='month', data=flights)

## distribution plot with distplot
sns.distplot(flights.column) # univariate distribution
with sns.axes_style('white'): # bivariate distribution
    sns.joint_plot(x=flights, y=train, kind='kde', color='b')


## FacetGrid
graph = sns.FacetGrid(flights, col='months')
graph.map(plt.hist, 'sepal_length')

## PairGrid
graph = sns.PairGrid(flights, col='months')
graph.map(plt.scatter)

## Box plot
sns.boxplot(x='passengers', y='months', data=flights)
sns.despine(offset=10, trim=True)

## Palplot
sns.palplot(flights)

## Countplot
sns.countplot(y='months', data=flights) 
# parameters:{
    # hue: '<df column>' # use hue with categorical data for more detailed graphs.
# } 

## Heatmap
sns.heatmap(flights.isnull())
# parameters:{
#     yticklabels=True/False,
#     cbar=True/False,
#     cmap='viridis'
# }

## Regplot
sns.regplot(x='GrLivArea_x_Rms', y='SalePrice', data=train); 

#@ Example
fig = plt.figure(figsize=(20, 15))
sns.set(font_scale=1.5)
sns.set_style(style='darkgrid')

# (Corr= 0.817185) Box plot overallqual/salePrice
fig1 = fig.add_subplot(221)
sns.boxplot(x='OverallQual', y='SalePrice', data=train)

# (Corr= 0.700927) GrLivArea vs SalePrice plot
fig2 = fig.add_subplot(222) 
sns.scatterplot(x = train.GrLivArea, y = train.SalePrice, hue=train.OverallQual, palette= 'Spectral')

# (Corr= 0.680625) GarageCars vs SalePrice plot
fig3 = fig.add_subplot(223) 
sns.scatterplot(x = train.GarageCars, y = train.SalePrice, hue=train.OverallQual, palette= 'Spectral')

# (Corr= 0.650888) GarageArea vs SalePrice plot
fig4 = fig.add_subplot(224)
sns.scatterplot(x = train.GarageArea, y = train.SalePrice, hue=train.OverallQual, palette= 'Spectral')

fig5 = plt.figure(figsize=(16, 8))
fig6 = fig5.add_subplot(121)
sns.scatterplot(y = train.SalePrice , x = train.TotalBsmtSF, hue=train.OverallQual, palette= 'YlOrRd')

fig7 = fig5.add_subplot(122)
sns.scatterplot(y = train.SalePrice, x = train['1stFlrSF'], hue=train.OverallQual, palette= 'YlOrRd')

plt.tight_layout(); plt.show()

