from typing import List

def list_to_int_plus_one(numbers: List[int]) -> int:
    # return int(''.join(map(str, numbers))) + 1
    
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            break
        
        i -= 1
        
    return numbers


print(list_to_int_plus_one([1, 2, 3])) # [1, 2, 4]    