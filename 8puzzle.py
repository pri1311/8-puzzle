import random
import numpy as np
import time

from frontier import (
    QueueFrontier,
    PriorityQueueFrontier,
    PriorityQueueHammingFrontier,
    PriorityQueueManhattanFrontier,
    PriorityQueueAStarFrontier,
)

seq = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Defines each node in search space graph
class BoardState(object):
    def __init__(self, nums, parentMove, pos, moves, parent) -> None:
        super().__init__()
        self.board = np.array(nums).reshape(3, 3).tolist()
        self.parentMove = parentMove
        self.pos = pos
        self.parent = parent
        self.moves = moves

    # return number of blocks out of place
    def hamming(self):
        ct = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != 9:
                    if self.board[i][j] != (j + 1) + (i * 3):
                        ct += 1
        return ct

    # return sum of Manhattan distances between blocks and goal
    def manhattan(self):
        dist = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != 9:
                    x = (j + 1) + (i * 3)
                    if self.board[i][j] != x:
                        dist += abs(seq[self.board[i][j]][0] - i) + abs(
                            seq[self.board[i][j]][1] - j
                        )
        return dist

    # Returns true if the goal is goal node.
    def goalTest(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != goal[i][j]:
                    return False
        return True

    # Returns the stringyfied version of board
    def getString(self):
        s = ""
        for i in range(0, 3):
            for j in range(0, 3):
                s += str(self.board[i][j])
        return s

    # Print current state of board
    def print(self):
        print("-------------")
        print(
            "| %i | %i | %i |" % (self.board[0][0], self.board[0][1], self.board[0][2])
        )
        print("-------------")
        print(
            "| %i | %i | %i |" % (self.board[1][0], self.board[1][1], self.board[1][2])
        )
        print("-------------")
        print(
            "| %i | %i | %i |" % (self.board[2][0], self.board[2][1], self.board[2][2])
        )
        print("-------------")


class Solver(object):
    def __init__(self, nums, pos) -> None:
        super().__init__()

        self.nums = nums
        self.initialState = BoardState(nums, "NIL", pos, 0, None)
        self.path = []  # To store the solution steps
        self.closed = []
        self.nodesTraversed = 0

    # Checks if the given orientation of board is solvable.
    # If the number of inversions is even - it is solvable, else it is not solvable.
    def isSolvable(self):
        ct = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if self.nums[i] != 9 and self.nums[j] < self.nums[i]:
                    ct += 1
        return ct % 2 == 0

    # Uninformed BFS search to find the least number of moves required to reach the goal state/ to solve the puzzle.
    def bfs(self, open):
        open.add(self.initialState)
        self.closed.append(self.initialState.getString())

        while open.empty() == False:
            state = open.remove()

            self.nodesTraversed += 1

            if state.goalTest() == True:
                ebf = self.backtrack(state)
                return ebf

            # print(state.board, state.parentMove)

            i, j = state.pos[0], state.pos[1]

            if i > 0 and i < 3 and j >= 0 and j < 3:
                newState = self.up(state)
                boardList = newState.getString()

                if boardList not in self.closed:
                    open.add(newState)
                    self.closed.append(boardList)

            if i >= 0 and i < 2 and j >= 0 and j < 3:
                newState = self.down(state)
                boardList = newState.getString()

                if boardList not in self.closed:
                    open.add(newState)
                    self.closed.append(boardList)

            if i >= 0 and i < 3 and j > 0 and j < 3:
                newState = self.left(state)
                boardList = newState.getString()

                if boardList not in self.closed:
                    open.add(newState)
                    self.closed.append(boardList)

            if i >= 0 and i < 3 and j >= 0 and j < 2:
                newState = self.right(state)
                boardList = newState.getString()

                if boardList not in self.closed:
                    open.add(newState)
                    self.closed.append(boardList)

    # Initialize the open as per the chosen algorithm
    def solve(self, choice):
        if choice == 0:
            choice = int(input())
        open = QueueFrontier()

        if choice == 1:
            open = QueueFrontier()
            print("Uniformed - BFS")
        elif choice == 2:
            print("Informed Best First Search - Hamming Heuristc")
            open = PriorityQueueHammingFrontier()
        elif choice == 3:
            print("Informed Best First Search - Manhattan Heuristc")
            open = PriorityQueueManhattanFrontier()
        elif choice == 4:
            print("Informed Best First Search - Hamming + Manhattan Heuristc")
            open = PriorityQueueFrontier()
        elif choice == 5:
            print("Informed Search - A* star Algorithm")
            open = PriorityQueueAStarFrontier()

        return self.bfs(open)

    # Moves the blank space up
    def up(self, state):
        board = []
        for li in state.board:
            board.append(li[:])
        a = state.pos[0]
        b = state.pos[1]
        board[a][b], board[a - 1][b] = board[a - 1][b], board[a][b]
        newState = BoardState(
            board, "Up", (state.pos[0] - 1, state.pos[1]), state.moves + 1, state
        )
        return newState

    # Moves the blank space down
    def down(self, state):
        board = []
        for li in state.board:
            board.append(li[:])
        a = state.pos[0]
        b = state.pos[1]
        board[a][b], board[a + 1][b] = board[a + 1][b], board[a][b]
        newState = BoardState(
            board, "Down", (state.pos[0] + 1, state.pos[1]), state.moves + 1, state
        )
        return newState

    # Moves the blank space to the left
    def left(self, state):
        board = []
        for li in state.board:
            board.append(li[:])
        a = state.pos[0]
        b = state.pos[1]
        board[a][b], board[a][b - 1] = board[a][b - 1], board[a][b]
        newState = BoardState(
            board, "Left", (state.pos[0], state.pos[1] - 1), state.moves + 1, state
        )
        return newState

    # Moves the blank space to the right
    def right(self, state):
        board = []
        for li in state.board:
            board.append(li[:])
        a = state.pos[0]
        b = state.pos[1]
        board[a][b], board[a][b + 1] = board[a][b + 1], board[a][b]
        newState = BoardState(
            board, "Right", (state.pos[0], state.pos[1] + 1), state.moves + 1, state
        )
        return newState

    # Backtracks and gets the solutions steps for the puzzle
    def backtrack(self, state):

        print("Path to the Solution is")
        node = state
        while node.parent != None:
            # print(node.board, node.parentMove)
            self.path.append(node.parentMove)
            node = node.parent

        self.path.reverse()
        print(self.path)

        print("Total Number of nodes visited: ", end="")
        print(self.nodesTraversed)

        print("Effective branching factor: ", end="")
        print(pow(self.nodesTraversed, 1 / len(self.path)))

        return pow(self.nodesTraversed, 1 / len(self.path))


# Function to get random configuration of the board
def getNums():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)
    a = b = 0
    for i in range(0, 9):
        if nums[i] == 9:
            a = int(i / 3)
            b = i % 3
            break

    # nums = [8, 1, 3, 4, 9, 2, 7, 6, 5]  # pos = (1, 1)
    # nums = [5, 2, 9, 3, 7, 6, 1, 8, 4]  # pos = (0, 2)
    # nums = [7, 8, 1, 3, 4, 9, 2, 5, 6]
    # (a, b) = (1, 2)
    return nums, (a, b)
    # return nums, (1, 1)


# Driver function
if __name__ == "__main__":
    print("1. Calculate branching factor (Hamming & Manhattan")
    print("2. Solve single 8 puzzle")

    choice = int(input())
    if choice == 1:
        begin = time.time()
        h1, h2, h3, ct = 0, 0, 0, 100

        while ct > 0:
            nums, (a, b) = getNums()

            solver = Solver(nums, (a, b))

            print("Initial board configuration: ")
            solver.initialState.print()

            if solver.isSolvable():
                ct -= 1
                print("Given orientation is solvable")

                h1 += solver.solve(2)
                solver = Solver(nums, (a, b))
                h2 += solver.solve(3)
                solver = Solver(nums, (a, b))
                h3 += solver.solve(4)
            else:
                print("Given orientation is not solvable")

        end = time.time()
        print("Effective branching factor for Hamming Heuristic is: ")
        print(h1 / 100)
        print("Effective branching factor for Manhattan Heuristic is: ")
        print(h2 / 100)
        print("Effective branching factor for Hamming + Manhattan Heuristic is: ")
        print(h3 / 100)
        print(f"Total runtime of the program is {end - begin}")

    else:
        nums, (a, b) = getNums()

        solver = Solver(nums, (a, b))
        print("Initial board configuration: ")
        solver.initialState.print()

        while True:
            if solver.isSolvable():
                print("Given orientation is solvable")
                print("Which search do you wish to perform:")
                print("1. Uniformed - BFS")
                print("2. Informed Best First Search - Hamming Heuristc")
                print("3. Informed Best First Search - Manhattan Heuristc")
                print("4. Informed Best First Search - Hamming + Manhattan Heuristc")
                print("5. Informed Search - A* Algorithm")
                solver.solve(0)
                break
            else:
                print("Given orientation is not solvable")
                nums, (a, b) = getNums()

                solver = Solver(nums, (a, b))
                print("Initial board configuration: ")
                solver.initialState.print()
