import heapq
from multiprocessing import heap
from this import d

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

solved = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

class Node:
    def __init__(self, parent_node, puzzle, misplaced_tiles, moves) -> None:
        self.parent_node = parent_node
        self.puzzle = puzzle
        self.misplaced_tiles = misplaced_tiles
        self.moves = moves


# recreating the general search algorithm that was presented in the slides
def generalSearch(initial, goal, queueing_function):
    g = calculateMisplacedTiles(initial, goal)
    root = Node(None, easy, g, 0)
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
        heapq.heappush(queueing_function, createNewNode(initial, goal, node, queueing_function.moves))
        

def createNewNode(initial_state, goal_state, root_node, moves):
    new_state = initial_state
    g = calculateMisplacedTiles(new_state, goal_state)
    new_node = Node(root_node, new_state, g, moves)
    return new_node
            
    
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
    

p_queue = []

printPuzzle(easy)
generalSearch(easy, solved, p_queue)
