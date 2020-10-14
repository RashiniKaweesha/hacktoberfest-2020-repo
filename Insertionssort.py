
search
Sign In
Home
Courses
Hire With Us
Algorithmskeyboard_arrow_down
Data Structureskeyboard_arrow_down
Languageskeyboard_arrow_down
Interview Cornerkeyboard_arrow_down
GATEkeyboard_arrow_down
CS Subjectskeyboard_arrow_down
Studentkeyboard_arrow_down
GBlog
Puzzles
What's New ?
▲
Insertion Sort
Last Updated: 25-07-2020
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

Example:
insertion-sort
Another Example:
12, 11, 13, 5, 6

Let us loop for i = 1 (second element of the array) to 4 (last element of the array)

i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
11, 12, 13, 5, 6

i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
11, 12, 13, 5, 6

i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
5, 11, 12, 13, 6

i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
5, 6, 11, 12, 13




Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
C++
C
Java
Python
# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
