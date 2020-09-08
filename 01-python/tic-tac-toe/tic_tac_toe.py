import re
import random as rand

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"


class TicTacToeGame():
    def __init__(self):
        self.board = [None] * 9
        self.turn = _PLAYER
        self.is_game_over = False
        self.winner = None

    def is_over(self):
        value = False
        winnerSymbol = None
        # Horizontals
        if self.board[0] != None and self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            value = True
            winnerSymbol = self.board[0]
        elif self.board[3] != None and self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            value = True
            winnerSymbol = self.board[3]
        elif self.board[6] != None and self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            value = True
            winnerSymbol = self.board[6]
        # Verticals
        elif self.board[0] != None and self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            value = True
            winnerSymbol = self.board[0]
        elif self.board[1] != None and self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            value = True
            winnerSymbol = self.board[1]
        elif self.board[2] != None and self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            value = True
            winnerSymbol = self.board[2]
        # Diagonals
        elif self.board[0] != None and self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            value = True
            winnerSymbol = self.board[0]
        elif self.board[2] != None and self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            value = True
            winnerSymbol = self.board[2]
        # None
        else:
            value = self.board.count(None) == 0
        if value == True:
            print("Game Over")
            if(winnerSymbol == _PLAYER_SYMBOL):
                self.winner = _PLAYER
            elif(winnerSymbol == _MACHINE_SYMBOL):
                self.winner = _MACHINE
            else:
                self.winner = "no one, it's a tie"
        return value

    def play(self):
        if self.turn == _PLAYER:
            self.player_turn()
            self.turn = _MACHINE
        else:
            self.machine_turn()
            self.turn = _PLAYER

    def player_choose_cell(self):
        print("Input empty cell bewtween 0 and 8")

        player_cell = input().strip()
        match = re.search("\d", player_cell)

        if not match:
            print("Input is not a number, please try again")

            return self.player_choose_cell()

        player_cell = int(player_cell)

        if self.board[player_cell] is not None:
            print("Cell is already taken, try again")

            return self.player_choose_cell()

        return player_cell

    def player_turn(self):
        chosen_cell = self.player_choose_cell()

        self.board[chosen_cell] = _PLAYER_SYMBOL

    def machine_turn(self):
        finished = False
        while not finished:
            pos = rand.randint(0, 8)
            if self.board[pos] == None:
                self.board[pos] = _MACHINE_SYMBOL
                finished = True

    def format_board(self):
        return self.strgConv(self.board[0])+"|"+self.strgConv(self.board[1])+"|"+self.strgConv(self.board[2])+"\n"+self.strgConv(self.board[3])+"|"+self.strgConv(self.board[4])+"|"+self.strgConv(self.board[5])+"\n"+self.strgConv(self.board[6])+"|"+self.strgConv(self.board[7])+"|"+self.strgConv(self.board[8])

    def strgConv(self, entry):
        if entry == None:
            return " "
        else:
            return entry

    def print(self):
        print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
        print(self.format_board())
        print()

    def print_result(self):
        print("The winner is "+self.winner)
