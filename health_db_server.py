"""
Database = Dictionary
keys -> ids for the patients
value: int

{1: {"id": 1, "name": "Jackson", "blood_type": "O+"},
 2: {"id": 2, "name": "Jackson", "blood_type": "O+"},
 3: {"id": 3, "name": "Jackson", "blood_type": "O+", "tests": []}


"""
from flask import Flask, request, jsonify


db = {}


app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id, "name": name,
                   "blood_type": blood_type, "tests": []}
    db[id] = new_patient
    print(db)


def add_test_to_db(id, test_name, test_result):
    db[id]["tests"] = {"id": id, "test_name": test_name,
                       "test_result": test_result}
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    # Call other functions to do the work
    answer, status_code = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    # Validate input
    expected_keys = ["name", "id", "blood_type"]
    expected_type = [str, int, str]
    validation = validate_input_data_generic(in_data,
                                             expected_keys, expected_type)
    if validation is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return an answer
    return "Patient successfully added", 200


@app.route("/add_test", methods=["POST"])
def post_test_result():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def add_test_driver(in_data):
    expected_keys = ["id", "test_name", "test_result"]
    expected_type = [int, str, int]
    validation = validate_input_data_generic(in_data,
                                             expected_keys, expected_type)
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"\
            .format(in_data["id"]), 400
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test successfully added", 200


def does_patient_exist_in_db(id):
    if id in db:
        return True
    else:
        return False


def validate_input_data_generic(in_data, expected_keys, expected_type):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_type):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


if __name__ == '__main__':
    app.run()
