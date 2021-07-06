# Time Complexity:O(n) for linear or sequential search as it traverse through all elements
def linear_search(list, item):
    for x in range(len(list)):
        if list[x] == item:
            return x
    return None


def main():
    my_array = [1, 2, 3, 4, 5, 6, 7, 10, 45, 869, 32, 44, 22, 55]
    print(linear_search(my_array, 45))
    print(linear_search(my_array, -1))


if __name__ == "__main__":
    main()
