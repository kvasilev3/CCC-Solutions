from itertools import count
import sys

swaps = 0

def swap(items:list, index1:int, index2:int):
    global swaps
    temp = items[index1]
    items[index1] = items[index2]
    items[index2] = temp
    swaps += 1

def inplace_counting_sort(line: str):
    global swaps
    swaps = 0
    lineAsList = list(line)
    size = len(lineAsList)
    valueIndex = {'unused':0, 'L':1, 'M':2, 'S':3}
    counts = [0] * len(valueIndex)
    positions = [0] * len(valueIndex)

    for c in lineAsList:
        counts[valueIndex[c]] += 1
    for i in range(2,len(valueIndex)):
        counts[i] += counts[i-1]
    positions = counts[:]

    i = 0
    while i < size:
        c = lineAsList[i]
        placed = positions[valueIndex[c] - 1] <= i & i < positions[valueIndex[c]]
        if placed:
            i += 1
        else:
            swap(lineAsList, i, counts[valueIndex[c]] - 1)
            counts[valueIndex[c]] -= 1
    return swaps

def doSingleStepSwaps(items:list, letter1, index1Start, index1End, letter2, index2Start, index2End):
    index1 = index1Start
    index2 = index2Start
    while index1 < index1End:
        if items[index1] == letter1:
            while index2 < index2End:
                if items[index2] == letter2:
                    swap(items, index1, index2)
                    break
                index2 += 1
        index1 += 1

def optimalSort(line:str):
    global swaps
    swaps = 0

    groupIndex = {'unused':0, 'L':1, 'M':2, 'S':3}
    counts = [0, line.count('L'), line.count('M'), line.count('S')]
    for i in range(2,len(groupIndex)):
        counts[i] += counts[i-1]
    
    lineAsList = list(line)

    # Do the direct swaps - when the two elements will go into their groups
    for g in range(1,len(counts)):
        groupKey = list(groupIndex.keys())[g]
        groupStartIndex = counts[g-1]
        groupEndIndex = counts[g]
        groupIndexes = [0, 0, counts[1], counts[2]]
        for j in range(groupStartIndex, groupEndIndex):
            currentValue = lineAsList[j]
            if currentValue != groupKey:
                currentValueGroupIndex = groupIndex[currentValue]
                # Loop through the group of the current element at position j
                while groupIndexes[currentValueGroupIndex] < counts[currentValueGroupIndex]:
                    if lineAsList[groupIndexes[currentValueGroupIndex]] == groupKey:
                        swap(lineAsList, j, groupIndexes[currentValueGroupIndex])
                        break
                    groupIndexes[currentValueGroupIndex] += 1

    # Do the indirect swaps - where a swap will bring only one of the elements to 
    # its correct position; the second element will need another swap
    for g in range(1,len(counts)):
        groupKey = list(groupIndex.keys())[g]
        groupStartIndex = counts[g-1]
        groupEndIndex = counts[g]
        searchIndex = groupEndIndex
        for j in range(groupStartIndex, groupEndIndex):
            currentValue = lineAsList[j]
            if currentValue != groupKey:
                while searchIndex < len(lineAsList):
                    if lineAsList[searchIndex] == groupKey:
                        swap(lineAsList, j, searchIndex)
                        break
                    searchIndex += 1

    #doSingleStepSwaps(lineAsList, 'M', counts[0], counts[1], 'L', counts[1], counts[2])
    #doSingleStepSwaps(lineAsList, 'S', counts[1], counts[2], 'M', counts[2], counts[3])
    #doSingleStepSwaps(lineAsList, 'L', counts[2], counts[3], 'S', counts[0], counts[1])
    return swaps

def findAndSwapElement(items:list, startIndex:int, endIndex:int, findValue:str, swapIndex:int):
    for i in range(startIndex, endIndex):
        if items[i] == findValue:
            swap(items, i, swapIndex)
            break
    return i

def optimalSort2(line:str):
    global swaps
    swaps = 0

    lineAsList = list(line)
    lGroupSize = lineAsList.count('L')
    mGroupSize = lineAsList.count('M')
    sGroupSize = lineAsList.count('S')

    lGroupBoundary = lGroupSize
    mGroupBoundary = lGroupBoundary + mGroupSize
    sGroupBoundary = mGroupBoundary + sGroupSize
    
    # 1. Do the direct swaps - when the two elements will go into their groups

    mGroupIndex = lGroupBoundary
    sGroupIndex = mGroupBoundary
    for lGroupIndex in range(0, lGroupBoundary):
        if lineAsList[lGroupIndex] == 'M':
            # Loop through the M group and find an element L, so that it can be swapped with the current element
            mGroupIndex = findAndSwapElement(lineAsList, mGroupIndex, mGroupBoundary, 'L', lGroupIndex)

        elif lineAsList[lGroupIndex] == 'S':
            # Loop through the S group and find an element L, so that it can be swapped with the current element
            sGroupIndex = findAndSwapElement(lineAsList, sGroupIndex, sGroupBoundary, 'L', lGroupIndex)
    
    sGroupIndex = mGroupBoundary
    for mGroupIndex in range(lGroupBoundary, mGroupBoundary):
        # The direct swaps between L and M group have already been done in the previous loop.
        # Here we only look for direct swaps between M and S groups
        if lineAsList[mGroupIndex] == 'S':
            # Loop through the S group and find an element M, so that it can be swapped with the current element
            sGroupIndex = findAndSwapElement(lineAsList, sGroupIndex, sGroupBoundary, 'M', mGroupIndex)
    
    # 2. Do the indirect swaps - where a swap will bring only one of the elements to 
    #    its correct position; the second element will need an additional swap

    searchIndex = lGroupBoundary
    for lGroupIndex in range(0, lGroupBoundary):
        if lineAsList[lGroupIndex] != 'L':
            # Loop through all groups after L, and find an element L, so that it can be swapped with the current element
            searchIndex = findAndSwapElement(lineAsList, searchIndex, len(lineAsList), 'L', lGroupIndex)

    searchIndex = mGroupBoundary
    for mGroupIndex in range(lGroupBoundary, mGroupBoundary):
        if lineAsList[mGroupIndex] != 'M':
            # Loop through all groups after M, and find an element M, so that it can be swapped with the current element
            searchIndex = findAndSwapElement(lineAsList, searchIndex, len(lineAsList), 'M', mGroupIndex)

    return swaps

def calculateNeededSwaps(line):
    lGroupSize = line.count('L')
    mGroupSize = line.count('M')
    sGroupSize = line.count('S')

    lGroupBoundary = lGroupSize
    mGroupBoundary = lGroupBoundary + mGroupSize
    sGroupBoundary = mGroupBoundary + sGroupSize

    mElementsInLGroup = 0
    sElementsInLGroup = 0
    for i in range(0, lGroupBoundary):
        if line[i] == 'M':
            mElementsInLGroup +=1
        elif line[i] == 'S':
            sElementsInLGroup +=1
    
    lElementsInMGroup = 0
    sElementsInMGroup = 0
    for i in range(lGroupBoundary, mGroupBoundary):
        if line[i] == 'L':
            lElementsInMGroup +=1
        elif line[i] == 'S':
            sElementsInMGroup +=1
    
    lElementsInSGroup = 0
    mElementsInSGroup = 0
    for i in range(mGroupBoundary, sGroupBoundary):
        if line[i] == 'L':
            lElementsInSGroup +=1
        elif line[i] == 'M':
            mElementsInSGroup +=1

    directSwaps = min(mElementsInLGroup, lElementsInMGroup) + \
        min(sElementsInLGroup, lElementsInSGroup) + \
        min(sElementsInMGroup, mElementsInSGroup)

    # The three abs() expressions below should return equal values. Thus, it should be 
    # enough to just calculate one of them. But for completeness, we do all of them and 
    # take the maximim.
    indirectSwaps = max(abs(mElementsInLGroup - lElementsInMGroup),
        abs(sElementsInLGroup - lElementsInSGroup),
        abs(sElementsInMGroup - mElementsInSGroup))
    # Every set of 3 elements will need two swaps to get into their correct places
    indirectSwaps = indirectSwaps * 2

    return directSwaps + indirectSwaps

def j4():
    for line in sys.stdin:
        line = line.strip()
        print(optimalSort2(line))
        #print(calculateNeededSwaps(line))

if __name__ == '__main__':
    j4()
