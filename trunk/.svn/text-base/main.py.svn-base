import sys
import random
import atexit
import threading

import curses

import card
import cardlist
from player import Player, PlayerThread, turnState
from enum import Enumerate

def int_input(prompt):
    """Get an int value from stdin."""
    try:
        return int(raw_input(prompt))
    except ValueError:
        pass

def draw_console(screen):
    for i, v in enumerate(supply):
        screen.move(i, 1)
        out = '+' if v[1] > 9 else str(v[1])
        out += ' $' + str(v[0].cost) + ' '
        out += v[0].name.ljust(13)
        out += v[0].desc
        hl = iMode is iModes.SUPPLY and hlIndex == i
        screen.addstr(out, get_color_pair(v[0], hl))

    screen.move(18, 1)
    screen.addstr("Status message goes here!")

    row = 20
    for i, v in enumerate(active.hand):
        if i % 5 == 0:
            screen.move(row, 1)
            row += 1
        hl = iMode is iModes.HAND and hlIndex == i
        screen.addstr(v.name.ljust(15), get_color_pair(v, hl))

    screen.refresh()

def get_color_pair(card_, hl=False):
    """Cache of all the color pairs used by curses with string names."""
    cType = card_.ctyp.keys()
    if card.cTypes.Attack in cType:
        return cColors['BLACK_ON_RED'] if hl else cColors['RED_ON_BLACK']
    if card.cTypes.Victory in cType:
        return cColors['BLACK_ON_GREEN'] if hl else cColors['GREEN_ON_BLACK']
    if card.cTypes.Treasure in cType:
        return cColors['BLACK_ON_YELLOW'] if hl else cColors['YELLOW_ON_BLACK']
    if card.cTypes.Reaction in cType:
        return cColors['BLACK_ON_BLUE'] if hl else cColors['BLUE_ON_BLACK']
    return cColors['BLACK_ON_WHITE'] if hl else cColors['WHITE_ON_BLACK']

# Determine number of players
numPlayers = 0
while not 0 < numPlayers < 7:
    numPlayers = int_input("How many players? [1-6] ")

# Select a random seed
seed = int_input("Select random seed: (0 for auto) ")
random.seed() if seed == 0 or seed is None else random.seed(seed)

# Set up supply
vAmount = numPlayers * 4 if numPlayers < 4 else numPlayers * 3
sAmount = 1 if numPlayers < 5 else 2

supply = list()
supply.append((card.Curse, (numPlayers - 1) * 10))
supply.append((card.Copper, 60 - 7 * numPlayers))
supply.append((card.Silver, 40 * sAmount))
supply.append((card.Gold, 30 * sAmount))
supply.append((card.Estate, 24 * sAmount - 3 * numPlayers))
supply.append((card.Duchy, vAmount))
supply.append((card.Province, vAmount))
kingdom = list()
for item in random.sample(cardlist.base, 10):
    kingdom.append((item, vAmount if card.cTypes.Victory in item.ctyp else 10))
kingdom.sort(key = lambda x: x[0].cost)
supply.extend(kingdom)

# Reset random seed for shuffling later
random.seed()

# Set up curses display
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
curses.curs_set(0)
curses.start_color()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_BLUE)

cColors = {'WHITE_ON_BLACK': curses.color_pair(0), 
        'RED_ON_BLACK': curses.color_pair(1),
        'GREEN_ON_BLACK': curses.color_pair(2),
        'YELLOW_ON_BLACK': curses.color_pair(3),
        'BLUE_ON_BLACK': curses.color_pair(4),
        'BLACK_ON_WHITE': curses.color_pair(5),
        'BLACK_ON_RED': curses.color_pair(6),
        'BLACK_ON_GREEN': curses.color_pair(7),
        'BLACK_ON_YELLOW': curses.color_pair(8),
        'BLACK_ON_BLUE': curses.color_pair(9)}

# init input modes
iModes = Enumerate('NONE SUPPLY HAND YES_NO')
iMode = iModes.HAND
hlIndex = 0

# init players
players = list()
threads = list()
for i in range(numPlayers):
    players.append(Player(supply))
active = players[0]
for i in players:
    i.setPlayers(players)
    t = PlayerThread(i)
    t.start()
    threads.append(t)
    
# Main loop
while True:
    draw_console(stdscr)
    event = stdscr.getch()
    if event == ord('q'):
        break
    elif event == ord(' '):
        submited = None
    elif iMode == iModes.HAND:
        if event == curses.KEY_LEFT and hlIndex > 0:
            hlIndex -= 1
        elif event == curses.KEY_RIGHT and hlIndex < len(active.hand) - 1:
            hlIndex += 1
        elif event == curses.KEY_UP and hlIndex > 4:
            hlIndex -= 5
        elif event == curses.KEY_DOWN and hlIndex < len(active.hand) - 5:
            hlIndex += 5
        elif event == curses.KEY_ENTER or event == 10:
            active.selected = supply[hlIndex]
    elif iMode == iModes.SUPPLY:
        if event == curses.KEY_UP and hlIndex > 0:
            hlIndex -= 1
        if event == curses.KEY_UP and hlIndex < len(supply) - 1:
            hlIndex += 1
        elif event == curses.KEY_ENTER or event == 10:
            active.selected = supply[hlIndex]
    elif iMode == iModes.YES_NO:
        pass

# Clean up player threads
for t in threads:
    t.state = turnState.Exit
    t.isRunning.set()
    t.join()

# Tear down curses display
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
