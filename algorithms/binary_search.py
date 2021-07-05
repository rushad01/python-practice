def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low+high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid+1
    return None


my_array = [1, 2, 3, 4, 5, 7, 9, 11, 16, 30, 43, 55,
            67, 68, 69, 71, 75, 77, 79, 80, 92, 93, 95, 99, 100]

print(binary_search(my_array, 1))
print(binary_search(my_array, 75))
print(binary_search(my_array, 94))
