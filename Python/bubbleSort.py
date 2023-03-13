def bubbleSort(randomList):
    randomListLenght = len(randomList)
    randomListLenghtMinusOne = randomListLenght - 1
    for x in randomList:
        x=0
        y=1
        for z in range(0,randomListLenghtMinusOne):
            if randomList[x] > randomList[y]:
                pivot = randomList[x]
                randomList[x] = randomList[y]
                randomList[y] = pivot
            #print("One comparasion has been made")
            #print(f"{x=}\n{y=}\n")
            x += 1
            y += 1
    return(randomList)
