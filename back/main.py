from flask import Flask, jsonify, json
from req import req, get_weather_data


app = Flask(__name__)
app.config["SECRET_KEY"] = "yfdwk64qowyerhr124429478293"

@app.route("/")
def main():
    return json.dumps(get_weather_data(), indent=4)




if __name__ == "__main__":
    app.run()
