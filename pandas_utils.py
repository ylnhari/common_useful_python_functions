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
  
  
  def load_a_csv_with_index_if_exists_else_create_empty_dataframe(csv_file_path, column_list, index_axis_name):
    """Load a csv file from specified location of exists else create an empty dataframe 
       with give column name and index axis name. Remove (.rename_axis()) if you don't want index
       axis to have a name (a default range index will be created) and then append new rows to the dataframe
       Parameters
       ----------
       csv_file_path : (str)  path to csv file
       column_list : (list) list of column names(str)
       index_axis_name : (str) name wanted for the index column
    """
    from pathlib import Path
    import pandas as pd
    
    if Path(csv_file_path).exists(): # load csv file if path exists 
        df = pd.read_csv(csv_file_path, index_col = 0)  #here first column is considered as index (remove index_col if not required)
    else:
        df = pd.DataFrame(columns = column_list).rename_axis(index_axis_name) # Remove (.rename_axis()) if you don't want index axis to have a name
        
    # append rows to data frame by using index -> df.loc[index_value]  = [list of column values] or pandas series of values (whose length must be the number of columns)
    # insert a value into a cell -> df.loc[index_value, column_name] = value
    # create new column into the dataframe -> df[new_column_name] = [list of column values] or pandas series of values (whose length must be the number rows of dataframe)
        
