# Time Complexity: O(N) , We will perform N insertions in the dictionary
# Space Complexity: O(K) , K is size of map , worst case space will be O(N)

# Python3 program to count all duplicates
# from string using maps
def printDups(callstr):
    count = dict()
    for i in range(len(callstr)):
        if(callstr[i] in count): # If array element already exists in map , increment it's occurance
            count[callstr[i]]+=1
        else: # If this is the first occurance , initialize it to 1
            count[callstr[i]]=1
    for element,occurance in count.items(): #Iterating through occurance array map
        if(occurance>1): # If the count of characters is greater than 1 then duplicate found
            print(str(element)+", occurance="+str(occurance))
callstr = "hello jeevan sai"
printDups(callstr)

