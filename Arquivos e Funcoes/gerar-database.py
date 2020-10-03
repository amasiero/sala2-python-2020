import requests
import json

results = requests.get(
    'https://randomuser.me/api/?results=100&seed=fullstackio&nat=gb,us,de,br')
contacts = json.loads(results.content)

list_contacts = contacts['results']

with open('database.csv', 'w') as file:
    file.write('name, email, cell, phone\n')
    for contact in list_contacts:
        file.write(
            f'{contact["name"]["first"]} {contact["name"]["last"]},{contact["email"]},{contact["cell"]},{contact["phone"]}\n')
