def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left, left_inversions = merge_sort(left)
    right, right_inversions = merge_sort(right)

    merged = []
    inversions = left_inversions + right_inversions

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, inversions


filename = input("Enter the name of the input file: ")

with open(filename, 'r') as file:
    data = file.readlines()

# convert each line to an integer
data = [int(line.strip()) for line in data]

# sort the data using merge sort and track inversions
sorted_data, inversions = merge_sort(data)

# print the sorted data and number of inversions
for item in sorted_data:
    print(item)

print("Merge Sort Number of inversions:", inversions)
