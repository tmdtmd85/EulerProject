

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Bst:
    def __init__(self, node):
        self.root = node

    def insert(self, node):
        current_node = self.root
        while True:
            if node.value < current_node.value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = node
                    break
            elif node.value > current_node.value:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = node
                    break
            else:
                break

    def search(self, node):
        current_node = self.root

        while current_node:
            if current_node.value == node.value:
                return True
            elif node < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def tree_print(self, node):
        if node:
            left = self.tree_print(node.left)
            print(node.value)
            right = self.tree_print(node.right)
            return left + 1 + right
        return 0
if __name__ == '__main__':
    bst = Bst(Node(10**10))

    for a in range(2, 100+1):
        for b in range(2, 100+1):
            bst.insert(Node(a**b))

    print(bst.tree_print(bst.root))
