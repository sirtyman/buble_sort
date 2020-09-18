import time
import random

from sort_methods.sort import buble_sort


def test_bubble_sort():
    input_list = [5, 5, 5, 3, 1, 7]
    sorted_list = buble_sort.bubble_sort(input_list)

    assert sorted_list == [1, 3, 5, 5, 5, 7]


def test_benchmark_bubble_sort():
    random_range = 10000
    input_list = [random.randint(0, random_range) for _ in range(random_range)]
    start_time_s = time.time()
    sorted_list = buble_sort.bubble_sort(input_list)
    dt = time.time() - start_time_s

    assert dt < 10

