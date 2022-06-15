"""This Module Contains common useful function related to pandas"""


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
