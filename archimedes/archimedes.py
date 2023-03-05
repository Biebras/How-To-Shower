#%%
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.set_printoptions(threshold=np.inf)

class Archimedes:
    def __init__(self):
        self.imagePath = "../artwork/archimedes.png"
        self.clean_color = [194, 161, 126, 255]
        self.dirty_color = [51, 45, 61, 255]
        self.empty_color = [255, 255, 255, 255]
        self.image = Image.open(self.imagePath)
        self.body = np.array(self.image)
        self.rowCount = self.body.shape[0]
        self.colCount = self.body.shape[1]
        self.start_pos = (5, 66)
        
    def get_start(self):
        return self.start_pos
        
    def clean_skin(self, row, col):
        if self.is_skin(row, col) == False:
            print("Can't clean not skin")
            return False
        
        self.body[row][col] = self.clean_color
        return True
        
    def is_skin(self, row, col):
        if np.array_equal(self.body[row][col], self.empty_color):
            return False
        
        return True
    
    def get_skin_neighbors(self, row, col):
        neighbors = []
        
        if row > 0 and self.is_skin(row-1, col):
            neighbors.append((row-1, col))
            
        if row < self.rowCount-1 and self.is_skin(row+1, col):
            neighbors.append((row+1, col))
            
        if col > 0 and self.is_skin(row, col-1):
            neighbors.append((row, col-1))
            
        if col < self.colCount-1 and self.is_skin(row, col+1):
            neighbors.append((row, col+1))
            
        return neighbors
        
    def draw(self):
        plt.imshow(self.body)
        

def clean_body_bfs():
    fig, ax = plt.subplots()
    arch = Archimedes()
    ims = []
    
    #init visited cells to False
    visited = {}
    for col in range(arch.colCount):
        for row in range(arch.rowCount):
            visited[(row, col)] = False
    
    start_pos = arch.get_start()
    
    queue = []
    queue.append(start_pos)
    visited[start_pos] = True
    
    while queue:
        start = queue.pop(0)
        arch.clean_skin(start[0], start[1])
        
        for neighbour in arch.get_skin_neighbors(start[0], start[1]):
            pos = (neighbour[0], neighbour[1])
            if visited[pos] == False:
                queue.append(pos)
                visited[pos] = True
                
        im = ax.imshow(arch.body, animated=True)
        ims.append([im])
                
    arch.draw()
    
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)
    
    writer = animation.FFMpegWriter(
    fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("movie.mp4", writer=writer)

    
clean_body_bfs()
    
    

# %%
