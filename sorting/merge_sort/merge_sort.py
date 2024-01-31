def sort_sublist(unsorted_list, i):
    if i < len(unsorted_list):
        if unsorted_list[i-1] > unsorted_list[i]:
                    aux = unsorted_list[i]
                    unsorted_list[i] = unsorted_list[i-1]
                    unsorted_list[i-1] = aux
        i = i + 1
        sort_sublist(unsorted_list, i)


def insertion_sort(unsorted_list, j):
    if j < len(unsorted_list):
        j = j + 1
        sort_sublist(unsorted_list, 1)
        insertion_sort(unsorted_list, j)
    sorted_list = unsorted_list
    return sorted_list


def merge_subroutine(sorted_list, array1, array2, i, j):
    if len(array1 + array2) == 1:
        sorted_list.append((array1+array2)[0])
        return sorted_list

    if array1[0] < array2[0]:
        sorted_list.append(array1[0])
        array1.pop(0)
    if array2[0] < array1[0]:
        sorted_list.append(array2[0])
        array2.pop(0)
    
    merge_subroutine(sorted_list, array1, array2, i, j)

def merge_sort(unsorted_list):
    sorted_list = []
    n = len(unsorted_list)
    array1 = insertion_sort(unsorted_list[0:(n//2)], 1)
    array2 = insertion_sort(unsorted_list[(n//2):n], 1)
    merge_subroutine(sorted_list, array1, array2, 0, 0)
    return sorted_list

unsorted_list = [5, 9, 3, 4, 8, 1]
sorted_list = merge_sort(unsorted_list)
print(f"unsorted: {unsorted_list}")
print(f"sorted: {sorted_list}")