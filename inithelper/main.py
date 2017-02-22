from Cell import*

global originalDict

def main():
    originalfile = open("test.txt")
    lines = originalfile.readlines()
    print lines
    infolist = list()
    allElement = dict()

    for line in lines:
        lineclean = line.replace("\n","")
        result = lineclean.split("->")
        cell = Cell(result[0],result[1])
        infolist.append(cell)
        if allElement.has_key(result[0]) == False:
            allElement.setdefault(result[0],list())
        if allElement.has_key(result[1]) == False:
            allElement.setdefault(result[1],list())

    print infolist
    print allElement
    print "--------"
    buildGraph(infolist,allElement)

def buildGraph(infolist,allElement):
    for cell in infolist:
        dependencylist = (list)(allElement.get(cell.getDependencey()))
        dependencylist.append(cell.getByDependencey())
        allElement[cell.getDependencey()] = dependencylist
        print allElement[cell.getDependencey()]
    originalDict = allElement
    print "888888888"
    topSort(allElement,None)
    return

def topSort(allElement,header):
    if(header != None):
       pass
    else:
        externallist = list()
        for key in allElement:
            dependencylist = (list)(allElement[key])
            if(len(dependencylist) == 0):


    return

def prune(allElement,header):
    if(header == None):
        return allElement
    else:
        if(len(allElement[header]) == 0):
            result = dict()
            result.setdefault(allElement[header])
            return result;
        else:




if __name__=="__main__":
    main()




