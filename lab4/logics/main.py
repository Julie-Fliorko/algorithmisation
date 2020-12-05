from logics.get_data import get_data
from logics.write_data import write_data


def get_number_of_possible_ways(matrix: list, height: int, width: int, exits: tuple, chars: list):
    # число можливих рішень для кожної клітинки з лівішої колонки
    solutions_for_each_char_in_first_col = [0 for _ in range(height)]

    path_through_chars_steps_сщгте = {char: 0 for char in chars}  # tuple

    for i in exits:
        solutions_for_each_char_in_first_col[i] = 1
        path_through_chars_steps_сщгте[matrix[i][width - 1]] += 1

    # loop in reverse order
    # починаємо з `width-2` (перед остання колонка), до `-1` (перша колонка), з кроком `-1`
    for j in range(width - 2, -1, -1):  # loop in reverse order
        found_solutions = {}  # dict

        for i in range(height):
            current_cell_char = matrix[i][j]  # записуємо в табличку букву
            if current_cell_char == matrix[i][j + 1]:
                temporary_solution = path_through_chars_steps_сщгте[current_cell_char]  # якщо буква = букві в тому самому рядку , але в наступному рядку. То перестрибуємо
            else:
                temporary_solution = solutions_for_each_char_in_first_col[i] + path_through_chars_steps_сщгте[current_cell_char]
            solutions_for_each_char_in_first_col[i] = temporary_solution

            if found_solutions.keys().__contains__(current_cell_char):  # якщо з found_solutions ключ містить розглядуванц букву, тоді відповідь є temporary_solution
                found_solutions[current_cell_char] += temporary_solution
            else:
                found_solutions[current_cell_char] = temporary_solution

        for char, found_solutions_quantity in found_solutions.items():
            path_through_chars_steps_сщгте[char] += found_solutions_quantity

    return sum(solutions_for_each_char_in_first_col)


def main():
    FILE_NUM = 3

    data = get_data(FILE_NUM)

    width = data['width']
    height = data['height']
    matrix = data['matrix']
    chars = data['chars']

    exits = (0, height - 1)

    result = get_number_of_possible_ways(matrix, height, width, exits, chars)

    write_data(FILE_NUM, result)

    print(result)


if __name__ == '__main__':
    main()
