arr = [2,4,6,6,6]

# Escreva o código para a função soma, vista anteriormente
def recursive_sum(arr):
    if (len(arr) > 1):
        return arr[0] + recursive_sum(arr[1:])
    if(len(arr) == 1):
        return arr[0]
    
# Escreva uma função recursiva que conta o número de elementos em uma lista
def list_len(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + list_len(arr)
    
print(list_len(arr))