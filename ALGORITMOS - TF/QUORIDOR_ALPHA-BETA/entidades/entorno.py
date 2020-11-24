import threading
import xmlrpc

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn

from support import log
import propiedades as prop
import juego
from bot.acciones import Action

class Functions:
    @staticmethod
    def alive():
        return True

    @staticmethod
    def close():
        juego.BOARD.terminate()
        return False

    @staticmethod
    def do_action(action: Action):
        if juego.BOARD.current_player:
            juego.BOARD.do_action(action)

            if not juego.BOARD.finished:
                juego.BOARD.next_player()

            return True

        return False
