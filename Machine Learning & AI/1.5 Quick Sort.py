def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def sort_numbers_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    sorted_numbers = quick_sort(numbers)
    print("Sorted numbers:", sorted_numbers)

def sort_animals_file(filename):
    with open(filename, 'r') as file:
        animals = [line.strip() for line in file.readlines()]
    sorted_animals = quick_sort(animals)
    print("Sorted animals:", sorted_animals)

# Sorting the files
sort_numbers_file('numbers.txt')
sort_animals_file('animals.txt')
