class Country(object):
    class Navy:
        def __init__(self, sailors, ships):
            self.sailors = sailors
            self.ships = ships

        def nav():
            sailors = int(input("How many sailors do you have in your navy?: "))
            ships = int(input("How many ships do you have in your navy?: "))

    class Army:
        pass

    class AirForce:
        pass


india_navy = Country.Navy
if __name__ == "__main__":
    Country.Navy.nav()
