class VacuumWorld:
    def __init__(self, filename):
        self.grid = []
        self.robot_pos = None
        self.dirty_cells = set()
        self.rows = 0
        self.cols = 0
        
        self.load_world(filename)
    
    def load_world(self, filename):
        with open(filename, 'r') as f:
            self.cols = int(f.readline().strip())
            self.rows = int(f.readline().strip())
            
            # read the grid
            self.grid = []
            for r in range(self.rows):
                row = f.readline().strip()
                row_cells = []
                for c in range(self.cols):
                    cell = row[c]
                    row_cells.append(cell)
                    
                    if cell == '@':
                        self.robot_pos = (r, c)
                        row_cells[-1] = '_'  # Replace robot with empty cell in grid
                    elif cell == '*':
                        self.dirty_cells.add((r, c))
                
                self.grid.append(row_cells)
    
    def is_valid_move(self, r, c):
        return (0 <= r < self.rows and 
                0 <= c < self.cols and 
                self.grid[r][c] != '#')
    
    def is_dirty(self, r, c):
        return (r, c) in self.dirty_cells
    
    def display_world(self): 
        display = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                cell = self.grid[r][c]
                row.append(cell)
            display.append(row)
            
        # dirty cells
        for r, c in self.dirty_cells:
            display[r][c] = '*'
            
        # robot
        r, c = self.robot_pos
        display[r][c] = '@'
        
        for row in display:
            print(''.join(row))