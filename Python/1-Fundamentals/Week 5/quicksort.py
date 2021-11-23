my_list = [5,4,1,3,2]

def sort_part(the_list,low_idx,pivot_idx):
    pivot_val = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_val = the_list[low_idx]

        print(the_list,low_val,pivot_val)
        if low_val <= pivot_val:
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = low_val
            the_list[pivot_idx-1] = pivot_val
            pivot_idx -= 1

    return pivot_idx


def quicksort(the_list,low_idx,high_idx):
    if low_idx > high_idx:
        return
    
    pivot_idx = sort_part(the_list,low_idx,high_idx)
    quicksort(the_list,low_idx,pivot_idx-1)
    quicksort(the_list,pivot_idx+1,high_idx)

quicksort(my_list,0,len(my_list)-1)
print("my_list:",my_list)


