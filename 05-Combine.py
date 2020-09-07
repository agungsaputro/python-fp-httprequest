import requests
import json

urlPost = "https://jsonplaceholder.typicode.com/posts"
urlUser = "https://jsonplaceholder.typicode.com/users"


def combine (urlPost,urlUser):
    post = requests.get(urlPost).json()
    user = requests.get(urlUser).json()

    for p in post:
        p['user'] = [u for u in user if u['id'] == p['userId']] 
        result = json.dumps(p, indent=6)
        print(result)
    
    return combine

combine(urlPost,urlUser)
