def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
       
def sort_numbers_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    insertion_sort(numbers)
    print(numbers)

def sort_animals_file(filename):
    with open(filename, 'r') as file:
        animals = [line.strip() for line in file.readlines()]
    insertion_sort(animals)
    print(animals)


# Sorting the files
sort_numbers_file('numbers.txt')
sort_animals_file('animals.txt')
