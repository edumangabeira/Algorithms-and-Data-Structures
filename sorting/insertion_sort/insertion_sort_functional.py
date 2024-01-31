def insertion_sort(unsorted_list, j):
    if j < len(unsorted_list):
        j = j + 1
        sort_sublist(unsorted_list, 1)
        insertion_sort(unsorted_list, j)
    sorted_list = unsorted_list
    return sorted_list

def sort_sublist(unsorted_list, i):
    if i < len(unsorted_list):
        if unsorted_list[i-1] > unsorted_list[i]:
                    aux = unsorted_list[i]
                    unsorted_list[i] = unsorted_list[i-1]
                    unsorted_list[i-1] = aux
        i = i + 1
        sort_sublist(unsorted_list, i)            

unsorted_list = [5, 7, 8, 2, 4]
print(unsorted_list)
print(insertion_sort(unsorted_list, 1))





