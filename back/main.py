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
            point_B = form.location_B.data
            k_A = get_loc_code_by_coords(point_A)[0]  # Получаем код местоположения по координатам
            k_B = get_loc_code_by_coords(point_B)
            response_A = get_weather_data(k_A)  # Получаем данные о погоде
            response_B = get_weather_data(k_B)  # Получаем данные о погоде
            analize = check_bad_weather(response)  # Анализируем данные о погоде
            return jsonify(analize)  # Возвращаем анализ в формате JSON
    return render_template('main.html', form=form)  # Отображаем форму при GET-запросе


if __name__ == "__main__":
    app.run()
