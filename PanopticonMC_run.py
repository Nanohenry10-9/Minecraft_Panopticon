from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from time import sleep
from random import randint

mc.setting("world_immutable", False)

class player:
    class plr1:
        role = 1
    class plr2:
        role = 2
    class plr3:
        role = 3
    class plr4:
        role = 4
    class plr5:
        role = 5
    class plr6:
        role = 6

mc.events.clearAll()

redsUsed = 0
greensUsed = 0
yellowsUsed = 0
bluesUsed = 0
blacksUsed = 0
whitesUsed = 0

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
throwDiceX = [-236]
throwDiceZ = [-11]

blocks1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
blocks6 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
def checkBlocks1():
    blocks1OnPlace1 = mc.getBlock(-235, 72, -12)
    blocks1OnPlace2 = mc.getBlock(-235, 73, -12)
    blocks1OnPlace3 = mc.getBlock(-235, 74, -12)
    if blocks1OnPlace1 == 0:
        visibleLayers1 = 1
        mc.setBlock(blocks1X[0], blocksY, blocks1Z[0], 35, blocks1[0])
    elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 0:
        visibleLayers1 = 2
        i = 0
        while (i < 3):
            mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
            i = i + 1
    elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 0:
        visibleLayers1 = 3
        i = 0
        while (i < 6):
            mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
            i = i + 1
    elif blocks1OnPlace1 == 35 and blocks1OnPlace2 == 35 and blocks1OnPlace3 == 35:
        visibleLayers1 = 4
        i = 0
        while (i < 10):
            mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 35, blocks1[i])
            i = i + 1

def getPlayerNum():
    playerIds = mc.getPlayerEntityIds()
    P1 = playerIds[0]
    if P1 == 0:
        return 0
    else:
        P2 = playerIds[1]
        if P2 == 0:
            return 1
        else:
            P3 = playerIds[2]
            if P3 == 0:
                return 2
            else:
                P4 = playerIds[3]
                if P4 == 0:
                    return 3
                else:
                    P5 = playerIds[4]
                    if P5 == 0:
                        return 4
                    else:
                        P6 = playerIds[5]
                        if P6 == 0:
                            return 5
                        else:
                            return 6

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
    mc.postToChat("Alea iacta est!")
    if dColor == 1:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, white)
    elif dColor == 2:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, red)
    elif dColor == 3:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, green)
    elif dColor == 4:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, black)
    elif dColor == 5:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, blue)
    else:
        mc.setBlocks(-244, 77, -12, -245, 78, -13, 35, yellow)
    sleep(0.4)
    

players = 1#getPlayerNum() #That doesn't work

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks1[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks1[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks1[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks1[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks1[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks1[i] = green
    i = i + 1

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks2[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks2[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks2[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks2[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks2[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks2[i] = green
    i = i + 1

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks3[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks3[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks3[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks3[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks3[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks3[i] = green
    i = i + 1

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks4[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks4[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks4[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks4[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks4[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks4[i] = green
    i = i + 1

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks5[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks5[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks5[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks5[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks5[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks5[i] = green
    i = i + 1

i = 0
while (i < 10):
    doneRandoming = False
    while doneRandoming == False:
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
        blacksUsed = (blacksUsed + 1)
        blocks6[i] = grey #"grey" is black, but why it's gray is that it's seen much easier on the black game board
    elif blockColor == 2:
        bluesUsed = (bluesUsed + 1)
        blocks6[i] = blue
    elif blockColor == 3:
        yellowsUsed = (yellowsUsed + 1)
        blocks6[i] = yellow
    elif blockColor == 4:
        redsUsed = (redsUsed + 1)
        blocks6[i] = red
    elif blockColor == 5:
        whitesUsed = (whitesUsed + 1)
        blocks6[i] = white
    elif blockColor == 6:
        greensUsed = (greensUsed + 1)
        blocks6[i] = green
    i = i + 1

mc.setBlock(blocks1X[0], blocksY, blocks1Z[0], 35, blocks1[0])
mc.setBlock(blocks2X[0], blocksY, blocks2Z[0], 35, blocks2[0])
mc.setBlock(blocks3X[0], blocksY, blocks3Z[0], 35, blocks3[0])
mc.setBlock(blocks4X[0], blocksY, blocks4Z[0], 35, blocks4[0])
mc.setBlock(blocks5X[0], blocksY, blocks5Z[0], 35, blocks5[0])
mc.setBlock(blocks6X[0], blocksY, blocks6Z[0], 35, blocks6[0])

i = 1
while (i < 10):
    mc.setBlock(blocks1X[i], blocksY, blocks1Z[i], 0)
    i = i + 1
i = 1
while (i < 10):
    mc.setBlock(blocks2X[i], blocksY, blocks2Z[i], 0)
    i = i + 1
i = 1
while (i < 10):
    mc.setBlock(blocks3X[i], blocksY, blocks3Z[i], 0)
    i = i + 1
i = 1
while (i < 10):
    mc.setBlock(blocks4X[i], blocksY, blocks4Z[i], 0)
    i = i + 1
i = 1
while (i < 10):
    mc.setBlock(blocks5X[i], blocksY, blocks5Z[i], 0)
    i = i + 1
i = 1
while (i < 10):
    mc.setBlock(blocks6X[i], blocksY, blocks6Z[i], 0)
    i = i + 1
    
while (players < 6):
    print("Waiting for players")
    mc.postToChat("Waiting for players to connect")
    mc.postToChat("Current players amount:")
    mc.postToChat(players)
    sleep(5)
    players = 6#getPlayerNum()
    print("Players online: ", players)
    mc.postToChat("Waiting for players to connect")
    mc.postToChat("Current players amount:")
    mc.postToChat(players)

mc.postToChat("Enough players to play the game!")
print("Enough (6) players")
    
gTurn = 1
gRound = 1

while (gRound < 3):
    print("Round: ", gRound)
    gTurn = 1


    
    while (gTurn < 7):
        print("Turn: ", gTurn)
        tochat = ("It's your turn, player", gTurn)
        mc.postToChat(tochat)
        gTurn = gTurn + 1

        
        
    gRound = gRound + 1

print("Loop!")
while (True):
    checkBlocks1()
    blockEvents = mc.events.pollBlockHits()
    if (blockEvents):
        for blockEvent in blockEvents:
            mc.postToChat("Something was hit!")
            if blockEvents[0].pos.x == throwDiceX[0] and blockEvents[0].pos.y == throwDiceY and blockEvents[0].pos.z == throwDiceZ[0]:
                dice()
        mc.events.clearAll()
    sleep(0.2)
    
    
