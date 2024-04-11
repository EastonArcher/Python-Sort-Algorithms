def bubble_sort(arr):
    n = len(arr)
    inversions = 0

    for i in range(n):
        # set a flag to check if any swaps were made during this iteration
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                inversions += 1

        # if no swaps were made during this iteration, the array is already sorted
        if not swapped:
            break

    return arr, inversions


filename = input("Enter the name of the input file: ")

with open(filename, 'r') as file:
    data = file.readlines()

# convert each line to an integer
data = [int(line.strip()) for line in data]

# sort the data using bubble sort and track inversions
sorted_data, inversions = bubble_sort(data)

# print the sorted data and number of inversions
for item in sorted_data:
    print(item)

print("Bubble Sort Number of inversions:", inversions)

