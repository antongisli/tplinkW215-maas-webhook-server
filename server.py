from flask import Flask
from flask import jsonify
from flask import Response
import time

from pyW215.pyW215 import SmartPlug, ON, OFF

app = Flask(__name__)

# Fill in your smartplug details here
sp = SmartPlug('x.x.x.x', '123456')

# Where 123456 is the "code pin" printed on the setup card, x.x.x.x = ip address

# Get values if available otherwise return N/A
print(sp.current_consumption)
print(sp.temperature)
print(sp.total_consumption)
print(sp.state)

# Turn switch on and off

#sp.state = ON
#sp.state = OFF

@app.route('/power_on/', methods=['POST'])

def power_on():

    sp.state = ON

    return Response("{}", status=200, mimetype='application/json')



@app.route('/power_off/', methods=['POST'])

def power_off():
    sp.state = OFF
    time.sleep(30)
    return Response("{}", status=200, mimetype='application/json')



@app.route('/status/', methods=['GET'])
def power_status():
    if sp.state == OFF:
        return jsonify({"power_state": "stopped"})
    else:
        return jsonify({"power_state": "running"})



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=1800)

