def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    search_res = None

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == item:
            search_res = middle
            return search_res
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return search_res

print(binary_search([3, 5, 7, 8, 8, 9, 9], 8))