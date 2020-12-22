class Guitar:
    def __init__(self, name, year, cost):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        str = "{0} ({1}) : ${2}".format(self.name, self.year, self.cost)
        return str

    def get_age(self):
        self.age = 2020 - self.year
        return self.age

    def is_vintage(self):
        if self.get_age()>49:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost