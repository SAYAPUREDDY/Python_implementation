import random

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def create_tree(rows):
    tree = ""
    for i in range(rows):
        tree += " " * (rows - i - 1)
        if i == 0:
            tree += color_text("*", "32")  # ANSI color code for green
        else:
            tree += color_text("*" * (2 * i + 1), "32")  # ANSI color code for green
        tree += "\n"
    return tree

def add_decorations(tree, num_decorations):
    decorated_tree = tree.split("\n")
    for _ in range(num_decorations):
        row = random.randint(1, len(decorated_tree) - 2)
        col = random.randint(0, len(decorated_tree[row]) - 1)
        if decorated_tree[row][col] == "*":
            decoration_color = random.choice(["31", "33"])  # ANSI color codes for red and yellow
            decorated_tree[row] = decorated_tree[row][:col] + color_text("*", decoration_color) + decorated_tree[row][col + 1:]
    
    # Add 'S' letter structure in the middle
    middle_row = len(decorated_tree) // 2
    middle_col = len(decorated_tree[middle_row]) // 2 - 1
    decorated_tree[middle_row] = decorated_tree[middle_row][:middle_col] + color_text("S", "34") + decorated_tree[middle_row][middle_col + 1:]

    return "\n".join(decorated_tree)

tree_rows = 13  # Number of rows for the Christmas tree
decorations = 15  # Number of decorations to add

tree = create_tree(tree_rows)
tree_with_decorations = add_decorations(tree, decorations)

print(tree_with_decorations)

