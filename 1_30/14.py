

class Node:
    def __init__(self, n, prev_node):
        self.left = None
        self.number = n
        self.length = 0

        self.k = 1

        if n % 6 == 4 and n != 4:
            self.k += 1

        self.right = None

        self.prev_node = prev_node

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        self.current_node = self.root
        while True:
            if node.number < self.current_node.number:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = node
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = node
                    break
    def search(self, node):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.number == node.number:
                return True
            elif self.current_node.number > node.number:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


if __name__ == '__main__':
    node = Node(1, None)

    print(node.number, node.length, node.k)


