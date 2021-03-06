import pygame

from .dibujar import Drawable
from .coordenadas import Coord
from propiedades import DIR, DIRS_DELTA


class Wall(Drawable):
    def __init__(self,
                 screen: pygame.Surface,
                 board,
                 color: pygame.Color,
                 coord: Coord = None,
                 horiz: bool = None,
                 ):
        super().__init__(screen, color)
        self.board = board
        self.horiz: bool = horiz
        self.coord = coord
        self._hash = hash((self.horiz, self.coord))

    def __eq__(self, other) -> bool:
        assert isinstance(other, Wall)
        return self.horiz == other.horiz and self.coord == other.coord

    def __repr__(self):
        return "<Wall: %i, %i, %i>" % (self.coord.row, self.coord.col, int(self.horiz))

    def __hash__(self):
        return self._hash

    @property
    def coords(self):
        if self.horiz is None or self.coord is None:
            return None

        if self.horiz:
            return [self.coord, self.coord + DIRS_DELTA[DIR.W]]

        return [self.coord, self.coord + DIRS_DELTA[DIR.N]]

    @property
    def rect(self):
        c = self.coords
        if not c:
            return None

        cell = self.board.get_cell(self.coord)
        if self.horiz:
            x = cell.x
            y = cell.y + cell.height
            w = self.board.cell_pad + 2 * cell.width
            h = self.board.cell_pad
        else:
            x = cell.x + cell.width
            y = cell.y
            w = self.board.cell_pad
            h = self.board.cell_pad + 2 * cell.width

        return pygame.Rect(x, y, w, h)

    def draw(self):
        if self.color is None:
            return

        pygame.draw.rect(self.screen, self.color, self.rect, 0)

    def collides(self, wall):
        if self.horiz == wall.horiz:
            wc = wall.coords
            for c in self.coords:
                if c in wc:
                    return True

            return False

        # Only can collide if they form a cross
        if self.coord == wall.coord:
            return True

        return False

    @property
    def state(self) -> str:
        return "%i%i%i" % (self.coord.row, self.coord.col, self.horiz)
