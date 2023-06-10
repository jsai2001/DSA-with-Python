# Insertion sort in Python
def insertionSort(array):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        '''
        Compare key with each element on the left of it
        until an element smaller than it is found , so we 
        can get an sorted order , by doing the same operation
        repeated on the array until end of the array , we get an
        array which is sorted
        
        For descending order , change key<array[j] to key>array[j]
        
        Remember , we need to shift all the greater values to right ,
        and the stop that we are having here is either the array is to the
        extreme left , if we find any element which is lesser than the key value,
        It means that we can't shift the smaller element to the right as it is smaller than key,
        so the key must be placed next to the smaller element that we found (array[j]),
        And replace the array[j+1] with the key , which is also next to the array[j] 
        
        it seems array[j](value which is lesser than key)<array[j+1](key)<values which are greater than key
        '''
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        # Place key at after the element just smaller than it is
        array[j+1] = key
data = [9,5,1,4,3]
insertionSort(data)
print('Sorted Array in Ascending Order: ')
print(data)
        