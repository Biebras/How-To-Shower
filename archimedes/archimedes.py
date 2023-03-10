#%%
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

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
        self.frames = []
        
    def record_frame(self):
        self.frames.append(np.array(self.body))
        
    def clean_skin(self, row, col):
        if self.is_skin(row, col) == False:
            print("Can't clean not skin")
            return False
        
        self.body[row][col] = self.clean_color
        self.record_frame()
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
        
    def generate_video(self, filename):
        width = self.colCount
        height = self.rowCount
        fps = 5000
        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        for frame in self.frames:
            frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST)
            out.write(frame)

        out.release()
    
    

# %%
