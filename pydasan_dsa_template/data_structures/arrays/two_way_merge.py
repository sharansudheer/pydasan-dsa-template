#  https://www.baeldung.com/cs/2-way-vs-k-way-merge
# https://www.geeksforgeeks.org/dsa/merge-two-sorted-arrays/


# Initialize two pointers: i = 0 for traversing arr1, j = 0 for traversing arr2
# Create an empty array merged = []
# Merge the elements into merged: While both i < n and j < m:
# => If arr1[i] <= arr2[j], append arr1[i] to merged and increment i
# => Else, append arr2[j] to merged and increment j
# Append remaining elements (if any):
# => While i < n, append arr1[i] to merged and increment i
# => While j < m, append arr2[j] to merged and increment j
# Distribute the merged elements back:
# => Copy the first n elements of merged to arr1
# => Copy the remaining m elements to arr2



def mergeArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0

    # temporary array to store merged result
    merged = []

    # merge elements in sorted order
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # copy remaining elements from arr1
    while i < n:
        merged.append(arr1[i])
        i += 1

    # copy remaining elements from arr2
    while j < m:
        merged.append(arr2[j])
        j += 1

    # copy first n to arr1
    for i in range(n):
        arr1[i] = merged[i]

    # copy remaining m to arr2
    for j in range(m):
        arr2[j] = merged[n + j]

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    mergeArrays(arr1, arr2)

    print(*arr1)
    print(*arr2)