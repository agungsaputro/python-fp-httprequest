import requests
import json

urlPost = "https://jsonplaceholder.typicode.com/posts"
urlUser = "https://jsonplaceholder.typicode.com/users"
post = requests.get(urlPost).json()
user = requests.get(urlUser).json()

for p in post:
    p['user'] = [u for u in user if u['id'] == p['userId']] 
    dumps = json.dumps(p, indent=6)
    print(dumps)
