import unittest

# Define the merge_sort and merge functions outside of the test class and the main block
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class TestMergeSort(unittest.TestCase):
    
    # Positive case: sorting a typical array
    def test_typical_case(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])

    # Negative case: invalid data type in array
    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            merge_sort([1, 'a', 3])

    # Performance case: large array
    def test_large_array(self):
        large_array = list(range(1000, 0, -1))
        sorted_large_array = list(range(1, 1001))
        self.assertEqual(merge_sort(large_array), sorted_large_array)

    # Boundary case: empty array, single element, duplicates, already sorted, reverse-sorted
    def test_boundary_cases(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([5]), [5])
        self.assertEqual(merge_sort([5, 5, 5]), [5, 5, 5])
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 2, 1]), [1, 2, 3])

    # Idempotency case: running the sort multiple times gives the same result
    def test_idempotency(self):
        array = [3, 1, 4, 1, 5, 9, 2]
        sorted_once = merge_sort(array)
        sorted_twice = merge_sort(sorted_once)
        self.assertEqual(sorted_once, sorted_twice)

if __name__ == '__main__':
    unittest.main()

    