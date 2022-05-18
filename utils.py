def list_all_files_with_sepcific_extension_under_a_root_directory():
  """List all files under a root directory belonging to a specific Extension and save them as a list.
  """
  import glob
  root_path = r"C:\Users\laxmi.n.yelesetty\Downloads\transportplandata"
  file_extension = ".json"
  json_files = glob.glob(f"{root_path}\**\*{file_extension}", recursive=True)
  print(f"There are a total of {len(json_files)} Files in under the root path")
