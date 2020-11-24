import re
from typing import List, Dict, Set, Any
import pygame

import propiedades as prop
from entidades.coordenadas import Coord

PAWNS = None

MEMOIZED_WALLS: Dict[str, Any] = {}
MEMOIZED_NODES = None
MEMOIZED_NODES_HITS = None
BOARD = None


class CellArray:
    #Crea arreglo con los mismos valores y tamaño que el tablero
    def __init__(self, board, value: any):
        self.board = board
        self.rows = board.rows
        self.cols = board.cols
        self.array: List[List[Any]] = [[value for _ in range(self.cols)] for _ in range(self.rows)]

    def __getitem__(self, i: int) -> List[any]:
        return self.array[i]

    def get_cell(self, coord: Coord):
        return self.array[coord.row][coord.col]

    def set_cell(self, coord: Coord, value) -> None:
        self.array[coord.row][coord.col] = value


class DistArray(CellArray):
    #Arreglo que calcular las distancias mínimas para cada celda
    def __init__(self, pawn):
        self.pawn = pawn
        super().__init__(pawn.board, prop.INF)

        self.queue: Set[Coord] = set()
        self.MEMOIZE_DISTANCES = {}
        self.MEMO_HITS = 0
        self.MEMO_COUNT = 0
        self.stack = []
        self.update()

    def clean_memo(self):
        l_ = 1 + len(self.board.pawns) * 4
        k = self.board.state[l_:]
        k = '.' * l_ + k.replace('1', '.') + '$'
        r = re.compile(k)

        for q in list(self.MEMOIZE_DISTANCES.keys()):
            if not r.match(q):
                del self.MEMOIZE_DISTANCES[q]

    def update(self):
        #Calcula la distancia
        k = self.board.state
        try:
            self.array = self.MEMOIZE_DISTANCES[k]
            self.MEMO_HITS += 1
            return
        except KeyError:
            self.MEMO_COUNT += 1

        for i in range(self.rows):
            for j in range(self.cols):
                self.array[i][j] = prop.INF

        #Gana
        for goal in self.pawn.goals:
            self.set_cell(goal, 0)
            self.queue.add(goal)

        self.update_distances()
        self.MEMOIZE_DISTANCES[k] = self.array

    def update_cell(self, coord: Coord):
        #Si está bloqueada
        if coord in self.pawn.goals:
            return

        values = [self.get_cell(pos) for pos in self.pawn.valid_moves_from(coord)]
        newval = 1 + min(values)

        if newval < self.get_cell(coord):
            self.set_cell(coord, newval)
            self.queue.add(coord)

    def update_distances(self):
        cell = self.pawn.cell
        self.pawn.cell = None

        while self.queue:
            coord = self.queue.pop()
            for pos in self.pawn.valid_moves_from(coord):
                self.update_cell(pos)

        self.pawn.cell = cell

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                r = self.board[i][j].rect
                r.x = r.x + r.width - prop.FONT_SIZE
                r.y = r.y + r.height - prop.FONT_SIZE
                r.width = prop.FONT_SIZE
                r.height = prop.FONT_SIZE
                pygame.draw.rect(self.pawn.screen, prop.FONT_BG_COLOR, r, 0)
                self.board.msg(r.x, r.y, str(self.array[i][j]))

    def push_state(self):
        self.stack.append(self.array)
        super().__init__(self.pawn.board, prop.INF)

    def pop_state(self):
        self.array = self.stack.pop()

    @property
    def shortest_path_len(self):
        return min([self.get_cell(pos) for pos in self.pawn.valid_moves])


def init():
    global PAWNS
    global MEMOIZED_WALLS
    global MEMOIZED_NODES
    global MEMOIZED_NODES_HITS
    global BOARD

    PAWNS = 0
    MEMOIZED_WALLS = {}
    MEMOIZED_NODES = 0
    MEMOIZED_NODES_HITS = 0
    BOARD = None
