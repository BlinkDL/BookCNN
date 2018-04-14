from __future__ import print_function
import mxnet as mx
import sys
import os
import math
import random
import numpy as np
from board import GameState
import re

N = 19

WHITE = -1
BLACK = +1
EMPTY = 0

np.core.arrayprint._line_width = 120
colstr = 'ABCDEFGHJKLMNOPQRST'

first_run = True
iter = None
sym, arg_params, aux_params = mx.model.load_checkpoint("model//model", 39540)

features = 8

module = mx.mod.Module(symbol=sym, context=[mx.gpu()])

# init board data
board = GameState()

data = [[[ 0 for x in range(N) ] for y in range(N)] for c in range(features)]

def piece(color):
    if color == WHITE:
        return 'O'
    elif color == BLACK:
        return 'X'
    else:
        return '.'

def debug_print(*args, **kwargs):
    return
    print(*args, file=sys.stderr, **kwargs)

def main():
    clear_board()
    gtp_io()

def clear_board():
    global board
    board = GameState()
    
def print_board():
    debug_print(piece(-board.current_player) + ' move at ' + str(board.history[-1]) + ' #' + str(len(board.history)))
    y_desc = '   ' + ' '.join(colstr) + '    ' + ' '.join(colstr)
    debug_print(y_desc)
    for y in range(0, N):
        x_desc = str(N - y).rjust(2) + ' '
        line = x_desc
        for x in range(0, N):
            here = y * N + x;
            line += piece(board.board[x][y]) + ' '
        line += x_desc
        for x in range(0, N):
            if board.liberty_counts[x][y] > 9:
                line += '@ '
            elif board.liberty_counts[x][y] > 0:
                line += str(board.liberty_counts[x][y]) + ' '
            else:
                line += '  '
        line += x_desc
        debug_print(line)
    debug_print(y_desc)

def print_data():
    np.set_printoptions(formatter={'all':lambda x: str("%i" % x)})
    for c in range(0, features):
        debug_print(c)
        debug_print(data[0][c])

def do_move(player, move):
    global board
    if move == None: # pass?
        board.do_move(None, player)
        return
    board.do_move((move % N, move // N), player)


def make_prediction():
    global data, board, first_run, iter
    # clear data
    data = [[[ 0 for x in range(N) ] for y in range(N)] for c in range(features)]
    
#   fill data
#   OLD:
#   7   6   5   4   3   2   1   0
#   me  opp e   l1  l2  l3  l4+ last_play
    if len(board.history) > 0: # played some moves?
        last_move = board.history[-1]
        if last_move != None: # last move is not pass
            data[0][last_move[1]][last_move[0]] = 1 # last_move
    for x in range(0,N):
        for y in range(0,N):
            here = y * N + x;
            if len(board.history) > 0: # played some moves?
                # fill channel 5,6,7
                if board.board[x][y] == -board.current_player:
                    data[6][y][x] = 1 # opp
                elif board.board[x][y] == EMPTY:
                    data[5][y][x] = 1 # empty
                else:
                    data[7][y][x] = 1 # me
                # fill channel 1,2,3,4
                if board.liberty_counts[x][y] >= 4:
                    data[1][y][x] = 1
                elif board.liberty_counts[x][y] == 3:
                    data[2][y][x] = 1
                elif board.liberty_counts[x][y] == 2:
                    data[3][y][x] = 1
                elif board.liberty_counts[x][y] == 1:
                    data[4][y][x] = 1
            else:
                data[5][y][x] = 1 # empty

    data=np.array([data])              
    print_data()

    iter = mx.io.NDArrayIter(data=data)

    if first_run:
        module.bind(data_shapes=iter.provide_data)
        module.set_params(arg_params, aux_params)
        first_run = False

    pred = module.predict(iter).asnumpy()
    
    # remove forbidden moves
    for x in range(0,N):
        for y in range(0,N):
            here = y * N + x;
            if board.board[x][y] != EMPTY:
                pred[0][here] = 0
            if (x, y) == board.ko:
                pred[0][here] = 0
    
    best_move = (pred.tolist()[0].index(np.nanmax(pred)))
    
    # DEBUG: print prediction
    np.set_printoptions(formatter={'all':lambda x: str("%s" % str(int(round(x*100.0,0))).rjust(2))})
    debug_print(pred.reshape(N,N))

    # SUICIDE => PASS
    if board.is_suicide((best_move % N, best_move // N)):
        best_move = fill_policy(pred[0])
        if best_move is not None:
            (x, y) = best_move
            best_move = y * N + x
    
    # make best move
    do_move(board.current_player, best_move)
        
    return best_move

def fill_policy(pred):
    debug_print("filling...")
    # try to kill enemy 1-liberty groups (might be bad in very rare cases?)
    for x in range(0,N):
        for y in range(0,N):
            if board.board[x][y] == -board.current_player and board.liberty_counts[x][y] == 1:
                for e in board.liberty_sets[x][y]:
                    break
                if e != board.ko: # must avoid ko
                    return e
    # try to play best move inside unsettled regions (hence always fail at seki) (might not be best coz approx. flood fill)
    # firstly, approx. flood fill (assuming full coverage because we are in end-game)
    black = [[0 for col in range(N)] for row in range(N)]
    white = [[0 for col in range(N)] for row in range(N)]
    for x in range(0,N):
        color = None
        for y in range(0,N):
            if board.board[x][y] != EMPTY:
                color = board.board[x][y]
            if color == BLACK:
                black[x][y] = 1
            elif color == WHITE:
                white[x][y] = 1
        color = None
        for y in range(0,N):
            if board.board[x][N - 1 - y] != EMPTY:
                color = board.board[x][N - 1 - y]
            if color == BLACK:
                black[x][N - 1 - y] = 1
            elif color == WHITE:
                white[x][N - 1 - y] = 1
    for y in range(0,N):
        color = None
        for x in range(0,N):
            if board.board[x][y] != EMPTY:
                color = board.board[x][y]
            if color == BLACK:
                black[x][y] = 1
            elif color == WHITE:
                white[x][y] = 1
        color = None
        for x in range(0,N):
            if board.board[N - 1 - x][y] != EMPTY:
                color = board.board[N - 1 - x][y]
            if color == BLACK:
                black[N - 1 - x][y] = 1
            elif color == WHITE:
                white[N - 1 - x][y] = 1
    # do area estimation
    best_move = None
    best_prob = 0
    area = [[0 for col in range(N)] for row in range(N)]
    for x in range(0,N):
        for y in range(0,N):
            if black[x][y] > 0:
                area[x][y] += 1
            if white[x][y] > 0:
                area[x][y] += 2
            if area[x][y] == 3:
                here = y * N + x;
                if pred[here] > best_prob:
                    if not board.is_suicide((x, y)): # must avoid suicide
                        best_prob = pred[here]
                        best_move = (x, y)
    np.set_printoptions(formatter={'all':lambda x: 'X' if x == 1 else 'O' if x == 2 else ' ' if x == 3 else '?'})
    debug_print(np.transpose(np.array(area)))
    return best_move

################################################################################
# GTP
################################################################################

def parse_coord(s):
    if s.upper() == 'PASS':
        return None
    return int((N - int(s[1:])) * N + colstr.index(s[0].upper()))

def str_coord(c):
    if c is None:
        return 'pass'
    row, col = divmod(c, N)
    return '%c%d' % (colstr[col], N - row)

def gtp_io():
    known_commands = ['boardsize', 'clear_board', 'komi', 'play', 'genmove',
                      'quit', 'name', 'version', 'known_command',
                      'list_commands', 'protocol_version']

    while True:
        try:
            line = raw_input().strip()
        except EOFError:
            break
        if line == '':
            continue
        command = [s.lower() for s in line.split()]
        if re.match('\d+', command[0]):
            cmdid = command[0]
            command = command[1:]
        else:
            cmdid = ''
        ret = ''
        if command[0] == "boardsize":
            if int(command[1]) != N:
                debug_print("Warning: Trying to set incompatible boardsize %s (!= %d)" % (command[1], N))
                ret = None
        elif command[0] == "clear_board":
            clear_board() # clear board
        elif command[0] == "komi":
            pass # set komi
        elif command[0] == "play":
            c = parse_coord(command[2])
            if command[1].upper() == 'BLACK':
                do_move(BLACK, c)
            else:
                do_move(WHITE, c)
            print_board()
        elif command[0] == "genmove":
            move = make_prediction()
            if move is None:
                ret = 'pass'
            elif False:
                ret = 'resign'
            else:
                ret = str_coord(move)
            print_board()
        elif command[0] == "name":
            ret = 'zzCNNTest'
        elif command[0] == "version":
            ret = '0.01'
        elif command[0] == "list_commands":
            ret = '\n'.join(known_commands)
        elif command[0] == "known_command":
            ret = 'true' if command[1] in known_commands else 'false'
        elif command[0] == "protocol_version":
            ret = '2'
        elif command[0] == "quit":
            print('=%s \n\n' % (cmdid,), end='')
            os.system("taskkill /im pytho.exe /f") # remember to copy python as pytho (such that it wont kill training process)
            break
        else:
            debug_print('Warning: Ignoring unknown command - %s' % (line,))
            ret = None
        
        if ret is not None:
            print('=%s %s\n\n' % (cmdid, ret,), end='')
        else:
            print('?%s ???\n\n' % (cmdid,), end='')
        sys.stdout.flush()
        
if __name__=="__main__":
    main()

os.system("taskkill /im pytho.exe /f")
    