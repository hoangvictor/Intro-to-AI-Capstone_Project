from parameters import *
import time
import queue

def GreedyBFS_analysis(data, parameters):        
    #-------------------------------------- 4 different A* algorithms --------------------------------------
    
    def norm_GreedyBFS_list(img_array, start_node, goal_node, img_shape, theta, heuristic):
        steps_count = 0 # Save our number of steps
        visited_nodes = set() # Save our visited nodes
        frontier = [start_node] # Add the start_node to the frontier

        while len(frontier) > 0: # While there is something inside the frontier, continue the algorithm
            
            # Sort the frontier in reverse order, here Python uses timsort
            frontier = sorted(frontier, reverse = True)
            
            # Pop the last node, which has the lowest value of f
            actual_node = frontier.pop()
            
            # Add 1 to steps_count for each time we enter a node
            steps_count += 1 
            
            # Save the temporary g-score of the actual node
            tmp_g_score = actual_node.g
            
            # Return the steps_count for analysis process
            if actual_node == goal_node:
                return steps_count
            
            # Add the position (tuple(x,y)) to visited_node
            visited_nodes.add(actual_node.position)
            
            # Create a list of temporary visited nodes, add these nodes to the frontier after the for loop below 
            tmp_visited_nodes = []

            # Iterate over all neighbors of the actual node
            for next_pos in next_pos_list(img_array, actual_node, img_shape, theta):
                steps_count += 1 # Add 1 for each time we check the next node
                next_node = Node(next_pos) # Create next_node with position next_pos
                
                # If next_pos in visited_nodes, we don't do anything
                if next_pos not in visited_nodes:

                    #f = h + g, update f-score
                    next_node.h = heuristic(next_node, start_node, goal_node, delta) 
                    next_node.f = next_node.h
                    next_node.parent = actual_node

                    # If next_node in frontier
                    if next_node in frontier:
                        idx = frontier.index(next_node) # Find the index of next_node in the frontier
                        
                        # If the f-score of the duplicate node is more than that of the actual next_node
                        if frontier[idx] > next_node: 
                            frontier.remove(next_node) # Remove this next_node in the frontier
                            tmp_visited_nodes.append(next_node) # And append the actual next_node to the frontier
                    else:
                        tmp_visited_nodes.append(next_node) # Append the actual next_node to the frontier
            
            # Add all the nodes inside tmp_visited_nodes into frontier
            frontier += tmp_visited_nodes
        
        # Return the number of steps counted for analysis process
        return steps_count
    
    
    def norm_GreedyBFS_priority_queue(img_array, start_node, goal_node, img_shape, theta, heuristic):
        steps_count = 0 #Save our number of steps
        visited_nodes = set() # Save our visited nodes
        frontier = queue.PriorityQueue()
        frontier.put((0, start_node))

        while frontier.empty() == False:
            actual_node = frontier.get()[1]        
            steps_count += 1 # Add 1 for each time we enter a node
            
            # Save the temporary g-score of the actual node
            tmp_g_score = actual_node.g

            if actual_node == goal_node:
                return steps_count

            visited_nodes.add(actual_node.position)

            # Iterate over all neighbors of the actual node
            for next_pos in next_pos_list(img_array, actual_node, img_shape, theta):
                steps_count += 1 # Add 1 for each time we check the next node
                next_node = Node(next_pos) # Create next_node with position next_pos
                
                # If next_pos in visited_nodes, we don't do anything
                if next_pos not in visited_nodes:

                     #f = h + g
                    next_node.h = heuristic(next_node, start_node, goal_node, delta) 
                    next_node.f = next_node.h
                    next_node.parent = actual_node

                    # Check if there exists a node having the same position as next_node (denoted as duplicate node) 
                    # in the frontier or not
                    if (next_node.f, next_node) in frontier.queue:
                        # Find the index of the duplicate node in the frontier.queue
                        idx = frontier.queue.index((next_node.f, next_node)) 

                        # Check the f-value of the 2 nodes (next_node and the duplicate node in the frontier)
                        if frontier.queue[idx][0] > next_node.f:
                            
                            # Replace the duplicate node by the next_node with lower f-score
                            # Step 1: Create a temporary queue
                            tmp_queue = queue.PriorityQueue()
                            
                            # Step 2: Put all the elements of the frontier to tmp_queue until we find the duplicate node
                            while t != frontier.queue[idx]:
                                t = frontier.get()
                                tmp_queue.put(t)
                            
                            # Step 3: Delete the duplicate node
                            t = frontier.get()
                            
                            # Step 4: Reput all the elements from the tmp_queue to the frontier
                            while tmp_queue.empty() == False:
                                t = tmp_queue.get()
                                frontier.put(t)    
                                
                            frontier.put((next_node.f, next_node)) # Put next_node to frontier
                    else:
                        frontier.put((next_node.f, next_node)) # Put next_node to frontier
        
        # Return the number of steps counted for analysis process
        return steps_count
    
    
    def GreedyBFS_list_with_init(grid, img_array, start_node, goal_node, img_shape, theta, heuristic):    
        steps_count = 0 #Save our number of steps
        visited_nodes = set() # Save our visited nodes
        frontier = [start_node] # Add the start_node to the frontier

        while len(frontier) > 0: # While there is something inside the frontier, continue the algorithm
            
            # Sort the frontier in reverse order, here Python uses timsort
            frontier = sorted(frontier, reverse = True)
            
            # Pop the last node, which has the lowest value of f
            actual_node = frontier.pop()
            
            # Add 1 to steps_count for each time we enter a node
            steps_count += 1 
            
            # Save the temporary g-score of the actual node
            tmp_g_score = actual_node.g
            
            # Return the steps_count for analysis process
            if actual_node == goal_node:
                return steps_count
            
            # Add the position (tuple(x,y)) to visited_node
            visited_nodes.add(actual_node.position)
            
            # Create a list of temporary visited nodes, add these nodes to the frontier after the for loop below 
            tmp_visited_nodes = []

            # Iterate over all neighbors of the actual node
            for next_pos in grid[actual_node.position[0]][actual_node.position[1]]:
                steps_count += 1 # Add 1 for each time we check the next node
                next_node = Node(next_pos) # Create next_node with position next_pos
                
                # If next_pos in visited_nodes, we don't do anything
                if next_pos not in visited_nodes:

                    #f = h + g, update f-score
                    next_node.h = heuristic(next_node, start_node, goal_node, delta) 
                    next_node.f = next_node.h
                    next_node.parent = actual_node

                    # If next_node in frontier
                    if next_node in frontier:
                        idx = frontier.index(next_node) # Find the index of next_node in the frontier
                        
                        # If the f-score of the duplicate node is more than that of the actual next_node
                        if frontier[idx] > next_node: 
                            frontier.remove(next_node) # Remove this next_node in the frontier
                            tmp_visited_nodes.append(next_node) # And append the actual next_node to the frontier
                    else:
                        tmp_visited_nodes.append(next_node) # Append the actual next_node to the frontier
            
            # Add all the nodes inside tmp_visited_nodes into frontier
            frontier += tmp_visited_nodes
        
        # Return the number of steps counted for analysis process
        return steps_count
    
    
    #------------------------------------ Retrieving data from parameters ------------------------------------
    
    #List of image size:
    img_size = parameters['img_size']
    
    #Type of frontier (list or priority_queue)
    frontier_type = parameters['frontier_type']    
    
    #Type of finding neighbors (find_first_before_run or find_while_running   finding_neighbors = parameters['finding_neighbors']
    finding_neighbors = parameters['finding_neighbors']
    
    #Choose GreedyBFS version
    if finding_neighbors == 'find_while_running' and frontier_type == 'list':
        GreedyBFS = norm_GreedyBFS_list 
    elif finding_neighbors == 'find_while_running' and frontier_type == 'priority_queue':
        GreedyBFS = norm_GreedyBFS_priority_queue
    elif finding_neighbors == 'find_first_before_run' and frontier_type == 'list':
        GreedyBFS = GreedyBFS_list_with_init
    
    #Type of heuristic function (manhattan; tie_breaking_high_g_cost)
    global heuristics
    heuristic_type = parameters['heuristic_type'] 
    heuristic = heuristics[heuristic_type]
    
    #Delta for heuristic functions
    delta = 0.001
    if 'delta' in parameters.keys():
        delta = parameters['delta']

    #Number of random starting points and ending points to run analysis
    num_points = parameters['num_points'] 
    
    #-------------------------------------------- Analysis process --------------------------------------------
    # Store the analysis results
    analysis_results = []
    
    # Iterate over all the image size in data.keys()
    for size in data.keys():
        
        # Preparation
        analysis_results.append(AnalysisResults(size)) # Create a new AnalysisResults object and append it to the list
        pair_node_list = random_initialization(num_points, size) # Create a random pair of start node and goal node
        print("Image size: {}".format(size))

        # Run the analysis for loop
        for data_bin_key in data[size].keys():
                
            i = 1
            total_time = 0
            total_steps_count = 0
            num_images = len(data[size][data_bin_key])

            for start_node, goal_node in pair_node_list:
                
                # Create start_node and goal_node objects
                start_node = Node(start_node)
                goal_node = Node(goal_node)

                # Iterate over all image in data[size][data_bin_key], for example if we want to access to the list of
                # images of size 15 inside the data_bin (0,0.5) -> data[15][(0,0.5)]
                for tmp_data in data[size][data_bin_key]:
                    
                    # Different type of analysis for each finding_neighbors algorithm
                    if finding_neighbors ==  'find_first_before_run': 
                        grid = make_grid(tmp_data, (size, size), 2) # Make grid of neighbors first before run the algorithm
                        start_time = time.time()
                        steps_count = GreedyBFS(grid, tmp_data, start_node, goal_node, (size, size), 2, heuristic)
                        running_time = time.time() - start_time # Running time
                    else:
                        start_time = time.time()
                        steps_count = GreedyBFS(tmp_data, start_node, goal_node, (size, size), 2, heuristic)
                        running_time = time.time() - start_time # Running time  
                    
                    total_time += running_time
                    total_steps_count += steps_count

            print("Standard deviation range: {}".format(data_bin_key))
            
            # Average running time
            tmp_avg_run_time = total_time / num_images / num_points
            analysis_results[-1].avg_run_time[data_bin_key] = tmp_avg_run_time
            print("Average running time: {} s.".format(tmp_avg_run_time))

            # Average steps count
            tmp_avg_steps_count = total_steps_count // num_images // num_points
            analysis_results[-1].avg_steps_count[data_bin_key] = tmp_avg_steps_count
            print("Average steps counts: {} steps.".format(tmp_avg_steps_count))
                                         
        print("------------------------------------")
                                         
    return analysis_results