import requests
import json

def requisition(title):
    try:
        request = requests.get('http://www.omdbapi.com/?t=' + title)
        dictionary = json.loads(request.text)
        return dictionary
    except:
        print("Error network")
        return None

exit = False
while not exit:
    write = input("Type a movie name or EXIT to close")

    if exit == 'EXIT':
        exit = True
    else:
        movie = requisition(write)

print("Title:", movie['Title'])
print("Year:", movie['Year'])
print("Director:", movie['Director'])
print("Actors:", movie['Actors'])