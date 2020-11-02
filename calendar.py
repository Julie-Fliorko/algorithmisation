# ( given)
input_array_one = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
input_array_two = [(0, 1), (4, 7), (2, 3), (10, 11), (7, 10)]


# Python program for implementation of MergeSort
def mergeSort(array):

    """
    returns sorted array
    >>> mergeSort(input_array_one)
    [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
    >>> mergeSort(input_array_two)
    [(0, 1), (2, 3), (4, 7), (7, 10), (10, 11)]
    """


    if len(array) > 1:
        midd_indx = len(array) // 2  # Finding the middle of the array
        left_child = array[:midd_indx]  # Dividing the array elements
        right_child = array[midd_indx:]  # into 2 halves

        mergeSort(left_child)  # Sorting the first half
        mergeSort(right_child)  # Sorting the second half

        left_child_indx = right_child_indx = finnal_arr_indx = 0

        while left_child_indx < len(left_child) and right_child_indx < len(right_child):
            if left_child[left_child_indx] < right_child[right_child_indx]:
                array[finnal_arr_indx] = left_child[left_child_indx]
                left_child_indx += 1
            else:
                array[finnal_arr_indx] = right_child[right_child_indx]
                right_child_indx += 1
            finnal_arr_indx += 1


        while left_child_indx < len(left_child):
            array[finnal_arr_indx] = left_child[left_child_indx]
            left_child_indx += 1
            finnal_arr_indx += 1

        while right_child_indx < len(right_child):
            array[finnal_arr_indx] = right_child[right_child_indx]
            right_child_indx += 1
            finnal_arr_indx += 1


        return array

def solution(array):

    """
    best - O(N)
    worst - O(N^2)
    >>> solution(mergeSort(input_array_one))
    [(0, 1), (3, 8), (9, 12)]
    >>> solution(mergeSort(input_array_two))
    [(0, 1), (2, 3), (4, 11)]
    """
    output_array = []
    indx = 0

    while indx < len(array) - 1:
        if array[indx][1] == array[indx + 1][0]:
            first_el = array[indx][0]
            while indx < len(array) - 1 and array[indx][1] == array[indx + 1][0]:
                indx += 1
            second_el = array[indx][1]
            output_array.append((first_el, second_el))
            indx += 1

        elif array[indx][1] > array[indx + 1][0]:
            output_array.append((array[indx][0], array[indx + 1][1]))
            indx += 1

        else:
            output_array.append(tuple(array[indx]))

        indx += 1

    return output_array


if __name__ == "__main__":
    import doctest
    doctest.testmod()