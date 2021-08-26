from requests import get, post, head
from time import time
SECRET="APIKEYHERE"
HEADERS = {"TRN-Api-Key":SECRET}
URL="https://public-api.tracker.gg/v2/splitgate/standard/profile/PLATFORM/USERNAMEORID"
def save(data):
  with open('data.py','w')as file:
    file.write(f'A={data}')
def load():
  try:return __import__('data').A
  except ImportError:
    data={}
    save(data)
    return data
minutes = lambda n:n*60
while True:
    
    responce = get(URL, headers=HEADERS)
    
    data=(responce.json())
    
    save(data)
    data=load()
    print('UPDATED')
    
    for thing in 'kills', 'teabags', "deaths", "headshotKills":
      result = data['data']['segments'][0]['stats'][thing]['value']
      with open(f"{thing}.txt",'w')as file:file.write(str(result))
    now = time()
    while time()-now < minutes(1):...