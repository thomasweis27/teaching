def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def sort_numbers_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    selection_sort(numbers)
    print(numbers)

def sort_animals_file(filename):
    with open(filename, 'r') as file:
        animals = [line.strip() for line in file.readlines()]
    selection_sort(animals)
    print(animals)

# Sorting the files
sort_numbers_file('numbers.txt')
sort_animals_file('animals.txt')
