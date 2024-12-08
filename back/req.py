import requests
API_KEY = 'd9E3GspKBOCQyA5I9MIpBldoilHzbfwy'



def req(city):
    location_url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city}&language=ru'
    try:
        response = requests.get(location_url)
        data = response.json()
        if data:
            lat = data[0]['GeoPosition']['Latitude']
            long = data[0]['GeoPosition']['Longitude']
            return [lat, long]
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
        return None

def get_loc_code_by_coords(city):
    city_cor = f'{city[0]},{city[1]}'
    location_url = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={city_cor}'
    try:
        response = requests.get(location_url)
        data = response.json()
        if data:
            return [data['Key'], data['AdministrativeArea']['LocalizedName']]
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
        return None




    

def get_weather_data(loc_key):
    '''Фукция получения данных о погоде'''
    weather_url = f'http://dataservice.accuweather.com/currentconditions/v1/{loc_key}?apikey={API_KEY}&details=true' # запрос к api
    try:
        weather_r = requests.get(weather_url) # гет-запрос к api
        weather_data = weather_r.json()[0]
        temperature_celsius = weather_data['Temperature']['Metric']['Value']
        humidity_percentage = weather_data['RelativeHumidity']
        wind_speed_kh = weather_data['Wind']['Speed']['Metric']['Value']
        precipitation_probability = 0 if not weather_data['HasPrecipitation'] else 100
        wet_info = {
            'temperature_celsius': temperature_celsius,
            'humidity_percentage': f'{humidity_percentage}%',
            'wind_speed_kh': wind_speed_kh,
            'precipitation_probability': precipitation_probability
        }
        return wet_info
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса погода: {e}")