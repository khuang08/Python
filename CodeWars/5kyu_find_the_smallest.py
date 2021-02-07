'''
You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number,
remove this digit at that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.

#Task: Return an array or a tuple or a string depending on the language (see "Sample Tests") with

        the smallest number you got
        the index i of the digit d you took, i as small as possible
        the index j (as small as possible) where you insert this digit d to have the smallest number.

Example:

smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"

126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
index `i` in [29917, 0, 1].

29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

smallest(1000000) --> [1, 0, 6] or ...
'''

def num_to_digits(n):
    arr = [int(x) for x in str(n)]
    return arr

def digits_to_num(arr):
    n = ''.join([str(x) for x in arr])
    return int(n)

def smallest(n):
    arr = num_to_digits(n)
    length = len(arr)

     # compare first digit to next smallest
    small = min(arr)
    if arr[0] > small:
        small_index = arr.index(small)
        arr.pop(arr.index(small))
        arr.insert(0, small)
        return[digits_to_num(arr), small_index, 0]
    else:
    # store first digit and compare next digit to smallest
        temp = []
        while(len(arr) > 0):
            temp.append(arr[0])
            arr.pop(0)
            small = min(arr)
            if small == 0:
                small_index = arr.index(small)
                arr.pop(arr.index(small))
                arr.replace(arr.index(small), small)
                swap_value = arr[0]
                results = temp + arr
                return[digits_to_num(results), small_index, arr.index(swap_value)]
            
            elif arr[0] > small:
                small_index = arr.index(small)
                arr.pop(arr.index(small))
                arr.insert(0, small)
                swap_value = arr[0]
                results = temp + arr
                return[digits_to_num(results), small_index, arr.index(swap_value)]
            
                
print(smallest(261235)) #[126235, 2, 0]
print(smallest(209917)) #[29917, 0, 1])
print(smallest(285365)) #[238565, 3, 1])
print(smallest(269045)) #[26945, 3, 0])
print(smallest(296837)) #[239687, 4, 1])
