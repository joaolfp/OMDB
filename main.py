import requests
import json

try:
    request = requests.get('http://www.omdbapi.com/?t=interstellar')
except:
    print("Error network")
    exit()

dictionary = json.loads(request.text)

print("Title:", dictionary['Title'])
print("Year:", dictionary['Year'])
print("Director:", dictionary['Director'])
print("Actors:", dictionary['Actors'])