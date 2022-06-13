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
