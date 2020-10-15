class Film:
    bubble_sort_comparison_counter = 0
    bubble_sort_swap_counter = 0
    heap_sort_comparison_counter = 0
    heap_sort_swap_counter = 0

    def __init__(self, name, runtime_in_min, num_of_responses):
        self.name = name
        self.runtime_in_min = runtime_in_min
        self.num_of_responses = num_of_responses

    def __str__(self):
        return ' '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__]) + '\n'
        # return f"Film: [name: {self.name}, duration_in_min: {self.duration_in_min}, num_of_responses: {self.num_of_responses}"

    @staticmethod
    def bubble_sort_by_num_of_responses_descending(objects):
        n = len(objects)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if objects[j].num_of_responses < objects[j + 1].num_of_responses:
                    Film.bubble_sort_comparison_counter += 1
                    objects[j], objects[j + 1] = objects[j + 1], objects[j]
                    Film.bubble_sort_swap_counter += 2
                    print([an_object.num_of_responses for an_object in objects])
        return objects

    @staticmethod
    def heap_sort_runtime_in_min_acs(objects):

        n = len(objects)

        def compare_element_from_heapsort(first_element, second_element):
            objects.heap_sort_comparison_counter += 1
            if first_element < second_element:

                return True
            else:

                return False


        def heapify(objects, n, i):
            largest = i
            l = 2 * i
            r = 2 * i + 1

            if l < n and compare_element_from_heapsort(objects[i].visitors, objects[l].visitors):
                largest = l

            if r < n and compare_element_from_heapsort(objects[largest].visitors, objects[r].visitors):
                largest = r

            if largest != i:
                objects[i], objects[largest] = objects[largest], objects[i]  # swap
                objects.heap_sort_swap_counter += 1
                heapify(objects, n, largest)

        for i in range(n, -1, -1):
            heapify(objects, n, i)

        for i in range(n - 1, 0, -1):
            objects[i], objects[0] = objects[0], objects[i]  # swap
            objects.heap_sort_swap_counter += 1
            heapify(objects, i, 0)
        """
        n = len(objects)

        def compare_element_from_heapsort(first_element, second_element):
            Film.heap_sort_comparison_counter += 1
            if first_element > second_element:

                return True
            else:

                return False

        for i in range(n, -1, -1):


            # heapify
            largest = i
            l = 2 * i
            r = 2 * i + 1

            if l < n and compare_element_from_heapsort(objects[i].visitors, objects[l].visitors):
                largest = l

            if r < n and compare_element_from_heapsort(objects[largest].visitors, objects[r].visitors):
                largest = r

            if largest != i:
                objects[i], objects[largest] = objects[largest], objects[i]  # swap
                Film.heap_sort_swap_counter += 1

                # heapify i=largest
                l = 2 * largest
                r = 2 * largest + 1

                if l < n and compare_element_from_heapsort(objects[i].visitors, objects[l].visitors):
                    largest = l

                if r < n and compare_element_from_heapsort(objects[largest].visitors, objects[r].visitors):
                    largest = r


        for i in range(n - 1, 0, -1):
            objects[i], objects[0] = objects[0], objects[i]  # swap
            Film.heap_sort_swap_counter += 1

            # heapify n=i i=0
            largest = 0
            l = 2 * 0
            r = 2 * 0 + 1

            if l < n and compare_element_from_heapsort(objects[n].visitors, objects[l].visitors):
                largest = l

            if r < n and compare_element_from_heapsort(objects[largest].visitors, objects[r].visitors):
                largest = r

            if largest != n:
                objects[n], objects[largest] = objects[largest], objects[n]  # swap
                Film.heap_sort_swap_counter += 1
        return objects"""
