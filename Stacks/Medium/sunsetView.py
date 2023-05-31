# Sunset Views
# Given an array of buildings and a direction that all of the buildings face, return an array of the indices of
# the buildings that can see the sunset.
# A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction
# that it faces.
# The input array named buildings contains positive, non-zero integers representing the heights of the
# buildings. A building at index i thus has a height denoted by buildings[i] . All of the buildings face
# the same direction, and this direction is either east or west, denoted by the input string named
# direction , which will always be equal to either "EAST" or "WEST" . In relation to the input array,
# you can interpret these directions as right for east and left for west.
# Important note: the indices in the ouput array should be sorted in ascending order.
# Sample Input #1
# buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# direction = "EAST"
# Sample Output #1
# [1, 3, 6, 7]
# // Below is a visual representation of the sample input.
# // _
# // | |_ _
# // _| | | |_ _
# // | | | | | | | |_
# // | | | | | |_| | |
# // |_|_|_|_|_|_|_|_|
# Sample Input #2
# buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# direction = "WEST"
# Sample Output #2
# [0,1]

def sunsetViews(buildings, direction):
    # Write your code here.
    res = []
    currMax = 0
    if len(buildings) == 1:
        return [0]
    rangeStart = len(buildings)-1 if direction == 'EAST' else 0
    rangeEnd = len(buildings) if direction == 'WEST' else -1
    step = 1 if rangeStart == 0 else -1
    for i in range(rangeStart, rangeEnd, step):
        if currMax < buildings[i]:
            res.append(i)
            currMax = buildings[i]
    if direction == 'EAST':
        res = res[::-1]
    return res
