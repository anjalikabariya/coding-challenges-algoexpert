'''Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m)
and returns a one-dimensional array of all the array's elements in spiral order.
Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a
spiral pattern all the way until every element has been visited.

Sample Input
array = [
 [1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7],
]

Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
'''

def spiralTraverse(array):
    # Write your code here.
    def fun(arr, lc, rc, lr, rr, res):
        for c in range(lc, rc+1):
            res.append(arr[lr][c])
        for r in range(lr+1, rr+1):
            res.append(arr[r][rc])
        if not lr < rr or not lc < rc:
            return
        for c in range(rc-1, lc-1, -1):
            res.append(arr[rr][c])
        for r in range(rr-1, lr, -1):
            res.append(arr[r][lc])

    lc = 0
    rc = len(array[0])-1
    lr = 0
    rr = len(array)-1
    res = []
    while lr <= rr and lc <= rc:
        fun(array, lc, rc, lr, rr, res)
        lr += 1
        rr -= 1
        lc += 1
        rc -= 1
    return res
