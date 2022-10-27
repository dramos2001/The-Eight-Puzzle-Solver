import heapq

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


# function to calcualte the total number of misplaced tiles in the puzzle
# this number equates to g in the heuristic function   
# to be used for manhattan and misplaced tile heuristics     
def calculateMisplacedTiles(puzzle, goal) -> int:
    count = 0
    for i in range(3):
        for j in range(3):
            if ((puzzle[i][j] != goal[i][j]) and (puzzle[i][j])):
                count+=1
                
    return count
            
# print the n x n puzzle in its entirety            
def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])
    print('\n')
    
    
p_queue = []
g = calculateMisplacedTiles(easy, solved)
print(g)
root = Node(None, easy, g, 0)
heapq.heappush(p_queue, root)
printPuzzle(easy)
