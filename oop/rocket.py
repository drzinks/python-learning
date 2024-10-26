class Rocket:
    """
    description of class
    """

    def __init__(self, speed = 1):
        self.altitude = 0
        self.speed = speed

    def move_up(self):
        """
        moves the rocket up
        """
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on altitude " + str(self.altitude) + " m."


from random import randint
class RocketBoard:
    def __init__(self, amount_of_rockets=5):
        self.rockets = [Rocket(randint(1,6)) for _ in range(amount_of_rockets)]

        for _ in range (10): #0 to 9
            rocket_to_move = randint(0,len(self.rockets) - 1)
            self.rockets[rocket_to_move].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1: Rocket,rocket2: Rocket) -> int:
        return abs(rocket1.altitude - rocket2.altitude)