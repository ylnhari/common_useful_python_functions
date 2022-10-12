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

def check_for_null_values_remove_from_dataframe(df):
    """
      Check dataframe columns or rows containing null values in them and remove them 
      -> atleast one null values in rows
      -> all values of a row are null
      -> atleast one null value in columns
      -> all values in the column are null
     Parameters
     ----------
      df : (pandas dataframe)
    """
    # atleast one null values in rows
    rows_with_atleast_one_null_value = df.isnull().any(axis=1)
    # remove rows with atleast one null value
    d = d[~rows_with_atleast_one_null_value]
    
    # all values of a row are null
    rows_with_all_null_values = df.isnull().all(axis=1)
    # remove rows with all null values
    df = df[~rows_with_all_null_values]
    
    # atleast one null value in columns
    columns_with_atleast_one_null_value = df.isnull().any(axis= 0)
    # remove columns with atleast one numm value in them
    df = df.loc[:,~columns_with_atleast_one_null_value]
    
    # all values in the column are null
    columns_with_all_null_values = df.isnull().all(axis= 0)
    # remove columns with all null values
    df = df.loc[:,~columns_with_all_null_values]
    
    
def change_datatype_of_a_df_column(df, col_name, dtype_string):
  """Change the Column  dtype.
  
  supported dtype_strings are:- 'category', 'boolean','string','object','int', 'float', 'datetime64[ns, <tz>]', period[<freq>]',
  'Sparse', 'Sparse[int]', 'Sparse[float]', 'interval', 'Interval', 'Interval[<numpy_dtype>]', 'Interval[datetime64[ns, <tz>]]', 
  'Interval[timedelta64[<freq>]]', 'Int8', 'Int16', 'Int32', 'Int64', 'UInt8', 'UInt16', 'UInt32', 'UInt64', 'Int8', 'Int16', 'Int32', 
  'Int64', 'UInt8', 'UInt16', 'UInt32', 'UInt64' 
  
  Parameters
  ----------
    df : (pandas dataframe)
    col_name : (str) name of the column
    dtype_string : (str) Name of the string identified of pandas supported datatype
    
  have a look at :- https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes
  """
    df[col_name] = df[col_name].astype(dtype_string)
    # exanple :- convert Data type of Column to integer
    #            df[col_name] = df[col_name].astype("int")
    return df
    
def set_pandas_options():
  pd.set_option("display.max_rows", None) # show all rows in a jupyter cell.
  pd.set_option("display.max_columns", None) # show all columns in a jupyter cell.
  pd.set_option("display.max_colwidth", None) # show all data in a cell of dataframe.

