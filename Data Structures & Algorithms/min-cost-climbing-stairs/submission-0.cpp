class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        std::vector<int> costs(cost.size() + 1);
        
        for (int i{ 2 }; i <= cost.size(); ++i) {
            costs[i] = std::min(costs[i-1] + cost[i-1], costs[i-2] + cost[i-2]);
        }
        return costs.back();
    }
};
