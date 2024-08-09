class TreeNode:
    def __init__(self, key, name, age):
        self.key = key
        self.name = name
        self.age = age
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key): 
        if self.root == None: #checking to see if tree is empty
            self.root = TreeNode(key)
        else:
            self.insert_recursive(self.root, key)
            # recursive comparison to find where this treenode goes
    
    def insert_recursive(self, node, key):
        if key < node.key:
            if node.left == None:
                node.left = TreeNode(key)
            else:
                self.insert_recursive(node.left, key)
        elif key > node.key:
            if node.right == None:
                node.right = TreeNode(key)
            else:
                self.insert_recursive(node.right, key)
    
    def print_tree(self):
        self.print_tree_recursive(self.root, 0)

    def print_tree_recursive(self, node, depth):
        if node is None:
            return None

        self.print_tree_recursive(node.right, depth+1)
        print("    "*depth + str(node.key))
        self.print_tree_recursive(node.left, depth+1)

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        # Base case, what we are looking doesn't exist
        if node is None:
            return False
        # Base case we find what we are looking for
        if key == node.key:
            return True
        elif key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)
        
    def find_smallest(self, node):
        while node.left:
            node = node.left
        return node
    
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        # base case
        if node is None:
            print(f'{key} is not here!')
            return node
        
        #Binary Search to find Target
        print(f'Is {node.key} == {key}')
        if key < node.key:
            print('recursive left')
            print(f'Node {node.key} left was {node.left.key if node.left else "None"}')
            node.left = self.delete_recursive(node.left, key)
            print(f'Node {node.key} left is now {node.left.key if node.left else "None"}')
        elif key > node.key:
            print('recursive right')
            print(f'Node {node.key} right was {node.right.key if node.right else "None"}')
            node.right = self.delete_recursive(node.right, key)
            print(f'Node {node.key} right is now {node.right.key if node.right else "None"}')
        #Found the target
        else:
            print(f'Found target {node.key} == {key}')
            if node.left == None: #if left is None, I have a single right branch, or Im dealing with a leaf
                print(f'Returning right branch of {key}' if node.right else f'{key} is a leaf, replacing with None')
                return node.right
            elif node.right == None: #Here, Im dealing with a single branch to the left
                print(f'Returning left branch of {key}')
                return node.left
            
            print("Node to be removed has two branches")
            print(f'Need to find the smallest node to the right of {key}')
            smallest = self.find_smallest(node.right)
            print(f'The smallest node on the right is {smallest.key}, replacing {key} with the {smallest.key}')
            node.key = smallest.key
            print(f'Now removing {smallest.key}')
            node.right = self.delete_recursive(node.right, smallest.key)
            print(f"The old {node.key} has been removed!")
        print(f'Returning {node.key}')
        return node





tree = BinaryTree()

nodes = [50,30,40,20,70,60,80,90,75]
for node in nodes:
    tree.insert(node)

print('Printing Tree')
tree.print_tree()

# print(tree.search(50))

tree.delete(70)

tree.print_tree()
