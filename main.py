import requests

try:
    request = requests.get("https://www.omdbapi.com/?t=intersteller")
except:
    print("Error network")
    exit()

print(request.text)