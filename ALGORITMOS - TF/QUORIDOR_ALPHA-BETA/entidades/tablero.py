from typing import Set, List, Union
import pygame

from support import log
from entidades.entorno import Functions
import propiedades as prop

from bot.acciones import ActionMovePawn, ActionPlaceWall
from bot.bot import BOT

from .dibujar import Drawable
from .ficha import Pawn
from .casilla import Cell
from .pared import Wall
from .coordenadas import Coord

from propiedades import DIR


class Board(Drawable):
    def __init__(self,
                 screen: pygame.Surface,
                 rows=prop.DEF_ROWS,
                 cols=prop.DEF_COLS,
                 cell_padding=prop.CELL_PAD,
                 color=prop.BOARD_BG_COLOR,
                 border_color=prop.BOARD_BRD_COLOR,
                 border_size=prop.BOARD_BRD_SIZE):

        Drawable.__init__(self, screen=screen, color=color, border_color=border_color, border_size=border_size)
        self.rows: int = rows
        self.cols: int = cols
        self.cell_pad = cell_padding
        self.mouse_wall = None
        self.player: int = 0
        self.board: List[List[Cell]] = []
        self.computing = False
        self._state = None

        for i in range(rows):
            self.board.append([])
            for j in range(cols):
                self.board[-1].append(Cell(screen, self, coord=Coord(i, j)))

        self.pawns: List[Pawn] = []
        self.pawns += [Pawn(screen=screen,
                            board=self,
                            color=prop.PAWN_A_COL,
                            border_color=prop.PAWN_BORDER_COL,
                            coord=Coord(rows - 1, 3),
                            )]
        self.pawns += [Pawn(screen=screen,
                            board=self,
                            color=prop.PAWN_B_COL,
                            border_color=prop.PAWN_BORDER_COL,
                            coord=Coord(0, 3)
                            )]
        self.pawns += [Pawn(screen=screen,
                            board=self,
                            color=prop.PAWN_C_COL,
                            border_color=prop.PAWN_BORDER_COL,
                            coord=Coord(3, 0)
                            )]
        self.pawns += [Pawn(screen=screen,
                            board=self,
                            color=prop.PAWN_D_COL,
                            border_color=prop.PAWN_BORDER_COL,
                            coord=Coord(3, cols - 1)
                            )]

        self.regenerate_board(prop.CELL_COLOR, prop.CELL_BORDER_COLOR)
        self.num_players = prop.DEFAULT_NUM_PLAYERS
        self.walls: Set[Wall] = set()
        self.draw_players_info()
        self._AI = []
        self._AI += [BOT(self.pawns[0], level=prop.LEVEL)]
        self._AI += [BOT(self.pawns[1], level=prop.LEVEL)]
        self._AI += [BOT(self.pawns[2], level=prop.LEVEL)]
        self._AI += [BOT(self.pawns[3], level=prop.LEVEL)]

    def regenerate_board(self, c_color, cb_color, c_width=prop.CELL_WIDTH, c_height=prop.CELL_HEIGHT):
        y = self.cell_pad
        for i in range(self.rows):
            x = self.cell_pad
            for j in range(self.cols):
                cell = self.board[i][j]
                cell.x, cell.y = x, y
                cell.color = c_color
                cell.border_color = cb_color
                cell.height = c_height
                cell.width = c_width
                cell.pawn = None
                x += c_width + self.cell_pad
            y += c_height + self.cell_pad

        for pawn in self.pawns:
            pawn.cell = self.get_cell(pawn.coord)

    def draw(self):
        super().draw()

        for row in self:
            for cell in row:
                cell.draw()

        if prop.__DEBUG__:
            for p in self.pawns:
                if p.BOT:
                    p.distances.draw()
                    break

        for wall in self.walls:
            wall.draw()

    def get_cell(self, coord: Coord) -> Cell:
        return self.board[coord.row][coord.col]

    def set_cell(self, coord: Coord, value: Cell):
        self.board[coord.row][coord.col] = value

    def __getitem__(self, i: int) -> List[Cell]:
        return self.board[i]

    def in_range(self, coord: Coord) -> bool:
        return 0 <= coord.col < self.cols and 0 <= coord.row < self.rows

    def putWall(self, wall: Wall) -> None:
        if wall in self.walls:
            return

        self.walls.add(wall)
        i, j = wall.coord

        if wall.horiz:
            self.board[i][j].set_path(DIR.S, False)
            self.board[i][j + 1].set_path(DIR.S, False)
        else:
            self.board[i][j].set_path(DIR.W, False)
            self.board[i + 1][j].set_path(DIR.W, False)

        self._state = None

    def removeWall(self, wall: Wall) -> None:
        if wall not in self.walls:
            return

        self.walls.remove(wall)
        i, j = wall.coord

        if wall.horiz:
            self.board[i][j].set_path(DIR.S, True)
            self.board[i][j + 1].set_path(DIR.S, True)
        else:
            self.board[i][j].set_path(DIR.W, True)
            self.board[i + 1][j].set_path(DIR.W, True)

        self._state = None

    #Para jugador persona
    def onMouseClick(self, x, y):
        cell = self.which_cell(x, y)
        if cell is not None:
            pawn = self.current_player
            if not pawn.can_move(cell.coord):
                return

            self.do_action(ActionMovePawn(pawn.coord, cell.coord))
            cell.set_focus(False)
            self.draw()

            if self.finished:
                self.draw_player_info(self.player)
                return

            self.next_player()
            self.draw_players_info()
            return

        wall = self.wall(x, y)
        if not wall:
            return

        if self.can_put_wall(wall):
            self.do_action(ActionPlaceWall(wall))
            self.next_player()
            self.draw_players_info()

    #Para jugador persona
    def onMouseMotion(self, x, y):
        if not self.rect.collidepoint(x, y):
            return

        for row in self.board:
            for cell in row:
                cell.onMouseMotion(x, y)

        if self.which_cell(x, y):
            if self.mouse_wall:
                self.mouse_wall = None
                self.draw()

            return

        if not self.current_player.walls:
            return

        wall = self.wall(x, y)
        if not wall:
            return

        if self.can_put_wall(wall):
            self.mouse_wall = wall
            self.draw()
            wall.draw()

    def can_put_wall(self, wall) -> bool:
        if not self.current_player.walls:
            return False

        for w in self.walls:
            if wall.collides(w):
                return False

        result = True
        self.putWall(wall)

        for pawn in self.pawns:
            if not pawn.can_reach_goal():
                result = False
                break

        self.removeWall(wall)
        return result

    def wall(self, x, y) -> Union[Wall, None]:
        if not self.rect.collidepoint(x, y):
            return None

        j = (x - self.x) // (self.board[0][0].width + self.cell_pad)
        i = (y - self.y) // (self.board[0][0].height + self.cell_pad)
        cell = self.board[i][j]

        horiz = x < (cell.x + cell.width)
        if horiz:
            if j > 7:
                j = 7
        else:
            if i > 7:
                i = 7

        if i > 7 or j > 7:
            return None

        return self.new_wall(Coord(i, j), horiz, cell.wall_color)

    def new_wall(self, coord: Coord, horiz: bool, color: pygame.Color = None) -> Wall:
        if color is None:
            color = self.board[0][0].wall_color
        return Wall(self.screen, self, color, coord, horiz)

    @property
    def x(self):
        return self.board[0][0].x

    @property
    def y(self):
        return self.board[0][0].y

    @property
    def width(self):
        return (self.cell_pad + self.board[0][0].width) * self.cols

    @property
    def height(self):
        return (self.cell_pad + self.board[0][0].height) * self.rows

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def next_player(self):
        self.player = (self.player + 1) % self.num_players
        self.update_pawns_distances()

    def update_pawns_distances(self):
        for pawn in self.pawns:
            pawn.distances.update()

    def which_cell(self, x, y):
        for row in self.board:
            for cell in row:
                if cell.rect.collidepoint(x, y):
                    return cell

        return None

    @property
    def current_player(self):
        return self.pawns[self.player]

    def draw_player_info(self, player_num):
        pawn = self.pawns[player_num]
        r = pawn.rect
        r.x = self.rect.x + self.rect.width + prop.PAWN_PADDING
        r.y = (player_num + 1) * (r.height + prop.PAWN_PADDING)
        if self.current_player is pawn:
            pygame.draw.rect(self.screen, prop.CELL_VALID_COLOR, r, 0)
            pygame.draw.rect(self.screen, pawn.border_color, r, 2)
        else:
            pygame.draw.rect(self.screen, self.color, r, 0)

        pawn.draw(r)
        rect = pygame.Rect(r.x + 1, r.y + r.h + 3, prop.GAUGE_WIDTH, prop.GAUGE_HEIGHT)

        if pawn.percent is not None:
            pygame.draw.rect(self.screen, prop.FONT_BG_COLOR, rect, 0)
            rect.width = int(prop.GAUGE_WIDTH * pawn.percent)
            pygame.draw.rect(self.screen, prop.GAUGE_COLOR, rect, 0)
            rect.width = prop.GAUGE_WIDTH
            pygame.draw.rect(self.screen, prop.GAUGE_BORDER_COLOR, rect, 1)
        else:
            pygame.draw.rect(self.screen, prop.FONT_BG_COLOR, rect, 0)

        r.x += r.width + 20
        r.width = 6
        pygame.draw.rect(self.screen, prop.WALL_COLOR, r, 0)

        r.x += r.width * 2 + 10
        r.y += r.height // 2 - 5
        r.height = prop.FONT_SIZE
        r.width *= 3
        pygame.draw.rect(self.screen, prop.FONT_BG_COLOR, r, 0)
        self.msg(r.x, r.y, str(pawn.walls))

        if self.finished and self.current_player == pawn:
            self.msg(r.x + prop.PAWN_PADDING, r.y, "¡JUGADOR %i GANA!" % (1 + self.player))
            x = self.rect.x
            y = self.rect.y + self.rect.height + prop.PAWN_PADDING
            self.msg(x, y, "Presiona cualquier tecla para salir")

    def msg(self, x, y, str_, color=prop.FONT_COLOR, fsize=prop.FONT_SIZE):
        font = pygame.font.SysFont(None, fsize)
        fnt = font.render(str_, True, color)
        self.screen.blit(fnt, (x, y))

    def draw_players_info(self):
        for i in range(len(self.pawns)):
            self.draw_player_info(i)

    def do_action(self, action: Union[ActionPlaceWall, ActionMovePawn]):
        player_id = self.current_player.id

        if isinstance(action, ActionPlaceWall):
            wdir = 'horizontal' if action.horiz else 'vertical'
            log('Jugador %i coloca %s pared en (%i, %i)' % (player_id, wdir, action.coord.col, action.coord.row))
            self.putWall(self.new_wall(action.coord, action.horiz))
            self.current_player.walls -= 1
        else:
            log('Jugador %i se mueve a (%i, %i)' % (player_id, action.dest.row, action.dest.col))
            self.current_player.move_to(action.dest)
            self._state = None

        for pawn in self.pawns:
            if pawn.is_network_player:
                pawn.do_action(action)

    def computer_move(self):
        while self.current_player.BOT and not self.finished:
            self.draw()
            self.draw_players_info()
            action, x = self.current_player.BOT.move()
            self.do_action(action)

            if self.finished:
                break

            self.next_player()

        self.draw()
        self.draw_players_info()
        self.computing = False

    @property
    def finished(self):
        return any(pawn.coord in pawn.goals for pawn in self.pawns)

    @property
    def state(self):
        if self._state is not None:
            return self._state

        result = str(self.player)  # jugador
        result += ''.join(p.state for p in self.pawns)
        result += ''.join(self.board[i][j].state for j in range(self.cols - 1) for i in range(self.rows - 1))
        self._state = result

        return result
