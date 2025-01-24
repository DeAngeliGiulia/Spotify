import request
def richiesta():
    response = requests.get('http://open-notify.org/Open-Notify-API/People-In-Space/') # richiedo i dati
    data = response.json() # da json a dict python
    return data.get('people', [])