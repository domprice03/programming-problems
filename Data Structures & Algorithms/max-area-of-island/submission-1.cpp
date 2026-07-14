#include <cstddef>  // For std::size_t
#include <utility>  // For std::pair

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area{ 0 };

        for (std::size_t i{ 0 }; i < grid.size(); ++i) {
            for (std::size_t j{ 0 }; j < grid[i].size(); ++j) {
                if (grid[i][j] == 1) {
                    max_area = std::max(max_area, breadthFirstSearch({ i, j }, grid));
                }
            }
        }

        return max_area;
    }

private:
    using point = std::pair<int, int>;

    const int getGridPoint(
        point p,
        const std::vector<std::vector<int>>& grid
    ) const noexcept {
        return grid[p.first][p.second];
    }

    const int breadthFirstSearch(
        const point& start_point,
        std::vector<std::vector<int>>& grid
    ) noexcept {
        int area{ 1 };
        std::queue<point> q{ };
        q.push(start_point);
        grid[start_point.first][start_point.second] = 2;
        point curr{ };
        point next{ };

        while (!q.empty()) {
            curr = q.front();
            q.pop();
            // Above
            if (curr.first > 0) {
                next = { curr.first-1, curr.second };
                if (getGridPoint(next, grid) == 1) {
                    q.push(next);
                    grid[next.first][next.second] = 2;
                    ++area;
                }
            }
            // Below
            if (curr.first < grid.size()-1) {
                next = { curr.first+1, curr.second };
                if (getGridPoint(next, grid) == 1) {
                    q.push(next);
                    grid[next.first][next.second] = 2;
                    ++area;
                }
            }
            // Left
            if (curr.second > 0) {
                next = { curr.first, curr.second-1 };
                if (getGridPoint(next, grid) == 1) {
                    q.push(next);
                    grid[next.first][next.second] = 2;
                    ++area;
                }
            }
            // Right
            if (curr.second < grid[0].size()-1) {
                next = { curr.first, curr.second+1 };
                if (getGridPoint(next, grid) == 1) {
                    q.push(next);
                    grid[next.first][next.second] = 2;
                    ++area;
                }
            }
        } 

        return area;
    }
};
