def analyze_ID(input_line):
    patient_data = first_line.strip("\n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)