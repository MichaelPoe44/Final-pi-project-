#for use in the gui
import requests

response = requests.get("http://192.168.1.180:8000/signal")

if response.status_code == 200:
    recieved_data = response.json
    print("recieved data")
    #unlock box
else:
    print("recieved no data")
    #do nothing
