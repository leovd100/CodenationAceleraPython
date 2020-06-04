import requests
import hashlib

#print(hashlib.sha1(b"good is the enemy of great, but great is the enemy of shipped. jeffrey zeldman").hexdigest())


url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=8e31f890912b404a2f156ac619f31a5fea0da5b7'
files = {'answer': open('answer.json', 'rb')}
headers = { 'content-type': 'multipart/form-data' }
#
# answer = open('answer.json','r')
# print(answer)

r = requests.post(url, headers,files = files)
print(r.status_code)
print(r.text)