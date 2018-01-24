# The constants describing the multiplicative factor for finding a word in
# a particular direction.  These should be used in function get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4
 

def get_current_player(player_one_turn):
    """ (bool) -> str

    Return 'Player One' iff player_one_turn is True; otherwise, return
    'Player Two'.

    >>> get_current_player(True)
    'Player One'
    >>> get_current_player(False)
    'Player Two'
    """
    
    # Get appropriate player whether the parameter is True or False
    if player_one_turn == True:
        return 'Player One'
    return 'Player Two'

# Define the other functions from the handout here
def get_winner(player_one_score, player_two_score):
    """ (int, int) -> str
    
    Precondition: player_one_score and player_two_score >= 0    
        
    Return 'Player One wins!' if player_one_score is greater than \
    player_two_score or 'Player Two wins!' if player_two_score is \
    greater than player_one_score. If both player_one_score \
    and player_two_score are equal, return 'Tie game!'.
    
    >>> get_winner(5, 2)
    'Player One wins!'
    >>> get_winner(2, 5)
    'Player Two wins!'
    >>> get_winner(5, 5)
    'Tie game!'
    """
    
    # Get winner depending on which player has highest score or if their \
    # scores are equal
    if player_one_score > player_two_score:
        return 'Player One wins!'
    elif player_one_score < player_two_score:
        return 'Player Two wins!'
    else:
        return 'Tie game!'
    
def get_factor(direction):
    """ (str) -> int
     
    Return specific factor 1, 2, 3, or 4 for the given direction forward, down,\ 
    backward, up, respectively.
    
    >>> get_factor('forward')
    1
    >>> get_factor('down')
    2
    >>> get_factor('backward')
    3
    >>> get_factor('up')
    4
    """
    
    # Get direction according to the different factor constants
    if direction == 'forward':
        return FORWARD_FACTOR
    elif direction == 'down':
        return DOWN_FACTOR
    elif direction == 'backward':
        return BACKWARD_FACTOR
    else:
        if direction == 'up':
            return UP_FACTOR
        
def get_points(direction, remaining_num_words):
    """ (str, int) -> int
    
    Precondition: remaining_num_words > 0
    
    Return direction multiplied by 5 if remaining_num_words is greater or \ 
    equal to 5.If remaining_num_words is less than 5, return 10 minus \
    remaining_num_words all multiplied by direction factor. In addition if \
    remaining_num_words is equal to 1, add 25 points.
    
    >>> get_points('up', 7)
    20
    >>> get_points('backward', 3)
    21
    >>> get_points('down', 1)
    43
    """
    
    # Get points from the number of remaining words and the direction
    if remaining_num_words >= 5:
        return get_factor(direction) * 5
    elif 1 < remaining_num_words < 5:
        return get_factor(direction) * (10 - remaining_num_words)
    else:
        if remaining_num_words == 1:
            return get_factor(direction) * (10 - remaining_num_words) + 25
        
def calculate_score(puzzle, direction, guessed_word, row_or_column_num, 
                    remaining_num_words):
    """ (str, str, str, int , int) -> int
    
    Precondition1: 0 <= row_or_column_num < number of rows or columns in puzzle
    Precondition2: direction MUST be 'forward', 'backward', 'down', or 'up'
    Precondition3: puzzle MUST have existing incidices in the column if the \
    guessed_word is found in that column
    
    Return score when word is found in appropriate direction and row_or_column \
    with appropriate num_of_remaining_words; otherwise return 0. 
    
    >>> calculate_score('amax\nmich\nceci\n', 'forward', 'ama', 0, 6)
    5
    >>> calculate_score('adnamax\ncecilia\n', 'backward', 'amanda', 0, 6)
    15
    >>> calculate_score('ang\nlii\neca\nskr\nsyc\n', 'up', 'craig', 2, 1)
    61
    >>> calculate_score('fm\nai\nbc\nrh\nia\nce\nel\n', 'down', 'Michael', 1, 4)
    0
    """
        
    # Get string out of the puzzle
    if direction == 'forward':
        puzzle_string = get_row(puzzle, row_or_column_num)
    elif direction == 'backward':
        puzzle_string = reverse(get_row(puzzle, row_or_column_num))
    elif direction == 'down':
        puzzle_string = get_column(puzzle, row_or_column_num)
    elif direction == 'up':
        puzzle_string = reverse(get_column(puzzle, row_or_column_num))
    else:
        puzzle_string = ''
        
    # Check if guessed word is in the string   
    if puzzle_string != '' and contains(puzzle_string, guessed_word):
        score = get_points(direction, remaining_num_words)
    else:
        score = 0
        
    return score
        
# Helper functions.  Do not modify these, although you are welcome to call
# them.

def get_row(puzzle, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle

    Return row row_num of puzzle.

    >>> get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """

    rows = puzzle.strip().split('\n')
    return rows[row_num]


def get_column(puzzle, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle

    Return column col_num of puzzle.
    >>> get_column('abcde\nefghi\nijklm\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def reverse(s):
    """ (str) -> str

    Return a reversed copy of s.

    >>> reverse('abc')
    'cba'
    """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed

    return s_reversed


def contains(s1, s2):
    """ (str, str) -> bool

    Return whether s2 appears anywhere in s1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return s2 in s1

