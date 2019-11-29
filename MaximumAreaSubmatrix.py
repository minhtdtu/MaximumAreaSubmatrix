import re
import timeit
start = timeit.timeit()
def maximalRectangle(matrix,numRowCol):
    if not matrix:
        return 0
    maxArea = 0
    lookupTable = [0 for _ in range(numRowCol)]
    for row in range(numRowCol):
        for col in range(numRowCol):
            # If it is "1" then sum column
            if int(matrix[row][col]) > 0:
                lookupTable[col] += int(matrix[row][col])
            else:
                # Clean the column if it's 0's.
                lookupTable[col] = 0
        # Calculate the maximum area.
        maxArea = max(maxArea, maximalRectangleInHistogram(lookupTable))
    return maxArea


def maximalRectangleInHistogram(histogram):
    # Create Stack for storing the index.
    posStack = []
    i = 0
    maxArea = 0
    while i < len(histogram):
        # if stack = None or current height is greater than the top one of the stack then append to posStack
        if len(posStack) == 0 or histogram[i] > histogram[posStack[-1]]:
            posStack.append(i)
            i += 1
        else:   #Update maxArea
            curr = posStack.pop()
            width = i if len(posStack) == 0 else i - posStack[-1] - 1
            maxArea = max(maxArea, width * histogram[curr])
    # Clean the stack.
    while posStack:
        curr = posStack.pop()
        width = i if len(posStack) == 0 else len(histogram) - posStack[-1] - 1
        maxArea = max(maxArea, width * histogram[curr])
    return maxArea
# Create value and read f
matrix = file
numRowCol = int(open('in.txt', "r").readline()[0:])
file = open('in.txt', "r")
readFile = file.readlines()[1:]
for line in readFile:
    line = line.replace(" ","")
    line = line.replace("\n","")
    matrix.append(line)

print(maximalRectangle(matrix,numRowCol))
answer = maximalRectangle(matrix, numRowCol)
# Write file
with open('out.txt', 'w') as f:
    f.write("%s " % answer)
    f.write('\n')
end = timeit.timeit()
# Check running time
print('Start: ',start)
print('End: ',end)
print(float(end - start))

