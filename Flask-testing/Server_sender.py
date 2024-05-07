import requests

def Condition_met():
    url = 'http://192.168.1.180:800/signal' #replace with active server
    data = {'conditon_met': True} 
    response = requests.post(url,json=data)
    if response.status_code == 200:
        print("signal sent successfully")
    else:
        print("Failed to send Condition met")

def Condition_not_met():
    url = 'http://192.168.1.180:800/signal' #replace with active server
    data = {'conditon_met': False} 
    response = requests.post(url,json=data)
    if response.status_code == 200:
        print("signal sent successfully")
    else:
        print("Failed to send Condition not met")

if __name__ == '__main__':
    Condition_met()
    #Condition_not_met()