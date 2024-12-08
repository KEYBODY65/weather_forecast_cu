from flask import Flask, jsonify
from req import req, get_weather_data, get_loc_code_by_coords
from check_models import check_bad_weather

app = Flask(__name__)
app.config["SECRET_KEY"] = ""

@app.route("/")
def main():
    g = req('Москва')
    k = get_loc_code_by_coords(g)[0]
    response = get_weather_data(k)
    return jsonify(response)




if __name__ == "__main__":
    app.run()
