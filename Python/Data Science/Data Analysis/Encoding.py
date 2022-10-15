from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

df = pd.DataFrame({
    '# transforms categorical values into ordinal numerical value in ordered sets.': [34.244,63.951, 80.94, 60.665, 127.061, 54.511, 318.523],
    'GDP': [
        1785387,2833687,3874437,2167744,4602367,2950039,17348075
    ],
     'Continent': [
        'America', 'Europe', 'Europe', 'Europe','Asia', 'Europe', 'America'
    ],
    'Surface Area': [
        9984670,640679,357114,301336,377930,242495,9525067
    ],
    'HDI': [
        0.912,0.888,0.916,0.873,0.891,0.907,0.915
    ]
}, columns=['Population', 'GDP', 'Continent', 'Surface Area', 'HDI'])

## Handling categorical data
## 1. label Encoding - works well with decision trees, random forests
#   a. preprocessing
encoder = LabelEncoder()
df['Population'] = encoder.fit_transform(df['Population']) 

#   b. category codes
df['Population'] = df['Population'].astype('category')
df['Population'] = df['Population'].cat.codes

## 2. one hot encoding - works well with LR, KMC, KNN, ANN
# limited to low no of uniue values
# always remove one dummy variable column
# Multicollinearity? occurs where there is a relationship between the independent variables, and it is a major threat to multiple linear regression and logistic regression problems.
#   a. onehotencoder class
onehotencoder = OneHotEncoder(sparse=False, handle_unknown='error', drop='first')
onehotdf = pd.DataFrame(onehotencoder.fit_transform(df['Continent']))
df = df.join(onehotdf)
#   b. pandas
onehotdf = pd.get_dummies(df['Continent'], prefix='Continent', drop_first=True)
df = pd.concat([df, onehotdf], axis=1)
df.drop('Continent', axis=1, inplace=True)

## 3. Ordinal Encoding
# transforms categorical values into ordinal numerical value in ordered sets.
#@ The input to this transformer should be an array-like of integers or strings, denoting the values taken on by categorical (discrete) features.
data = {'Customer_Rating': ['Poor', 'Average', 'Good', 'Very Good', 'Excellent']}
df = pd.DataFrame(data)
rating_dict = {'Poor': 1, 'Average': 2, 'Good': 3, 'Very Good': 4, 'Excellent': 5}
df['Customer_Rating'] = df.Customer_Rating.map(rating_dict)

