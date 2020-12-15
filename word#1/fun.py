from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi.minecraft import CmdPlayer
import time
import random

#Create a new thread
mc = Minecraft.create()

spawn = [-98.5, 68, 144.5]
maze = [-123.5, 63, 149.5]

def free_pos():
    result = dict()
    pos = mc.player.getPos()
    #nord
    block = pos.clone()
    block.z -= 1
    if mc.getBlock(block) == 0:
        result["nord"] = True
    else:
        result["nord"] = False
    #sud
    block = pos.clone()
    block.z += 1
    if mc.getBlock(block) == 0:
        result["sud"] = True
    else:
        result["sud"] = False
    #est
    block = pos.clone()
    block.x -= 1
    if mc.getBlock(block) == 0:
        result["est"] = True
    else:
        result["est"] = False
    #ovest
    block = pos.clone()
    block.x += 1
    if mc.getBlock(block) == 0:
        result["ovest"] = True
    else:
        result["ovest"] = False
    return [y for y in result.keys() if result[y] == True]

def move(direction):
    player_pos = mc.player.getPos()
    if direction == "nord":
        player_pos.z -= 1
        return player_pos
    if direction == "sud":
        player_pos.z += 1
        return player_pos
    if direction == "est":
        player_pos.x -= 1
        return player_pos
    if direction == "ovest":
        player_pos.x += 1
        return player_pos

def solve_maze(n_step):
    history = [mc.player.getPos()]
    for a in range(n_step):
        where = move(random.choice(free_pos()))
        while where in history:
            where = move(random.choice(free_pos()))
        history.append(where)
        mc.player.setPos(where)
        
solve_maze(100)


