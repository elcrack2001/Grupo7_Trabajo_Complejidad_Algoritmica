from typing import List
import pygame

import propiedades as prop
from .dibujar import Drawable
from .coordenadas import Coord


class Cell(Drawable):
    def __init__(self,
                 screen: pygame.Surface,
                 board,
                 coord: Coord,
                 x=None,
                 y=None,
                 width=prop.CELL_WIDTH,
                 height=prop.CELL_HEIGHT,
                 color=prop.CELL_COLOR,
                 wall_color=prop.WALL_COLOR,
                 focus_color=prop.CELL_VALID_COLOR,
                 border_color=prop.CELL_BORDER_COLOR,
                 border_size=prop.CELL_BORDER_SIZE,
                 pawn=None
                 ):

        super().__init__(screen, color, border_color, border_size)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wall_color = wall_color
        self.normal_color = color
        self.focus_color = focus_color
        self.pawn = pawn
        self.board = board
        self.walls = []
        self.coord = coord
        self.has_focus: bool = False
        self.path: List[bool] = [True] * len(prop.DIRS)

        if coord.row == 0:
            self.set_path(prop.DIR.N, False)
        elif coord.row == self.board.rows - 1:
            self.set_path(prop.DIR.S, False)

        if coord.col == 0:
            self.set_path(prop.DIR.E, False)
        elif coord.col == self.board.cols - 1:
            self.set_path(prop.DIR.W, False)

    def set_path(self, direction: int, value: bool) -> None:
        self.path[direction] = value
        new_coord = self.coord + prop.DIRS_DELTA[direction]
        if not self.board.in_range(new_coord):
            return

        self.board.get_cell(new_coord).path[prop.OPPOSITE_DIRS[direction]] = value

    def draw(self):
        Drawable.draw(self)
        if self.pawn:
            self.pawn.draw()

    def onMouseMotion(self, x, y):
        if not self.rect.collidepoint(x, y):
            self.set_focus(False)
            return

        if self.has_focus or self.pawn:
            return

        if self.board.current_player.can_move(self.coord):
            self.set_focus(True)

    def set_focus(self, val):
        val = bool(val)
        if self.has_focus == val:
            return

        self.color = self.focus_color if val else self.normal_color
        self.has_focus = val
        self.draw()

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    @property
    def state(self) -> str:
        return ''.join('01'[self.path[d]] for d in (prop.DIR.S, prop.DIR.W))
