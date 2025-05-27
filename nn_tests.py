import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np
import pandas as pd



data = pd.read_csv('Data/Final_data/final_depr')
data.head()
#tensor = torch.tensor(data)
#print(tensor)

#print(f"tensor shape: {tensor.shape}")
#print(f"tensor data type: {tensor.dtype}")