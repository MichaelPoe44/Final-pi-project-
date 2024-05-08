import requests

def Condition_met():
    url = 'http://172.20.10.2:8000'
    data = {'condition_met':True}
    response = requests.post(url,json=data)
    if response.status_code:
        print("signal sent successfully")
    else:
        print("Failed to send Condition met")

def Condition_not_met():
    url = 'http://172.20.10.2:800/signal' #replace with active server
    data = {'conditon_met': False} 
    response = requests.post(url,json=data)
    if response.status_code == 200:
        print("signal sent successfully")
    else:
        print("Failed to send Condition not met")

if __name__ == '__main__':
    Condition_met()
    #Condition_not_met()