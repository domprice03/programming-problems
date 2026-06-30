/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <algorithm>

class Solution {
public:
    // DP / recursive: sum of solutions to left and right nodes.
    int diameterOfBinaryTree(TreeNode* root) {
        heightOfBinaryTree(root);
        return m_max;
    }

private:
    int m_max{ };

    int heightOfBinaryTree(TreeNode* node) {
        if (node == nullptr)
            return 0;

        int max{ };
        TreeNode* left{ node->left };
        TreeNode* right{ node->right };        

        int left_height{ heightOfBinaryTree(left) };
        int right_height{ heightOfBinaryTree(right) };

        m_max = std::max(m_max, left_height + right_height);
        std::cout << m_max << std::endl;
        return std::max(left_height, right_height) + 1;
    }
};
