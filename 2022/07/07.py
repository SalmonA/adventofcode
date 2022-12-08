with open('input.txt', 'r') as f:
    history = f.readlines()

class node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"{self.name} ({self.size}) \n {self.children}"

root = node("/", 0, None)
currentNode = root

for command in history:
    match command.split():
        case ['$', 'cd', '/']:
            currentNode = root
        case ['$', 'cd', '..']:
            currentNode = currentNode.parent
        case ['$', 'cd', dirName]:
            currentNode = list(filter(lambda node: node.name == dirName, currentNode.children))[0]
        case ['dir', dirName]:
            currentNode.children.append(node(dirName, 0, currentNode))
        case ['$', 'ls']:
            pass
        case [fileSize, fileName]:
            currentNode.children.append(node(fileName, int(fileSize), currentNode))

def getSize(node):
    size = 0
    size += node.size
    for child in node.children:
        size += getSize(child)
    return size

def dirSizes(node):
    dirs = []
    if node.children:
        dirs.append(getSize(node))
    for child in node.children:
        dirs += dirSizes(child)
    return dirs

q1 = sum([x for x in dirSizes(root) if x < 100000]) 

missingSpace = 30000000 - (70000000 - getSize(root))
q2 = min([x for x in dirSizes(root) if x > missingSpace]) 

print(q1)
print(q2)