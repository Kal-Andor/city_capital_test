from city import City

# Főváros esetén a feladat nem határozta meg explicit módon a setter metódusok létrehozását csak a getter-ekét de ennek ellenére létrehoztam.
# Illetve szintén nem volt meghatározva, hogy a szennyezettség és a metrók száma értékek legyenek-e szükségesek az osztály
# példányosításánál, ezért a megadásukat opcionálissá tettem, alapértelmezett értékek beállításával.


class Capital(City):
    _contamination: int
    _nr_of_metros: int

    def __init__(self, name: str, population: int, contamination: int = 45, nr_of_metros: int = 6):
        super().__init__(name, population)  # az örökölt osztály inicializálása
        self.contamination = contamination
        self.nr_of_metros = nr_of_metros

    @property
    def contamination(self):
        return self._contamination

    @contamination.setter
    def contamination(self, value: int):
        if type(value) is not int:
            raise ValueError
        self._contamination = value

    @property
    def nr_of_metros(self):
        return self._nr_of_metros

    @nr_of_metros.setter
    def nr_of_metros(self, value: int):
        if type(value) is not int:
            raise ValueError
        self._nr_of_metros = value

    def adequate(self):
        if self.population < 100000 and self.contamination < 50 and self.nr_of_metros > 5:
            return True
        else:
            return False

    def __str__(self):
        template: str = "Név: {name}, Lakosság: {population}, Szenyezetség: {contamination}, Metrók száma: {nr_of_metros}, Megfelelő: {adequate}"

        final_string = template.format(
            name=self.name,
            population=self.population,
            contamination=self.contamination,
            nr_of_metros=self.nr_of_metros,
            adequate="Igen" if self.adequate() else "Nem",
        )
        return final_string
