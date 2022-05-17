# target array to sort
arr = [2, 4, 5, 5434, 53, 98, 7, 4, 34]

# functioning having sorting algorithm
def sortArr(arr):
    newArr = []
    newArr.append(arr.pop(arr.index(min(arr))))

    while len(arr) > 0:
        newArr.append(arr.pop(arr.index(min(arr))))

    return newArr

# Show output
print(sortArr(arr))
