"""This Module Contains common useful function related to pandas"""

from datetime import datetime, date
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
import pandas as pd

def check_if_pandas_column_has_only_alphanumeric_values(data_frame):
  """
  check for presence of only alphanumeric values in a panda data frame 
  object, categoryDtype  columns
  Parameters
  ----------
  data_frame : pd.dataframe
      a pandas data frame
  Returns
  -------
      boolean value
  """
  columns_to_check_for_alphanumeric = data_frame.select_dtypes(['object','category']).columns.to_list()
  for column in columns_to_check_for_alphanumeric:
    if data_frame[column].apply(lambda x : x.isalnum()).any():
      print(f"Some Rows of Column {column} have invalid values")


def get_categorical_columns(df):
  """
    Parameters
    ----------
      df : (pandas dataframe) 
    Returns
    -------
      list of column Names
  """
    return list(df.select_dtypes(include=['object']).columns)


def get_numerical_columns(df):
  """
    Parameters
    ----------
      df : pandas dataframe
    Returns
    -------
      list of column Names
  """
    return list(df.select_dtypes(include=['float64', 'float32', 'int32', 'int64']).columns)
