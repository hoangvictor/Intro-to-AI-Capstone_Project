from data_preparation import *
from Astar_analysis import *
from GreedyBFS_analysis import *
from UCS_analysis import *

#---------------------------Comparison of frontier definitions---------------------------------------------
#------------------A_star--------------------
print("Comparison of frontier definitions - Astar")
#List (with timsort)
print("List (with timsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = Astar_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'
if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'Astar - ' + parameters['frontier_type'] + ' - result.pkl'

with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Priority queue (with heapsort)
print("Priority queue (with heapsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'priority_queue',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}

analysis_results = Astar_analysis(data, parameters)

# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'Astar - ' + parameters['frontier_type'] + ' - result.pkl'

with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#------------Greedy BFS------------
print("Comparison of frontier definitions - GreedyBFS")
#List (with timsort)
print("List (with timsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = GreedyBFS_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'GreedyBFS - ' + parameters['frontier_type'] + ' - result.pkl'

with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Priority queue (with heapsort)
print("Priority queue (with heapsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'priority_queue',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}

analysis_results = GreedyBFS_analysis(data, parameters)

# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'GreedyBFS - ' + parameters['frontier_type'] + ' - result.pkl'

with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#-----------UCS--------------
print("Comparison of frontier definitions - UCS")
#List (with timsort)
print("List (with timsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = UCS_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'
if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'UCS - ' + parameters['frontier_type'] + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Priority queue (with heapsort)
print("Priority queue (with heapsort)")
parameters = {
    'img_size': img_size,
    'frontier_type': 'priority_queue',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = UCS_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_frontier_definitions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'UCS - ' + parameters['frontier_type'] + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)


#-------------------Influence of standard deviation to the running time------------------------
print("Influence of standard deviation to the running time")
#---------A_star---------
print("A-star")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = Astar_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_different_algorithms'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'Astar - ' + parameters['frontier_type'] + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#--------Greedy BFS-------
print("Greedy BFS")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = GreedyBFS_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_different_algorithms'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'GreedyBFS - ' + parameters['frontier_type'] + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#----------UCS-------------
print("UCS")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100
}
analysis_results = UCS_analysis(data, parameters)
# Save the data
tmp_path = path + '/comparison_of_different_algorithms'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'UCS - ' + parameters['frontier_type'] + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)


img_size = [img_size[2], img_size[4]] # From now, only image size 25 and 50 are considered

#----------------------------------Comparison of heuristic functions--------------------------------------
print("Comparison of heuristic functions")
#Tie-breaking High g-cost
print("Tie-breaking High g-cost")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'tie_breaking_high_g_cost',
    'num_points': 100,
    'delta': 0.01 # Change delta here
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/heuristic_functions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'tie-breaking-high-g-cost - ' + ' delta = ' + str(parameters['delta']) + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Variance of Tie-breaking High g-cost
print("Variance of Tie-breaking High g-cost")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'var_tie_breaking_high_g_cost',
    'num_points': 100,
    'delta': 0.01 # Change delta here
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/heuristic_functions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'variance-of-tie-breaking-high-g-cost - ' + ' delta = ' + str(parameters['delta']) + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Tie-breaking Low g-cost
print("Tie-breaking Low g-cost")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'tie_breaking_low_g_cost',
    'num_points': 100,
    'delta': 0.01 # Change delta here
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/heuristic_functions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'tie-breaking-low-g-cost - ' + ' delta = ' + str(parameters['delta']) + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Variance of Tie-breaking Low g-cost
print("Variance of Tie-breaking Low g-cost")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'var_tie_breaking_low_g_cost',
    'num_points': 100,
    'delta': 0.01 # Change delta here
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/heuristic_functions'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'variance-of-tie-breaking-low-g-cost - ' + ' delta = ' + str(parameters['delta']) + ' - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)


#----------------------------------Finding neighbours methods-------------------------------
print("Finding neighbours methods")
#Find while running
print("Find while running")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_while_running',
    'heuristic_type': 'manhattan',
    'num_points': 100,
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/find_neighbors'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'find_while_running - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)

#Find first before run
print("Find first before run")
parameters = {
    'img_size': img_size,
    'frontier_type': 'list',
    'finding_neighbors': 'find_first_before_run',
    'heuristic_type': 'manhattan',
    'num_points': 100,
}
analysis_results = Astar_analysis(data, parameters) # Use only Astar
# Save the data
tmp_path = path + '/find_neighbors'

if os.path.exists(tmp_path) == False:
    os.mkdir(tmp_path)

tmp_path = tmp_path + '/' + 'find_first_before_run - result.pkl'
with open(tmp_path, 'wb') as f:
    pickle.dump(analysis_results, f)
