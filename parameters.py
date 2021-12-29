import numpy as np

#------------------------------------------ Node definition -----------------------------------------
class Node():
    # Node initialization
    def __init__(self, position):
        self.position = position # Tuple (x,y)
        self.g = 0 # g-cost
        self.h = 0 # h-cost
        self.f = None # f-cost
        self.parent = None # Parent node

    # Print the node
    def __str__(self):
        return str(self.position)

    # Equality of 2 nodes (position)
    def __eq__(self, other):
        return self.position == other.position

    # Less than
    def __lt__(self, other):
        return self.f < other.f

    # Greater than
    def __gt__(self, other):
        return self.f > other.f


#---------------------------------------Heuristic functions-------------------------------------------
# Manhattan distance
def manhattan(actual_node, start_node ,goal_node, delta):
    actualPos = actual_node.position
    endPos = goal_node.position
    return abs(actualPos[0] - endPos[0]) + abs(actualPos[1] - endPos[1])

# There are many states with the same f-cost, and we have to choose the order in which to expand them.
# For tie_breaking_high_g_cost, we preferred states closer to the goal node than the goal state.
def tie_breaking_high_g_cost(actual_node, start_node, goal_node, delta = 0.001):
    actualPos = actual_node.position
    endPos = goal_node.position
    return manhattan(actual_node, start_node, goal_node, delta) * (1 + delta)

# Variance of tie breaking high g-cost, we vary the value of delta in tie_breaking_high_g_cost, according
# to the position of the actual node
def var_tie_breaking_high_g_cost(actual_node, start_node, goal_node, delta = 0.001):
    actualPos = actual_node.position
    endPos = goal_node.position
    rate1 = manhattan(actual_node, start_node, goal_node, delta)
    rate2 = manhattan(start_node, start_node, goal_node, delta)
    return rate1 * (1 + delta* (0.5 + rate1/rate2))

# There are many states with the same f-cost, and we have to choose the order in which to expand them.
# For tie_breaking_low_g_cost, we preferred states closer to the start node than the goal state.
def tie_breaking_low_g_cost(actual_node, start_node, goal_node, delta = 0.001):
    actualPos = actual_node.position
    endPos = goal_node.position
    return manhattan(actual_node, start_node, goal_node, delta) * (1 - delta)

# Variance of tie breaking low g-cost, we vary the value of delta in tie_breaking_low_g_cost, according
# to the position of the actual node
def var_tie_breaking_low_g_cost(actual_node, start_node, goal_node, delta = 0.001):
    actualPos = actual_node.position
    endPos = goal_node.position
    rate1 = manhattan(actual_node, start_node, goal_node, delta)
    rate2 = manhattan(start_node, start_node, goal_node, delta)
    return rate1 * (1 + delta * (1.5 - rate1/rate2))

# Heuristics dictionary containing all kinds of heuristic functions
heuristics = {
    'manhattan': manhattan,
    'tie_breaking_high_g_cost': tie_breaking_high_g_cost,
    'var_tie_breaking_high_g_cost': var_tie_breaking_high_g_cost,
    'tie_breaking_low_g_cost': tie_breaking_low_g_cost,
    'var_tie_breaking_low_g_cost': var_tie_breaking_low_g_cost
}


#----------------------------------------- Finding neighbors ----------------------------------------
# Finding while runing
def next_pos_list(array, actual_node, img_shape, theta):
    '''
    array: array of height value
    actual_node: node object of the actual node that you want to find its neighbors
    img_shape: tuple(x_size, y_size) - size of the image
    theta: maximum distance of heigh between 2 consecutive positions
    '''
    res = []
    x_size, y_size = img_shape
    actualPos = actual_node.position
    actual_nodeValue = array[actualPos[0]][actualPos[1]]

    # Conditions checking for neighbors
    if actualPos[0] + 1 < x_size and abs(actual_nodeValue - array[actualPos[0] + 1][actualPos[1]]) <= theta:
        res.append((actualPos[0] + 1, actualPos[1]))
    if actualPos[1] + 1 < y_size and abs(actual_nodeValue - array[actualPos[0]][actualPos[1] + 1]) <= theta:
        res.append((actualPos[0], actualPos[1] + 1))
    if actualPos[0] - 1 >= 0 and abs(actual_nodeValue - array[actualPos[0] - 1][actualPos[1]]) <= theta:
        res.append((actualPos[0] - 1, actualPos[1]))
    if actualPos[1] - 1 >= 0 and abs(actual_nodeValue - array[actualPos[0]][actualPos[1] - 1]) <= theta:
        res.append((actualPos[0], actualPos[1] - 1))

    return res


# Find neighbors first before run
def make_grid(array, img_shape, theta):
    '''
    array: array of height value
    img_shape: tuple(x_size, y_size) - size of the image
    theta: maximum distance of heigh between 2 consecutive positions
    '''
    grid = [[None for j in range(len(array))] for i in range(len(array))]
    x_size, y_size = img_shape

    for i in range(len(array)):
        for j in range(len(array)):
            res = []
            actual_nodeValue = int(array[i][j])

            # Conditions checking for neighbors
            if i + 1 < x_size and abs(actual_nodeValue - int(array[i + 1][j])) <= theta:
                res.append((i + 1,j))
            if j + 1 < y_size and abs(actual_nodeValue - int(array[i][j + 1])) <= theta:
                res.append((i,j + 1))
            if i - 1 >= 0 and abs(actual_nodeValue - int(array[i - 1][j])) <= theta:
                res.append((i - 1,j))
            if j - 1 >= 0 and abs(actual_nodeValue - int(array[i][j - 1])) <= theta:
                res.append((i,j - 1))
            grid[i][j] = res # grid[i][j] contains a list of points which can be the neighbors of the point at position (i,j)

    return grid


#----------------------------------------- Data initialization ----------------------------------------
# Random the position of node
def init(size):
    start_node = (np.random.randint(0,size), np.random.randint(0,size))
    goal_node = (np.random.randint(0,size), np.random.randint(0,size))
    return start_node, goal_node

# Create a list of n pairs of nodes
def random_initialization(n, size):
    return [init(size) for i in range(n)]

#-------------------------------------- Analysis initialization -------------------------------------
# Define the class containing our analysis results
class AnalysisResults:
    def __init__(self, size):
        self.size = size # Size of image

        # Dictionary of average run time and average steps_count, for example:
        # avg_run_time[(0,0.5)] returns the average run time of image inside the
        # bin of standard deviation from 0 to 0.5
        self.avg_run_time = {}
        self.avg_steps_count = {}
