#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from readxml import *
import matplotlib.pyplot as plt

def main():
    cur = "Euro"
    startdate = "01.01.2019"
    enddate = "01.03.2019"
    tup = getInput(cur, startdate, enddate)
    #print(tup)
    if tup is not None:
        plt.plot(tup[0], tup[1], marker = ".")
        plt.gcf().autofmt_xdate()
        title = "Currency rates: {} on period {} - {}".format(cur, startdate,enddate)
        plt.title(title)
        plt.xlabel("Dates")
        plt.ylabel(cur)
        plt.grid(b = True, linestyle = "--")
        plt.show()

main()
