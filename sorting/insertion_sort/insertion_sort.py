unsorted_list = [5, 7, 8, 2, 4]

def sort_list(unsorted_list):
    sorted_list = unsorted_list.copy()
    for j in range(1, len(sorted_list)):
        for i in range(1, len(sorted_list)):
            if sorted_list[i-1] > sorted_list[i]:
                aux = sorted_list[i]
                sorted_list[i] = sorted_list[i-1]
                sorted_list[i-1] = aux
        print(f"unsorted: {unsorted_list}")
        print(f"sorted: {sorted_list}")

sort_list(unsorted_list)





