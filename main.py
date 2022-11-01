import heapq
from copy import copy, deepcopy

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

impossible = [[0, 7, 2],
              [4, 6, 1],
              [3, 5, 8]]

# the goal state of the 8 puzzle 
solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]


class Node:
    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle
        self.misplaced_tiles = 0
        self.moves = 0
        
    def solved(self) -> bool:
        return (self.puzzle == solved and self.misplaced_tiles == 0)
    
    def __lt__(self, other):
        return (self.misplaced_tiles < other.misplaced_tiles)
    
    
def setEmptyTilePosition(puzzle):
    for i in range(3):
        for j in range(3):
            if (puzzle[i][j] == 0):
                return [i, j]
            
            
def moveUp(initial_node, empty_tile):
    if (empty_tile[0] is not 0):
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x-1][empty_y]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x-1][empty_y] = 0
        # set new empty tile position
        # calculate heuristic
        

def moveDown(initial_node, empty_tile):
    if (empty_tile[0] is not 2):
        temp_puzzle = deepcopy(initial_node.puzzle)
        empty_x = empty_tile[0]
        empty_y = empty_tile[1]
        shifted = temp_puzzle[empty_x+1][empty_y]
        temp_puzzle[empty_x][empty_y] = shifted
        temp_puzzle[empty_x+1][empty_y] = 0
        # set new empty tile position
        # calculate heuristics

  
def uniformCostSearch(puzzle, heuristic):
    root = Node(puzzle)
    empty_tile_pos = setEmptyTilePosition(root.puzzle)
    p_queue = []
    heapq.heappush(p_queue, root)
    num_expanded_nodes = 0
    max_queue_len = 0
    
    puzzle_states = []
    puzzle_states.append(puzzle)
    
    while (len(p_queue) > 0):
        max_queue_len = max(len(p_queue), max_queue_len)
        head_node = heapq.heappop(p_queue)
        
        if (head_node.solved()):
            while (len(puzzle_states) > 0):
                printPuzzle(puzzle_states.pop())
            
            print("Number of nodes expanded: ", num_expanded_nodes)
            print("Max queue size: ", max_queue_len)
            return head_node
        else:
            printPuzzle(head_node.puzzle)
            print("Expanding")
            num_expanded_nodes+=1
            empty_tile_pos = setEmptyTilePosition(head_node.puzzle)
            # compute movements here to create 
            puzzle_states.append(head_node.puzzle)
          

    
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
    
    
# main driver code for the program
def main():
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
        elif difficulty == "5":
            print("Difficulty of 'impossible' selected.")
            default_puzzle = impossible
            
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
    
    
# ask the user which algorithm to use to solve the puzzle
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

main()
