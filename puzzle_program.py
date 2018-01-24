import puzzle_functions


def get_num_rows(puzzle):
    """ (str) -> int

    Return the number of rows in puzzle, which is a game board.

    >>> get_num_rows('abcd\nefgh\nijkl\n')
    3
    """

    return puzzle.count('\n')


def get_num_cols(puzzle):
    """ (str) -> int

    Return the number of columns in puzzle, which is a game board.

    >>> get_num_cols('abcd\nefgh\nijkl\n')
    4
    """

    return puzzle.index('\n')


def print_puzzle(puzzle):
    """ (str) -> NoneType

    Print the puzzle with row and column numbers and two spaces
    between each letter.
    """

    # Split puzzle into rows and get dimensions.
    puzzle_rows = puzzle.strip().split('\n')
    num_rows = get_num_rows(puzzle)
    num_columns = get_num_cols(puzzle)

    # Print the column headings.
    print('   ', end='')
    for col_number in range(num_columns):
        print(col_number, ' ', end='')

    print()

    # Print each row number and row.
    for row_number in range(num_rows):
        print(row_number, end='  ')
        print('  '.join(puzzle_rows[row_number]))

    print()


def print_words(words):
    """ (list of str) -> NoneType

    Print the items from words.
    """

    print('The remaining words to be found: ')
    for word in words:
        print(word, end=' ')
    print('\n')


def get_direction_calculate_score(puzzle, guess, current_player_name, words):
    """ (str, str, str, str, list of str) -> int

    Prompt for the direction and the row or column number.  Based on these
    answers and the number of words left to be found, calculate and return the
    appropriate score.
    """

    # Prompt for the direction.
    direction = None
    while direction not in ['up', 'down', 'forward', 'backward']:
        direction = input(
            current_player_name +
            ', enter the direction (up, down, forward, or backward): ')

    # Prompt for the row or column number, check whether the word occurs in
    # that row or column in the direction specified, and calculate the score.
    if direction == 'up' or direction == 'down':
        row_or_col_num = int(
            input('Enter the column number where ' + guess + ' occurs: '))
    elif direction == 'forward' or direction == 'backward':
        row_or_col_num = int(
            input('Enter the row number where ' + guess + ' occurs: '))

    words_left = len(words)

    return puzzle_functions.calculate_score(
        puzzle, direction, guess, row_or_col_num, words_left)


def take_turn(puzzle, words, current_player_name):
    """ (str, list of str, str) -> int

    Prompt the current player (according to player_one_turn) to make a guess,
    and then return the number of occurrences of that word in the puzzle. If the
    guess isn't in words, then return 0.  Remove the guess from the list of
    words.
    """

    num_rows = get_num_rows(puzzle)
    num_cols = get_num_cols(puzzle)

    # Prompt for a word from the list of valid words.
    guess = input(current_player_name + ', please enter a word: ').strip()

    score = get_direction_calculate_score(
        puzzle, guess, current_player_name, words)

    # Remove the guess from the word list.
    words.remove(guess)

    return score


def game_over(words):
    """ (list of str) -> bool

    Return True iff words is empty.

    >>> game_over(['dan', 'paul'])
    False
    >>> game_over([])
    True
    """

    return len(words) == 0


def play_game(puzzle, words):
    """ (str, list of words) -> Nonetype

    Prompt the players to guess words that occur in the puzzle.
    Print the score after each turn.  Print the winner.
    """

    # Whether it's Player One's turn; if False, it's Player Two's turn.
    player_one_turn = True

    # The scores for the two players.
    player_one_score = 0
    player_two_score = 0

    print('''***************************************
**       Where's That Word?          **
***************************************''')

    # Prompt for a guess and add up the points until the game is over.
    while not game_over(words):

        print_puzzle(puzzle)
        print_words(words)

        # Get the name of the player whose turn it is.
        current_player_name = \
            puzzle_functions.get_current_player(player_one_turn)

        # Have the player take their turn and get the score.
        score = take_turn(puzzle, words, current_player_name)

        # Update the score for whoever's turn it is.
        if player_one_turn:
            player_one_score = player_one_score + score
            print(current_player_name + "'s score is " +
                  str(player_one_score) + '.\n')
        else:
            player_two_score = player_two_score + score
            print(current_player_name + "'s score is " +
                  str(player_two_score) + '.\n')

        player_one_turn = not player_one_turn

    print(puzzle_functions.get_winner(player_one_score, player_two_score))


# The main program begins here ###

puzzle = """rmhlzxceuq
bxmichelle
mnnejluapv
caellehcim
xdydanagbz
xiniarbprr
vctzevbkiz
jgfavqwjan
quotjenhna
iumxddbxnd
"""

words = ['brian', 'dan', 'jen', 'michelle', 'paul']

play_game(puzzle, words)