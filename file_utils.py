"""Utilities for file operations."""

def list_all_files_with_sepcific_extension_under_a_root_directory():
  """List all files under a root directory belonging to a specific Extension and save them as a list.
  """
  import glob
  root_path = r"C:\Users\laxmi.n.yelesetty\Downloads\transportplandata"
  file_extension = ".json"
  json_files = glob.glob(f"{root_path}\**\*{file_extension}", recursive=True)
  print(f"There are a total of {len(json_files)} Files in under the root path")

def save_xls(dict_df, path):
    """Save a dictionary of dataframes to an excel file, with each dataframe as a separate page.
    Parameters
    ----------
        dict_df : python dict
            dictionary of dataframes
        path : Pathlib.Path or str
            path of the excel file
    """

    with ExcelWriter(path) as writer:  # initialize Excel writer
        for key in dict_df:  # save each DataFrame
            print(f"Saving DataFrame  {key}")
            dict_df[key].to_excel(writer, key)

    print(f"Successfully saved File at {path}")
