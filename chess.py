# Chess board
board = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
]

print(board[1][1])

# Output board

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
print_board(board)


def get_piece(board):
    pos = input("Введите координату (например, e4): ").lower()
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    if 0 <= col <= 7 and 0 <= row <= 7:
        figure = board[row][col]
        print(f"На позиции {pos} стоит: {figure}")
    else:
        print("Некорректные координаты!")

get_piece(board)


