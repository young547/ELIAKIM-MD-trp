
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = '3ee0235659823323bbb8cf218e85098f'  # Your Numverify key

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.json
    phone = data.get('phone_number')
    if not phone:
        return jsonify(error="Phone number is required"), 400

    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone}"
    resp = requests.get(url)
    info = resp.json()

    if not info.get('valid'):
        return jsonify(error="Invalid phone number")

    result = {
        'country': info.get('country_name'),
        'location': info.get('location'),
        'carrier': info.get('carrier'),
        'line_type': info.get('line_type')
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
