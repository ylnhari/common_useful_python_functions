def list_all_files_with_sepcific_extension_under_a_root_directory():
  """List all files under a root directory belonging to a specific Extension and save them as a list.
  """
  import glob
  root_path = r"C:\Users\laxmi.n.yelesetty\Downloads\transportplandata"
  file_extension = ".json"
  json_files = glob.glob(f"{root_path}\**\*{file_extension}", recursive=True)
  print(f"There are a total of {len(json_files)} Files in under the root path")

  
def progress_bar_for_your_loop():
  """Adding Progress BAr to you loop.
  
  When running big loops we may wan't to see the progress of the run
  we have tqdm library to do so , Following code has to be addded to
  your loop, if tqdm was not installed you can use `pip3 install tqdm`
  """
  from tqdm import tqdm
  any_range_you_want = range(0, 100)
  for i in tqdm(any_range_you_want, desc ="Text to be displayed beside progress bar"):
    """write your code"""
    pass
