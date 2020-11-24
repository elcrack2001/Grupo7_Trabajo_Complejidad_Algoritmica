from abc import ABC
from entidades.pared import Wall
from entidades.coordenadas import Coord


class Action(ABC):
    "Acciones"


class ActionPlaceWall(Action):
    def __init__(self, wall: Wall):
        self.coord = wall.coord
        self.horiz = wall.horiz

    def __repr__(self):
        return 'PlaceWall<{} {}>'.format(self.coord, '|-'[self.horiz])


class ActionMovePawn(Action):
    def __init__(self, from_: Coord, to_: Coord):
        self.orig = from_
        self.dest = to_

    def __repr__(self):
        return 'Move{{({}, {}) -> ({}, {})}}>'.format(self.orig.row, self.orig.col, self.dest.row, self.dest.col)
