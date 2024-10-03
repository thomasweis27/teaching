def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sort_numbers_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    bubble_sort(numbers)
    print(numbers)


def sort_animals_file(filename):
    with open(filename, 'r') as file:
        animals = [line.strip() for line in file.readlines()]
    bubble_sort(animals)
    print(animals)


# Sorting the files
sort_numbers_file('numbers.txt')
sort_animals_file('animals.txt')
