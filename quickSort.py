def quicksort(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0

    pivot = arr[n//2]
    left = []
    right = []
    equal = []
    inversions = 0

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
            inversions += len(equal)
        else:
            equal.append(x)

    left, left_inversions = quicksort(left)
    right, right_inversions = quicksort(right)
    inversions += left_inversions + right_inversions

    return left + equal + right, inversions


filename = input("Enter the name of the input file: ")

with open(filename, 'r') as file:
    data = file.readlines()

# convert each line to an integer
data = [int(line.strip()) for line in data]

# sort the data using quicksort and track inversions
sorted_data, inversions = quicksort(data)

# print the sorted data and number of inversions
for item in sorted_data:
    print(item)

print("Number of inversions:", inversions)
