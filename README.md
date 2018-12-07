# PCS-II-Homework
        This analysis contains an algorithm of two functions: QuickSort and MergeSort. 
    In QuickSort, the function partition is defined and this partition() method(having three parameters: array= arr, low= starting index and high = ending last index) takes a string and separates it at the its first occurrence. Using a variable i minus 1, taking a single number as a pivot,keeps iterating through the list,checking which number is smaller or higher than the pivot, until the whole list is completely sorted.
    A for loop is created , if the current element is smaller than or equal to pivot, the i variable adds to the index, the array of i and j should be equal to that of j to i, i + an integer 1 should be returned.  The quicksort function , the starting index should be less than the ending index using an if loop, calling the function pi should be equal to the three parameters (arr,low,high)... the elements should be sorted before and after partition. 
   
   In Merge Sort, the unsorted list is divided into 'n' sublists, each having one element, because a list consisting of one element is always sorted, it merges these sublists to produce new sorted sublists, in the end, only one sorted list is produced. Multiple for loops are dfeined and this works recursively checking each through each list before moving to the next, requiring an equal amount of additional space as the unsorted list. 
   MergeSort is defined with a variable x, a new list is created , the length of x should be greater than 2, x is returned , two new variables y and z are formed then a while, if and else loop is used, the length of the variable 'y' should be greater than that of z else you pop or append , this should be recursively repeated, a last else should be formed which pops finally and a result is returned.
  
    A new function called measure this is defined for both QuickSort and MergeSort, to be used in the 'timeit' an empty list is created , a for loop is used with a parameter size a , a random integer with size is added to the empty list at position using the import 'timeit', prints the setup and the previously defined function 'MeasureThis', the QuickSort runs faster than the MergeSort with a little time difference...
  In conclusion,the 'timeit' execution works for both Sorting methods of any integer. Using QuickSort algorithm is faster because it can be easily implemented and does not require extra space,you do not have to use the for loop multiple times, while for the Mergesort algorithm the 'timeit' exceution is a less faster ,multiple loops are created. Depending on the way the code is written it is better with 'sorted large linked list', also performs the same data as QuickSort regardless if the data is sorted or not. MergeSort also requires extra space ,works as a divide and conquer algorithm with performances always same for worst, average and best cases.
