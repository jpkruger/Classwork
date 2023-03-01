import requests


out_data = {"name": "Jackson Kruger", "net_id": "jpk41",
            "e-mail": "jpk41@duke.edu"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.status_code)
print(r.text)
