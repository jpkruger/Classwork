import requests


message = {"user": "jpk41",
           "message": "Jefferson, you look beautiful today"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=message)
# r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/jrb187")
# j_message = r1.json()
# print(j_message)
