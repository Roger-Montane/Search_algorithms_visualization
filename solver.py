import pygame
from constants import *
import Queue
import algorithm_visualizer


def print_path(parent, goal, start, grid):
    path = [goal]

    # trace the path back till we reach start
    while goal != start:
        goal = parent[goal]
        path.insert(0, goal)
    for room in path:
        grid[room[0]][room[1]] = FINAL_PATH


def solver(algorithm, grid, start, finish):
    if algorithm == 'BFS':
        # FIFO
        ds = Queue.Queue()
    elif algorithm == 'DFS':
        # STACK
        ds = Queue.LifoQueue()
    elif algorithm == 'UCS':
        # PRIO
        ds = Queue.PriorityQueue()
    elif algorithm == 'IDS':
        # STACK
        ds = Queue.LifoQueue()
    elif algorithm == 'GREEDY':
        # PRIO
        ds = Queue.PriorityQueue()
    elif algorithm == 'ASTAR':
        # PRIO
        ds = Queue.PriorityQueue()
    else:
        print("No algorithm selected")
        return;


    print("START = ", start)
    print("FINISH = ", finish)
    ds.put(start)

    visited = set()
    finalPath = set()
    prevQueueSize = 0

    #redraw_window(grid)

    if algorithm == 'DFS' or algorithm == 'BFS' or algorithm == 'UCS':
        flag = False
        parent = {}
        parent[start] = start
        while not ds.empty():
            room = ds.get()
            #redraw_window(grid)

            for d in ((room[0], room[1]-1), (room[0]-1, room[1]-1), (room[0]-1, room[1]), (room[0]-1, room[1]+1),
                        (room[0], room[1]+1), (room[0]+1, room[1]+1), (room[0]+1, room[1]), (room[0]+1, room[1]-1)):
                #redraw_window(grid)
                newRoom = d
                #print(newRoom)

                if newRoom[0] < 0 or newRoom[0] >= SQUARES or newRoom[1] < 0 or newRoom[1] >= SQUARES:
                    pass
                elif room == finish:
                    flag = True
                    print(room)
                    # PRINT PATH ??
                    parent[newRoom] = room
                    #print(parent)
                    print_path(parent, room, start, grid)
                    grid[room[0]][room[1]] = FINISH
                    grid[start[0]][start[1]] = FINISH
                    print("DONE !!!")
                    return;
                elif newRoom not in visited and grid[newRoom[0]][newRoom[1]] != WALL:
                    visited.add(newRoom)
                    grid[newRoom[0]][newRoom[1]] = VISITED
                    parent[newRoom] = room
                    ds.put(newRoom)

        if flag == False:
            print("NO SOLUTION FOUND !!!")
            grid[start[0]][start[1]] = START

            #redraw_window(grid)

    elif algorithm == 'IDS':
        flag = False
        parent = {}
        parent[start] = start
        while not ds.empty():
            room = ds.get()
            #redraw_window(grid)

            if room == finish:
                flag = True
                print(room)
                # PRINT PATH ??
                parent[newRoom] = room
                #print(parent)
                print_path(parent, room, start, grid)
                grid[room[0]][room[1]] = FINISH
                grid[start[0]][start[1]] = FINISH
                print("DONE !!!")
                return;
            ###########################################################

            iterations = 1
            for x in range(iterations):
                for d in ((room[0], room[1]-1), (room[0]-1, room[1]-1), (room[0]-1, room[1]), (room[0]-1, room[1]+1),
                            (room[0], room[1]+1), (room[0]+1, room[1]+1), (room[0]+1, room[1]), (room[0]+1, room[1]-1)):
                    #redraw_window(grid)
                    newRoom = d
                    #print(newRoom)

                    if newRoom[0] < 0 or newRoom[0] >= SQUARES or newRoom[1] < 0 or newRoom[1] >= SQUARES:
                        pass
                    elif newRoom not in visited and grid[newRoom[0]][newRoom[1]] != WALL:
                        visited.add(newRoom)
                        grid[newRoom[0]][newRoom[1]] = VISITED
                        parent[newRoom] = room
                        ds.put(newRoom)
                iterations += 1

        if flag == False:
            print("NO SOLUTION FOUND !!!")
            grid[start[0]][start[1]] = START

            #redraw_window(grid)

    elif algorithm == 'GREEDY':
        # while not DATASTRUCTURE empty:
            # do everything
        pass
    
    elif algorithm == 'ASTAR':
        # while not DATASTRUCTURE empty:
            # do everything
        pass