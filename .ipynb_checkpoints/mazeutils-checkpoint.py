# Modified from https://github.com/davecom/ClassicComputerScienceProblemsInPython
# Mostly clearing out type hints and comments
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from typing import NamedTuple
import random

class Cell:
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"
    
class MazeLocation(NamedTuple):
    row: int
    column: int
    
class Maze:
    def __init__(self, rows = 10, columns = 10, sparseness = 0.2, start = MazeLocation(0, 0), goal = MazeLocation(9, 9)):
        self.rows = rows
        self.columns = columns
        self.start = start
        self.goal = goal
        self.grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self.randomly_fill(rows, columns, sparseness)
        self.grid[start.row][start.column] = Cell.START
        self.grid[goal.row][goal.column] = Cell.GOAL
        
    def randomly_fill(self, rows, columns, sparseness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1) < sparseness:
                    self.grid[row][column] = Cell.BLOCKED
                
    def __str__(self):
        output = ''
        for row in self.grid:
            output += "".join([c for c in row]) + "\n"
        return output
    
    
    def goal_test(self, m1):
        return m1 == self.goal
    
    def successors(self, m1):
        locations = []
        
        if m1.row + 1 < self.rows and self.grid[m1.row + 1][m1.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row + 1, m1.column))
        if m1.row - 1 >= 0 and self.grid[m1.row - 1][m1.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row - 1, m1.column))
        if m1.column + 1 < self.columns and self.grid[m1.row][m1.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row, m1.column + 1))
        if m1.column - 1 >= 0 and self.grid[m1.row][m1.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row, m1.column - 1))
        return locations
    
    
    def mark(self, path):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL
        
    def clear(self, path):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self.grid[self.start.row][self.start.column] = Cell.START
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL
    
from math import sqrt
def euclidean_dist(goal):
    def distance(m1):
        xdist = m1.column - goal.column
        ydist = m1.row - goal.row
        return sqrt((xdist)**2 + (ydist)**2)
    return distance