def elementsRemoval(array):
    minCost = 0

    for i in range(len(array)):
        minCost += sum(array[i:])

    return minCost


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))
    A.sort(reverse=True)
    print(elementsRemoval(A))
