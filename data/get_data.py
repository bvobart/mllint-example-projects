"""Downloads data.xml from my personal Google Drive"""
import os
import re
import requests

url = 'https://drive.google.com/uc?export=download&id=1Q3lpw9yA3SwGhmisOTGzgi6I0RjjUmjG'
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.xml') # ./data.xml relative to this file

# Downloading file from Google Drive requires a session with cookies so that Google's no antivirus notification can be confirmed.
with requests.Session() as sess:
  confirm = sess.get(url)
  confirm_code = re.search('confirm=(.+)&amp;id=', confirm.text).group(1)

  data = sess.get(f"{url}&confirm={confirm_code}")
  with open(filename, 'wb') as f:
    f.write(data.content)
