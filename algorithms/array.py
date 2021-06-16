# Experiments using python's array

def array_experiment():
    arr = [2, 3, 5, 7, 9, 11]

    arr.pop()
    print("Array after pop operation: ", arr)

    arr.append(6)
    print("Array after append(6) operation: ", arr)

    print("Index of 6: ", arr.index(6))

    arr.remove(6)
    print("Removed 6: ", arr)

    arr.reverse()
    print("Reversed array: ", arr)
    print("Sorted array: ", sorted(arr))

    arr.sort()
    print("Sorted in place: ", arr)

    print("Number of element in arr array: ", len(arr))


def main():
    array_experiment()


if __name__ == "__main__":
    main()
