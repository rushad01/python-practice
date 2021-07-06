# Time Complexity;Ω(n^2)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def main():
    print(selectionSort([1, 3, 5, 7, 2, 11, 9, 14, 54, 32, 56, 6]))


if __name__ == "__main__":
    main()
