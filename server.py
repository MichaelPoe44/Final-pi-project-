from flask import Flask, request

app = Flask(__name__)
Condition_met = False
counter = 0

@app.route('/signal',methods=['POST'])
def receive_signal():
    # global Condition_met
    # data = request.json
    # if data["condition_met"]==True:
    #     print("received signal:", data)
    #     Condition_met = True

    # else:
    #     print("codition not met")
    #     Condition_met = False
    global counter 
    counter += 1
    print("recieved signal")
    if counter % 2 == 1:
        Condition_met = True
    else:
        Condition_met = False
    print(Condition_met)
    return "signal recieved successfully", 200

@app.errorhandler(404)
def not_fount(error):
    global counter
    global Condition_met
    counter += 1
    print(counter)
    if counter % 2 == 1:
        Condition_met = True
    else:
        Condition_met = False
    return '404 not found', 404





@app.route('/signal',methods=['GET'])
def get_signal():
    if Condition_met:
        return "Recieved GET request", 200
    else:
        print("test")
        return "Condition not met", 201

