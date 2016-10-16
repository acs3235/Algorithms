##find the shortest path from the top-left corner to the bottom right corner.

import Queue

maze = [[0, 1, 0, 0, 0],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 1, 0]]


def get(matrix,position):
    number = matrix
    for element in position:
        number = number[element]
    
    return number

def put(matrix,position,entry):
    matrix[position[0]][position[1]] = entry

def traverse_maze(maze):
    q = Queue.Queue()
    
    sp = [0, 0]
    
    q.put(sp)
    
    m = len(maze)
    n = len(maze[0])
    
    dimensions = [m,n]
    
    visited = [[None] * n for i in range(m)]
    put(visited,sp,"start")
    
    ep = [m-1, n-1]
    
    
    path = findPath(q,ep,maze,visited,dimensions)
    print path
    

def findPath(q,ep,maze,visited,dimensions):
    node = q.get()
    for i,direction in enumerate(node):
        
        newnode1 = list(node)
        newnode1[i] = newnode1[i] + 1
        
        if newnode1 == ep:
            print "found it!!"
            final_list = [newnode1]
            while get(visited,node) != "start":
                final_list.append(node)
            
                node = get(visited,node)
            final_list.append(node)
            return final_list
                
            
        
        if newnode1[i] < dimensions[i] and get(visited,newnode1) == None and get(maze,newnode1) != 1:
            put(visited,newnode1,node)
            q.put(newnode1)
            
        newnode2 = list(node)
        newnode2[i] = newnode2[i] - 1
        
        if newnode2 == ep:
            print "found it!"
            final_list = [newnode1]
            while get(visited,node) != "start":
                final_list.append(node)
            
                node = get(visited,node)
            final_list.append(node)
            return final_list
        
        if newnode2[i] >=0 and get(visited,newnode2) == None and get(maze,newnode2) != 1:
            put(visited,newnode2,node)
            q.put(newnode2)
        
    return findPath(q,ep,maze,visited,dimensions)
    
traverse_maze(maze)