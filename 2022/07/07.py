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

history = [x.replace('$ ', '') for x in history if not x.startswith("$ ls")]

root = node("/", 0, None)
currentNode = root

for command in history:
    match command.split():
        case ['cd', dirName]:
            if dirName == "/":
                currentNode = root
            elif dirName == "..":
                currentNode = currentNode.parent
            else:
                currentNode = list(
                    filter(lambda node: node.name == dirName, currentNode.children))[0]
        case ['dir', dirName]:
            currentNode.children.append(node(dirName, 0, currentNode))
        case [fileSize, fileName]:
            currentNode.children.append(node(fileName, int(fileSize), currentNode))

def getSize(node):
    size = 0
    size += node.size
    for child in node.children:
        size += getSize(child)
    return size

def q1(node):
    sum = 0
    size = getSize(node)
    if node.children and size < 100_000:
        sum += size
    for child in node.children:
        sum += q1(child)
    return sum

def dirSizes(node):
    dirs = []
    if node.children:
        dirs.append(getSize(node))
    for child in node.children:
        dirs += dirSizes(child)
    return dirs


missingSpace = 30000000 - (70000000 - getSize(root))
q2 = next(filter(lambda x: x > missingSpace, sorted(dirSizes(root))))

print(q1(root))
print(q2)
