'''Write a function that takes in a non-empty array of integers and returns an array of the same length, where
each element in the output array is equal to the product of every other number in the input array.
In other words, the value at output[i] is equal to the product of every number in the input array other
than input[i] .
Note that you're expected to solve this problem without using division.

Sample Input
array = [5, 1, 4, 2]

Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4'''

def arrayOfProducts(array):
    # Write your code here.
    # create prefix and suffix array
    s = [1]*len(array)
    p = [1]*len(array)
    products = [1]*len(array)
    for i in range(len(array)):
        if i == 0:
            p[i] = array[i]
        else:
            p[i] = array[i] * p[i-1]
    for i in reversed(range(len(array))):
        if i == len(array)-1:
            s[i] = array[i]
        else:
            s[i] = array[i] * s[i+1]
    for i in range(len(array)):
        if i==0:
            products[i] = s[i+1]
        elif i==len(array)-1:
            products[i] = p[i-1]
        else:
            products[i] = p[i-1] * s[i+1]
    return products