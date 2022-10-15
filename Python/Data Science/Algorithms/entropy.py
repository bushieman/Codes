import numpy as np
import pandas as pd

data = [
    [1, 30, 'No'],
    [1, 15, 'No'],
    [1, 5, 'No'],
    [0, 10, 'No'],
    [0, 5, 'No'],
    [0, 15, 'Yes'],
    [0, 20, 'Yes'],
    [0, 25, 'Yes'],
    [0, 30, 'Yes'],
    [0, 30, 'Yes'],
]

train_data = pd.DataFrame(data)
train_data.columns = ['Rain', 'Time', 'Walk']
walk = pd.get_dummies(train_data['Walk'], drop_first=True)
train_data = pd.concat([train_data, walk], axis=1)
train_data.drop('Walk', axis=1, inplace=True)
train_data.rename(columns={'Yes': 'Walk'}, inplace=True)

def entropy(y):
    instance = np.bincount(y)
    ratio = instance/len(y)
    return np.sum([-(item * np.log2(item)) for item in ratio if item > 0])

true_values = []
false_values = []
def get_values():
    for i in range(len(train_data)):
        if train_data['Rain'][i] == 1:
            true_values.append(train_data['Walk'][i])
        else:
            false_values.append(train_data['Walk'][i])

get_values()

def info_gain(true_values, false_values, attributes, predict):
    instance = np.bincount(attributes)
    ratio = instance/len(attributes)
    E_yes = entropy(true_values)
    E_no = entropy(false_values)
    prediction = entropy(predict)
    total_ent = (ratio[0] * E_no) + (ratio[1] * E_yes)
    return prediction - float(total_ent)

info_gain(true_values, false_values, train_data['Rain'], train_data['Walk'])


