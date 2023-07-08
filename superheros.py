import requests
import cped
from heroList import hero_list

base_url = "https://superheroapi.com/api/"
key = cped.TOKEN

# lowercase full list of characters in list
lowered = [x.lower() for x in hero_list]
character = "nebula"
id = lowered.index(character.lower()) + 1

# for char in lowered:
#     print(str(lowered.index(char) + 1) + ": " + char)

full_url = base_url + key + "/" + str(id) + "/powerstats"

response = requests.get(full_url)

if response.status_code == 200: 
    data = response.json()
    
    print(data)
else:
    print("An error has occured: " + str(response.status_code))