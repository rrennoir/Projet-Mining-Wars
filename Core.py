import pygame
import configparser
# import time


pygame.init()

black = (0, 0, 0)

red = (255, 0, 0)
redLight = (120, 0, 0)

green = (0, 255, 0)
test = (70, 100, 50)

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


def update(player1, player2):
    playerList = (player1, player2)

    # Phase one (buy)
    for playerOrderBuy in playerList:
        for buy in reversed(playerOrderBuy.ToBuy):

            buyIndex = playerOrderBuy.ToBuy.index(buy)

            name = buy[0]
            className = buy[1]

            playerOrderBuy.ToBuy.pop(buyIndex)
            if name in playerOrderBuy.vehicles:
                continue

            playerOrderBuy.buy(name, className)

    # Phase two (move)
    for playerOrderMove in playerList:
        for vehicle in playerOrderMove.vehicles:
            playerOrderMove.vehicles[vehicle].move()

    # Phase three (state change)
    for playerOrderState in playerList:
        for vehicle in playerOrderState.vehicles:
            playerOrderState.vehicles[vehicle].stateChange()

    # Phase four (attack)
    for playerOrderAtt in playerList:
        for vehicle in playerOrderAtt.vehicles:
            pass


class Map:
    def __init__(self, dimention):
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
        self.order = []
        self.ToBuy = []

        self.baseCoordinate = base1
        self.color = blue
        if number != 1:
            self.color = red
            self.baseCoordinate = base2

    def buy(self, name, vehicleClassName):
        if vehicleClassName == 'scout':
            vehicleClass = scout

        elif vehicleClassName == 'warship':
            vehicleClass = warship

        elif vehicleClassName == 'excavator-S':
            vehicleClass = excavator_S

        elif vehicleClassName == 'excavator-M':
            vehicleClass = excavator_M

        else:
            vehicleClass = excavator_L

        if self.ore >= vehicleClass.cost:
            self.vehicles.update({name: Vehicles(self, name, vehicleClass)})
            self.ore -= vehicleClass.cost

        else:
            print('Not enough ore!')

    def orderControle(self, order):

        orders = order.split()
        for command in orders:

            index_order = command.find(':')
            if index_order == -1:
                continue

            vehicleName = command[:index_order]
            vehicleClass = command[index_order + 1:]
            if vehicleClass in ('scout', 'warship', 'excavator-S', 'excavator-M', 'excavator-L'):
                if vehicleName in self.vehicles:
                    continue

                self.ToBuy.append([vehicleName, vehicleClass])

            if '@' in command:

                index_order_type = command.find('@')
                index_coord_separator = command.find('-', index_order)

                vehicle = command[:index_order]

                # Get all the coordinate info in the order
                row = command[index_order_type + 1:index_coord_separator]
                column = command[index_coord_separator + 1:]

                # Check if the coordinate given are digit
                if not (row.isdigit() and column.isdigit()):
                    continue

                self.vehicles[vehicle].finalCoordinate = [int(column), int(row)]

            if 'release' in command or 'lock' in command:

                order = command[index_order + 1:]
                if order not in ('release', 'lock'):
                    continue

                vehicle = command[:index_order]
                self.vehicles[vehicle].finalState = order

    def draw(self):
        # Draw Base.
        size = caseSize * 1

        # -1 because array start at 1,1 not 0,0
        baseRect = pygame.Rect((self.baseCoordinate[0] - 1) * caseSize,
                               (self.baseCoordinate[1] - 1) * caseSize, size, size)

        pygame.draw.ellipse(screen, self.color, baseRect)

        # Draw vehicles.
        for Vehicle in self.vehicles:
            vehicleObject = player1.vehicles[Vehicle]

            # -1 because array start at 1,1 not 0,0
            rectangle = pygame.Rect((vehicleObject.coord[0] - 1) * caseSize,
                                    (vehicleObject.coord[1] - 1) * caseSize, caseSize, caseSize)

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

        if vehiclesClass.state:
            self.state = 'release'
        else:
            self.state = None

        self.attackDmg = vehiclesClass.attackDmg
        self.cost = vehiclesClass.cost

        self.ore = 0
        self.coord = player.baseCoordinate.copy()
        self.finalCoordinate = []
        self.finalState = ''

    def move(self):

        if self.finalCoordinate == [] or self.finalCoordinate == self.coord or self.state == 'lock':
            self.finalCoordinate = []
            return

        deltaX = self.finalCoordinate[0] - self.coord[0]
        deltaY = self.finalCoordinate[1] - self.coord[1]

        if deltaX != 0:
            self.coord[0] += deltaX / abs(deltaX)
        if deltaY != 0:
            self.coord[1] += deltaY / abs(deltaY)

    def stateChange(self):
        if self.state is None or self.finalState == '' or self.finalState == self.state:
            self.finalState = ''
            return

        if self.finalState == 'release':
            self.state = 'release'

        else:
            self.state = 'lock'

        self.finalState = ''

    def attack(self, target):
        coord = self.coord

        # Measures the Manhattan distance(|row_b - row_a| + |column_b - column_a|)
        deltaX = abs(coord - target)
        deltaY = abs(coord - target)
        deltaTotal = deltaX + deltaY

        if deltaTotal > self.range:
            return

        if target == coord:
            pass
            # update the other

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

map = Map([10, 10])

player1 = Player(configGlob, 1)
player2 = Player(configGlob, 2)

# player1.buy('jean', excavator_L)
# player1.buy('paul', excavator_M)

player1.orderControle('jean:scout')
player1.orderControle('engi:excavator-S')

# draw the map before the 1st command
map.draw()

Ended = False
while not Ended:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            quit()
    
    map.draw()

    # player1.orderControle(input("Player 1's order: "))
    # player2.orderControle(input("Player 2's order: "))

    update(player1, player2)

    player1.draw()
    player2.draw()
    pygame.display.update()
    screen.blit(background, (0, 0))
