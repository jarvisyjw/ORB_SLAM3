import random

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def modify_edge_ids(edges, min_id, max_id, percentage, magnitude):
    total_edges = len(edges)
    non_adjacent_edges = [ edge for edge in edges
                         if  abs(int(edge.split()[1]) - int(edge.split()[2])) > 1 ]
    
    num_edges_to_modify = int(len(non_adjacent_edges) * percentage)
    print("len of lc edge:",len(non_adjacent_edges),"\nlen of modify lc edge:",num_edges_to_modify)
    selected_indices = random.sample(range(len(non_adjacent_edges)), num_edges_to_modify)

    
    for idx in selected_indices:
        edge = non_adjacent_edges[idx]
        parts = edge.split()
        edge_id1 = int(parts[1])
        edge_id2 = int(parts[2])
        
        if magnitude == "slight":
            change = random.randint(-15, 15)
        elif magnitude == "med":
            change = random.randint(-300, 300)
        elif magnitude == "huge":
            change = 0

        new_edge_id1 = max(min_id, min(max_id, edge_id1 + change))
        new_edge_id2 = max(min_id, min(max_id, edge_id2 + change))

        if magnitude == "huge":
            new_edge_id1 = random.randint(min_id,max_id)
            new_edge_id2 = random.randint(min_id,max_id)
            
        parts[1] = str(new_edge_id1)
        parts[2] = str(new_edge_id2)
        original_index = edges.index(edge)
        edges[original_index] = ' '.join(parts) + "\n"

def process_file(filename, mode,idx,data_name):
    lines = read_file(filename)
    vertex_lines = [line for line in lines if line.startswith("VERTEX")]
    edge_lines = [line for line in lines if line.startswith("EDGE")]

    min_id = int(vertex_lines[0].split()[1])
    max_id = int(vertex_lines[-1].split()[1])

    
    if mode == "slight-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.2, "slight")
    elif mode == "med-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.5, "med")
    elif mode == "huge-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.5, "med")
        modify_edge_ids(edge_lines, min_id, max_id, 0.2, "huge")
    elif mode == "sslight-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.05, "slight")
    modified_lines = vertex_lines + edge_lines
    write_file(f"./data/{data_name}_samples/{idx}.g2o", modified_lines)


# Example usage
if __name__=="__main__":
    # data_name = "city10000"
    data_name = "ais2klinik"
    # data_name = "kitti_00"
    # data_name = "kitti_02"
    # data_name = "kitti_05"
    # data_name = "manhattan"
    # data_name = "MIT"
    # data_name = "sphere2500"




    n = 100
    for i in range(1,n+1):
        if i < 70:
            process_file(f'./data/{data_name}.g2o', 'sslight-mix',i, data_name)  # Change 'slight-mix' to 'med-mix' or 'huge-mix' as needed
        if i >= 70 and i < 80:
            process_file(f'./data/{data_name}.g2o', 'slight-mix', i, data_name)  # Change 'slight-mix' to 'med-mix' or 'huge-mix' as needed
        if i >= 80 and i < 90:
            process_file(f'./data/{data_name}.g2o', 'med-mix', i, data_name)  # Change 'slight-mix' to 'med-mix' or 'huge-mix' as needed
        if i >= 90:
            process_file(f'./data/{data_name}.g2o', 'huge-mix', i, data_name)  # Change 'slight-mix' to 'med-mix' or 'huge-mix' as needed
