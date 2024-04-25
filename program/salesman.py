from graph import *
import math

class Salesman:
    def __init__(self, cities: Graph) -> None:
        self.citiesGraph = cities
        self.citiesThatWillBeVisited = []

    def chooseCities(self, maxCities: int) -> None:
        avaliableCities = []
        for cityIndex in range(len(self.citiesGraph.cities)):
            if not self.citiesGraph.cities[cityIndex].visited:
                avaliableCities.append(cityIndex)

        farthestCity = max(avaliableCities, key= lambda candidate: self.citiesGraph.distances[0][candidate])

        self.citiesThatWillBeVisited.append(farthestCity)
        self.citiesGraph.cities[farthestCity].visited = True
        avaliableCities.remove(farthestCity)

        while(len(self.citiesThatWillBeVisited) < maxCities and avaliableCities):
            coordinatesAverage = [0, 0]
            for city in self.citiesThatWillBeVisited:
                coordinatesAverage[0] += self.citiesGraph.cities[city].coordinates[0]
                coordinatesAverage[1] += self.citiesGraph.cities[city].coordinates[1]
            coordinatesAverage[0] /= len(self.citiesThatWillBeVisited)
            coordinatesAverage[1] /= len(self.citiesThatWillBeVisited)

            nearestCity = min(avaliableCities, key= lambda candidate: math.dist(coordinatesAverage, self.citiesGraph.cities[candidate].coordinates))
            
            self.citiesThatWillBeVisited.append(nearestCity)
            self.citiesGraph.cities[nearestCity].visited = True
            avaliableCities.remove(nearestCity)

    def getTour(self) -> list[int]:
        choosenCities = self.citiesThatWillBeVisited.copy()

        tour = [0]

        nearestCity = min(choosenCities, key= lambda candidate: self.citiesGraph.distances[tour[-1]][candidate])

        tour.append(nearestCity)
        choosenCities.remove(nearestCity)

        while(choosenCities):
            for city in tour:
                nextCity = min(choosenCities, key= lambda candidate: self.citiesGraph.distances[city][candidate])

            smallerDistanceIncrease = self.citiesGraph.distances[0][nextCity] +self.citiesGraph.distances[tour[1]][nextCity] - self.citiesGraph.distances[0][tour[1]]
            betterPosition = 1

            for position in range(1, len(tour)-1):
                distanceIncrease = self.citiesGraph.distances[tour[position]][nextCity] +self.citiesGraph.distances[tour[position+1]][nextCity] - self.citiesGraph.distances[tour[position]][tour[position+1]]
                if (distanceIncrease < smallerDistanceIncrease):
                    smallerDistanceIncrease = distanceIncrease
                    betterPosition = position+1

            tour.insert(betterPosition, nextCity)
            choosenCities.remove(nextCity)
            
        return tour + [0]