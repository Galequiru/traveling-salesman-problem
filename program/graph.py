class Graph:
    def __init__(self, size: int) -> None:
        self.size = size
        self.cities = [City(None) for _ in range(size)]
        self.distances = [[0 for _ in range(size)] for _ in range(size)]

    def setCoordinates(self, cityIndex: int, coordinates: tuple[int,int]):
        self.cities[cityIndex].coordinates = coordinates

    def setDistance(self, city1: int, city2: int, distance: int):
        self.distances[city1][city2] = self.distances[city2][city1] = distance
        
class City:
    def __init__(self, coordinates: tuple[int,int]) -> None:
        self.coordinates = coordinates
        self.visited = False