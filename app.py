from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = "a6311858fb35df63b55216bae4aa952a"


@app.route('/')
def home():
    # URL to fetch the weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API_KEY}&units=metric"
    # Make a request to the OpenWeatherMap API
    response = requests.get(url)
    weather_data = response.json()
    # Extract the temperature and weather description
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    # Return the weather data in HTML format
    return render_template_string("<h1>Current weather in London, UK</h1><p>Temperature: "
                                  "{{temperature}}°C<br>Description: {{description}}</p>",
                                  temperature=temperature, description=description)


@app.route('/ping')
def ping():
    # Return PONG in HTML format
    return "<h1>PONG</h1>"

@app.route('/health')
def health():
    # Return HEALTHY in JSON format
    return jsonify(status="HEALTHY")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
