from flask import Flask, jsonify, request, render_template
from req import req, get_weather_data, get_loc_code_by_coords
from check_models import check_bad_weather
from forms.main_form import LocationForm

app = Flask(__name__, template_folder='/home/misha/Документы/Python_Projects/weather-forecast/templates', static_folder='/home/misha/Документы/Python_Projects/weather-forecast/static')
app.config["SECRET_KEY"] = "yfdwk64qowyerhr124429478293"

@app.route("/", methods=['GET', 'POST'])
def main():
    form = LocationForm()
    analize = {}
    if request.method == "POST":  # Проверяем, был ли отправлен POST-запрос
        if form.validate_on_submit():  # Проверяем, что форма валидн
            point_A = form.location_A.data  # Получаем данные из поля location_A
            point_B = form.location_B.data # Получаем данные из поля location_B
            k_A = get_loc_code_by_coords(req(point_A))[0]  # Получаем код местоположения по координатам A
            k_B = get_loc_code_by_coords(req(point_B))[0] # Получаем код местоположения по координатам B
            response_A = get_weather_data(k_A)  # Получаем данные о погоде A
            response_B = get_weather_data(k_B)  # Получаем данные о погоде B
            print(response_B)
            analize_A = check_bad_weather(response_A)  # Анализируем данные о погоде A
            analize_B = check_bad_weather(response_B)  # Анализируем данные о погоде A
            weather_data = {
            f'Анализ погодных условий в городе: {point_A}':{
            'temperature_celsius': response_A['temperature_celsius'],
            'precipitation_probability': response_A['precipitation_probability'],
            'humidity_percentage': response_A['humidity_percentage'],
            'wind_speed': response_A['wind_speed'],
            'analyze': analize_A
            },

            f'Анализ погодных условий в городе: {point_B}':{
            'temperature_celsius': response_B['temperature_celsius'],
            'precipitation_probability': response_B['precipitation_probability'],
            'humidity_percentage': response_B['humidity_percentage'],
            'wind_speed': response_B['wind_speed'],
            'analyze': analize_B}
            }
            return render_template('weather.html', data=weather_data)  # Отображаем данные о погоде
    return render_template('main.html', form=form)  # Отображаем форму при GET-запросе


if __name__ == "__main__":
    app.run()
