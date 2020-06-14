import torch
import torch.nn as nn
import torch.optim as optim


## Chapter 1 Implementation
class Encoder(nn.Module):
    def __init__(self, emb_dim, hid_dim, dropout):
        nn.Module.__init__(self)
        pass

    def forward(self,src):
        pass


class Decoder(nn.Module):
    def __init__(self, emb_dim,hid_dim,output_dim,dropout):
        nn.Module.__init__(self)
        pass

    def forward(self,trg, hidden, cell):
        pass


class Seq2Seq(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        pass

    def forward(self):
        pass

