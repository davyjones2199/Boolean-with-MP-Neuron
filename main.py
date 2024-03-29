# -*- coding: utf-8 -*-
"""Machine Learning-2 Assignment-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rnWs73izuLCNP_yIg6x5l7DJANm11LcH
"""

import numpy as np

class MPNeuron:
    def __init__(self):
        pass
    def AND(self,array):
        if np.sum(array) == len(array):
            return 1
        else:
            return 0

    def OR(self,array):
        if np.sum(array) > 0:
            return 1
        else:
            return 0

    def NOT(self,value):
        if value == 1:
            return 0
        else:
            return 1

    def NAND(self,array):
        return self.NOT(self.AND(array))

    def NOR(self,array):
        return self.NOT(self.OR(array))

    def XOR(self,array):
        if np.sum(array) > 0 and np.sum(array) < len(array):
            return 1
        else:
            return 0

    def XNOR(self,array):
        return self.NOT(self.XOR(array))
