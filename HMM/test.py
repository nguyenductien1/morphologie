import requests
data = open('/Users/dtn/Desktop/Modele/jeux_videos_update.n3').read()
headers = {'Content-Type': 'text/n3;'}
r = requests.post('http://localhost:3030/ds_jeux/data', data=data, headers=headers)