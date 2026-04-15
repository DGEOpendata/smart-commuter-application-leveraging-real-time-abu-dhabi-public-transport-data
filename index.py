python
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the base URL for the Real-time Public Transport API
API_BASE_URL = "https://api.transport.abudhabi.ae/realtime"

# Example endpoint for fetching real-time bus location data
def get_bus_data(route_id):
    endpoint = f"{API_BASE_URL}/buses/{route_id}"
    response = requests.get(endpoint, headers={"Authorization": "Bearer YOUR_API_KEY"})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data."}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_bus_info', methods=['POST'])
def get_bus_info():
    route_id = request.form['route_id']
    bus_data = get_bus_data(route_id)
    return render_template('bus_info.html', bus_data=bus_data)

if __name__ == "__main__":
    app.run(debug=True)
