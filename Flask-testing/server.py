from flask import Flask, request

app = Flask(__name__)

@app.route('/signal',methods=['POST'])
def receive_signal():
    data = request.json
    if "condition_met" in data:
        print("received signal:", data)
    else:
        print("codition not met")
    return "signal recieved successfully", 200

#if __name__ == "__main__":
   # app.run(debug=True, host="0.0.0.0", port=5000)