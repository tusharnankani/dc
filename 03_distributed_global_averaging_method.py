'''
Input
1. Agreed upon time
2. Number of Machines
3. Local time of these machines

Calculations
1. Current Skew (of all machines): Current Local Time - Agreed upon time 
2. Calculate Skew after constant units of times * Number of machines

Output
1. Average of all skews for a specific machine
2. Current (latest) - average of skews = Time to be adjusted
'''

def print_time(nodes_data):
    for (node_number, local_time) in nodes_data:
        print(f"Node {node_number}: {local_time}")

def print_skews(skews):
    print("\n--- Skews ---")
    for (item, skew_lst) in skews.items():
        print(f"Node {item}: {skew_lst[-1]}")
    print()

def mean(lst):
    return (sum(lst) / len(lst))

def adjust_time(nodes_data, skews):
    avg_skews = []
    print("\nCalculated Skews for all iterations")
    for (node_number, skews_lst) in skews.items():
        print(f"Node {node_number}: {skews_lst}")
        avg_skews.append((node_number, mean(skews_lst)))
    
    print('\nAverage Skews Computed:')
    for (node_number, avg) in avg_skews:
        print(f'Node {node_number} : {avg} ', end='')

        status = 'ahead' if avg >= 0 else 'behind'
        print(f'(Node {node_number} is {abs(avg)} units {status})')

        print()
        
    # creating a dict for directly accessing average later
    avg_skews_dict = {node_number: avg for (node_number, avg) in avg_skews}
    print(avg_skews_dict.items())

    new_data = []
    for (node_number, local_time) in nodes_data:
        new_data.append((node_number, local_time - avg_skews_dict[node_number]))

    print("\nFinal Adjusted Time")
    print_time(new_data)

def DGA(nodes_data, agreed_time):
    # dict() => number: list => node_number: [calculated skews at every iteration]
    skews = {}
    total_nodes = len(nodes_data)
    for i in range(total_nodes):
        skews[i] = []

    for i in range(total_nodes):

        print(f"\nCurrent Node {nodes_data[i][0]}: {nodes_data[i][1]}")
        time_to_resync = agreed_time - nodes_data[i][1]

        print(f"--- After {time_to_resync} ---")

        new_data = []
        
        for (node_number, local_time) in nodes_data:
            local_time = local_time + time_to_resync
            new_data.append((node_number, local_time))
        
        nodes_data = new_data
        print_time(nodes_data)

        for (node_number, local_time) in nodes_data:
            skews[node_number].append(local_time - agreed_time)
        
        print_skews(skews)

        print(f"Current Sender who sends broadcast resync: Node {nodes_data[i][0]}")
        print("______________________________________________________________________")

    adjust_time(nodes_data, skews)


if __name__ == "__main__":
    agreed_time = int(input("Enter the Agreed upon time for resync: "))
    total_nodes = int(input("Enter the number of nodes on the network: "))
    local_time_of_nodes = [int(input(f"Enter the local time of node {x}: ")) for x in range(total_nodes)]
    
    # [list] of (tuples) 
    nodes_data = [(node_number, local_time) for (node_number, local_time) in zip(range(total_nodes), local_time_of_nodes)]
    
    # Sort in descending order; according to the local time (second item in the tuple)
    nodes_data = sorted(nodes_data, key=lambda x:x[1], reverse=True)

    print("----- Current Time -----")
    print_time(nodes_data)

    DGA(nodes_data, agreed_time)



'''
$ py "03_distributed_global_averaging method.py"
Enter the Agreed upon time for resync: 40
Enter the number of nodes on the network: 5
Enter the local time of node 0: 15
Enter the local time of node 1: 9
Enter the local time of node 2: 25
Enter the local time of node 3: 36
Enter the local time of node 4: 2
----- Current Time -----
Node 3: 36
Node 2: 25
Node 0: 15
Node 1: 9
Node 4: 2

Current Node 3: 36
--- After 4 ---
Node 3: 40
Node 2: 29
Node 0: 19
Node 1: 13
Node 4: 6

--- Skews ---
Node 0: -21
Node 1: -27
Node 2: -11
Node 3: 0
Node 4: -34

Current Sender who sends broadcast resync: Node 3
______________________________________________________________________

Current Node 2: 29
--- After 11 ---
Node 3: 51
Node 2: 40
Node 0: 30
Node 1: 24
Node 4: 17

--- Skews ---
Node 0: -10
Node 1: -16
Node 2: 0
Node 3: 11
Node 4: -23

Current Sender who sends broadcast resync: Node 2
______________________________________________________________________

Current Node 0: 30
--- After 10 ---
Node 3: 61
Node 2: 50
Node 0: 40
Node 1: 34
Node 4: 27

--- Skews ---
Node 0: 0
Node 1: -6
Node 2: 10
Node 3: 21
Node 4: -13

Current Sender who sends broadcast resync: Node 0
______________________________________________________________________

Current Node 1: 34
--- After 6 ---
Node 3: 67
Node 2: 56
Node 0: 46
Node 1: 40
Node 4: 33

--- Skews ---
Node 0: 6
Node 1: 0
Node 2: 16
Node 3: 27
Node 4: -7

Current Sender who sends broadcast resync: Node 1
______________________________________________________________________

Current Node 4: 33
--- After 7 ---
Node 3: 74
Node 2: 63
Node 0: 53
Node 1: 47
Node 4: 40

--- Skews ---
Node 0: 13
Node 1: 7
Node 2: 23
Node 3: 34
Node 4: 0

Current Sender who sends broadcast resync: Node 4
______________________________________________________________________

Calculated Skews for all iterations
Node 0: [-21, -10, 0, 6, 13]
Node 1: [-27, -16, -6, 0, 7]
Node 2: [-11, 0, 10, 16, 23]
Node 3: [0, 11, 21, 27, 34]
Node 4: [-34, -23, -13, -7, 0]

Average Skews Computed:
Node 0 : -2.4 (Node 0 is 2.4 units behind)

Node 1 : -8.4 (Node 1 is 8.4 units behind)

Node 2 : 7.6 (Node 2 is 7.6 units ahead)

Node 3 : 18.6 (Node 3 is 18.6 units ahead)

Node 4 : -15.4 (Node 4 is 15.4 units behind)

dict_items([(0, -2.4), (1, -8.4), (2, 7.6), (3, 18.6), (4, -15.4)])

Final Adjusted Time
Node 3: 55.4
Node 2: 55.4
Node 0: 55.4
Node 1: 55.4
Node 4: 55.4
'''
