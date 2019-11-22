import re
def maximalRectangle(matrix):
    if not matrix:
        return 0
    maxArea = 0
    maxRow = len(matrix)
    maxCol = len(matrix[0])
    # For every row in the given 2D matrix, it is a "Largest Rectangle in
    # Histogram" problem, which is the sub-problem.
    lookupTable = [0 for _ in range(maxCol)]
    for row in range(maxRow):
        for col in range(maxCol):
            # If it is "1"
            if int(matrix[row][col]) > 0:
                # Accumulate the column if if's 1's.
                lookupTable[col] += int(matrix[row][col])
            else:
                # Clean the column if it's 0's.
                lookupTable[col] = 0
        # self.debugPrint(lookupTable)
        # Calculate the maximum area.
        maxArea = max(maxArea, maximalRectangleInHistogram(lookupTable))
    return maxArea


def maximalRectangleInHistogram(histogram):
    # Stack for storing the index.
    posStack = []
    i = 0
    maxArea = 0
    while i < len(histogram):
        if len(posStack) == 0 or histogram[i] > histogram[posStack[-1]]:
            # Advance the index when either the stack is empty or the
            # current height is greater than the top one of the stack.
            posStack.append(i)
            i += 1
        else:
            curr = posStack.pop()
            width = i if len(posStack) == 0 \
                else i - posStack[-1] - 1
            maxArea = max(maxArea, width * histogram[curr])
    # Clean the stack.
    while posStack:
        curr = posStack.pop()
        width = i if len(posStack) == 0 \
            else len(histogram) - posStack[-1] - 1
        maxArea = max(maxArea, width * histogram[curr])
    return maxArea


def debugPrint(historgram):
    out = [i for i in historgram]
    print(out)
matrix = []
file = open('in2.txt', "r")
for line in file:
    line = line.replace(" ","")
    line = line.replace("\n","")
    matrix.append(line)

print(maximalRectangle(matrix))
answer = maximalRectangle(matrix)
with open('out2.txt', 'w') as f:
    f.write("%s " % answer)
    f.write('\n')