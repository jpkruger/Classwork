import tkinter as tk
from tkinter import ttk
import requests


def create_blood_string(blood_letter, rh):
    blood_string = "{}{}".format(blood_letter, rh)
    return blood_string


def id_number_verification(patient_id):
    if 1 <= patient_id <= 1000000:
        return True
    else:
        return False


def send_data_to_server(patient_name, patient_id, blood_string, donation):
    patient = {"id": patient_id, "name": patient_name,
               "blood_type": blood_string}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
    return r.text


def check_and_upload_data(patient_name, patient_id,
                          blood_letter, rh, donation):
    blood_string = create_blood_string(blood_letter, rh)
    patient_id = int(patient_id)
    if id_number_verification(patient_id) is False:
        return "Patient ID number is incorrect"
    msg = send_data_to_server(patient_name, patient_id, blood_string, donation)
    return msg


def set_up_window():

    def ok_btn_cmd():
        print("OK Clicked")
        patient_name = name_value.get()
        patient_id = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        donation = donation_value.get()
        msg = check_and_upload_data(patient_name, patient_id,
                                    blood_letter, rh, donation)
        status_label.configure(text=msg)

    def cancel_btn_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Donor Database GUI")
    # root.geometry("500x300")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky="W")

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1, sticky="E")
    name_value = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1, padx=5)

    id_label = ttk.Label(root, text="ID:")
    id_label.grid(column=0, row=2, sticky="E")
    id_value = tk.StringVar()
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2, padx=5)

    ok_button = ttk.Button(root, text="OK", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="CANCEL", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)

    blood_letter_value = tk.StringVar()
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3, sticky="W")

    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4, sticky="W")

    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                               value="AB")
    AB_check.grid(column=0, row=5, sticky="w")

    O_check = ttk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6, sticky="W")

    rh_factor_value = tk.StringVar()
    rh_factor_value.set("-")
    check_box_widget = ttk.Checkbutton(root, text="RH Positive",
                                       variable=rh_factor_value,
                                       onvalue="+", offvalue="-")
    check_box_widget.grid(column=1, row=4)

    donation_label = ttk.Label(root, text="Closest Donation Center")
    donation_label.grid(column=2, row=0)
    donation_value = tk.StringVar()
    donation_combobox = ttk.Combobox(root, textvariable=donation_value)
    donation_combobox.grid(column=2, row=1)
    donation_combobox["values"] = ("Durham", "Apex", "Raleigh")
    donation_combobox.state(["readonly"])

    status_label = ttk.Label(root, text="")
    status_label.grid(column=0, row=7, columnspan=10)

    root.mainloop()


if __name__ == '__main__':
    set_up_window()
