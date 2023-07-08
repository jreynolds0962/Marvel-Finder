import requests
import cped
from heroList import hero_list


def get_power_stats(character):
    # lowercase full list of characters in list
    lowered = [x.lower() for x in hero_list]
    
    if character.lower() in lowered:
        base_url = "https://superheroapi.com/api/"
        key = cped.TOKEN
        
        id = lowered.index(character.lower()) + 1

        # for char in lowered:
        #     print(str(lowered.index(char) + 1) + ": " + char)

        full_url = base_url + key + "/" + str(id) + "/powerstats"
        response = requests.get(full_url)

        if response.status_code == 200: 
            data = response.json()
            
            return data
        else:
            print("An error has occured: " + str(response.status_code))
            return "Warning: API error"
    else:
        return "Warning: Could not find character in character list. Please input a different character name."


