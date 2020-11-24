import os
from pygame import Color

from entidades.coordenadas import Coord


__DEBUG__ = False

FRAMERATE = 25

GAME_TITLE = 'Quoridor - Complejidad Algorítmica'

DEFAULT_NUM_PLAYERS = 4

CELL_WIDTH = 41
CELL_HEIGHT = 41
CELL_PAD = 7
CELL_BORDER_SIZE = 2

DEF_ROWS = 11
DEF_COLS = 11

NUM_WALLS = 5

FONT_COLOR = Color(0, 10, 50)
FONT_BG_COLOR = Color(255, 255, 255)
FONT_SIZE = 20

BOARD_BG_COLOR = Color(240, 255, 255)
BOARD_BRD_COLOR = Color(0, 0, 40)
BOARD_BRD_SIZE = 1

CELL_BORDER_COLOR = Color(40, 40, 40)
CELL_COLOR = Color(240, 247, 234)
CELL_VALID_COLOR = Color(120, 223, 109)

WALL_COLOR = Color(120, 90, 60)

PAWN_A_COL = Color(158, 60, 60)
PAWN_B_COL = Color(60, 60, 158)
PAWN_C_COL = Color(209, 1, 206)
PAWN_D_COL = Color(39, 209, 1)
PAWN_BORDER_COL = Color(0, 0, 0)

GAUGE_WIDTH = CELL_WIDTH
GAUGE_HEIGHT = 5
GAUGE_COLOR = Color(128, 40, 40)
GAUGE_BORDER_COLOR = Color(0, 0, 0)

PAWN_PADDING = 25


class DIR:
    N = 0
    S = 1
    E = 2
    W = 3


DIRS = {DIR.N, DIR.S, DIR.E, DIR.W}
OPPOSITE_DIRS = [DIR.S, DIR.N, DIR.W, DIR.E]
DIRS_DELTA = [Coord(-1, 0), Coord(+1, 0), Coord(0, -1), Coord(0, +1)] #opuesto

LEVEL = 0

INF = 99

CACHE_ENABLED = False
CACHE_DIR = './__cache'
CACHE_AI_FNAME = os.path.join(CACHE_DIR, 'bot.memo')
CACHE_DIST_FNAME = os.path.join(CACHE_DIR, 'dist.memo')
