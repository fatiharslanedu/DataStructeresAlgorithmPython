# nums = {1, 2, 2, 3}
# print(type(nums))
# nums.add(5)
# nums.update({6,7}) #todo: same with add.
# print(nums)
# nums.pop() #todo: remove the first element
# print(nums)
# #todo: .discard not created the keyError if the element not exist.
# #todo: but .remove do this
# empty_frozenset = frozenset()
# #todo: only difference between set and frozenset is immutable.
# Belov = ["Physics", "Math", "Russian"]
# Smith = ["Math", "Geometry", "English"]
# Sarada = ["Japanese", "Math", "Physics"]
# print(len(set(Belov + Sarada + Smith)))
# number = input()
# print([sum(map(int, number[:i + 1])) for i in range(len(number))])
# print([list(map(int, number[:i + 1])) for i in range(len(number))])
# school = [["Mary", "Jack", "Tiffany"],
#           ["Brad", "Claire"],
#           ["Molly", "Andy", "Carla"]]

# student_list = []
# for class_group in school:
#     for student in class_group:
#         student_list.append(student)

# print(student_list)

# print([student for class_group in school for student in class_group])
# print([[j for j in range(5)] for i in range(2)])
# number = int(input())
# total = 0
# winner_name = []
# for i in range(number):
#     string = input().split()
#     if string[1] == 'win':
#         winner_name.append(string[0])
#         total += 1

# print(winner_name)
# print(total)

# players = [input().split() for line in range(number)]
# print(players)
# winners = list(filter(lambda x: x[1] == 'win', players))
# print(winners)
# names = list(map(lambda x: x[0], winners))
# print(names, len(names), sep="\n")
# def split(stri):
#     return [i for i in stri]

# number = split(input())
# number = list(map(int, number))
# res = [(number[i] + number[i + 1]) / 2 for i in range(len(number) - 1) if i < len(number)]
# print(res)
# text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
#         ["Ephemeral", "lasts", "one", "day", "only"],
#         ["Accolade", "is", "an", "expression", "of", "praise"]]

# n = int(input())
# print([pre for group in text for pre in group if len(pre) <= n])

# def split(string):
#     return [x for x in string]


# def reformat(string: str):
#     list1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     k = 0
#     for i in range(3):
#         for j in range(3):
#             list1[i][j] = string[k]
#             k += 1

#     return list1


# string = 'XXXOO__O_'
# row0 = 0
# string = split(string)
# string = reformat(string)
# for i in range(3):
#         print("|", end=" ")
#         for j in range(3):
#             if i == 0 and string[0][j] == 'X':
#                 row0 += 1
#             print(string[i][j], end=" ")
            
#         print("|", end="\n")
       
# print(row0)        
PLAYER_O = 'O'
PLAYER_X = 'X'
GAME_NOT_FINISHED = 'Game not finished'
DRAW = 'Draw'
X_WINS = 'X wins'
O_WINS = 'O wins'
IMPOSSIBLE = 'Impossible'


def has_row_straight(player, board):
    return [player, player, player] in board


def has_column_straight(player, board):
    return (player, player, player) in zip(*board)


def has_diagonal_straight(player, board):
    return player == board[0][0] == board[1][1] == board[2][2] or \
           player == board[0][2] == board[1][1] == board[2][0]


def is_winner(player, board):
    return has_row_straight(player, board) or \
           has_column_straight(player, board) or \
           has_diagonal_straight(player, board)


def is_game_finished(board):
    return all(token in (PLAYER_O, PLAYER_X) for row in board for token in row)


def token_count(search_token, board):
    return len([token for row in board for token in row if token == search_token])


def player_token_diff(board):
    return abs(token_count(PLAYER_O, board) - token_count(PLAYER_X, board))


def two_winners(board):
    return is_winner(PLAYER_O, board) and is_winner(PLAYER_X, board)


def is_impossible(board):
    return player_token_diff(board) >= 2 or two_winners(board)


def board_state(board):
    if is_impossible(board):
        return IMPOSSIBLE
    if is_winner(PLAYER_X, board):
        return X_WINS
    if is_winner(PLAYER_O, board):
        return O_WINS
    if is_game_finished(board):
        return DRAW
    return GAME_NOT_FINISHED


def print_board(board):
    print('---------')
    for row in board:
        print('|', *row, '|')
    print('---------')


def board_2d(board_1d):
    # 0, 3, 6 are the indexes of the first token in each row
    return [[board_1d[y + x] for x in range(3)] for y in (0, 3, 6)]


def prompt_move():
    while True:
        coords = input("Enter the coordinates: ").split()
        if not all(coord.isdigit() for coord in coords):
            print('You should enter numbers!')
        elif not all(1 <= int(coord) <= 3 for coord in coords):
            print('Coordinates should be from 1 to 3!')
        elif game_board[3 - int(coords[1])][int(coords[0]) - 1] in (PLAYER_O, PLAYER_X):
            print('This cell is occupied! Choose another one!')
        else:
            return 3 - int(coords[1]), int(coords[0]) - 1


game_board = board_2d(' ' * 9)
player_turn = PLAYER_X
while board_state(game_board) == GAME_NOT_FINISHED:
    print_board(game_board)
    move_x, move_y = prompt_move()
    game_board[move_x][move_y] = player_turn
    player_turn = PLAYER_O if player_turn == PLAYER_X else PLAYER_X
print_board(game_board)
print(board_state(game_board))