import requests

def richiesta():
    response = requests.get('http://api.open-notify.org/astros.json') # richiedo i dati
    print(response.text)  # Print the response content to see what was returned

    data = response.json() # da json a dict python
    return data.get('people', [])