def bubble_basic(lst):
    """basic bubble sort"""
    outside_loop_count = 0
    inside_loop_count = 0
    print(lst)
    for i in range(len(lst) - 1):   # for checking upto 2nd to last element
        for j in range(len(lst) - 1):
            print(f"j: {lst[j]}, j+1: {lst[j+1]}")
            if lst[j] > lst[j + 1]:
                print(f"swapping {lst[j]} & {lst[j+1]}")
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            print(lst)
            inside_loop_count += 1
            print("INSIDE LOOP", inside_loop_count, 'DONE')
        outside_loop_count += 1
        print("OUTSIDE LOOP", outside_loop_count, 'DONE')

lst = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_basic(lst)
print("bubble_basic sort:", lst)