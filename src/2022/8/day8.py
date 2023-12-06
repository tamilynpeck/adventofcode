class Tree:
    def __init__(self, height, x, y, row, column):
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.height = height

    def compare(self, other_trees):
        shorter_trees = [True if i < self.height else False for i in other_trees]
        if not other_trees or all(shorter_trees):
            return True

    def is_visable(self):
        left_trees = self.row[0 : self.x]
        if self.compare(left_trees):
            return True

        right_trees = self.row[self.x + 1 :]
        if self.compare(right_trees):
            return True

        up_trees = self.column[0 : self.y]
        if self.compare(up_trees):
            return True

        down_trees = self.column[self.y + 1 :]
        if self.compare(down_trees):
            return True

        # print(f"{self.height} NOT VISIBLE @ ({self.x}, {self.y})")
        return False

    def __str__(self):
        return f"Tree({self.height}, ({self.x}, {self.y}), {self.row}, {self.column})"


class TreetopTreeHouse:
    def __init__(self, data):
        self.data = data
        self.trees = [[char for char in row] for row in self.data]

    def visible_trees(self):
        visible_tree_count = 0
        for y, row in enumerate(self.trees):
            for x, height in enumerate(row):
                column = [row[x] for row in self.trees]
                tree = Tree(height, x, y, row, column)

                if tree.is_visable():
                    visible_tree_count += 1

        return visible_tree_count
