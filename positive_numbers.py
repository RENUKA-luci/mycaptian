def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers


# Example usage
list1 = [12, -7, 5, 64, -14]
positive_nums1 = print_positive_numbers(list1)
print(f"Input: list1 = {list1} Output: {positive_nums1}")

list2 = [12, 14, -95, 3]
positive_nums2 = print_positive_numbers(list2)
print(f"Input: list2 = {list2} Output: {positive_nums2}")
