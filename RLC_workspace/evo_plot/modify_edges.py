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
    non_adjacent_edges = [edge for i, edge in enumerate(edges) 
                          if i == 0 or i == len(edges) - 1 or 
                          abs(int(edge.split()[1]) - int(edges[i-1].split()[1])) > 1 or 
                          abs(int(edge.split()[2]) - int(edges[i-1].split()[2])) > 1]
    
    num_edges_to_modify = int(len(non_adjacent_edges) * percentage)
    print("len of lc edge:",len(non_adjacent_edges),"\nlen of modify lc edge:",num_edges_to_modify)
    selected_indices = random.sample(range(len(non_adjacent_edges)), num_edges_to_modify)

    
    for idx in selected_indices:
        edge = non_adjacent_edges[idx]
        parts = edge.split()
        edge_id1 = int(parts[1])
        edge_id2 = int(parts[2])
        
        if magnitude == "slight":
            change = random.randint(-5, 5)
        elif magnitude == "med":
            change = random.randint(-15, 15)
        elif magnitude == "huge":
            change = random.randint(-50, 50)

        new_edge_id1 = max(min_id, min(max_id, edge_id1 + change))
        new_edge_id2 = max(min_id, min(max_id, edge_id2 + change))
        
        parts[1] = str(new_edge_id1)
        parts[2] = str(new_edge_id2)
        original_index = edges.index(edge)
        edges[original_index] = ' '.join(parts) + "\n"

def process_file(filename, mode):
    lines = read_file(filename)
    vertex_lines = [line for line in lines if line.startswith("VERTEX")]
    edge_lines = [line for line in lines if line.startswith("EDGE")]

    # min_id = int(vertex_lines[0].split()[1])
    # max_id = int(vertex_lines[-1].split()[1])
    min_id = 0
    max_id = 4540
    
    if mode == "slight-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.05, "slight")
    elif mode == "med-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.1, "med")
    elif mode == "huge-mix":
        modify_edge_ids(edge_lines, min_id, max_id, 0.1, "med")
        modify_edge_ids(edge_lines, min_id, max_id, 0.02, "huge")
    
    modified_lines = vertex_lines + edge_lines
    write_file(f"./data/kitti_00_vo+lc+hfp.g2o", modified_lines)

# Example usage
if __name__=="__main__":
    process_file('./data/kitti_00.g2o', 'huge-mix')  # Change 'slight-mix' to 'med-mix' or 'huge-mix' as needed
    