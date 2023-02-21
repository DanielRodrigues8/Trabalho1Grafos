#Daniel Rodrgiues Martins 19.1.8147

from collections import deque
import time


def solve_lab(lab, start, end): 
    rows, cols = len(lab), len(lab[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = {start: None}
    queue = deque([start])
    visited[start[0]][start[1]] = True
    while queue:
        row, col = queue.popleft()
        if (row, col) == end:
            return parent
        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + row_offset, col + col_offset
            if (0 <= new_row < rows) and (0 <= new_col < cols) and (not visited[new_row][new_col]) and (lab[new_row][new_col] != "#"):
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[(new_row, new_col)] = (row, col)
    return None

def build(parent, start, end):
    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    return path

def load_lab(filename):
    with open(filename) as f:
        lab = [list(line.strip()) for line in f]
    start, end = None, None
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == "S":
                start = (i, j)
            elif lab[i][j] == "E":
                end = (i, j)
    return lab, start, end

def main():
    while True:
        filename = input("Digite o nome do arquivo de entrada e caso queira encerrar digite 0: ")
        if filename == "0":
            break
        lab, start, end = load_lab(filename)
        start_time = time.perf_counter()
        parent = solve_lab(lab, start, end)
        end_time = time.perf_counter()
        if parent:
            path = build(parent, start, end)
            print("Caminho:")
            for node in path:
                print(node)
            print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")
        else:
            print("Não existe uma solução para o labirinto.")

if __name__ == "__main__": 
    main()
