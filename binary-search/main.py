s1 = [1, 2, 2, 4, 5, 7, 8]

def binary_search(arr: list, item: int) -> int:
    """
    Binary tree function
    """
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        guess = arr[mid]

        if guess == item:
            return mid

        elif guess < arr[mid]:
            lower = mid + 1

        else:
            upper = mid - 1

    return None

print(binary_search(s1, 5))

