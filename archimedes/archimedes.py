#%%
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.set_printoptions(threshold=np.inf)

class Archimedes:
    def __init__(self):
        self.imagePath = "../artwork/archimedes.png"
        self.clean_color = [194, 161, 126]
        self.dirty_color = [51, 45, 61]
        self.empty_color = [255, 255, 255]
        self.image = Image.open(self.imagePath)
        self.image = self.image.convert('RGB')
        self.body = np.array(self.image)
        self.rowCount = self.body.shape[0]
        self.colCount = self.body.shape[1]
        self.start_pos = (5, 55)
        
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
    arch = Archimedes()
    frames = []
    frames.append(np.array(arch.body))
    print(arch.body.shape)
    
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
        frames.append(np.array(arch.body))
        
        for neighbour in arch.get_skin_neighbors(start[0], start[1]):
            pos = (neighbour[0], neighbour[1])
            if visited[pos] == False:
                queue.append(pos)
                visited[pos] = True
    
    #arch.draw()
    frames.append(np.array(arch.body))
    width = arch.colCount
    height = arch.rowCount
    out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 4000, (width, height))

    for frame in frames:
        frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST)
        out.write(frame)

    out.release()
    

    
clean_body_bfs()
    
    

# %%
