import requests

api_key = '0RvWYG0TzMAt1XOemk0dwSBWGyAjKVjs'
city = 'Москва'
location_url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}&language=ru'


def req():
    try:
        response = requests.get(location_url)
        data = response.json()
        if data:
            return data[0]['Key']
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
        return None

def get_weather_data():
    k = req()
    weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{k}?apikey={api_key}&details=true'
    try:
        weather_r = requests.get(weather_url)
        print(weather_r)
        weather_data = weather_r.json()[0]
        temperature_celsius = weather_data['Temperature']['Metric']['Value']
        humidity_percentage = weather_data['RelativeHumidity']
        wind_speed_ms = weather_data['Wind']['Speed']['Metric']['Value'] * 0.277778
        precipitation_probability = 0 if not weather_data['HasPrecipitation'] else 100
        wet_info = {
            'temperature_celsius': temperature_celsius,
            'humidity_percentage': humidity_percentage,
            'wind_speed_ms': wind_speed_ms,
            'precipitation_probability': precipitation_probability
        }
        return wet_info
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса погода: {e}")


