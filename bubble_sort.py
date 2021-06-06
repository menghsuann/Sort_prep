def bubble(list_a):
    indexing_length = len(list_a) - 1 #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a 
#time complexity of Bubble Sort is O(n2)
#https://www.studytonight.com/data-structures/bubble-sort
#https://www.youtube.com/watch?v=g_xesqdQqvA&list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv&t=0s
