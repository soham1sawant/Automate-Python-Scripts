# number_of_astronauts_in_ISS.py

import requests, json

def get_people():
    response = requests.get("http://api.open-notify.org/astros.json")

    if response.status_code == 200:
        people = response.json()["number"]
        return people
    else:
        return 'Error'

success = get_people()

if success != 'Error':
    print("The number of Astronauts on the ISS is : ",success)
else:
    print("Error! retrieving information")