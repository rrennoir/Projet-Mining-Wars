import pygame
import configparser
# import time


pygame.init()

black = (0, 0, 0)

red = (255, 0, 0)
redLight = (120, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)
blueLight = (0, 0, 120)

white = (255, 255, 255)

caseSize = 15

base1 = [3, 3]
base2 = [7, 7]

displaySize = [700, 650]
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


class Map:
    def __init__(self, dimention, screenSize):
        self.column = dimention[0]
        self.line = dimention[1]
        self.color = [blueLight, redLight]
        
        self.tileSize = caseSize

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

                rectangle = pygame.Rect(xOffset, yOffset, self.tileSize, self.tileSize)
                pygame.draw.rect(screen, self.color[index], rectangle)


class Player:
    def __init__(self, config, number):
        
        self.baseHP = config.getint('base_hp')
        self.ore = config.getint('starting_ore')
        self.vehicles = {}

        self.baseCoordinate = base1
        self.color = blue
        if number != 1:
            self.color = red
            self.baseCoordinate = base2

    def buy(self, name, vehicleClass):

        if self.ore >= vehicleClass.cost:
            self.vehicles.update({name: Vehicles(self, name, vehicleClass)})

        else:
            print('Not enough ore!')

    def update(self):
        for elements in self.vehicles:
            self.vehicles[elements].update()

    def draw(self):
        # Draw Base.
        size = caseSize * 1

        # -1 because array start at 1,1 not 0,0
        baseRect = pygame.Rect((self.baseCoordinate[0] - 1) * caseSize,
                               (self.baseCoordinate[1] - 1) * caseSize, size, size)

        pygame.draw.ellipse(screen, self.color, baseRect)

        # Draw vehicles.
        for Vehicle in self.vehicles:
            vehicleObejct = player1.vehicles[Vehicle]

            # -1 because array start at 1,1 not 0,0
            rectangle = pygame.Rect((vehicleObejct.coord[0] - 1) * caseSize,
                                    (vehicleObejct.coord[1] - 1) * caseSize, caseSize, caseSize)

            pygame.draw.rect(screen, white, rectangle)        

    def delVehicles(self, name):
        self.vehicles.pop(name)


class VehiclesClass:
    def __init__(self, vehiclesClass):
        self.life = vehiclesClass.getint('life')
        self.range = vehiclesClass.getint('range')
        self.maxOre = vehiclesClass.getint('max ore')
        self.state = vehiclesClass.getboolean('lock')
        self.attackDmg = vehiclesClass.getint('attack')
        self.cost = vehiclesClass.getint('cost')


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
        self.coord = player.baseCoordinate.copy()
        self.finalCoordinate = []

    def move(self, finalCoord):

        if finalCoord == self.coord:
            self.finalCoordinate = []
            return


        print(finalCoord, self.coord)


        self.finalCoordinate = finalCoord
        deltaX = self.finalCoordinate[0] - self.coord[0]
        deltaY = self.finalCoordinate[1] - self.coord[1]

        print(deltaX, deltaY)


        if deltaX != 0:
            self.coord[0] += deltaX / abs(deltaX)
        if deltaY != 0:
            self.coord[1] += deltaY / abs(deltaY)

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

map = Map([10, 10], displaySize)

player1 = Player(configGlob, 1)
player2 = Player(configGlob, 2)

player1.buy('jean', excavator_L)
player1.buy('paul', excavator_M)

Ended = False
while not Ended:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            quit()
    
    map.draw()
    
    player1.vehicles['jean'].move([7, 10])
    player1.vehicles['paul'].move([1, 1])

    player1.update()

    player2.update()

    player1.draw()
    player2.draw()
    pygame.display.update()
    screen.blit(background, (0, 0))
