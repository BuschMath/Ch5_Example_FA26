import csv
def makeDataList(dataName):
    with open("earthquakes.csv", 'r') as inFile:
        dataList = []

        csvReader = csv.reader(inFile)    #get iterator
        titles = next(csvReader)      #read first line

        colNum = 0                    #search for colName
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum = colNum + 1

        if colNum == len(titles):     #was titles end reached?
            print("Error:", dataName, "not found.")
        else:
            for line in csvReader:				
                dataList.append(float(line[colNum]))
    return dataList

def makeDataListComprehension(dataName):
    with open("earthquakes.csv", "r") as inFile:
        dataList = []

        csvReader = csv.reader(inFile)    #get iterator
        titles = next(csvReader)          #read first line

        colNum = 0                    #search for colName
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum = colNum + 1

        if colNum == len(titles):     #was titles end reached?
            print("Error:", dataName, "not found.")
        else:
            dataList = [(float(line[colNum])) for line in csvReader]
    return dataList

def frequencyTable(aList):
    countDict = {}
    for item in aList:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    itemList = list(countDict.keys())
    itemList.sort()

    print("ITEM", "FREQUENCY")
    for item in itemList:
        print("{0:4.2} {1:6}".format(item, countDict[item]))
      
def correlation(xList, yList):
    import statistics
    xBar = statistics.mean(xList)
    yBar = statistics.mean(yList)
    xStd = statistics.stdev(xList)
    yStd = statistics.stdev(yList)
    num = 0.0
    for i in range(len(xList)):
        num = num + (xList[i] - xBar) * (yList[i] - yBar)
    corr = num / ((len(xList) - 1) * xStd * yStd)
    return corr

