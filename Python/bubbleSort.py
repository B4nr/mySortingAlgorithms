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



def inputNumbers():
    y = int(input("Quantos numeros voce quer comparar?"))
    #y = 3
    global list
    list = []
    for x in range(y):
        z = input(f"Digite o numero {x+1}: ")
        list.append(z)

inputNumbers()
print(bubbleSort(list))
