array = [57010,40840,69871,14425,70605]


def greatest_on_the_right(arr):
    start = 0
    end = len(arr) -1

    while start < end:
        if start + 1 != end:
            maxi = max(arr[start+1:end+1])
            arr[start] = maxi
        start += 1
        print(arr)

    arr[end-1] = arr[end]
    arr[start] = -1

    return arr

print(greatest_on_the_right(array))