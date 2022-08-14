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
bar_items = ['value',
             'params_gamma',
             'params_learning_rate',
             'params_max_depth',
             'params_min_child_weight',
             'params_n_iters',
             'params_reg_alpha', 
             'params_reg_lambda',
             'params_subsample']
bar_labels = ['value',
              'complexity',
              'learning_rate',
              'tree depth',
              'min_child_wt',
              'iterations',
              'reg_alpha',
              'reg_lambda',
              'subsample']
fig = plot_experiments('test plot experiments',
                       data,
                       893,
                       1628,
                       bar_items,
                       bar_labels)

fig = plot_experiments('test plot experiments',
                       data,
                       1628,
                       1628,
                       bar_items,
                       bar_labels)