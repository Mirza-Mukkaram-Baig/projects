def binary_search(list, key):
    start = 0
    end = len(list) - 1

    while(start <= end):
        mid = int((start + end) / 2)

        if(list[mid] == key):
            return mid
        elif(list[mid]>key):
            end = mid - 1
        else:
            start = mid + 1

    return -1