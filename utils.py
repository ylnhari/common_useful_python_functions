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

 def str2bool(string_value):
    """
    Convert a String to a boolean value.

    Parameters
    ----------
    string_value : string_value
        a python string object

    Returns
    -------
        boolean value
    """
    return string_value.lower() in ("yes", "true", "t", "1")

def send_message_to_slack():
  """
  From your workflows you may need to post messages to slack about 
          notifying about the run status of your programs, 
          sharing results/records created etc.
  This Function helps you in acheiving it.     
  """
  import sys
  import logging
  import json
  import requests
  
  # webhook_url (str) : a url of the incoming webhook of the slack pointing towards a channel.
  # see this article for webhook creation -> https://slack.com/intl/en-in/help/articles/115005265063-Incoming-webhooks-for-Slack
  webhook_url =  "https://hooks.slack.com/services/*******"

  # message you need to send
  message = "what you want to display in slack"
  
  # you can create rich, interactive UI based messages , pictures etc 
  # use this to create a the body for the above mentioned types of messages -> https://app.slack.com/block-kit-builder
  # prepare body for a post request
  body = {
    "attachments": [
      {
        "blocks": [
          {
            "text": {
              "text": f"{message}",
              "type": "mrkdwn"
            },
            "type": "section"
          }
        ],
        "color": "#9733EE"
      }
    ]
  }
  # prepare headers
  byte_length = str(sys.getsizeof(body))
  headers = {'Content-Type': "application/json",
             'Content-Length': byte_length}
  # send a post request
  response = requests.post(webhook_url, data=json.dumps(body), headers=headers)

  if response.status_code != 200: # if message is not successfully sent
      logging.error("Log you error")
      # perform necessary error handling

      
def get_latitude_longitude_from_address(address):
  """This Function helps to Fetch Latitide and Longitude values for a given address from the google Maps API's
  Inorder to use this function we need a Google Maps API account setup and an Access Key.
  More About the setup can be found here -> https://developers.google.com/maps/get-started
  Parameters
  ----------
  address : (str) address of the location.
  Returns
  -------
  tuple : latitude(str), longitude(str)
  """
  import googlemaps
  gmaps = googlemaps.Client(key='Add your Key')
  geocode_result = gmaps.geocode(address)
  latitude  = geocode_result[0]['geometry']['location']['lat']
  longitude = geocode_result[0]['geometry']['location']['lng']
  return latitude, longitude


def get_latitude_longitude_from_address_with_exception_handling(addresses):
  """Typically we may need to extract coordinates for multiple locations at the same time so there
  are high chances of failure while calling Google Map GeoDecode API.So this function helps us 
  to process addresses sequencially and save the results in a file either in case of execptions or successfull run.
  This Function also helps to resume the activity after clearing the exception by fetching the saved
  co-ordinates file and processing only those addresses which are not already processed.
  Parameters
  ----------
  addresses : (list) a python list of address(str) of the location.
  Functions called
  ----------------
  get_latitude_longitude_from_address
  """
  from pathlib import Path
  import pandas as pd
  from tqdm import tqdm
  name_of_the_file_to_save = "your_file_name.csv"
  # Fetch any existing processed records
  if Path(name_of_the_file_to_save).exists():
      # read already fetched files
      location_coordinates_df = pd.read_csv(name_of_the_file_to_save)
      # create dataframe of fetched locations
      locations_already_processed = location_coordinates_df["Name"].to_list()
  else: # if there are no  pre fetched locations
      # create empty data frame to fetch locations
      locations_already_processed = []
      location_coordinates_df = pd.DataFrame(columns = ['Name', 'latitude', 'longitude'])

  # Fetch Location Coordinates
  try:
      for location_address in tqdm(addresses): # for every location
          if location_address not in locations_already_processed: # if it is not pre fetched
              latitude, longitude = get_latitude_logitude(location_address) # get coordinates
              # append coordinates to dataframe
              location_coordinates_df = location_coordinates_df.append({'Name' : location_address, 'latitude' : latitude, 'longitude' : longitude},
                                                                      ignore_index = True)
              locations_already_processed.append(location_address)
      print("All addresses fetched successfully !!!")
  except Exception as e: # if error occured while calling Google API
      print(f"Error Occured While Processing address {location_address}")
      print(f"Error : {e}")
  finally:
      # Finally Save File
      location_coordinates_df.to_csv(name_of_the_file_to_save, index=False)
      print(f"Fetched Coordinates saved to file {name_of_the_file_to_save}")
      
      
def get_curr_date_and_time():
    """
        Function to fetch current date and time
        return(str):
            data and time as a string
    """
    from datetime import datetime, date
    return date.today().strftime("%d/%m/%Y") + " " + datetime.now().strftime("%H:%M:%S")
