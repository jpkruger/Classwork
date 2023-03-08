from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server On"


@app.route("/info", methods=["GET"])
def info_route():
    return "This server was written for BME547"


@app.route("/HDL_analysis", methods=["POST"])
def HDL_route_handler():
    """
    in_data = {"name": <patient_name>,
               "HDL_value": <HDL_result>"}
    """
    from bloodcalculator import HDL_analysis
    in_data = request.get_json()
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis


@app.route("/add", methods=["POST"])
def add_route_handler():
    data = request.get_json()
    result = data["a"] + data["b"]
    if result < 0:
        return "The answer was less than zero, BAD", 400
    return jsonify(result)


@app.route("/add_two/<a>/<b>", methods=["GET"])
def add_two_handler(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()
