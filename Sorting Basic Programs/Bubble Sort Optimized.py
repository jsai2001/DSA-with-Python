# Create Bubble Sort function
# Sorting from end to start of the array
def bubble_sort(arr):
    # Now we are declaring a flag called not_sorted
    # If it means , that no need of furthur swappings are needed
    # So , we can exit the iteration and return the list as it is sorted
    # If not_sorted is false , then we must perform the swappings for sorting the array
    # We can stop the iterations once the swap has done
    not_sorted = True
    total_iterations = 0
    while(not_sorted):
        not_sorted = False
        # We expect the array to be sorted. So , we initialize not_sorted with False
        # The inner for loop below here , decides whether the array is sorted or not
        # If array is sorted , then not_sorted remains False ,
        # If any of element of array "arr[i]>arr[i+1]",
        # then it denotes the array is not yet sorted , so initialize the not_sorted = True
        
        # Here in for loop , we can iterate upto len(arr)-1 , but we continously
        # checks and compare untill the last of the array , but as we know , we 
        # no need to compare the n ending elements for n iterations ,
        # So , we replaced the len(arr)-1 with len(arr)-total_iteration-1 , which
        # iterates until some element depends on the num of iterations
        for i in range(len(arr)-total_iterations-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                not_sorted = True
        total_iterations += 1
    # We are assuming total_iterations-1 as the result because ,
    # the while loop , we also considered the stage where all elements are sorted
    # and no sorting and swapping are required.
    print("Total number of iterations performed: ",total_iterations-1)
    return arr

arr = [5,3,8,6,7,2]
print("Unsorted: ",arr)
# Calling the bubble sort function
print("Sorted: ",bubble_sort(arr))