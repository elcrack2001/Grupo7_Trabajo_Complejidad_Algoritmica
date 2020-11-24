import re
from typing import List, Union, Tuple

from support import log, LogLevel
import juego
import propiedades as prop
from propiedades import INF
from memo_cache import PersistentDict

from entidades.pared import Wall
from entidades.coordenadas import Coord
from .acciones import Action, ActionPlaceWall, ActionMovePawn


class BOT:
    def __init__(self, pawn, level=1):
        self.level = level  # Level of difficulty
        self.board = pawn.board
        if prop.CACHE_ENABLED:
            self._memoize_think = PersistentDict(prop.CACHE_AI_FNAME, flag='c')
        else:
            self._memoize_think = {}

        pawn.BOT = self
        log('Jugador %i es controlado por la A.I.' % pawn.id)

    @property
    def available_actions(self) -> List[Union[ActionPlaceWall, ActionMovePawn]]:
        player = self.pawn
        result = [ActionMovePawn(player.coord, x) for x in player.valid_moves]

        if not player.walls:
            return result

        k = self.board.state[1 + 4 * len(self.board.pawns):]
        try:
            return result + juego.MEMOIZED_WALLS[k]
        except KeyError:
            pass

        color = self.board[0][0].wall_color
        tmp: List[Union[ActionPlaceWall, ActionMovePawn]] = []

        for i in range(self.board.rows - 1):
            for j in range(self.board.cols - 1):
                for horiz in (False, True):
                    wall = Wall(self.board.screen, self.board, color, Coord(i, j), horiz)
                    if self.board.can_put_wall(wall):
                        tmp.append(ActionPlaceWall(wall))

        juego.MEMOIZED_WALLS[k] = tmp
        return result + tmp

    def clean_memo(self):
        if prop.CACHE_ENABLED:
            return

        L = 1 + len(self.board.pawns) * 4
        k = self.board.state[L:]
        k = '.' * L + k.replace('1', '.') + '$'
        r = re.compile(k)

        for q in list(self._memoize_think.keys()):
            if not r.match(q):
                del self._memoize_think[q]

    def move(self) -> Tuple[Action, int]:
        for coord in self.pawn.valid_moves:
            if coord in self.pawn.goals:
                return ActionMovePawn(self.pawn.coord, coord), -INF

        self.pawn.percent = 0  # Percentage done
        move, h, alpha, beta = self.think(bool(self.level % 2))
        self.clean_memo()
        self.distances.clean_memo()
        return move, h

    def do_action(self, action: Union[ActionPlaceWall, ActionMovePawn]):
        if isinstance(action, ActionPlaceWall):
            self.board.putWall(self.board.new_wall(action.coord, action.horiz))
            self.pawn.walls -= 1
        else:
            self.pawn.move_to(action.dest)

    def undo_action(self, action: Union[ActionPlaceWall, ActionMovePawn]):
        if isinstance(action, ActionPlaceWall):
            self.board.removeWall(self.board.new_wall(action.coord, action.horiz))
            self.pawn.walls += 1
        else:
            self.pawn.move_to(action.orig)

    def think(self, is_max: bool, ilevel=0, alpha=INF, beta=-INF):

        #Retorna movimiento o poner pared

        k = str(ilevel) + self.board.state[1:]
        try:
            r = self._memoize_think[k]
            juego.MEMOIZED_NODES_HITS += 1
            return r
        except KeyError:
            juego.MEMOIZED_NODES += 1
            pass

        result = None
        stop = False

        if ilevel >= self.level:
            # algoritmo min max -> alpha beta
            # h -> distancia mínima del jugador hacia la meta

            HH = INF
            h_j0 = self.distances.shortest_path_len #min distancia del jugador
            h_p0 = self.board.pawns[(self.board.player + 1) % 2].distances.shortest_path_len #min distancia de todos

            for action in self.available_actions:
                self.do_action(action)

                p = self.pawn
                self.board.update_pawns_distances()
                h_j1 = self.distances.shortest_path_len
                h_p1 = min([pawn.distances.shortest_path_len for pawn in self.board.pawns if pawn is not p])
                h = h_j1 - h_p1

                if is_max:
                    h = -h
                    if h > HH:
                        HH = h
                        result = action

                        if HH >= alpha:
                            HH = alpha
                            stop = True
                elif h < HH:
                    HH = h
                    result = action

                    if HH <= beta:
                        HH = beta
                        stop = True

                elif self.level == 0 and h == HH and h_j1 <= h_j0 and h_p1 > h_p0:
                    result = action

                self.undo_action(action)
                if stop:
                    break

            self._memoize_think[k] = result, HH, alpha, beta
            return result, HH, alpha, beta

        HH = -INF if is_max else INF
        player = self.board.current_player
        player.distances.push_state()
        r = self.available_actions
        count_r = 0
        L = float(len(r))

        for action in r:
            if not ilevel and player.percent is not None:
                count_r += 1
                player.percent = count_r / L
                self.board.draw_player_info(player.id)

            self.do_action(action)
            self.board.next_player()
            dummy, h, alpha1, beta1 = self.think(not is_max, ilevel + 1, alpha, beta)
            self.previous_player()

            if is_max:
                if h > HH:
                    result, HH = action, h
                    if HH >= alpha:
                        HH = alpha
                        stop = True
                    else:
                        beta = HH
            else:
                if h < HH: #es minimo
                    result, HH = action, h
                    if HH <= beta:
                        HH = beta
                        stop = True
                    else:
                        alpha = HH

            self.undo_action(action)
            if stop:
                break

        player.distances.pop_state()
        self._memoize_think[k] = result, HH, alpha, beta
        return result, HH, alpha, beta

    @property
    def pawn(self):
        return self.board.current_player

    @property
    def distances(self):
        return self.pawn.distances

    def previous_player(self):
        self.board.player = (self.board.player + self.board.num_players - 1) % self.board.num_players

    def flush_cache(self):
        if isinstance(self._memoize_think, PersistentDict):
            self._memoize_think.close()
