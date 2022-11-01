import heapq

from numpy import tile

# pre-defined initial puzzle states for the user to choose from
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]

very_easy = [[1, 2, 0],
             [4, 5, 3],
             [7, 8, 6]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

medium = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]

hard = [[8, 7, 1],
        [6, 0, 2],
        [5, 4, 3]]

# the goal state of the 8 puzzle 
solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]


class Node:
    def __init__(self, parent_node, puzzle, misplaced_tiles, moves, empty_tile) -> None:
        self.parent_node = parent_node
        self.puzzle = puzzle
        self.misplaced_tiles = misplaced_tiles
        self.moves = moves
        self.empty_tile = empty_tile
        
    def solved(self) -> bool:
        return (self.puzzle == solved)
        
    def boardToTuple(self) -> tuple:
        return tuple(map(tuple, self.puzzle))
    
    def __lt__(self, other):
        return (self.misplaced_tiles < other.misplaced_tiles)
    


def uniformCostSearch(puzzle, heuristic):
    root = Node(None, puzzle, 0, 0, emptyTilePosition(puzzle))
    p_queue = []
    repeated_states = dict()
    heapq.heappush(p_queue, root)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[root.boardToTuple()] = "This is the parent board"
    
    puzzle_states_stack = []
    
    while (len(p_queue) > 0):
        max_queue_size = max(len(p_queue), max_queue_size)
        head_node = heapq.heappop(p_queue)
        repeated_states[head_node.boardToTuple()] = "This can be anything"
        
        if (head_node.solved()):
            while (len(puzzle_states_stack) > 0):
                printPuzzle(puzzle_states_stack.pop())
            
            print("Number of nodes expanded: ", num_nodes_expanded)
            print("Max queue size: ", max_queue_size)
            return head_node
        
        for i in range(4):
            new_tile_position = [head_node.empty_tile[0], 
                                 head_node.empty_tile[1]]
            child_node = createNewNode(head_node.puzzle, solved, head_node, head_node.moves+1,
                                       head_node.empty_tile, new_tile_position)
            heapq.heappush(p_queue, child_node)
        
        puzzle_states_stack.append(head_node.puzzle)
            

# recreating the general search algorithm that was presented in the slides
def generalSearch(initial, goal, queueing_function):
    g = calculateMisplacedTiles(initial, goal)
    root = Node(None, initial, g, 0, emptyTilePosition(initial))
    heapq.heappush(queueing_function, root)
    
    while():
        # first we check if the queue is empty
        if not queueing_function.heap:
            return False
        # if not true we pop off the head off nodes
        node = heapq.heappop(queueing_function)
        # determine if the head is the goal state
        if (node.misplaced_tiles == 0):
            return node
        # if not create all of the head node's children and push it into the queue
        #heapq.heappush(queueing_function, createNewNode(initial, goal, node, queueing_function.moves))
        

def createNewNode(initial_state, goal_state, root_node, moves, empty_tile, new_empty_tile):
    new_state = initial_state
    g = calculateMisplacedTiles(new_state, goal_state)
    
    tile_x = empty_tile[0]
    tile_y = empty_tile[1]
    tile_x_2 = new_empty_tile[0]
    tile_y_2 = new_empty_tile[1]
    new_state[tile_x][tile_y] = new_state[tile_x_2][tile_y_2]
    new_state[tile_x_2][tile_y_2] = new_state[tile_x][tile_y]
    
    new_node = Node(root_node, new_state, g, moves, emptyTilePosition(initial_state))
    return new_node
            

# determine where the empty tile is in the puzzle
def emptyTilePosition(puzzle):
    for i in range(3):
        for j in range(3):
            if (puzzle[i][j] == 0):
                return [i, j]
    
# function to calcualte the total number of misplaced tiles in the puzzle
# this number equates to g in the heuristic function   
# to be used for manhattan and misplaced tile heuristics     
def calculateMisplacedTiles(puzzle, goal) -> int:
    num = 0
    for i in range(3):
        for j in range(3):
            if ((puzzle[i][j] != goal[i][j]) and (puzzle[i][j])):
                num+=1
                
    return num
            
# print the n x n puzzle in its entirety            
def printPuzzle(puzzle):
    for i in range(3):
        print(puzzle[i])
    print('\n')
    
def driverCode():
    game_mode = input("Welcome to my 8-Puzzle Solver. Type 1 to use a default puzzle, or 2 to "
                      + "make your own.\n")
    if (game_mode == "1"):
        default_puzzle = []
        
        difficulty = input("You chose to use one of the default puzzles in this program. Enter your desired"
              + " difficulty on a scale from 0 to 5.\n")
        
        if difficulty == "0":
            print("Difficulty of 'trivial' selected.")
            default_puzzle = trivial
        elif difficulty == "1":
            print("Difficulty of 'very easy' selected.")
            default_puzzle = very_easy
        elif difficulty == "2":
            print("Difficulty of 'easy' selected.")
            default_puzzle = easy
        elif difficulty == "3":
            print("Difficulty of 'medium' selected.")
            default_puzzle = medium
        elif difficulty == "4":
            print("Difficulty of 'hard' selected.")
            default_puzzle = hard
            
        chooseAlgorithm(default_puzzle)
    elif (game_mode == "2"):
        custom_puzzle = []
        
        print("Enter the numbers for the puzzle one by one. Hit enter after inputting each number" +
              "Nine valid numbers should be entered, including 0 for the blank space.\n")
        
        for i in range(3):
            arr = []
            for j in range(3):
                arr.append(int(input()))
            custom_puzzle.append(arr)
            
        chooseAlgorithm(custom_puzzle)
    

def chooseAlgorithm(puzzle):
    algorithm = input("Select an algorithm:\n1. Uniform Cost Search\n2. Misplaced Tile Heuristic"
                      + "\n3. Manhattan Distance Heuristic\n")
    if algorithm == "1":
        print("You chose: Uniform Cost Search")
        uniformCostSearch(puzzle, 0)
    elif algorithm == "2":
        print("You chose: Misplaced Tile Heuristic Search")
        # misplacedTileSearch(puzzle)
    elif algorithm == "3":
        print("You chose: Manhattan Distance Heuristic Search")
        # manhattanSearch(puzzle)

driverCode()
#generalSearch(very_easy, solved, p_queue)
