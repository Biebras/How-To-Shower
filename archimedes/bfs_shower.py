from archimedes import Archimedes

def clean_body_bfs():
    arch = Archimedes()

    #init visited cells to False
    visited = {}
    for col in range(arch.colCount):
        for row in range(arch.rowCount):
            visited[(row, col)] = False
    
    start_pos = (5, 55)
    
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
    
    return arch
    
arch = clean_body_bfs()
arch.generate_video("bfs_arch.mp4")