from collections import deque

'''
    This code was written  by Bruno Melo Moreira
'''


class City:
    name = None
    childs = None
    depth = None
    distance = None

    def __init__(self, name, childs, depth, distance):
        self.name = name
        self.childs = childs
        self.depth = depth
        self.distance = distance


eforie = City("Eforie", None, 6, 86)
neamt = City("Neamt", None, 7, 87)
hirsova = City("Hiraova", [eforie], 5, 98)
iasi = City("Iasi", [neamt], 6, 92)
vaslui = City("Vaslui", [iasi], 5, 142)
urziceni = City("Urziceni", [vaslui, hirsova], 4, 85)
giurgiu = City("Giurgiu", None, 4, 90)

bucharest = City("Craiova", [giurgiu, urziceni], 7, 101)
pitesti = City("Pitesti", [bucharest], 6, 138)
craiova = City("Craiova", [pitesti], 5, 146)
bucharest = City("Bucharest", [giurgiu, urziceni], 6, 101)
pitesti = City("Pitesti", [bucharest], 5, 97)
rimnicuVilcea = City("Rimnicu Vilcea", [craiova, pitesti], 4, 80)
bucharest = City("Bucharest", [giurgiu, urziceni], 5, 211)
fagaras = City("Fagaras", [bucharest], 4, 99)
sibiu = City("Sibiu", [rimnicuVilcea, fagaras], 3, 151)
oradea = City("Oradea", [sibiu], 2, 71)
zerind = City("Zerind", [oradea], 1, 75)



bucharest = City("Bucharest", [giurgiu, urziceni], 5, 101)
pitesti = City("Pitesti", [bucharest], 4, 138)
craiova = City("Craiova", [pitesti], 3, 146)
bucharest = City("Bucharest", [giurgiu, urziceni], 4, 101)
pitesti = City("Pitesti", [bucharest], 3, 97)
rimnicuVilcea = City("Rimnicu Vilcea", [craiova, pitesti], 2, 80)
bucharest = City("Bucharest", [giurgiu, urziceni], 3, 211)
fagaras = City("Fagaras", [bucharest], 2, 99)
sibiu = City("Sibiu", [rimnicuVilcea, fagaras], 1, 140)


bucharest = City("Bucharest", [giurgiu, urziceni], 8, 101)
pitesti = City("Pitesti", [bucharest], 7, 138)
rimnicuVilcea  = City("Pitesti", [pitesti], 6, 146)
bucharest = City("Bucharest", [giurgiu, urziceni], 7, 101)
pitesti = City("Pitesti", [bucharest], 6, 138)
craiova = City("Craiova", [pitesti, rimnicuVilcea ], 5, 120)
dobreta = City("Dobreta", [craiova], 4, 75)
mehadia = City("Mehadia", [dobreta], 3, 70)
lugoj = City("Lugoj", [mehadia], 2, 111)
timisoara = City("Timisoara", [lugoj], 1, 118)
arad = City("Arad", [timisoara, sibiu, zerind], 0, 0)

def getMinDistance(city):
    minChild = city.childs[0]
    for child in city.childs:
        if(child.distance < minChild.distance ):
            minChild = child
    return minChild

def breadthSearch(firstCity):
    queue = deque([firstCity])
    path = []
    while (True):
        city = queue.popleft()
        if (city.name == "Bucharest"):
            print(path)
            break
        else:
            path.append(city.name)
            for child in city.childs:
                queue.append(child)

def depthSearch(firstCity):
    stack = [firstCity]
    path = []
    while (True):
        city = stack.pop()
        if (city.name == "Bucharest"):
            print(path)
            break
        else:
            path.append(city.name)
            for child in city.childs:
                stack.append(child)

def iterativeDepthSearch(firstCity, maxDepth):
    stack = [firstCity]
    path = []
    while(True):
        city = stack.pop()
        if (city.name == "Bucharest"):
            path.append(city.name)
            print(path)
            break
        else:
            if(city.depth < maxDepth):
                path.append(city.name)
                for child in city.childs:
                    stack.append(child)
        if (stack == []):
            print("No results were found")
            break

def uniformCostSearch(firstCity):
    queue = deque([firstCity])
    path = []
    while (True):
        city = queue.popleft()
        if (city.name == "Bucharest"):
            print(path)
            break
        else:
            path.append(city.name)
            queue.append(getMinDistance(city))



breadthSearch(arad)
depthSearch(arad)
iterativeDepthSearch(arad, 3)
uniformCostSearch(arad)