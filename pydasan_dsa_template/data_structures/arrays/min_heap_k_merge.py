import heapq

def mergeArrays(mat):
    k = len(mat)

    output = []

    # Min-heap: (value, (array index, element index))
    minHeap = []

    # Push first element of each array
    for i in range(k):
        if len(mat[i]) > 0:
            heapq.heappush(minHeap, (mat[i][0], i, 0))

    # Merge all elements
    while minHeap:
        val, i, j = heapq.heappop(minHeap)
        output.append(val)

        # Push next element from same array
        if j + 1 < len(mat[i]):
            heapq.heappush(minHeap, (mat[i][j + 1], i, j + 1))

    return output

if __name__ == "__main__":
    mat = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]
    ]

    result = mergeArrays(mat)
    print(" ".join(map(str, result)))
