from mcpi.minecraft import Minecraft
from time import sleep
from random import randint

mc = Minecraft.create()
mc.setting("world_immutable", True)


class player:
    class plr1:
        role = 1
        numOfBlocks = 0

        class roleInfo:
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

mc.events.clearAll()

redsUsed = 0
greensUsed = 0
yellowsUsed = 0
bluesUsed = 0
blacksUsed = 0
whitesUsed = 0


class gameOverText:
    x = -228
    y = 68
    z = 33


class welcomeText:
    x = -228
    y = 68
    z = 29

blue = 11
green = 13
red = 14
white = 0
black = 15
yellow = 4
grey = 7

blocksY = 71

blocks1X = [-230, -224, -224, -219, -217, -219, -214, -212, -212, -214]
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

throwDiceY = 73
throwDiceX = [-236, -240, -248, -252, -248, -240]
throwDiceZ = [-12, -18, -18, -12, -6, -5]

blocks1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

all_blocks = [blocks1, blocks2, blocks3, blocks4, blocks5, blocks6]

visibleLayers = [1, 1, 1, 1, 1, 1]


def checkBlocks(player):
    if player == 1:
        blocks1OnPlace1 = mc.getBlock(-235, 72, -12)
        blocks1OnPlace2 = mc.getBlock(-235, 73, -12)
        blocks1OnPlace3 = mc.getBlock(-235, 74, -12)
        if blocks1OnPlace1 == 0:
            mc.setBlock(blocks1X[0], blocksY, blocks1Z[0], 35, blocks1[0])
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 0:
            i = 0
            while (i < 3):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
                i = i + 1
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 0:
            i = 0
            while (i < 6):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
                i = i + 1
        elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 35:
            i = 0
            while (i < 10):
                mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
                i = i + 1
    elif player == 2:
        print("Not possible yet")
    elif player == 3:
        print("Not possible yet")
    elif player == 4:
        print("Not possible yet")
    elif player == 5:
        print("Not possible yet")
    elif player == 6:
        print("Not possible yet")


def getPlayerNum():
    try:
        playerIds = mc.getPlayerEntityIds()
        return len(playerIds)
    except:
        return 0


def dice():
    mc.postToChat("Throwing the dice...")
    dColor = randint(1, 6)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, black)
    sleep(0.4)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, green)
    sleep(0.4)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, red)
    sleep(0.4)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, yellow)
    sleep(0.4)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, blue)
    sleep(0.4)
    mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, white)
    sleep(0.4)
    mc.postToChat("Alea iacta est! (The dice is thrown!)")
    if dColor == 1:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, white)
        return white
    elif dColor == 2:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, red)
        return red
    elif dColor == 3:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, green)
        return green
    elif dColor == 4:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, black)
        return black
    elif dColor == 5:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, blue)
        return blue
    else:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, yellow)
        return yellow


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

players = getPlayerNum()


def prepare_block(blocks):
    global blacksUsed
    global bluesUsed
    global yellowsUsed
    global redsUsed
    global whitesUsed
    global greensUsed
    i = 0
    while (i < 10):
        doneRandoming = False
        while not doneRandoming:
            blockColor = randint(1, 6)
            if blockColor == 1:
                if blacksUsed <= 10:
                    doneRandoming = True
            if blockColor == 2:
                if bluesUsed <= 10:
                    doneRandoming = True
            if blockColor == 3:
                if yellowsUsed <= 10:
                    doneRandoming = True
            if blockColor == 4:
                if redsUsed <= 10:
                    doneRandoming = True
            if blockColor == 5:
                if whitesUsed <= 10:
                    doneRandoming = True
            if blockColor == 6:
                if greensUsed <= 10:
                    doneRandoming = True
        if blockColor == 1:
            blacksUsed += 1
            blocks[i] = grey  # "grey" is black, but why it's gray is that it's seen much easier on the black game board
        elif blockColor == 2:
            bluesUsed += 1
            blocks[i] = blue
        elif blockColor == 3:
            yellowsUsed += 1
            blocks[i] = yellow
        elif blockColor == 4:
            redsUsed += 1
            blocks[i] = red
        elif blockColor == 5:
            whitesUsed += 1
            blocks[i] = white
        elif blockColor == 6:
            greensUsed += 1
            blocks[i] = green
        i = i + 1

for blocks in all_blocks:
    prepare_block(blocks)

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

# "Game begin" -----------------------------------------------------------------------------------------------------

while (players < 6):
    print("Waiting for players")
    mc.postToChat("Waiting for players to connect")
    mc.postToChat("Current players amount:")
    mc.postToChat(players)
    sleep(5)
    players = getPlayerNum()
    print("Players online: ", players)
    mc.postToChat("Waiting for players to connect")
    mc.postToChat("Current players amount:")
    mc.postToChat(players)

mc.postToChat("Enough players to play the game!")
print("Enough (6) players")

mc.setBlock(welcomeText.x, welcomeText.y, welcomeText.z, 152)  # <-- Welcomes players
mc.setBlock(welcomeText.x, welcomeText.y, welcomeText.z, 0)    # <-- This line is needed too!

print("Entering the game loop...")
gRound = 1
gTurn = 1
turnDone = False
someoneWon = False
while not someoneWon:
    for gRound in range(1, 11):
        textToChat = "Round:", gRound
        mc.postToChat(textToChat)
        print(textToChat)
        for gTurn in range(1, 7):
            turnDone = False
            while not turnDone:
                textToChat = "Turn:", gTurn
                mc.postToChat(textToChat)
                print(textToChat)
                checkBlocks(gTurn)
                plrWantsToDo = checkClicks(gTurn)
                if plrWantsToDo == 1:
                    diceColor = dice()
                    if gTurn == 1:
                        if diceColor in blocks1:
                            mc.setBlock(-235, 71 + visibleLayers[gTurn], -12, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    elif gTurn == 2:
                        if diceColor in blocks2:
                            mc.setBlock(-239, 71 + visibleLayers[gTurn], -19, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    elif gTurn == 3:
                        if diceColor in blocks3:
                            mc.setBlock(-249, 71 + visibleLayers[gTurn], -19, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    elif gTurn == 4:
                        if diceColor in blocks4:
                            mc.setBlock(-253, 71 + visibleLayers[gTurn], -12, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    elif gTurn == 5:
                        if diceColor in blocks5:
                            mc.setBlock(-249, 71 + visibleLayers[gTurn], -5, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    elif gTurn == 6:
                        if diceColor in blocks6:
                            mc.setBlock(-239, 71 + visibleLayers[gTurn], -5, 35, diceColor)
                            print("New block for player", gTurn)
                            visibleLayers[gTurn] += 1
                    turnDone = True

                elif plrWantsToDo == 0:
                    turnDone = True
                sleep(0.2)
    someoneWon = True

print("Game Over")
mc.setBlock(gameOverText.x, gameOverText.y, gameOverText.z, 152)  # <-- When game is over
mc.setBlock(gameOverText.x, gameOverText.y, gameOverText.z, 0)    # <-- This line too!
