from flask import Flask, jsonify, json
from req import req, get_weather_data, get_loc_code_by_coords


app = Flask(__name__)
app.config["SECRET_KEY"] = ""

@app.route("/")
def main():
    g = req('Москва')
    k = get_loc_code_by_coords(g)[0]
    return json.dumps(get_weather_data(k), indent=4)




if __name__ == "__main__":
    app.run()
