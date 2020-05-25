# -*- coding: UTF-8 -*-
import os
import time
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import scipy.special as sc
class prng():

    def __init__(self):
        pass
    def _igamc_(self, x):
        a = 9/2
        value = sc.gammaincc(a, x/2)
        print("@_igmac_ out -> ", value)
        return value
    # para: clas:
    # `0: Gaussian Distribution
    # `1: Binomial Diatribution
    # para: m times.
    def _chi_(self, clas, m):
        refs_list = []
        if clas == 0:
            # gen normal distribute curve as artificial p-value
            mu, sigma = 0.4, 0.2
            s = list()
            #s = np.random.normal(mu, sigma, 10)
            #s = [0.186356,0.180314,0.007372,0.491297,0.822325,0.139918,0.395549,0.255937,0.774986,0.534146]
            random_d = random.random()
            for i in range(1,11):
                s.append(random_d)
            # Create the bins and histogram
            print(s)
            pass
        elif clas == 1:
            pass
        else:
            print("para clas is error!\n")
        x_result = 0
        for i in range(1 ,10):
            x_result = x_result + ((s[i] - (m/10))**2) /(m/10)
        print("@_chi_ out -> ", x_result)
        success = (x_result >= 0.01)
        return x_result

    def run(self):
        v = self._igamc_(self._chi_(0, 1))


if __name__ == '__main__':
    t = prng()
    t.run()