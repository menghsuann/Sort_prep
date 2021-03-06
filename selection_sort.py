def selection_sort(list_a):
    indexing_length = range(0, len(list)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a
  #https://www.youtube.com/watch?v=4CykZVqBuCw&list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv&index=2
  #O(n2) 
