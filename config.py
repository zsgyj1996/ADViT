# -*- coding: utf-8 -*-

import torch

class Config():
    def __init__(self):
        self.USE_CUDA = True and torch.cuda.is_available()
    

        