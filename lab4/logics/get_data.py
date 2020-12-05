def get_data(file_num):
    with open('../in&out/in_' + str(file_num), 'r') as file:
        width, height = [int(number) for number in file.readline().split()]
        matrix = []
        chars = []

        for row in file.readlines():
            matrix.append(row.replace('\n', ''))
            for sym in row:
                if sym != '\n' and sym not in chars:  # якщо не новий рядок і не є в списку chars, то додати char
                    chars.append(sym)

        chars.sort()

    return {'width': width, 'height': height, 'matrix': matrix, 'chars': chars}


if __name__ == '__main__':
    print(get_data(1))
