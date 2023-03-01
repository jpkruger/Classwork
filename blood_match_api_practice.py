import requests


def blood_match_driver():
    url = "http://vcm-7631.vm.duke.edu:5002"
    patients = get_patient(url)
    donor_blood_type = get_blood_types(url, patients.get("Donor"))
    recipient_blood_type = get_blood_types(url, patients.get("Recipient"))
    result = is_match(donor_blood_type, recipient_blood_type)
    check_result(url, result)


def get_patient(url):
    r = requests.get(url+"/get_patients/jpk41")
    patients = r.json()
    return patients


def get_blood_types(url, id):
    r = requests.get(url + "/get_blood_type/" + id)
    blood_type = r.text
    return blood_type


def is_match(bt_1, bt_2):
    if bt_1 == bt_2:
        result = "Yes"
    elif bt_1 != bt_2:
        result = "No"
    return result


def check_result(url, result):
    result_check = {"Name": "jpk41", "Match": result}
    r = requests.post(url + "/match_check", json=result_check)
    print(r.text)


if __name__ == "__main__":
    blood_match_driver()
