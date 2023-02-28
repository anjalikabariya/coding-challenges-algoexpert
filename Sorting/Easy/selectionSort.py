'''Write a function that takes in an array of integers and returns a sorted version of that array. Use the
Selection Sort algorithm to sort the array.
If you're unfamiliar with Selection Sort, we recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.
Sample Input
array = [8, 5, 2, 9, 5, 6, 3]
Sample Output
[2, 3, 5, 5, 6, 8, 9]
'''
def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        smallest = i
        for j in range(i+1,len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[smallest], array[i] = array[i], array[smallest]
    return array
