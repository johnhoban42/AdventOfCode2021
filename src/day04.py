from typing import List


# Class for monitoring a 5x5 bingo card
# Cells are marked by replacing its original value with -1. A board has a bingo
# when some row or column has a sum of -5.
class BingoBoard:

    # Store each bingo board as a list of length 25 with some metadata
    def __init__(self, board: List[int]):
        self.board = board
        self.has_bingo = False

    # Check row 0-4 for a bingo
    def check_row(self, r: int):
        assert 0 <= r <= 4
        if sum(self.board[i] for i in range(5*r, 5*r+5)) == -5:
            self.has_bingo = True

    # Check col 0-4 for a bingo
    def check_col(self, c: int):
        assert 0 <= c <= 4
        if sum(self.board[i] for i in range(c, 25+c, 5)) == -5:
            self.has_bingo = True

    # Mark a board and check the appropriate row/col for bingo
    def mark_board(self, num: int):
        try:
            i = self.board.index(num)
        except ValueError:
            return
        self.board[i] = -1
        self.check_row(i // 5)
        self.check_col(i % 5)

    # Score a board based on which cells are unmarked
    def get_score(self):
        unmarked = list(filter(lambda x: x != -1, self.board))
        return sum(unmarked)


# Parse source
src = open("../inputs/day04.txt").readlines()
nums = list(map(int, src[0].strip().split(",")))
boards = []
for i in range(2, len(src), 6):
    b = []
    for row in range(i, i+5):
        src[row] = src[row].replace("  ", " ")
        b.extend(list(map(int, src[row].strip().split(" "))))
    boards.append(BingoBoard(b))

# Play bingo
# PART 1: Use first board done for score
# PART 2: Use last board done for score
score1 = 0
score2 = 0
winner = None
while boards:
    n = nums.pop(0)
    i = 0
    while i < len(boards):
        b = boards[i]
        b.mark_board(n)
        if b.has_bingo:
            if not winner:  # first board done
                winner = b
                score1 = b.get_score() * n
            elif len(boards) == 1:  # last board done
                score2 = b.get_score() * n
            # Remove the finished board and adjust the iterator accordingly
            boards.remove(b)
            i -= 1
        i += 1

print(f"PART 1: {score1}")
print(f"PART 2: {score2}")
