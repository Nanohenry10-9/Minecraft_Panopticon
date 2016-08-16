from mcpi.minecraft import Minecraft

mc = Minecraft.create()
X1 = -188
X2 = -300
Z1 = 46
Z2 = -69

boardHeight = 50

mc.setBlocks(X1, 70, Z1, X2, 70, Z2, 173)

betweenX = (X1 + X2) / 2
betweenZ = (Z1 + Z2) / 2

mc.setBlock(betweenX, 70, betweenZ, 42)
