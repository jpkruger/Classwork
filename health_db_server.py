"""
Database = Dictionary
keys -> ids for the patients
value: int

{1: {"id": 1, "name": "Jackson", "blood_type": "O+"},
 2: {"id": 2, "name": "Jackson", "blood_type": "O+"},
 3: {"id": 3, "name": "Jackson", "blood_type": "O+", "tests": []}


"""
from flask import Flask, request, jsonify
from pymodm import connect
from PatientModel import Patient
from pymodm import errors as pymodm_errors
from secrets import mongodb_acct, mongdb_pswd


app = Flask(__name__)


def init_server():
    connect("mongodb+srv://{}:{}@bme547.axizgtv"
            ".mongodb.net/healthdb?retryWrites=true&w=majority"
            .format(mongodb_acct, mongdb_pswd))


def add_patient_to_db(id, name, blood_type):
    new_patient = Patient(patient_id=id, patient_name=name,
                          blood_type=blood_type)
    saved_patient = new_patient.save()
    return saved_patient


def add_test_to_db(id, test_name, test_result):
    x = Patient.objects.raw({"_id": id}).first()
    x.tests.append((test_name, test_result))
    x.save()


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
    try:
        db_item = Patient.objects.raw({"_id": id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return True


def validate_input_data_generic(in_data, expected_keys, expected_type):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_type):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
    answer, status = get_results_driver(patient_id)
    return jsonify(answer), status


def get_results_driver(patient_id):
    # validation = validate_patient_id_from_get(patient_id)
    # if validation is not True:
    #     return validation, 400
    # patient = db[int(patient_id)]
    # return patient["tests"], 200
    pass


def validate_patient_id_from_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        return "Patient id should be an integer"
    if does_patient_exist_in_db(patient_num) is False:
        return "Patient id of {} does not exist in database"\
            .format(patient_num)
    return True


if __name__ == '__main__':
    init_server()
    app.run()
