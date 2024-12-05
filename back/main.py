from flask import Flask
from req import req, get_weather_data


app = Flask(__name__)
app.config["SECRET_KEY"] = "yfdwk64qowyerhr124429478293"

@app.route("/")
def main():
    print(get_weather_data())
    return "Hello, World!"




if __name__ == "__main__":
    app.run()
