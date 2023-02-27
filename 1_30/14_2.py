

class Node:
    def __init__(self, n, prev_node, parent_node, init):
        self.left = None
        self.number = n
        self.length = 0

        self.k = 1

        if n % 6 == 4 and n != 4:
            self.k += 1

        self.right = None
        self.init = init
        self.parent_node = parent_node
        self.direction = 0

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
                    node.parent_node = self.current_node
                    node.direction = 1
                    break
            elif node.number > self.current_node.number:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = node
                    node.parent_node = self.current_node
                    node.direction = -1
                    break
            else:
                self.current_node.k -= node.init

                tmp = node
                prev = tmp.prev_node
                length = self.current_node.length

                while True:
                    tmp.length = length

                    if prev == None:
                        break
                    tmp.prev = None
                    tmp = prev
                    prev = prev.prev_node
                    length += 1


                if self.current_node.k == 0:
                    self.delete(self.current_node)
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

    def delete(self, node):
        current_node = node
        if current_node.left == None and current_node.right == None:
            if current_node.direction == 1:
                current_node.parent_node.left = None
            elif current_node.direction == -1:
                current_node.parent_node.right = None
            else:
                self.root = None
        elif current_node.left != None:
            if current_node.left.right == None:
                if current_node.direction == 1:
                    current_node.parent_node.left = current_node.left
                    current_node.left.right = current_node.right
                elif current_node.direction == -1:
                    current_node.parent_node.right = current_node.left
                    current_node.left.right = current_node.right
                else:
                    self.root = current_node.left
                    current_node.left.right = current_node.right
            else:
                tmp = current_node.left.right

                while True:
                    if tmp.left == None and tmp.right == None:
                        if tmp.direction == 1:
                            tmp.parent_node.left = None
                            tmp.left = current_node.left
                            tmp.right = current_node.right
                            break
                        elif tmp.direction == -1:
                            tmp.parent_node.right = None
                            tmp.left = current_node.left
                            tmp.right = current_node.right
                            break
                        else:
                             raise Exception("error!!")
                    elif tmp.left != None:
                        tmp = tmp.left
                    elif tmp.right != None:
                        tmp = tmp.right

        elif current_node.right != None:
            if current_node.right.left == None:
                if current_node.direction == 1:
                    current_node.parent_node.left = current_node.right
                    current_node.right.left = current_node.left
                elif current_node.direction == -1:
                    current_node.parent_node.right = current_node.right
                    current_node.right.left = current_node.left
                else:
                    self.root = current_node.right
                    current_node.right.left = current_node.left
            else:
                tmp = current_node.right.left

                while True:
                    if tmp.left == None and tmp.right == None:
                        if tmp.direction == 1:
                            tmp.parent_node.left = None
                            tmp.left = current_node.left
                            tmp.right = current_node.right
                            break
                        elif tmp.direction == -1:
                            tmp.parent_node.right = None
                            tmp.left = current_node.left
                            tmp.right = current_node.right
                            break
                        else:
                            raise Exception("error!!")
                    elif tmp.left != None:
                        tmp = tmp.left
                    elif tmp.right != None:
                        tmp = tmp.right

    def print(self, node):
        if node:
            print(node.left)
            print(node.number, node.length)
            print(node.right)



if __name__ == '__main__':

    bst = BST(Node(1, None, None, 0))

    for i in range(1, 10000):
        current_node = Node(i, None, None, 0)
        bst.insert(current_node)
        while True:
            if current_node.number == 1:
                break
            if current_node.number % 2 == 1:
                current_node = Node(3*current_node.number+1, current_node, None, 1)
            else:
                current_node = Node(int(current_node.number/2), current_node, None, 1)
        print(i)

    bst.print(bst.root)
