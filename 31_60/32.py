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

        if current_node == None:
            self.root = node
            return

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
            right = self.tree_print(node.right)
            return left + [node.value] + right
        return []


def ex(memory, n):
    while True:
        memory[n % 10] += 1
        n = int(n/10)
        if n == 0:
            break


def calc(pair, bst):
    for i in range(0 if pair[0] == 1 else 10**(pair[0]-1), 10**pair[0]):
        for j in range(0 if pair[0] == 1 else 10**(pair[0]-1), 10**pair[1]):
            memory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ex(memory, i)
            ex(memory, j)
            ex(memory, i*j)
            if memory[0] == 0 and sum(memory[1:]) == 9 and 0 not in memory[1:]:
                print(str(i)+"*"+str(j)+"="+str(i*j))
                bst.insert(Node(i*j))

def abc():
    for summation in range(2, 5+1):
        a = 1
        while True:
            b = summation - a
            if b < a:
                break
            yield a, b
            a += 1

if __name__ == '__main__':
    bst = Bst(None)

    for tmp in abc():
        calc(tmp, bst)
    print(sum(bst.tree_print(bst.root)))
