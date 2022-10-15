import torch
import torch.nn as nn
import pandas as pd
import math
import torch
from torch.utils.data import DataLoader, TensorDataset
from torch.utils.data.dataset import random_split

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
num_epochs = 20
 
def get_data():
    train_data = pd.read_csv('train.csv')
    y = train_data['TARGET']
    X = train_data.drop(['ID', 'TARGET'], axis=1)
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    y_tensor = torch.tensor(y.values, dtype=torch.float32)
    ds = TensorDataset(X_tensor, y_tensor)
    train_ds, val_ds = random_split(ds, [math.floor(int(0.8*len(ds))), math.ceil(int(0.2*len(ds)))])

    test_data = pd.read_csv('test.csv')
    test_ids = test_data['ID']
    X = test_data.drop(['ID',], axis=1)
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    y_tensor = torch.tensor(test_ids.values, dtype=torch.float32)
    test_ds = TensorDataset(X_tensor, y_tensor)

    return train_ds, val_ds, test_ds, test_ids


class NN(nn.Module):
    def __init__(self, input_size):
        super(NN, self).__init__()
        self.net = nn.Sequential(
            nn.BatchNorm1d(input_size),
            nn.Linear(input_size, 50),
            nn.ReLU(inplace=True),
            nn.Linear(50, 1),
        )

    # forward 
    def forward(self, x):
        return torch.sigmoid(self.net(x)).view(-1)

# model
model = NN(input_size=369).to(DEVICE) # why is the input size 369 and not 200

# loss function
lossFn = nn.BCELoss()  

# optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=2e-3, weight_decay=1e-4)

train_ds, val_ds, test_ds, test_ids = get_data()

# load the data
train_loader = DataLoader(train_ds, batch_size=1024, shuffle=True)
val_loader = DataLoader(val_ds, batch_size=1024)
test_loader = DataLoader(test_ds, batch_size=1024)

x, y = next(iter(train_loader))
print(x.shape)

for _ in range(num_epochs):
    data, targets = next(iter(train_loader)) # batch
    # for ids, (data, targets) in enumerate(train_loader):
    data = data.to(DEVICE)
    targets = targets.to(DEVICE)

    # creating a forward pass
    scores = model(data)
    print('scores: ', scores)
    
    predictions = torch.max(scores)
    print('predictions: ', predictions)

    loss = lossFn(scores, targets)
    print(loss.item())
    # backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
