#include <cstdlib>
#include <cstdint>
#include <initializer_list>
#include <string>
#include <iostream>

template <typename T>
struct Node {
    T data;
    Node<T>   *left;
    Node<T>   *right;

    Node(T data, Node<T> *left=nullptr, Node<T> *right=nullptr)
        : data{ data }, left{ left }, right{ right }
    { }
};

template <typename T>
class BinaryTree {
    Node<T> *root;

    static void insert(Node<T> *&node, T data) {
        if (!node) {
            node = new Node{ data };
            return;
        }
        if (data < node->data)
            insert(node->left,  data);
        else
            insert(node->right, data);
    }

    static void display(std::ostream& out, const Node<T> *node) {
        if (!node)
            return;
        display(out, node->left);
        out << node->data << ' ';
        display(out, node->right);
    }

    static void recReplaceWithOposite(Node<T> *node) {
        if (!node)
            return ;
        recReplaceWithOposite(node->left);
        node->data = -node->data;
        recReplaceWithOposite(node->right);
    }
public:
    BinaryTree()
        : root{ nullptr }
    { }

    BinaryTree(std::initializer_list<T> values)
        : root{ nullptr }
    {
        for (T value : values)
            insert(value);
    }

    void insert(int32_t data) {
        insert(root, data);
    }

    void replaceNegativesWithAbs() {
        Node<T> *firstNegative{ root };
        while (firstNegative && firstNegative->data >= 0)
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
    BinaryTree<int32_t> btree{};
    std::string input{};
    std::cout << "Enter the numbers to add to the tree (leave the line blank to complete):\n";
    while (true) {
        std::getline(std::cin, input);
        if (input.empty())
            break;   
        try {
            int32_t value = std::stoi(input);
            btree.insert(value);             
        } catch (const std::invalid_argument& e) {
            std::cout << "Please enter a valid integer.\n";
        } catch (const std::out_of_range& e) {
            std::cout << "The number is out of range.\n";
        }
    }
    std::cout << btree << '\n';
    btree.replaceNegativesWithAbs();
    std::cout << btree << '\n';
    return EXIT_SUCCESS;
}
