import re
def maximalRectangle(matrix,numRowCol):
    if not matrix:
        return 0
    maxArea = 0
    lookupTable = [0 for _ in range(numRowCol)]
    for row in range(numRowCol):
        for col in range(numRowCol):
            # If it is "1"
            if int(matrix[row][col]) > 0:
                lookupTable[col] += int(matrix[row][col])
            else:
                # Clean the column if it's 0's.
                lookupTable[col] = 0
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
            posStack.append(i)
            i += 1
        else:
            curr = posStack.pop()
            width = i if len(posStack) == 0 else i - posStack[-1] - 1
            maxArea = max(maxArea, width * histogram[curr])
    # Clean the stack.
    while posStack:
        curr = posStack.pop()
        width = i if len(posStack) == 0 else len(histogram) - posStack[-1] - 1
        maxArea = max(maxArea, width * histogram[curr])
    return maxArea


def debugPrint(historgram):
    out = [i for i in historgram]
    print(out)
matrix = []
numRowCol = int(open('in.txt', "r").readline()[0])
file = open('in.txt', "r")
readFile = file.readlines()[1:]
for line in readFile:
    line = line.replace(" ","")
    line = line.replace("\n","")
    matrix.append(line)

print(maximalRectangle(matrix,numRowCol))
answer = maximalRectangle(matrix, numRowCol)
with open('out.txt', 'w') as f:
    f.write("%s " % answer)
    f.write('\n')

