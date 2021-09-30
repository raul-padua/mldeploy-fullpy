import torch
import torch.nn as nn
import torch.nn.functional as F
from test import Net



model = torch.load('testnn.pt')
model.eval()

