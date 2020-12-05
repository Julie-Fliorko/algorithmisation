def write_data(file_number, data):
    with open('../in&out/out' + str(file_number), 'w') as file:
        file.write(str(data))
