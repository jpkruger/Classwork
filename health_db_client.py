import requests


server = "http://127.0.0.1:5000"


patient = {"id": 1, "name": "Jackson", "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)


# patient = {"mrn": 2, "name": "John", "blood_type": "A+"}
# r = requests.post(server + "/new_patient", json=patient)
# print(r.status_code)
# print(r.text)


data = {"id": 2, "test_name": "HDL", "test_result": 150}
r = requests.post(server + "/add_test", json=data)
print(r.status_code)
print(r.text)


# r = requests.get(server + "/get_results/1")
# print(r.status_code)
# print(r.text)
# answer = r.json()
# for t in answer:
#     print(t)
