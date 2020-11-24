import os
import pygame
from pygame.locals import *
from pygame import Color
import threading
import argparse
import time

from support import log, LogLevel
import propiedades as prop
import juego

from entidades.tablero import Board


def dispatch(events, board: Board):
    for event in events:
        if event.type == QUIT:
            return False

        if hasattr(event, 'key'):
            if event.key == K_ESCAPE or board.finished:
                return False

        if board.computing or board.finished or board.current_player.is_network_player:
            continue

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            board.onMouseClick(x, y)

        if event.type == MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            board.onMouseMotion(x, y)

    return True


def main() -> int:
    juego.init()

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level",
                        help="Dificultad por defecto -> 0",
                        default=prop.LEVEL, type=int)

    parser.add_argument('-d', '--debug', action='store_true')

    parser.add_argument('-C', '--cache', action='store_true')

    options = parser.parse_args()
    prop.LEVEL = options.level
    prop.__DEBUG__ = options.debug
    prop.CACHE_ENABLED = options.cache

    log('Quoridor - Complejodad Algorítmica - Grupo 7')
    log('Iniciando...')
    start = time.time()
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption(prop.GAME_TITLE)
    screen = pygame.display.get_surface()

    screen.fill(Color(255, 255, 255))
    board = juego.BOARD = Board(screen)
    board.draw()

    if prop.CACHE_ENABLED:
        if not os.path.exists(prop.CACHE_DIR):
            os.makedirs(prop.CACHE_DIR, exist_ok=True)

        if not os.path.isdir(prop.CACHE_DIR):
            prop.CACHE_ENABLED = False

    cont = True
    while cont:
        clock.tick(prop.FRAMERATE)
        pygame.display.flip()

        if not board.computing and not board.finished:
            if board.current_player.BOT:
                board.computing = True
                thread = threading.Thread(target=board.computer_move)
                thread.start()

        cont = dispatch(pygame.event.get(), board)
    end = time.time()
    game_time = (end - start)
    del board.rows
    pygame.quit()

    if prop.CACHE_ENABLED:
        for pawn in board.pawns:
            if pawn.BOT is not None:
                pawn.BOT.flush_cache()

    log('Nodos guardados: %i' % juego.MEMOIZED_NODES)
    log('Nodos utilizados guardados: %i' % juego.MEMOIZED_NODES_HITS)

    for pawn in board.pawns:
        log('Distancias guardadas para [%i]: %i' % (pawn.id, pawn.distances.MEMO_COUNT))
        log('Distancias recorridas guardadas [%i]: %i' % (pawn.id, pawn.distances.MEMO_HITS))

    log('Tiempo de juego en segundos: ')
    log(game_time)
    log('¡Adiós!')
    return 0


if __name__ == '__main__':
    main()
