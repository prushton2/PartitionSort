# PartitionSort
A quick sorting algorithm that uses partitions to recursively sort an array

## Time complexity
I dont know. I dont know how to evaluate that, ill figure it out later. It is probably O(n log n) because thats quicksort's time complexity

## How it works
This algorithm uses recursive partition sorting, very similar to quicksort. The program picks a pivot (end of the list). The lower and upper side of the pivot are added to their own lists, and then those lists are recursed into the sorting algorithm. Once the list has no items, it returns an empty list to collapse the recursion stack and rebuild the list in sorted order.
