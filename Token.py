class Token:
    def __init__(self, token_lexeme, token_type, token_row, token_column):
        self.token = token_lexeme
        self.lexeme = token_type
        self.row = token_row
        self.column =token_column



class Tree(object):

    def __init__(self, value):
        if value is not None:
            self.token = value.token
            self.lexeme = value.lexeme
            self.row = value.row
            self.column =value.column
        else:
            self.token = None
            self.lexeme = None
            self.row = 0
            self.column = 0

        self.esq = None
        self.dir = None
        self.pai = None


class SyntaxTree(object):

    def __init__(self):
        self.root = None
        self.current = None

    def add_child_node(self, new_node, father=None):
        if not father:
            father = self.current
 
        new_node.father = father
        if not father.first_son:
            father.first_son = new_node
        else:
            current_node = father.first_son
            while current_node.right:
                current_node = current_node.right
            current_node.right = new_node
            new_node.left = current_node
        self.current = new_node

    def switch(self, left, right):
        left_left = left.left
        right_right = right.right
        left.left = right
        left.right = right_right
        right.left = left_left
        right.right = left
        if left_left:
            left_left.right = right
        if right_right:
            right_right.left = left

