## 8 PUZZLE USING SEARCH ALGORITHMS


#### `The problem`
The 8-puzzle problem is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid with 8 square blocks labelled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square. The following shows a sequence of legal moves from an initial board position (left) to the goal position (right).

#### `ALgorithms`
1. Uniformed - BFS
2. Informed Best First Search - Hamming Heuristc
3. Informed Best First Search - Manhattan Heuristc
4. Informed Best First Search - Hamming + Manhattan Heuristc
5. Informed Search - A* Algorithm


#### `Best-first search`
We define a state of the game to be the board position, the number of moves made to reach the board position, and the previous state. First, insert the initial state (the initial board, 0 moves, and a null previous state) into a priority queue. Then, delete from the priority queue the state with the minimum priority, and insert onto the priority queue all neighbouring states (those that can be reached in one move). Repeat this procedure until the state dequeued is the goal state. The success of this approach hinges on the choice of priority function for a state. We consider two priority functions:
1. `HAMMING PRIORITY FUNCTION.`
The number of blocks in the wrong position. Intuitively, a state with a small number of blocks in the wrong position is close to the goal state.
2. `MANHATTAN PRIORITY FUNCTION.`
The sum of the distances (sum of the vertical and horizontal distance) from the blocks to their goal positions.
For example, the Hamming and Manhattan priorities of the initial state below are 5 and 10, respectively.

Note that we do not count the blank tile when computing the Hamming or Manhattan priorities.)

#### `A critical optimization`
After implementing best-first search, you will notice one annoying feature: states corresponding to the same board position are enqueued on the priority queue many times. To prevent unnecessary exploration of useless states, when considering the neighbors of a state, don't enqueue the neighbor if its board position is the same as the previous state.

#### `Detecting infeasible puzzles`
Not all initial board positions can lead to the goal state. 
Reference - https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/

#### `How to Get Started`
git clone ''
cd 8puzzle
python 8puzzle.py

#### `Program Flow`
On running the file, program gives two options, first - run 100 configurations to compute and compare Effective Branching Factor for Greedy Best First search using hamming and Manhattan heuristic. This takes around 90 – 140 seconds. 
Second – Find solution to a single board. Further gives option to run either of the 5 possible algorithms (Uniformed Breadth First Search, Informed Best First Search using Hamming Heuristic, Informed Best First Search using Manhattan Heuristic, Informed Best First Search using Manhattan Heuristic + Hamming Heuristic and A* Algorithm).

`Global Variables and Functions:`

| Name    | Definition                                              |
|---------|---------------------------------------------------------|
| seq     | Provides the position of a numbered tile in a 3x3 board |
| goal    | Defines the goal state of the board                     |
| getNums | Function to get random configuration of the board       |


`BOARDSTATE CLASS`
Defines each node in search space graph. Stores the 3x3 board state, position of the blank, parent state, parent Move and number of moves to reach the current state. Following are the methods in BoardState Class:

| Name      | Definition                                                |
|-----------|-----------------------------------------------------------|
| init      | Initializes all the variables for the object              |
| hamming   | Return number of blocks out of place                      |
| manhattan | Return sum of Manhattan distances between blocks and goal |
| goalTest  | Returns true if the node is goal node                     |
| getString | Returns the stringyfied version of board                  |
| print     | Print current state of board                              |

`SOLVER CLASS`
Main agent that solves the puzzle. Stores the initial state, path, and total number of nodes traversed. It also keeps a track of open and closed frontier for various algorithms. Following are the methods in Solver Class:

| Name       | Definition                                                                                                                                        |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| init       | Initializes all the variables for the object                                                                                                      |
| isSolvable | Checks if the given orientation of board is solvable. If the number of inversions in the board is even - it is solvable, else it is not solvable. |
| bfs        | Main search method, that explores various nodes in the state space graph.                                                                         |
| solve      | Initialize the open as per the chosen algorithm                                                                                                   |
| up         | Moves the blank space up                                                                                                                          |
| down       | Moves the blank space down                                                                                                                        |
| left       | Moves the blank space to the left                                                                                                                 |
| right      | Moves the blank space to the right                                                                                                                |
| backtrack  | Backtracks and gets the solutions steps for the puzzle                                                                                            |
