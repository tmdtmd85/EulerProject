
triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

class Node:
    def __init__(self, left, number, right):
        self.left = left
        self.number = number
        self.right = right

class Tree:
    def __init__(self):
        lines = [[Node(None, int(c), None) for c in line.split(' ')] for line in triangle.split('\n')]
        self.root = Node(None, lines.pop(0)[0].number, None)
        prev_line = [self.root]
        for line in lines:
            for n in range(len(line)-1):
                prev_line[n].left = line[n]
                prev_line[n].right = line[n+1]
            prev_line = line
    def find_min(self, node):
        if node.left == None and node.right == None:
            return [[node.number], node.number]
        if not node.left != None and node.right != None:
            raise Exception("Something goes to wrong!!")

        left_max = self.find_min(node.left)
        right_max = self.find_min(node.right)

        if left_max[1] >= right_max[1]:
            left_max[0].append(node.number)
            return [left_max[0], left_max[1] + node.number]
        else:
            right_max[0].append(node.number)
            return [right_max[0], right_max[1] + node.number]



if __name__ == '__main__':
    tree = Tree()
    print(tree.find_min(tree.root))
