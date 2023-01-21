from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows , num_cols = len(image), len(image[0])

        def bfs(root):
            queue = deque([root])
            visited = set()
            r,c = root
            old_color = image[r][c]
            image[r][c] = color
            visited.add((r,c))
            while queue:
                node_coords = queue.popleft()
                r,c = node_coords
                delta_row = [-1, 0, 1, 0]
                delta_col = [0, 1, 0, -1]
                for i in range(len(delta_row)):
                    n_r = r+delta_row[i]
                    n_c = c+delta_col[i]

                    if n_r in range(num_rows) and n_c in range(num_cols) and image[n_r][n_c] == old_color and (n_r,n_c) not in visited:
                        image[n_r][n_c] = color
                        queue.append((n_r,n_c))
                        visited.add((n_r,n_c))


        bfs((sr,sc))

        return image

