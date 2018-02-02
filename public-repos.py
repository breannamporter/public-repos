import requests
import sys

# build request url from input
username = sys.argv[1]
URL = "https://api.github.com/users/" + username + "/repos"

# get repo data from api
r = requests.get(url = URL)
data = r.json()

# print public repo names
for i in range (len(data)):
    print (data[i]['name'])
