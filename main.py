import time
from film import Film


def read_from_csv(filename):
    with open(filename, 'r') as f:
        f.readline()
        objects = [Film(*item) for item in [line.strip().split(';') for line in f.readlines()]]
    return objects


"""def main():
    objects = read_from_csv('films.csv')

    print('------------------------')
    print('Bubble sort (descending)')
    print('------------------------')
    start = time.time()
    objects = Film.bubble_sort_by_num_of_responses_descending(objects)
    end = time.time() - start
    print("Time spent: " + str(end))
    print("Number of comparisons: " + str(Film.bubble_sort_comparison_counter))
    print("Number of swaps: " + str(Film.bubble_sort_swap_counter))
    print('------------------------')
    [print(object_to_show) for object_to_show in objects]"""


if __name__ == '__main__':
    #main()
    objects = read_from_csv('films.csv')

    print('------------------------')
    print('Bubble sort (descending)')
    print('------------------------')
    start = time.time()
    objects = Film.bubble_sort_by_num_of_responses_descending(objects)
    end = time.time() - start
    print("Time spent: " + str(end))
    print("Number of comparisons: " + str(Film.bubble_sort_comparison_counter))
    print("Number of swaps: " + str(Film.bubble_sort_swap_counter))
    print('------------------------')
    [print(an_object) for an_object in objects]

    print('======================')
    print('Heap sort (ascending)')
    print('======================')
    start = time.time()
    objects = Film.heap_sort_runtime_in_min_acs(objects)
    end = time.time() - start
    print("Time spent: " + str(end))
    print("Number of comparisons: " + str(Film.heap_sort_comparison_counter))
    print("Number of swaps: " + str(Film.heap_sort_swap_counter))
    print('======================')

    [print(object) for object in objects]
