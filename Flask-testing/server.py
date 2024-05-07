from flask import Flask, request

app = Flask(__name__)
Condition_met = False


@app.route('/signal',methods=['POST'])
def receive_signal():
    global Condition_met
    data = request.json
    if data["condition_met"]==True:
        print("received signal:", data)
        Condition_met = True


    else:
        print("codition not met")
        Condition_met = False
    return "signal recieved successfully", 200

@app.route('/signal',methods=['GET'])
def get_signal():
    if Condition_met:
        return "Recieved GET request", 200
    else:
        return "Condition not met", 201

