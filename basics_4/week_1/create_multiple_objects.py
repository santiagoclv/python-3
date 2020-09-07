city_names = ["Shangai", "Montevideo", "Madrid"]
population = [100, 1, 3]
counties = ["China", "Uruguay", "España"]

city_tuples = zip(city_names, population, counties)

class City:
    def __init__(self, city, population, country):
        self.city = city
        self.population = population
        self.country = country
    
    def __str__(self):
        return '{}, {} - population {}'.format(self.country, self.city, self.population)

cities = [City(*t) for t in city_tuples]

for city in cities:
    print(city)