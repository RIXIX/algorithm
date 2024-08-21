from collections import defaultdict, deque

def parse_input():
    n, c = map(int, input().split()) # parsing data n : 파이프의 개수 , c : 분기점의 개수
    tree = defaultdict(list) # defaultdict(<class 'list'>, {1: [2, 3], 3: [4, 5]}) 인접리스트


    for _ in range(c): # 분기점 개수만큼 반복 
        e, b1, b2 = map(int, input().split())
        tree[e].append(b1)
        tree[e].append(b2)    
        # tree {1: [], 2: []}
    return n, tree


def bfs_distance(tree, n):
    distances = [-1] * (n + 1) # 파이프 개수 +1 만큼 1차원 리스트 생성 [-1, -1 ... -n]
    queue = deque([(1, 1)])  # (current_node, distance_from_root)

    while queue:
        current, dist = queue.popleft() # (1,1) 2번쨰 (2,2)
        distances[current] = dist # distance[1] = 1
        
        for neighbor in tree[current]: # {1 : [2, 3]}
            if distances[neighbor] == -1:  # 아직 방문하지 않은 노드, distance[2]= -1 distance[3] = -1
                queue.append((neighbor, dist + 1)) # [(2, 2) (3, 2)]

    return distances

def print_distances(distances):
    for i in range(1, len(distances)):
        print(distances[i])


if __name__ == "__main__":
    n, tree = parse_input()
    distances = bfs_distance(tree, n)
    print_distances(distances)