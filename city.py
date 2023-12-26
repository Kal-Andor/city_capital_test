
class City:
    _name: str
    _population: int

    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    # getter metódus meghatározási módja pythonban
    @property
    def name(self):
        return self._name

    # setter metódus meghatározási módja pythonban
    @name.setter
    def name(self, value: str):
        # rutinellenörzése, hogy megfelelő típúsú értéket kapunk-e
        if type(value) is not str:
            raise ValueError
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value: int):
        if type(value) is not int:
            raise ValueError
        self._population = value

    def adequate(self):
        raise NotImplementedError

    # toString metódus python megfelelője
    def __str__(self):
        template: str = "Név: {name}, Lakosság: {population}"

        final_string = template.format(name=self.name, population=self.population)
        return final_string


if __name__ == "__main__":
    city = City("Székelyudvarhely", 34000)

    print(city)
