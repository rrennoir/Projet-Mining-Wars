import pygame
import configparser


pygame.init()

black = (0, 0, 0)

red = (255, 0, 0)
redLight = (120, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)
blueLight = (0, 0, 120)

white = (255, 255, 255)

caseSize = 15

displaySize = [1280, 720]
screen = pygame.display.set_mode(displaySize)
background = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()


def configSetup():
    """
    Convert a config file (config.ini) in to a variable

    Return:
    -------
    config: the config 
    """
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


class Map:
    def __init__(self, dimention, screenSize):
        self.column = dimention[0]
        self.line = dimention[1]
        self.color = [blueLight, redLight]
        
        self.tileSize = 15


    def draw(self):
        xOffset = 0
        for i in range(self.line):
            yOffset = i * self.tileSize

            offset = 0
            if i % 2 == 0:
                offset = 1

            for j in range(self.column):
                xOffset = j * self.tileSize

                index = 0
                if (j + offset) % 2 == 0:
                    index = 1

                rectangle = pygame.Rect(xOffset, yOffset , self.tileSize, self.tileSize)
                pygame.draw.rect(screen, self.color[index], rectangle)

class Player:
    def __init__(self, config, number):
        self.baseCoordinate = [0, 0]
        self.baseHP = int(config['base_hp'])
        self.ore = int(config['starting_ore'])
        self.vehicles = {}

        self.color = blue
        if number != 1:
            self.color = red

    def buy(self, name, vehicleClass):

        if self.ore >= vehicleClass.cost:
            self.vehicles.update({name: Vehicles(self, name, vehicleClass)})

        else:
            print('Not enough ore!')

    def update(self):
        for elements in self.vehicles:
            self.vehicles[elements].update()

    def draw(self):
        # Draw vehicles.
        for Vehicle in self.vehicles:
            vehicleObejct = player1.vehicles[Vehicle]

            rectangle = pygame.Rect(vehicleObejct.coord[0], vehicleObejct.coord[1] , caseSize, caseSize)
            pygame.draw.rect(screen, white, rectangle)        
        
        # Draw Base.
        size = caseSize * 5
        baseRect = pygame.Rect(self.baseCoordinate[0], self.baseCoordinate[1], size, size)
        pygame.draw.ellipse(screen, green, baseRect)

    def delVehicles(self, name):
        self.vehicles.pop(name)


class VehiclesClass:
    def __init__(self, vehiclesClass):
        self.life = int(vehiclesClass['life'])
        self.range = int(vehiclesClass['range'])
        self.maxOre = int(vehiclesClass['max ore'])
        self.state = str2bool(vehiclesClass['lock'])
        self.attackDmg = int(vehiclesClass['attack'])
        self.cost = int(vehiclesClass['cost'])


class Vehicles:
    def __init__(self, player, vehiclesName, vehiclesClass):
        self.name = vehiclesName

        self.life = vehiclesClass.life
        self.range = vehiclesClass.range
        self.maxOre = vehiclesClass.maxOre
        self.state = vehiclesClass.state
        self.attackDmg = vehiclesClass.attackDmg
        self.cost = vehiclesClass.cost

        self.ore = 0
        self.coord = player.baseCoordinate
        self.finalCoordinate = []

    def move(self, finalCoord):

        if finalCoord == self.coord:
            self.finalCoordinate = []
            return

        self.finalCoordinate = finalCoord

        deltaX = self.finalCoordinate[0] - self.coord[0]
        deltaY = self.finalCoordinate[1] - self.coord[1]

        self.coord[0] += deltaX
        self.coord[1] += deltaY
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

map = Map([80, 40], displaySize)

player1 = Player(configGlob, 1)
player2 = Player(configGlob, 2)

player1.buy('jean', excavator_L)
player1.buy('paul', excavator_M)

player1.vehicles['jean'].move([1, 2])
player1.update()

# player1.delVehicles('jean')

Ended = False
while not Ended:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            quit()

    
    map.draw()

    player1.update()
    # player2.update()

    player1.draw()
    # player2.draw()
    pygame.display.update()
    screen.blit(background, (0, 0))
