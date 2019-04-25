import time

class Maze(object):
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
    
    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if ((r, c) == self.location) or (((r,c) in visited) == 1):
                    print '*',
                else:
                    print self.grid[r][c],
            print
        print

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        curList = list();
        curL = tuple(self.location)
        curLx = curL[0]
        curLy = curL[1]
        # Possible moves will be:
        posMoves = (
            (curLx - 1, curLy),
            (curLx, curLy - 1),
            (curLx, curLy + 1),
            (curLx + 1, curLy)
            )
        # Get possible moves and add them to the stack
        for i in range (0, len(posMoves)):
            move = posMoves[i]
            r = move[0]
            c = move[1]
            # If a grid is not an obstacle 'X', it is a possible move.
            if self.grid[r][c] != 'X':
                stack.append(posMoves[i])
                curList.append(posMoves[i])
        print "Visit: "+str(self.location)+" Possible moves are: "+str(curList)
        print "Stack: "+str(stack)+"\n\n"
        # Select last move in stack and visit first, if it's not destination
        length = len(stack) # Get length of stack; used to reference last object in stack
        destination = (19, 18)
        if (str(move) != str(destination)):
            if (length != 0 ):
                least = length - 1
                move = stack[least]
                self.neighbor(move)
        else:
            print "Visit: "+str(move)
            print "HURRAY!!! AGENT FOUND THE GOAL!"
            visited.append(move)
    
    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        #Function to pop stack after move has been visited.
        def popStack():
            stack.pop()
            least = len(stack) - 1
            move = stack[least]
            self.neighbor(move)

        #Check if move has been visited or not
        if ((move in visited) == 1):
            # If location already visited, get next location from stack
            popStack()
   
        else:
            visited.append(move)
            stack.pop()
            self.location = tuple(move)
            self.moves()
        

class Agent(object):
    """Knows how to find the exit to a maze with DFS."""

    def dfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        print "Ordered path taken by Agent to get to goal: "+str(visited)+"\n"
        print "Total moves to get to goal with DFS: "+str(len(visited))+"\n"

def main():
    """Create a maze, solve it with DFS, and console-animate."""
    
    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1,1))
    global stack
    global visited
    stack = list()
    visited = [(1,1)]
    maze.display()
    maze.moves()

    agent = Agent()
    goal = Maze(grid, (19,18))
    path = agent.dfs(maze, goal)
    goal.display()

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()
