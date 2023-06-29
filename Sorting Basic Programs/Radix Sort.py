# Radix Sort in python
# Using counting sort to sort the elements in the basis of significanct places
def countingSort(array, place):
    size = len(array) # length of the array 'n'
    output = [0]*size # Memory which we use for each pass
    count = [0]*10 # count array used to store occurance in counting sort
    # Calculate count of elements
    for i in range(0,size):
        index = array[i]//place # This is used to get element at nth place of i
        count[index%10]+=1 # Adding the occurance into the count array
    # Calculate cumulative count , which is used to give the element position in sorted array "array"
    for i in range(1,10):
        count[i]+=count[i-1]
    # Place the elements in sorted order
    i = size - 1
    while i>=0:
        index = array[i]//place
        output[count[index%10]-1]=array[i]
        count[index%10]-=1
        i-=1
    for i in range(0,size):
        array[i]=output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element , to get detail about number of passes required
    max_element = max(array)
    # Apply counting sort to sort the elements based on place
    # We will sort the array , 
    # based on max_element passes of counting sort applied on respective place's index
    place = 1
    while max_element // place > 0:
        countingSort(array,place) #sort the array , based on the place using counting sort
        place*=10 #we sort the array , based on unit's place , ten's place upto max_element's place

data = [121,432,564,23,1,45,788]
radixSort(data)
print(data)