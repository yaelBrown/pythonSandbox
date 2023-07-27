# iteratively 
def remove_duplicates(arr):
    for i in range(len(arr)):
        if i < len(arr):
            _, arr[i] = arr[i], -1
            if _ in arr:
                del arr[i]
            else: 
                arr[i] = _
            _ = -1
    return arr

# using a set
def remove_duplicates2(arr):
    return list(set(arr))
    
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

# creating a new list
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
  
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]