import time
import pygame
import socket
import xmlrpc
from typing import List, Set

import propiedades as prop
import juego
from support import log

from .dibujar import Drawable
from .casilla import Cell
from .coordenadas import Coord


class Pawn(Drawable):
    goals: Set[Coord] = None

    def __init__(self,
                 screen: pygame.Surface,
                 board,
                 color,
                 border_color=prop.PAWN_BORDER_COL,
                 coord=None,
                 walls=prop.NUM_WALLS,
                 width=prop.CELL_WIDTH - prop.CELL_PAD,
                 height=prop.CELL_HEIGHT - prop.CELL_PAD,
                 ):
        super().__init__(screen, color, border_color)
        self.width = width
        self.height = height
        self._coord = coord
        self.board = board
        self.walls = walls
        self.__cell = None
        self.set_goal()
        self.id = juego.PAWNS
        self.distances = juego.DistArray(self)
        self.AI = None
        self.is_network_player = False
        self.percent = None

        juego.PAWNS += 1

    @property
    def cell(self) -> Cell:
        if self.coord is None:
            return None

        return self.board.get_cell(self.coord)

    @cell.setter
    def cell(self, cell):
        if self.__cell is not None:
            self.__cell.pawn = None

        self.__cell = cell
        if cell is not None:
            self.__cell.pawn = self

    def set_goal(self):
        if self.coord.row == 0:
            self.goals = {Coord(self.board.rows - 1, x) for x in range(self.board.cols)}
        elif self.coord.row == self.board.rows - 1:
            self.goals = {Coord(0, x) for x in range(self.board.cols)}
        elif self.coord.col == self.board.cols - 1:
            self.goals = {Coord(x, 0) for x in range(self.board.cols)}
        else:
            self.goals = {Coord(x, self.board.cols - 1) for x in range(self.board.rows)}

    def draw(self, r=None):
        if self.coord is None:
            return

        if r is None:
            r = self.rect

        pygame.draw.ellipse(self.board.screen, self.color, r, 0)
        pygame.draw.ellipse(self.board.screen, self.border_color, r, 2)

    @property
    def rect(self):
        return self.board.get_cell(self.coord).rect

    def can_go(self, direction: int) -> List[Coord]:
        assert self.cell is not None, format(self.coord.row, self.coord.col)

        if self.cell.path[direction] is False:
            return []

        new_coord = self.coord + prop.DIRS_DELTA[direction]
        if not self.board.in_range(new_coord):
            return []

        if self.board.get_cell(new_coord).pawn is None:
            return [new_coord]

        result = []

        for dir in prop.DIRS:
            if dir == prop.OPPOSITE_DIRS[direction]:
                continue

            if self.board.get_cell(new_coord).path[dir]:
                new_coord2 = new_coord + prop.DIRS_DELTA[dir]
                if not self.board.in_range(new_coord2):
                    continue

                if self.board.get_cell(new_coord2).pawn is None:
                    result.append(new_coord2)

        return result

    @property
    def valid_moves(self) -> List[Coord]:
        result: List[Coord] = []

        if self.cell is None:
            return result

        for dir in prop.DIRS:
            result.extend(self.can_go(dir))

        return result

    def valid_moves_from(self, coord: Coord) -> List[Coord]:
        current_pos = self._coord
        self._coord = coord
        result = self.valid_moves
        self._coord = current_pos

        return result

    def can_move(self, coord: Coord) -> bool:
        return coord in self.valid_moves

    def move_to(self, coord: Coord) -> None:
        if self.board.in_range(coord):
            self._coord = coord
            self.cell = self.board.get_cell(self.coord)

    def can_reach_goal(self, board=None) -> bool:
        if self.coord in self.goals:
            return True

        if board is None:
            board = juego.CellArray(self.board, False)

        if board.get_cell(self.coord):
            return False

        board.set_cell(self.coord, True)
        for move in self.valid_moves:
            current_pos = self.coord
            self.move_to(move)
            result = self.can_reach_goal(board)
            self.move_to(current_pos)
            if result:
                return True

        return False

    @property
    def state(self):
        return '%i%i%02i' % (self._coord.row, self._coord.col, self.walls)

    @property
    def coord(self) -> Coord:
        return self._coord

    @coord.setter
    def coord(self, coord: Coord) -> None:
        self.move_to(coord)
