import pygame
import configparser


pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# displaySize = [1280, 720]
# screen = pygame.display.set_mode(displaySize)
# background = pygame.Surface(screen.get_size())
# clock = pygame.time.Clock()


def configSetup():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    return config


def str2bool(string):
    """
    If input string equal to True return True, False other wise.

    Parameters:
    -----------
    string: String to test (str)

    Return:
    -------
    Result: True or False (bool)

    Version:
    --------
    Spec : Ryan Rennoir V.1 (15/04/2018)
    Impl : Ryan Rennoir V.1 (15/04/2018)
    """
    string = string.lower()
    if string == 'true':
        return True

    return False


class Player:
    def __init__(self, config):
        self.baseCoordinate = [0, 0]
        self.baseHP = int(config['base_hp'])
        self.ore = int(config['starting_ore'])
        self.vehicles = {}

    def buy(self, name, vehicleClass):

        if self.ore >= vehicleClass.cost:
            self.vehicles.update({name: Vehicles(self, name, vehicleClass)})

        else:
            print('Not enough ore!')

    def update(self):
        for elements in self.vehicles:
            self.vehicles[elements].update()

    def delVehicles(self, name):
        self.vehicles.pop(name)


class VehiclesClass:
    def __init__(self, vehiclesClass):
        self.life = int(vehiclesClass['life'])
        self.range = int(vehiclesClass['range'])
        self.maxOre = int(vehiclesClass['max ore'])
        self.state = str2bool(vehiclesClass['lock'])
        self.attack = int(vehiclesClass['attack'])
        self.cost = int(vehiclesClass['cost'])


class Vehicles:
    def __init__(self, player, vehiclesName, vehiclesClass):
        self.name = vehiclesName

        self.life = vehiclesClass.life
        self.range = vehiclesClass.range
        self.maxOre = vehiclesClass.maxOre
        self.state = vehiclesClass.state
        self.attack = vehiclesClass.attack
        self.cost = vehiclesClass.cost

        self.ore = 0
        self.coord = player.baseCoordinate
        self.finalCoordinate = []

    def move(self, finalCoord):

        if not finalCoord == self.coord:
            self.finalCoordinate = []
            return

        self.finalCoordinate = finalCoord
        # TODO

    def attack(self, target):
        pass  # TODO

    def changeState(self):
        pass  # TODO

    def update(self):
        pass  # TODO

    def __del__(self):
        # Only for debug
        print('Object %s deleted' % self.name)


config = configSetup()
configGlob = config['general']

# All vessel class config
scout = VehiclesClass(config['scout'])
warship = VehiclesClass(config['warship'])
excavator_S = VehiclesClass(config['excavator-S'])
excavator_M = VehiclesClass(config['excavator-M'])
excavator_L = VehiclesClass(config['excavator-L'])

player1 = Player(configGlob)
player1.buy('jean', excavator_L)
player1.buy('paul', excavator_M)
print(player1.vehicles)
player1.update()
player1.delVehicles('jean')

# Ended = False
# while not Ended:
#     clock.tick(60)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             loop = False
#             quit()
#
#     pygame.display.update()
#     screen.blit(background, (0, 0))
