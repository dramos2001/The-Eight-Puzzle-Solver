import heapq
import time
from copy import copy, deepcopy

# pre-defined initial puzzle states for the user to choose from
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

very_easy = [[1, 2, 3],
             [4, 5, 6],
             [0, 7, 8]]

easy = [[1, 2, 3],
        [5, 0, 6],
        [4, 7, 8]]

medium = [[1, 3, 6],
          [5, 0, 2],
          [4, 7, 8]]

hard = [[1, 6, 7],
        [5, 0, 3],
        [4, 8, 2]]

impossible = [[7, 1, 2],
              [4, 8, 5],
              [6, 3, 0]]

# the goal state of the 8 puzzle 
solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

# var equates to size of the puzzle (i.e. 3 for 3x3 puzzle/8 puzzle)
# can be changed to account for 15-puzzle, 25-puzzle, etc.
puzzle_size = 3


class Node:
    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle
        self.moves = 0
        self.h = 0
            
    def setHeuristicH(self, h):
        self.h = h
        
    def setMoves(self, moves):
        self.moves = moves
        
    def solved(self) -> bool:
        return (self.puzzle == solved)
    
    def __lt__(self, other):
        return ((self.moves + self.h) < (other.moves + other.h))
    

# function to determine where on the puzzle is the empty/zero space 
def setEmptyTilePosition(puzzle):
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if (puzzle[i][j] == 0):
                return [i, j]
            
            
# function to calcualte the total number of misplaced tiles in the puzzle
# this number equates to h in the heuristic function   
def calculateMisplacedTiles(puzzle) -> int:
    num = 0
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if ((puzzle[i][j] != solved[i][j]) and (puzzle[i][j])):
                num+=1
                
    return num


# function to calculate the manhattan distance heuristic of an eight puzzle
# used as a heuristic for A* search 
def calculateManhattanHeuristic(puzzle) -> int:
    distance = 0
    solved_dict = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 
                   5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1]}
    
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            if (puzzle[i][j] != 0 and puzzle[i][j] != solved[i][j]):
                coordinate = []
                coordinate = solved_dict[puzzle[i][j]]
                distance += abs(i-coordinate[0]) + abs(j-coordinate[1])
                
    return int(distance)
  
# function to create a new node where the empty space is moved up one space            
def moveUp(initial_node, empty_tile, algorithm):
    if (empty_tile[0] != 0):
        # shift empty tile up one space
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x-1][empty_y]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x-1][empty_y] = 0
        
        # calculate heuristic
        new_node = Node(temp_puzzle)
        new_node.setMoves(initial_node.moves+1)
        if (algorithm == "1"):
            new_node.setHeuristicH(0)
        elif (algorithm == "2"):
            h = calculateMisplacedTiles(new_node.puzzle)
            new_node.setHeuristicH(h)
        elif (algorithm == "3"):
            h = calculateManhattanHeuristic(new_node.puzzle)
            new_node.setHeuristicH(h)
            
        return new_node
        
# function to create a new node where the empty space is moved downd one space            
def moveDown(initial_node, empty_tile, algorithm):
    if (empty_tile[0] != puzzle_size-1):
        # shift empty tile down one space
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x+1][empty_y]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x+1][empty_y] = 0
        
        # calculate heuristics
        new_node = Node(temp_puzzle)
        new_node.setMoves(initial_node.moves+1)
        if (algorithm == "1"):
            new_node.setHeuristicH(0)
        elif (algorithm == "2"):
            h = calculateMisplacedTiles(new_node.puzzle)
            new_node.setHeuristicH(h)
        elif (algorithm == "3"):
            h = calculateManhattanHeuristic(new_node.puzzle)
            new_node.setHeuristicH(h)
            
        return new_node
    
        
# function to create a new node where the empty space is moved to the left one space          
def moveLeft(initial_node, empty_tile, algorithm):
    if (empty_tile[1] != 0):
        # shift empty tile to the left one space
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x][empty_y-1]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x][empty_y-1] = 0
        
        # calculate heuristics
        new_node = Node(temp_puzzle)
        new_node.setMoves(initial_node.moves+1)
        if (algorithm == "1"):
            new_node.setHeuristicH(0)
        elif (algorithm == "2"):
            h = calculateMisplacedTiles(new_node.puzzle)
            new_node.setHeuristicH(h)
        elif (algorithm == "3"):
            h = calculateManhattanHeuristic(new_node.puzzle)
            new_node.setHeuristicH(h)
            
        return new_node

# function to create a new node where the empty space is moved to the right one space            
def moveRight(initial_node, empty_tile, algorithm):
    if (empty_tile[1] != puzzle_size - 1):
        # shift empty tile to the right one space
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x][empty_y+1]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x][empty_y+1] = 0
        
        # calculate heuristics
        new_node = Node(temp_puzzle)
        new_node.setMoves(initial_node.moves+1)
        if (algorithm == "1"):
            new_node.setHeuristicH(0)
        elif (algorithm == "2"):
            h = calculateMisplacedTiles(new_node.puzzle)
            new_node.setHeuristicH(h)
        elif (algorithm == "3"):
            h = calculateManhattanHeuristic(new_node.puzzle)
            new_node.setHeuristicH(h)
            
        return new_node
  
# the general search algorithm to solve the 8 puzzle problem
# this function accepts custom puzzles or pre-defined puzzles and 
# allows for use of Uniform Cost search and A* with either the 
# misplaced tile heuristic or the manhattan distance heuristic
def generalSearch(algorithm, puzzle, heuristic):
    # for determining the runtime of the search algorithms
    start_time = time.time()
    
    # creating a priority queue and initializing it with the initial puzzle
    root = Node(puzzle)
    root.setHeuristicH(heuristic)
    empty_tile_pos = setEmptyTilePosition(root.puzzle)
    p_queue = []
    heapq.heappush(p_queue, root)
    heapq.heapify(p_queue)
    num_expanded_nodes = 1
    max_queue_len = 1
    
    # list to store puzzles that have been traversed/analyzed
    puzzle_states = []
    
    while (len(p_queue) > 0):
        # analyze first node for a solution
        max_queue_len = max(len(p_queue), max_queue_len)
        head_node = heapq.heappop(p_queue)
        
        # if the node has the solution print to user max queue size, depth, and algorithm runtime
        if (head_node.solved()):
            # print puzzle solution path
            print("Path to solved puzzle:")
            for i in puzzle_states:
                printPuzzle(i)
            
            print("Number of nodes expanded: ", num_expanded_nodes)
            print("Max queue size: ", max_queue_len)
            print("Answer found at depth: ", head_node.moves)
            print("Time for algorithm to finish:", time.time() - start_time, "seconds")     
            return
        # if the node is not one of the already checked puzzle states, we can analyze it and create new states from it
        if (head_node.puzzle not in puzzle_states):
            # show user which puzzle is being expanded
            print("The best state to expand with a g_n = ", head_node.moves, "and h_n = ", head_node.h, "is...")
            printPuzzle(head_node.puzzle)
            num_expanded_nodes+=1
            empty_tile_pos = setEmptyTilePosition(head_node.puzzle)
            
            # compute movements here to create new puzzle nodes and add them to a list
            new_nodes = []
            new_nodes.append(moveDown(head_node, empty_tile_pos, algorithm))
            new_nodes.append(moveUp(head_node, empty_tile_pos, algorithm))
            new_nodes.append(moveRight(head_node, empty_tile_pos, algorithm))
            new_nodes.append(moveLeft(head_node, empty_tile_pos, algorithm))
              
            # check that the nodes are not empty and add them to the priority queue
            for i in range(0, len(new_nodes)):
                temp = new_nodes[i]
                if (temp is not None and temp.puzzle not in puzzle_states):
                    heapq.heappush(p_queue, new_nodes[i])
                    max_queue_len = max(len(p_queue), max_queue_len)
            
            # add the original node to the list containing already visited puzzles
            puzzle_states.append(head_node.puzzle)
            new_nodes.clear()
    
    print("No solution found")
            
# print the n x n puzzle in its entirety            
def printPuzzle(puzzle):
    for i in range(puzzle_size):
        print(puzzle[i])
    print('\n')
    
    
# main driver code for the program
def main():
    # get user input to determine if they want to create a custom puzzle or use a default one
    game_mode = input("Welcome to my 8-Puzzle Solver. Type 1 to use a default puzzle, or 2 to "
                      + "make your own.\n")
    
    # user chooses a default puzzle; have the user choose one based on puzzle difficulty
    if (game_mode == "1"):
        default_puzzle = []
        
        difficulty = input("You chose to use one of the default puzzles in this program. Enter your desired"
              + " difficulty on a scale from 0 to 5.\n")
        
        if (difficulty == "0"):
            print("Difficulty of 'trivial' selected.")
            default_puzzle = trivial
        elif (difficulty == "1"):
            print("Difficulty of 'very easy' selected.")
            default_puzzle = very_easy
        elif (difficulty == "2"):
            print("Difficulty of 'easy' selected.")
            default_puzzle = easy
        elif (difficulty == "3"):
            print("Difficulty of 'medium' selected.")
            default_puzzle = medium
        elif (difficulty == "4"):
            print("Difficulty of 'hard' selected.")
            default_puzzle = hard
        elif (difficulty == "5"):
            print("Difficulty of 'impossible' selected.")
            default_puzzle = impossible
        
        # finally have user choose which algorithm to solve the puzzle
        chooseAlgorithm(default_puzzle)
    # user wants to input a custom puzzle
    elif (game_mode == "2"):
        custom_puzzle = []
        
        print("Enter the numbers for the puzzle one by one. Hit enter after inputting each number" +
              "Nine valid numbers should be entered, including 0 for the blank space.\n")
        
        # checks for input of numbers for the puzzle
        for i in range(puzzle_size):
            arr = []
            for j in range(puzzle_size):
                arr.append(int(input()))
            custom_puzzle.append(arr)
        
        # finally have user choose which algorithm to solve the puzzle
        chooseAlgorithm(custom_puzzle)
    
    
# ask the user which algorithm to use to solve the puzzle
def chooseAlgorithm(puzzle):
    algorithm = input("Select an algorithm:\n1. Uniform Cost Search\n2. Misplaced Tile Heuristic"
                      + "\n3. Manhattan Distance Heuristic\n")
    
    # user has chosen the Uniform Cost Search; heuristic is set to 0
    if algorithm == "1":
        print("You chose: Uniform Cost Search")
        generalSearch(algorithm, puzzle, 0)
    # user has chosen A* with the Misplaced Tile Heuristic; heuristic is computed using misplaced tiles function
    elif algorithm == "2":
        print("You chose: Misplaced Tile Heuristic Search")
        h = calculateMisplacedTiles(puzzle)
        generalSearch(algorithm, puzzle, h)
    # user has chosen A* with the Manhattan Distance Heuristic; heuristic is computed using manh. dist. function
    elif algorithm == "3":
        print("You chose: Manhattan Distance Heuristic Search")
        h = calculateManhattanHeuristic(puzzle)
        generalSearch(algorithm, puzzle, h)

main()
