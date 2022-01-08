from PIL import Image  # work with images
import numpy as np
import queue
import os
import pygame
import time

file_name = "Mars_MGS_MOLA_DEM.jpg"  # The name of the file we want to save
img = Image.open(file_name)  # Open our saved file above
img = img.convert("L")  # Convert to one channel grey image
img_array = np.asarray(img)  # Convert the image to an array
img_array = img_array.astype('int32')
img = img_array[3000:3050, 3000:3050].astype('float64')

WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


class Node:
    length = len(img)

    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.height = img[col][row]
        self.g = float('inf')
        self.f = float('inf')
        self.parent = None

    def get_position(self):
        return self.row, self.col

    def is_neighbor(self, other, gradient):
        return abs(self.height - other.height) <= gradient

    def get_neighbors(self, grid, gradient):
        if self.row < Node.length - 1 and self.is_neighbor(grid[self.row + 1][self.col], gradient):
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and self.is_neighbor(grid[self.row - 1][self.col], gradient):
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < Node.length - 1 and self.is_neighbor(grid[self.row][self.col + 1], gradient):
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and self.is_neighbor(grid[self.row][self.col - 1], gradient):
            self.neighbors.append(grid[self.row][self.col - 1])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width))


# Manhattan distance
def manhattan(node, goal):
    x_node, y_node = node.get_position()
    x_goal, y_goal = goal.get_position()
    return abs(x_node - x_goal) + abs(y_node - y_goal)

# There are many states with the same f-cost, and we have to choose the order in which to expand them.
# For tie_breaking_high_g_cost, we preferred states closer to the goal node than the goal state.


def tie_breaking_high_g_cost(node, goal, delta=0.1):
    x_node, y_node = node.get_position()
    x_goal, y_goal = goal.get_position()
    return manhattan(node, goal) * (1 + delta)

# There are many states with the same f-cost, and we have to choose the order in which to expand them.
# For tie_breaking_low_g_cost, we preferred states closer to the start node than the goal state.


def tie_breaking_low_g_cost(node, goal, delta=0.1):
    x_node, y_node = node.get_position()
    x_goal, y_goal = goal.get_position()
    return manhattan(node, goal) * (1 - delta)


def draw_file_name(current, draw):
    while current.parent != None:
        current = current.parent
        current.color = PURPLE
        draw()
    return None


def make_grid(rows, width):
    grid = []
    space = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, space)
            grid[i].append(node)
    return grid


def draw_grid(screen, rows, width):
    space = width // rows
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0, i * space), (width, i * space))
        for j in range(rows):
            pygame.draw.line(screen, GREY, (j * space, 0), (j * space, width))


def draw_main(screen, grid, rows, width):
    pygame.event.get()
    screen.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(screen)
    draw_grid(screen, rows, width)
    pygame.display.update()


def Astar(draw, grid, start, goal, heuristic):
    step = 0
    open_set = queue.PriorityQueue()
    open_set.put((0, step, start))
    start.g = 0
    check = {start}
    while not open_set.empty():
        step += 1
        current = open_set.get()[2]
        check.remove(current)
        if current.get_position() == goal.get_position():
            draw_file_name(goal, draw)
            goal.color = TURQUOISE
            return True
        for neighbor in current.neighbors:
            step += 1
            tmp = current.g + 1
            if tmp < neighbor.g:
                neighbor.parent = current
                neighbor.g = tmp
                neighbor.f = tmp + heuristic(neighbor, goal)
                if neighbor not in check:
                    open_set.put((neighbor.f, step, neighbor))
                    check.add(neighbor)
                    neighbor.color = GREEN
        draw()
        if current != start:
            current.color = RED
    return False


def GreedyBFS(draw, grid, start, goal, heuristic):
    step = 0
    open_set = queue.PriorityQueue()
    open_set.put((0, step, start))
    start.g = 0
    check = {start}
    while not open_set.empty():
        step += 1
        current = open_set.get()[2]
        check.remove(current)
        if current.get_position() == goal.get_position():
            draw_file_name(goal, draw)
            goal.color = TURQUOISE
            return True
        for neighbor in current.neighbors:
            step += 1
            tmp = current.g + 1
            if tmp < neighbor.g:
                neighbor.parent = current
                neighbor.g = tmp
                neighbor.f = heuristic(neighbor, goal)
                if neighbor not in check:
                    open_set.put((neighbor.f, step, neighbor))
                    check.add(neighbor)
                    neighbor.color = GREEN
        draw()
        if current != start:
            current.color = RED
    return False


def UCS(draw, grid, start, goal, heuristic=None):
    step = 0
    open_set = queue.PriorityQueue()
    open_set.put((0, step, start))
    start.g = 0
    check = {start}
    while not open_set.empty():
        step += 1
        current = open_set.get()[2]
        check.remove(current)
        if current.get_position() == goal.get_position():
            draw_file_name(goal, draw)
            goal.color = TURQUOISE
            return True
        for neighbor in current.neighbors:
            step += 1
            tmp = current.g + 1
            if tmp < neighbor.g:
                neighbor.parent = current
                neighbor.g = tmp
                neighbor.f = tmp
                if neighbor not in check:
                    open_set.put((neighbor.f, step, neighbor))
                    check.add(neighbor)
                    neighbor.color = GREEN
        draw()
        if current != start:
            current.color = RED
    return False


def main(screen, width, start, goal, gradient, algorithm, heuristic=manhattan):
    n = len(img)
    grid = make_grid(n, width)
    x_start, y_start = start
    x_goal, y_goal = goal
    run = True

    while run:
        draw_main(screen, grid, n, width)
        start = grid[y_start][x_start]
        start.color = YELLOW
        goal = grid[y_goal][x_goal]
        goal.color = TURQUOISE
        for row in grid:
            for node in row:
                node.get_neighbors(grid, gradient)
        result = algorithm(lambda: draw_main(
            screen, grid, n, width), grid, start, goal, heuristic)

        if result == True:
            time.sleep(3)
            run = False
    pygame.quit()


start = (1, 0)
goal = (49, 49)
gradient = 1  # Take 1 for see the big difference between heuristic functions for low version of Astar

WIDTH = 600  # Window width


def Astar_manhattan_distance():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Manhattan distance - low version of Astar")
    main(screen, WIDTH, start, goal, gradient, Astar, manhattan)


def Astar_Tie_breaking_High_g_cost():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(
        "Tie-breaking High g-cost - low version of Astar")
    main(screen, WIDTH, start, goal, gradient, Astar, tie_breaking_high_g_cost)


def Astar_Tie_breaking_Low_g_cost():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(
        "Tie-breaking Low g-cost - low version of Astar")
    main(screen, WIDTH, start, goal, gradient, Astar, tie_breaking_high_g_cost)


def GreedyBFS_visualization():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("GreedyBFS")
    main(screen, WIDTH, start, goal, gradient, GreedyBFS)


def UCS_visualization():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("UCS")
    main(screen, WIDTH, start, goal, gradient, UCS, manhattan)


run1, run2, run3, run4, run5 = (True for i in range(5))

# Change to True if you want to run the visualization
if run1 == False:
    Astar_manhattan_distance()
if run2 == False:
    Astar_Tie_breaking_High_g_cost()
if run3 == False:
    Astar_Tie_breaking_Low_g_cost()
if run4 == False:
    GreedyBFS_visualization()
if run5 == False:
    UCS_visualization()
