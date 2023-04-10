from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk
import base64
import requests


def set_up_window():
    filename = None
    wm_im_dwn = None

    def select_image():
        nonlocal filename
        filename = filedialog.askopenfilename(
            initialdir="C:/Users/kruge/repos/Classwork")
        if filename == "":
            return

    def upload_image():
        nonlocal filename
        if filename is None:
            messagebox.showerror("ERROR", message="No File Has Been Selected")
            return
        if filename == "":
            messagebox.showerror("ERROR", message="No File Has Been Selected")
            return
        b64_image = convert_image_file_to_base64_string(filename)
        in_dat = {"image": b64_image, "net_id": "jpk41", "id_no": 567}
        r = requests.post("http://vcm-21170.vm.duke.edu/add_image",
                          json=in_dat)

    def get_image():
        save_file_name = filedialog.asksaveasfilename()
        nonlocal wm_im_dwn
        wm_im_dwn = requests.get("http:"
                                 "//vcm-21170.vm.duke.edu/get_image/jpk41/567")
        wm_im_dwn = wm_im_dwn.text
        convert_base64_to_image_file(save_file_name, wm_im_dwn)

    root = tk.Tk()
    root.title("Image Processing Example")

    select_image_button = ttk.Button(root, text="Choose Image",
                                     command=select_image)
    select_image_button.grid(column=0, row=0)

    upload_image_button = ttk.Button(root, text="Upload Image",
                                     command=upload_image)
    upload_image_button.grid(column=0, row=1)

    get_wm_image_button = ttk.Button(root, text="Download Watermarked Image",
                                     command=get_image)
    get_wm_image_button.grid(column=0, row=2)

    root.mainloop()


def convert_image_file_to_base64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def convert_base64_to_image_file(new_filename, str_in):
    image_bytes = base64.b64decode(str_in)
    with open(new_filename, "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    set_up_window()
