#include <cstdlib>
#include <cstdint>
#include <initializer_list>
#include <iostream>

struct Node {
    int32_t data_;
    Node   *left;
    Node   *right;

    Node(int32_t data)
        : data_{ data }, left{ nullptr }, right{ nullptr }
    { }
};

class BinaryTree {
    Node *root;

    static void insert(Node *&node, int32_t data) {
        if (!node) {
            node = new Node{ data };
            return;
        }
        if (data < node->data_)
            insert(node->left,  data);
        else
            insert(node->right, data);
    }

    static void display(std::ostream& out, const Node *node) {
        if (!node)
            return;
        display(out, node->left);
        out << node->data_ << ' ';
        display(out, node->right);
    }

    static void recReplaceWithOposite(Node *node) {
        if (!node)
            return ;
        recReplaceWithOposite(node->left);
        node->data_ = -node->data_;
        recReplaceWithOposite(node->right);
    }
public:
    BinaryTree()
        : root{ nullptr }
    { }

    BinaryTree(std::initializer_list<int32_t> values)
        : root{ nullptr }
    {
        for (int32_t value : values)
            insert(value);
    }

    void insert(int32_t data) {
        insert(root, data);
    }

    void replaceNegativesWithAbs() {
        Node *firstNegative{ root };
        while (firstNegative && firstNegative->data_ >= 0)
            firstNegative = firstNegative->left;
        if (!firstNegative)
            return ;
        recReplaceWithOposite(firstNegative);
    }

    friend std::ostream& operator<<(std::ostream& out, const BinaryTree& btree) {
        BinaryTree::display(out, btree.root);
        return out;
    }
};

int main() {
    BinaryTree btree{ 5, 1, 3, 0, 2, 6, 4, -4, -2, -3, -1 };
    std::cout << btree << '\n';
    btree.replaceNegativesWithAbs();
    std::cout << btree << '\n';
    return EXIT_SUCCESS;
}
