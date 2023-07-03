import requests
import json
import time
import hashlib
import cped


marvel_url = "https://gateway.marvel.com/v1/public"
characters_endpoint = "characters"
private_key = cped.pr001
public_key = cped.pu002

timestamp = str(int(time.time()))

hash_value = hashlib.md5(f"{timestamp}{private_key}{public_key}".encode()).hexdigest()

character_list_url = f"{marvel_url}/{characters_endpoint}"

parameters = {
    "apikey": public_key,
    "ts": timestamp,
    "hash": hash_value,
    "limit": 100,  # Number of results per page
    "offset": 0   # Initial offset
}

character_dict = {}

while True:
    # Send GET request to get the character list
    response = requests.get(character_list_url, params=parameters)

    # Parse the response JSON
    data = response.json()

    for character in data["data"]["results"]:
        character_info = {
            "name": character["name"],
            "id": character["id"]
        }
        character_dict[character["id"]] = character_info

    if len(data["data"]["results"]) < parameters["limit"]:
        # Reached the last page, break the loop
        break

    parameters["offset"] += parameters["limit"]

with open("character_list.json", "w") as character_file:
    json.dump(character_dict, character_file)

print("Character list retrieved successfully.")
