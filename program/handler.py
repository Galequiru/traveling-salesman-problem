from graph import Graph
from salesman import Salesman
import io, math
import matplotlib.collections as mc
import matplotlib.pyplot as pl

class Handler:
    #def __init__(self) -> None:
    #    self.graph: Graph = None

    def createGraph(self, file: io.TextIOWrapper) -> Graph:
        lines = file.readlines()
        nCities = len(lines)
        graph = Graph(nCities)
        coordinatesArray = [(int(),int()) for _ in range(nCities)]

        for city in range(nCities):
            line = lines[city]
            coordinatesArray[city] = ( int(line[3:6]),
                                       int(line[7:]))
            graph.setCoordinates(int(line[:2]), coordinatesArray[city])

        for i in range(nCities):
            for j in range(i+1, nCities):
                graph.setDistance(i, j, math.ceil(math.dist(coordinatesArray[i], coordinatesArray[j])))

        return graph
    
    def getTourDistance(self, tour: list[int], distances: list[list[int]]) -> int:
        distance = 0

        for i in range(len(tour)-1):
            distance += distances[tour[i]][tour[i+1]]

        return distance
    
    def generateLines(self, coordinates: list[tuple[int,int]], tour: list[int]) -> list[list[int, int]]:
        lines = []
        
        for i in range(len(tour) -1):
            lines.append([
                coordinates[tour[i]],
                coordinates[tour[i+1]]
            ])

        return lines
    
    def drawTour(self, cities: Graph, tours: list[list[int]], problemName: str) -> None:
        color = ['y', 'b', 'g', 'r', 'm']
        title = ""
        totalDistance = 0

        fig, ax = pl.subplots()
        
        for i in range(len(tours)):
            lines = self.generateLines([city.coordinates for city in cities.cities], tours[i])
            lc = mc.LineCollection(lines, color=color[i])

            # calcula a distancia desse tour para colocá-la no título do gráfico
            distance = self.getTourDistance(tours[i], cities.distances)
            totalDistance += distance
            title = title + color[i] + "=" + str(distance) + " "
            ax.add_collection(lc)

        ax.autoscale()
        ax.margins(0.3)
        x = [city.coordinates[0] for city in cities.cities]
        y = [city.coordinates[1] for city in cities.cities]
        pl.scatter(x, y)
        pl.title(title+str(totalDistance))
        pl.xlabel('x')
        pl.ylabel('y')
        pl.savefig(problemName + ".png")
        pl.close()

    def solveProblem(self, problemRoute: str, problemName: str) -> None:
        file = io.open(problemRoute + problemName)
        cities = self.createGraph(file)
        nSalesman = int(problemName[-1])
        maxCities = math.ceil(cities.size / nSalesman)

        cities.cities[0].visited = True

        tours = []

        for _ in range(nSalesman):
            salesman = Salesman(cities)
            salesman.chooseCities(maxCities)
            tours.append(salesman.getTour())

        self.drawTour(cities, tours, problemName)