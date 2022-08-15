"""
Created on Sun Aug 14 12:12:50 2022

@author: Blaine Bateman
"""
#%% libraries
#
# data manipulation
#
import pandas as pd
#
# system utilities
#
import sys
#
#%% update path
#
sys.path.append(<path to plot_experiments.py>)
#
#%% import module
#
from plot_experiments import plot_experiments
#
#%% data
#
data = \
  pd.read_csv(<path to a suitable DataFrame in csv format>)
#
#%% visualize
#
bar_items = [<list of strings that are column names of data>]
bar_labels = [<list of strings you want to use in place of column names>]
fig = plot_experiments('test plot experiments',
                       data,
                       893,
                       1628,
                       bar_items,
                       bar_labels)