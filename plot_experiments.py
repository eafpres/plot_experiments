"""
Created on Sun Aug 14 11:33:58 2022

@author: Blaine Bateman
"""
#%% libraries
#
# data manipulation
#
import pandas as pd
import numpy as np
#
# visualization
#
import matplotlib # note--needed to support type hint
import matplotlib.pyplot as plt
#
# data scaling
#
import sklearn # note--needed to support type hint
from sklearn.preprocessing import MinMaxScaler
#
# string manipulation using regex
#
import re
#
#%% function def
#
def plot_experiments(
    name : str = None,
    experiments : pd.core.frame.DataFrame = None,
    labeled_experiment : int = None,
    best_experiment : int = None,
    bar_items : list[str] = None,
    bar_labels : list[str] = None
    ) -> matplotlib.figure.Figure:
  """
  

  Parameters
  ----------
  name : str
    DESCRIPTION. A string representing the name of the study

  experiments : pd.core.frame.DataFrame
    DESCRIPTION. A Pandas DataFrame with columns containing hyperparameter
                 values or other information about trials
                 Note that a subset of the columns is selected by 'bar_items'
                 The index of the DataFrame is assumed to match the run
                 number, such that integers can be passed in labeled_experiment
                 and best_experiment to affect the plotting behavior
                 
  labeled_experiment : int
    DESCRIPTION. The index of the trial to be highlighted on the chart
    
  best_experiment : int
    DESCRIPTION. The index of the trail identified as the best in the data
    
  bar_items : list[str]
    DESCRIPTION. A list of column names for the data to be used in the chart
    
  bar_labels : list[str]
    DESCRIPTION. A list of strings to be used to label the corresponding
                 columns. Note that the order of bar_labels is assumed
                 to be the same as the order of bar_items

  Returns
  -------
  fig : matplotlib.figure.Figure
    DESCRIPTION. A matplotlib figure that can be used for display

  """
#
# utility function to add range information to parameter names
#
  def format_bar_labels(
      bar_labels : list[str] = None,
      plot_scaler : sklearn.preprocessing._data.MinMaxScaler = None
      ) -> list[str]:
    """
    

    Parameters
    ----------
    bar_labels : list[str]
      DESCRIPTION. Labels for the columns chosen to be on the plot
                   These are the 'raw' names used to label the 
                   hyperparameters; they are updated by this function
                   
    plot_scaler : sklearn.preprocessing._data.MinMaxScaler
      DESCRIPTION. The scaler used to scale the data used on the plot
                   The scaler is used to extract the max and min
                   values for each parameter to add to the label
                   so that the relative plot can be interpreted

    Returns
    -------
    bar_labels : list[str]
      DESCRIPTION. The updated labels for the plot

    """    
    bar_labels = \
      pd.Series(zip(bar_labels,
                    list(zip(np.round(plot_scaler.data_min_, 2),
                             np.round(plot_scaler.data_max_, 2))))).astype(str)
    bar_labels = \
      pd.Series([re.sub("\',", "\'\n", bar_labels[i])
                 for i in bar_labels.index])
    bar_labels = \
      pd.Series([re.sub("[()]", "", bar_labels[i])
                 for i in bar_labels.index])
    bar_labels = \
      pd.Series([re.sub(", ", " - ", bar_labels[i])
                 for i in bar_labels.index])
    bar_labels = \
      pd.Series([re.sub("\'", "", bar_labels[i])
                 for i in bar_labels.index])    
#
    return bar_labels
#
# scale each hyperparamter range to [0, 1]
#
  plot_scaler = MinMaxScaler()
  bar_data = experiments[bar_items].dropna()
#
# preserve the index becuase it is used to identify the 
# labeled experiment in the bar plots
#  
  bar_index = bar_data.index
  bar_data = pd.DataFrame(plot_scaler.fit_transform(bar_data))
  bar_data.set_index(bar_index, drop = True, inplace = True)
#
# format the bar_labels then add them to the DataFrame
#  
  bar_labels = format_bar_labels(bar_labels, plot_scaler)
  bar_data.columns = bar_labels
#
# note that other logic could be applied here
#
  experiment = labeled_experiment
  fig, ax = plt.subplots(figsize = (9, 9))
  if experiment == best_experiment:
    fig.suptitle(name +  '_exp_' +  str(best_experiment) +
                 '** best experiment', color = 'red')
  else:
    fig.suptitle(name +  '_exp_' +  str(experiment))
#
# generate the plots
#    
  ax.boxplot(bar_data)
#
# add the formatted labels
#
  ax.set_xticklabels(bar_labels, rotation = 90, fontsize = 8)
#
# add the labeled run
#  
  values = experiments[bar_items].loc[experiment, :]
  for value in range(values.shape[0]):
    ax.scatter(value + 1,
               bar_data.loc[experiment, bar_labels[value]],
               color = 'red')
#
# labels and titles
#    
  ax.set_ylabel('normalized values', fontsize = 8)
  ax.set_title('boxplot of all experiments\n' +
               'this run shown as red points', fontsize = 10)
#
# return the figure to be used elsewhere
#  
  return fig