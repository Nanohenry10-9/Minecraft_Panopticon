#---------------------------------------Prepare-----------------------------------------

from mcpi.minecraft import Minecraft # Import Minecraft API
from time import sleep # Import sleep() from time library
from random import randint # import randint() from random library

mc = Minecraft.create() # Create connection between code and world
mc.setting("world_immutable", True) # Make the world immutable/mutable

playersNeededToPlay = 3 # The number of players needed to play the game
blocksToWin = 3


class player: # Create class "player"
    class plr1: # Class player one
        role = 1 # The role of the player
        numOfBlocks = 0 # The amount of blocks the player has

        class roleInfo: # This is a class for telling tha player that who is he/she
            class BH:
                x = -234
                y = 69
                z = -10

            class GH:
                x = -235
                y = 69
                z = -11

            class Ac:
                x = -237
                y = 69
                z = -11

            class NGO:
                x = -237
                y = 69
                z = -9

            class AV:
                x = -236
                y = 69
                z = -10

            class Tr:
                x = -235
                y = 69
                z = -9

    class plr2:
        role = 2
        numOfBlocks = 0

        class roleInfo:

            class BH:
                x = -239
                y = 69
                z = -20

            class GH:
                x = -240
                y = 69
                z = -19

            class Ac:
                x = -241
                y = 69
                z = -20

            class NGO:
                x = -239
                y = 69
                z = 18

            class AV:
                x = -238
                y = 69
                z = -19

            class Tr:
                x = -240
                y = 69
                z = -21

    class plr3:
        role = 3
        numOfBlocks = 0

        class roleInfo:

            class BH:
                x = -248
                y = 69
                z = -19

            class GH:
                x = -249
                y = 69
                z = -20

            class Ac:
                x = -247
                y = 69
                z = -20

            class NGO:
                x = -248
                y = 69
                z = -21

            class AV:
                x = -250
                y = 69
                z = -19

            class Tr:
                x = -249
                y = 69
                z = -18

    class plr4:
        role = 4
        numOfBlocks = 0

        class roleInfo:

            class BH:
                x = -252
                y = 69
                z = -11

            class GH:
                x = -253
                y = 69
                z = -10

            class Ac:
                x = -254
                y = 69
                z = -11

            class NGO:
                x = -253
                y = 69
                z = -12

            class AV:
                x = -252
                y = 69
                z = -13

            class Tr:
                x = -254
                y = 69
                z = -13

    class plr5:
        role = 5
        numOfBlocks = 0

        class roleInfo:

            class BH:
                x = -248
                y = 69
                z = -5

            class GH:
                x = -249
                y = 69
                z = -4

            class Ac:
                x = -249
                y = 69
                z = -6

            class NGO:
                x = -250
                y = 69
                z = -5

            class AV:
                x = -250
                y = 69
                z = -7

            class Tr:
                x = -251
                y = 69
                z = -6

    class plr6:
        role = 6
        numOfBlocks = 0

        class roleInfo:

            class BH:
                x = 239
                y = 69
                z = -5

            class GH:
                x = -240
                y = 69
                z = -7

            class Ac:
                x = -239
                y = 67
                z = -5

            class NGO:
                x = -240
                y = 69
                z = -4

            class AV:
                x = -237
                y = 69
                z = -6

            class Tr:
                x = -237
                y = 69
                z = -4

mc.events.clearAll() # Clear all "click" events


class gameOverText: # For showing the Game Over text
    x = -228
    y = 68
    z = 33


class welcomeText: # For showing the Welcome to Panopticon text
    x = -228
    y = 68
    z = 29

blocksY = 71  # Altitude of the board + 1

blocks1X = [-230, -224, -224, -219, -217, -219, -214, -212, -212, -214] # Locations of all blocks
blocks1Z = [-12, -15, -9, -20, -12, -4, -23, -16, -8, -1]

blocks2X = [-237, -237, -233, -238, -232, -228, -239, -234, -228, -223]
blocks2Z = [-23, -31, -28, -37, -34, -30, -43, -42, -39, -34]

blocks3X = [-251, -255, -251, -260, -256, -250, -265, -260, -254, -249]
blocks3Z = [-23, -28, -31, -30, -34, -37, -34, -39, -42, -43]

blocks4X = [-258, -264, -264, -269, -271, -269, -274, -276, -276, -274]
blocks4Z = [-12, -9, -15, -4, -12, -20, -1, -8, -16, -23]

blocks5X = [-251, -251, -255, -250, -256, -260, -249, -254, -260, -265]
blocks5Z = [-1, 7, 4, 13, 10, 6, 19, 18, 15, 10]

blocks6X = [-237, -233, -237, -228, -232, -238, -223, -228, -234, -239]
blocks6Z = [-1, 4, 7, 6, 10, 13, 10, 15, 18, 19]

throwDiceY = 73 # Locations of "Throw dice signs"
throwDiceX = [-236, -240, -248, -252, -248, -240]
throwDiceZ = [-12, -18, -18, -12, -6, -5]

blocks1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # Blocks that players have
blocks2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

all_blocks = [blocks1, blocks2, blocks3, blocks4, blocks5, blocks6] # All blocks

visibleLayers = [1, 1, 1, 1, 1, 1] # Visible layers
blocksToSee = [1, 1, 1, 1, 1, 1]

playerXPoses = [-235, -239, -249, -253, -249, -239] # Players positions (in the sectors)
playerYPoses = 72
playerZPoses = [-12, -19, -19, -12, -5, -5]

redstone_block = 152

mc.setBlocks(-235, 72, -12, -235, 79, -12, 0)
mc.setBlocks(-239, 72, -19, -239, 79, -19, 0)
mc.setBlocks(-249, 72, -19, -249, 79, -19, 0)


def checkBlocks(player): # Function for checking if there are blocks on the tower
    if player == 1:
        blocks1OnPlace1 = mc.getBlock(-235, 72, -12) # The coordinates of the towers bricks
        blocks1OnPlace2 = mc.getBlock(-235, 73, -12)
        blocks1OnPlace3 = mc.getBlock(-235, 74, -12)
        if blocks1OnPlace1 == 0: # Check how many blocks are there on the tower 
            mc.setBlock(blocks1X[0], blocksY, blocks1Z[0], 35, blocks1[0]) # Show the correct amount of blocks on the game board
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 0:
            for i in range(0, 3):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 0:
            for i in range(0, 6):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 35:
            for i in range(0, 10):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
    elif player == 2:
        blocks2OnPlace1 = mc.getBlock(-239, 72, -19)
        blocks2OnPlace2 = mc.getBlock(-239, 73, -19)
        blocks2OnPlace3 = mc.getBlock(-239, 74, -19)
        if blocks2OnPlace1 == 0:
            mc.setBlock(blocks2X[0], blocksY, blocks2Z[0], 35, blocks2[0])
        elif blocks2OnPlace1 == 35 and blocks2OnPlace2 == 0:
            for i in range(0, 3):
                mc.setBlock(blocks2X[i], blocksY, blocks2Z[i], 35, blocks2[i])
        elif blocks2OnPlace1 == 35 and blocks2OnPlace2 == 35 and blocks2OnPlace3 == 0:
            for i in range(0, 6):
                mc.setBlock(blocks2X[i], blocksY, blocks2Z[i], 35, blocks2[i])
        elif blocks2OnPlace1 == 35 and blocks2OnPlace2 == 35 and blocks2OnPlace3 == 35:
            for i in range(0, 10):
                mc.setBlock(blocks2X[i], blocksY, blocks2Z[i], 35, blocks2[i])
    elif player == 3:
        blocks3OnPlace1 = mc.getBlock(-249, 72, -19)
        blocks3OnPlace2 = mc.getBlock(-249, 73, -19)
        blocks3OnPlace3 = mc.getBlock(-249, 74, -19)
        if blocks3OnPlace1 == 0:
            mc.setBlock(blocks3X[0], blocksY, blocks3Z[0], 35, blocks3[0])
        elif blocks3OnPlace1 == 35 and blocks3OnPlace2 == 0:
            for i in range(0, 3):
                mc.setBlock(blocks3X[i], blocksY, blocks3Z[i], 35, blocks3[i])
        elif blocks2OnPlace1 == 35 and blocks2OnPlace2 == 35 and blocks2OnPlace3 == 0:
            for i in range(0, 6):
                mc.setBlock(blocks3X[i], blocksY, blocks3Z[i], 35, blocks3[i])
        elif blocks3OnPlace1 == 35 and blocks3OnPlace2 == 35 and blocks3OnPlace3 == 35:
            for i in range(0, 10):
                mc.setBlock(blocks3X[i], blocksY, blocks3Z[i], 35, blocks3[i])
    elif player == 4:
        print("Not possible yet")
    elif player == 5:
        print("Not possible yet")
    elif player == 6:
        print("Not possible yet")


def getPlayerNum(): # Function for getting the number of players online
    try: # Try/except is here because the mc.getPlayerEntityIds() function fails if there aren't any players online
        playerIds = mc.getPlayerEntityIds()
        return len(playerIds)
    except:
        return 0


class Color(object):

    def __init__(self, mc_value, dice_id):
        self.mc_value = mc_value
        self.dice_id = dice_id
        self.used = 0

black = Color(15, 0)
grey = Color(7, 1)  # use "grey" for black on the board: it's seen much easier on the black game board
blue = Color(11, 2)
yellow = Color(4, 3)
red = Color(14, 4)
white = Color(0, 5)
green = Color(13, 6)
all_colors = [black, grey, blue, yellow, red, white, green]  # The position in the list correspond to the dice ID

diceColor = Color(0, 0)


def dice(): 
    mc.postToChat("Throwing the dice...")
    for color in [black.mc_value, green.mc_value, red.mc_value, yellow.mc_value, blue.mc_value, white.mc_value]:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, color)
        sleep(0.4)
    mc.postToChat("Alea iacta est! (The dice is thrown!)")
    color = all_colors[randint(1, 6)]
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, color.mc_value)
    return color.mc_value


def checkClicks(plr):
    blockEvents = mc.events.pollBlockHits()
    if (blockEvents):
        if (plr == 1):
            if blockEvents[0].pos.x == throwDiceX[0] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[0]:
                return 1
            elif blockEvents[0].pos.x == -236 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -12:
                return 0
            else:
                return -1
            mc.events.clearAll()
        elif (plr == 2):
            if blockEvents[0].pos.x == throwDiceX[1] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[1]:
                return 1
            elif blockEvents[0].pos.x == -240 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -18:
                return 0
            else:
                return -1
            mc.events.clearAll()
        elif (plr == 3):
            if blockEvents[0].pos.x == throwDiceX[2] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[2]:
                return 1
            elif blockEvents[0].pos.x == -248 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -18:
                return 0
            else:
                return -1
            mc.events.clearAll()
        elif (plr == 4):
            if blockEvents[0].pos.x == throwDiceX[3] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[3]:
                return 1
            elif blockEvents[0].pos.x == -252 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -12:
                return 0
            else:
                return -1
            mc.events.clearAll()
        elif (plr == 5):
            if blockEvents[0].pos.x == throwDiceX[4] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[4]:
                return 1
            elif blockEvents[0].pos.x == -248 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -6:
                return 0
            else:
                return -1
            mc.events.clearAll()
        elif (plr == 6):
            if blockEvents[0].pos.x == throwDiceX[5] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[5]:
                return 1
            elif blockEvents[0].pos.x == -240 and blockEvents[0].pos.y == 72 and blockEvents[0].pos.z == -6:
                return 0
            else:
                return -1
            mc.events.clearAll()


def prepare_blocks(blocks):
    for i in range(0, 10):
        doneRandoming = False
        while not doneRandoming:
            color = all_colors[randint(1, 6)]
            if color.used >= 10:
                continue
            doneRandoming = True
        color.used += 1
        blocks[i] = color.mc_value

for blocks in all_blocks:
    prepare_blocks(blocks)

mc.setBlock(blocks1X[0], blocksY, blocks1Z[0], 35, blocks1[0])
mc.setBlock(blocks2X[0], blocksY, blocks2Z[0], 35, blocks2[0])
mc.setBlock(blocks3X[0], blocksY, blocks3Z[0], 35, blocks3[0])
mc.setBlock(blocks4X[0], blocksY, blocks4Z[0], 35, blocks4[0])
mc.setBlock(blocks5X[0], blocksY, blocks5Z[0], 35, blocks5[0])
mc.setBlock(blocks6X[0], blocksY, blocks6Z[0], 35, blocks6[0])

for i in range(1, 10):
    mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 0)
    mc.setBlock(blocks2X[i], blocksY, blocks2Z[i], 0)
    mc.setBlock(blocks3X[i], blocksY, blocks3Z[i], 0)
    mc.setBlock(blocks4X[i], blocksY, blocks4Z[i], 0)
    mc.setBlock(blocks5X[i], blocksY, blocks5Z[i], 0)
    mc.setBlock(blocks6X[i], blocksY, blocks6Z[i], 0)

players = getPlayerNum()
while (players < playersNeededToPlay):
    print("Waiting for players")
    mc.postToChat("Waiting for players to connect")
    print("Players online: ", players)
    mc.postToChat("Current players amount:")
    mc.postToChat(players)
    sleep(5)
    players = getPlayerNum()
    try:
        playerIDs = mc.getPlayerEntityIds()
        for i in range(0, players):
            mc.entity.setPos(playerIDs[i], -244, 80, -13)
    except:
        print("No players!")

playerIDs = mc.getPlayerEntityIds()
print(playerIDs)
for i in range(0, playersNeededToPlay):
    print(playerIDs[i], playerXPoses[i], playerYPoses, playerZPoses[i])
    print(mc.entity.getPos(playerIDs[i]))
    mc.entity.setTilePos(playerIDs[i], playerXPoses[i], playerYPoses, playerZPoses[i])
    print(mc.entity.getPos(playerIDs[i]))

def calcBlocksToSee(a):
    if a == 0:
        return 1
    elif a == 1:
        return 3
    elif a == 2:
        return 6
    elif a == 3:
        return 10
    else:
        return 10
    
    
#------------------------------------Loop---------------------------------------

mc.postToChat("Enough players to play the game!")
print("Enough players!")

mc.setBlock(welcomeText.x, welcomeText.y, welcomeText.z, redstone_block)  # <-- Welcomes players
mc.setBlock(welcomeText.x, welcomeText.y, welcomeText.z, 0)    # <-- This line is needed too!

sleep(3)

for x in range(0, players): # Tell who is who
    if x == 0:
        if player.plr1.role == 1:
            mc.setBlock(player.plr1.roleInfo.BH.x, player.plr1.roleInfo.BH.y, player.plr1.roleInfo.BH.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.BH.x, player.plr1.roleInfo.BH.y, player.plr1.roleInfo.BH.z, 0)
        elif player.plr1.role == 2:
            mc.setBlock(player.plr1.roleInfo.GH.x, player.plr1.roleInfo.GH.y, player.plr1.roleInfo.GH.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.GH.x, player.plr1.roleInfo.GH.y, player.plr1.roleInfo.GH.z, 0)
        elif player.plr1.role == 3:
            mc.setBlock(player.plr1.roleInfo.AV.x, player.plr1.roleInfo.AV.y, player.plr1.roleInfo.AV.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.AV.x, player.plr1.roleInfo.AV.y, player.plr1.roleInfo.AV.z, 0)
        elif player.plr1.role == 4:
            mc.setBlock(player.plr1.roleInfo.Tr.x, player.plr1.roleInfo.Tr.y, player.plr1.roleInfo.Tr.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.Tr.x, player.plr1.roleInfo.Tr.y, player.plr1.roleInfo.Tr.z, 0)
        elif player.plr1.role == 5:
            mc.setBlock(player.plr1.roleInfo.Ac.x, player.plr1.roleInfo.Ac.y, player.plr1.roleInfo.Ac.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.Ac.x, player.plr1.roleInfo.Ac.y, player.plr1.roleInfo.Ac.z, 0)
        elif player.plr1.role == 6:
            mc.setBlock(player.plr1.roleInfo.NGO.x, player.plr1.roleInfo.NGO.y, player.plr1.roleInfo.NGO.z, redstone_block)
            mc.setBlock(player.plr1.roleInfo.NGO.x, player.plr1.roleInfo.NGO.y, player.plr1.roleInfo.NGO.z, 0)
            
    elif x == 1:
        if player.plr2.role == 1:
            mc.setBlock(player.plr2.roleInfo.BH.x, player.plr2.roleInfo.BH.y, player.plr2.roleInfo.BH.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.BH.x, player.plr2.roleInfo.BH.y, player.plr2.roleInfo.BH.z, 0)
        elif player.plr2.role == 2:
            mc.setBlock(player.plr2.roleInfo.GH.x, player.plr2.roleInfo.GH.y, player.plr2.roleInfo.GH.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.GH.x, player.plr2.roleInfo.GH.y, player.plr2.roleInfo.GH.z, 0)
        elif player.plr2.role == 3:
            mc.setBlock(player.plr2.roleInfo.AV.x, player.plr2.roleInfo.AV.y, player.plr2.roleInfo.AV.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.AV.x, player.plr2.roleInfo.AV.y, player.plr2.roleInfo.AV.z, 0)
        elif player.plr2.role == 4:
            mc.setBlock(player.plr2.roleInfo.Tr.x, player.plr2.roleInfo.Tr.y, player.plr2.roleInfo.Tr.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.Tr.x, player.plr2.roleInfo.Tr.y, player.plr2.roleInfo.Tr.z, 0)
        elif player.plr2.role == 5:
            mc.setBlock(player.plr2.roleInfo.Ac.x, player.plr2.roleInfo.Ac.y, player.plr2.roleInfo.Ac.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.Ac.x, player.plr2.roleInfo.Ac.y, player.plr2.roleInfo.Ac.z, 0)
        elif player.plr2.role == 6:
            mc.setBlock(player.plr2.roleInfo.NGO.x, player.plr2.roleInfo.NGO.y, player.plr2.roleInfo.NGO.z, redstone_block)
            mc.setBlock(player.plr2.roleInfo.NGO.x, player.plr2.roleInfo.NGO.y, player.plr2.roleInfo.NGO.z, 0)

    elif x == 2:
        if player.plr3.role == 1:
            mc.setBlock(player.plr3.roleInfo.BH.x, player.plr3.roleInfo.BH.y, player.plr3.roleInfo.BH.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.BH.x, player.plr3.roleInfo.BH.y, player.plr3.roleInfo.BH.z, 0)
        elif player.plr3.role == 2:
            mc.setBlock(player.plr3.roleInfo.GH.x, player.plr3.roleInfo.GH.y, player.plr3.roleInfo.GH.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.GH.x, player.plr3.roleInfo.GH.y, player.plr3.roleInfo.GH.z, 0)
        elif player.plr3.role == 3:
            mc.setBlock(player.plr3.roleInfo.AV.x, player.plr3.roleInfo.AV.y, player.plr3.roleInfo.AV.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.AV.x, player.plr3.roleInfo.AV.y, player.plr3.roleInfo.AV.z, 0)
        elif player.plr3.role == 4:
            mc.setBlock(player.plr3.roleInfo.Tr.x, player.plr3.roleInfo.Tr.y, player.plr3.roleInfo.Tr.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.Tr.x, player.plr3.roleInfo.Tr.y, player.plr3.roleInfo.Tr.z, 0)
        elif player.plr3.role == 5:
            mc.setBlock(player.plr3.roleInfo.Ac.x, player.plr3.roleInfo.Ac.y, player.plr3.roleInfo.Ac.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.Ac.x, player.plr3.roleInfo.Ac.y, player.plr3.roleInfo.Ac.z, 0)
        elif player.plr3.role == 6:
            mc.setBlock(player.plr3.roleInfo.NGO.x, player.plr3.roleInfo.NGO.y, player.plr3.roleInfo.NGO.z, redstone_block)
            mc.setBlock(player.plr3.roleInfo.NGO.x, player.plr3.roleInfo.NGO.y, player.plr3.roleInfo.NGO.z, 0)

    elif x == 4:
        if player.plr4.role == 1:
            mc.setBlock(player.plr4.roleInfo.BH.x, player.plr4.roleInfo.BH.y, player.plr4.roleInfo.BH.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.BH.x, player.plr4.roleInfo.BH.y, player.plr4.roleInfo.BH.z, 0)
        elif player.plr4.role == 2:
            mc.setBlock(player.plr4.roleInfo.GH.x, player.plr4.roleInfo.GH.y, player.plr4.roleInfo.GH.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.GH.x, player.plr4.roleInfo.GH.y, player.plr4.roleInfo.GH.z, 0)
        elif player.plr4.role == 3:
            mc.setBlock(player.plr4.roleInfo.AV.x, player.plr4.roleInfo.AV.y, player.plr4.roleInfo.AV.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.AV.x, player.plr4.roleInfo.AV.y, player.plr4.roleInfo.AV.z, 0)
        elif player.plr4.role == 4:
            mc.setBlock(player.plr4.roleInfo.Tr.x, player.plr4.roleInfo.Tr.y, player.plr4.roleInfo.Tr.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.Tr.x, player.plr4.roleInfo.Tr.y, player.plr4.roleInfo.Tr.z, 0)
        elif player.plr4.role == 5:
            mc.setBlock(player.plr4.roleInfo.Ac.x, player.plr4.roleInfo.Ac.y, player.plr4.roleInfo.Ac.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.Ac.x, player.plr4.roleInfo.Ac.y, player.plr4.roleInfo.Ac.z, 0)
        elif player.plr4.role == 6:
            mc.setBlock(player.plr4.roleInfo.NGO.x, player.plr4.roleInfo.NGO.y, player.plr4.roleInfo.NGO.z, redstone_block)
            mc.setBlock(player.plr4.roleInfo.NGO.x, player.plr4.roleInfo.NGO.y, player.plr4.roleInfo.NGO.z, 0)

print("Entering the game loop...")
gRound = 1
oldGTurn = 0
gTurn = 1
turnDone = False
someoneWon = False
while not someoneWon:
    textToChat = "Round:", gRound
    mc.postToChat(textToChat)
    print(textToChat)
    for gTurn in range(1, 7):
        turnDone = False
        while not turnDone:
            if gTurn != oldGTurn:
                 textToChat = "Turn:", gTurn
                 mc.postToChat(textToChat)
                 print(textToChat)
                 oldGTurn = gTurn
            checkBlocks(gTurn)
            plrWantsToDo = checkClicks(gTurn)

            if gTurn > playersNeededToPlay: # For skipping the not-playing players (or their turn, because they're not present)
                plrWantsToDo = 0
                mc.postToChat("Skipping turn...")
                    
            if plrWantsToDo == 1:
                diceColor.mc_value = dice()
                if gTurn == 1:
                    print(blocks1[:blocksToSee[gTurn]])
                    if diceColor.mc_value in blocks1[:blocksToSee[gTurn]]:
                        mc.setBlock(-235, 71 + visibleLayers[gTurn], -12, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                elif gTurn == 2:
                    if diceColor.mc_value in blocks2[:blocksToSee[gTurn]]:
                        mc.setBlock(-239, 71 + visibleLayers[gTurn], -19, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                elif gTurn == 3:
                    if diceColor.mc_value in blocks3[:blocksToSee[gTurn]]:
                        mc.setBlock(-249, 71 + visibleLayers[gTurn], -19, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                elif gTurn == 4:
                    if diceColor.mc_value in blocks4[:blocksToSee[gTurn]]:
                        mc.setBlock(-253, 71 + visibleLayers[gTurn], -12, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                elif gTurn == 5:
                    if diceColor.mc_value in blocks5[:blocksToSee[gTurn]]:
                        mc.setBlock(-249, 71 + visibleLayers[gTurn], -5, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                elif gTurn == 6:
                    if diceColor.mc_value in blocks6[:blocksToSee[gTurn]]:
                        mc.setBlock(-239, 71 + visibleLayers[gTurn], -5, 35, diceColor.mc_value)
                        print("New block for player", gTurn)
                        mc.player.setPos(playerIDs[-1], -235, 72 + visibleLayers[gTurn], -12)
                        visibleLayers[gTurn] += 1
                        blocksToSee[gTurn - 1] = calcBlocksToSee(visibleLayers[gTurn])
                turnDone = True

            elif plrWantsToDo == 0:
                turnDone = True
            sleep(0.2)
        if visibleLayers[0] >= blocksToWin or visibleLayers[1] >= blocksToWin or visibleLayers[2] >= blocksToWin or visibleLayers[3] >= blocksToWin or visibleLayers[4] >= blocksToWin or visibleLayers[5] >= blocksToWin:
            someoneWon = True
        gRound = gRound + 1

#---------------------------------Game Over------------------------------------

print("Game Over")
mc.setBlock(gameOverText.x, gameOverText.y, gameOverText.z, redstone_block)  # <-- When game is over
mc.setBlock(gameOverText.x, gameOverText.y, gameOverText.z, 0)    # <-- This line too!
