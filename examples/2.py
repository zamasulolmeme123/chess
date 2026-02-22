class Move:
    """Хранит всю информацию об одном ходе"""
    
    def __init__(self, start_sq, end_sq, board):
        # start_sq и end_sq — это кортежи (row, col)
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row   = end_sq[0]
        self.end_col   = end_sq[1]
        # Запоминаем ЧТО двигали и ЧТО захватили — нужно для undo
        self.piece_moved    = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def __repr__(self):

        """Красивый вывод хода: Move(e2 → e4)"""
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        s = f"{cols[self.start_col]}{8 - self.start_row}"
        e = f"{cols[self.end_col]}{8 - self.end_row}"
        return f"Move({s} → {e}  [{self.piece_moved}])"

class GameState:
    """Полное состояние игры в любой момент"""
    
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.white_to_move = True
        self.move_log = []          # список объектов Move

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = '--'
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move   # меняем очередь

    def undo_move(self):
        if not self.move_log:       # если история пустая — нечего отменять
            return
        move = self.move_log.pop()  # берём последний ход из истории
        self.board[move.start_row][move.start_col] = move.piece_moved
        self.board[move.end_row][move.end_col] = move.piece_captured
        self.white_to_move = not self.white_to_move
    def whose_turn(self):
        if self.white_to_move:
            return "Белые"
        else:
            return "Чёрные"

def print_board(board):
    print("\n     a    b    c    d    e    f    g    h")
    print("   +----+----+----+----+----+----+----+----+")
    for i, row in enumerate(board):
        rank = 8 - i
        print(f" {rank} |", end="")
        for piece in row:
            print(f" {piece} |", end="")
        print()
        print("   +----+----+----+----+----+----+----+----+")
    print()


# ── Test ──────────────────────────────────────────────
gs = GameState()                    # создаём объект игры
print_board(gs.board)

# Ход: e2 → e4  (строка 6, столбец 4) → (строка 4, столбец 4)
move1 = Move((6, 4), (4, 4), gs.board)
print(move1)                        # → Move(e2 → e4  [wP])
gs.make_move(move1)
print_board(gs.board)

# Whose turn now 
print(gs.whose_turn())

# Отменяем ход
gs.undo_move()
print_board(gs.board)               # доска должна вернуться к начальной
