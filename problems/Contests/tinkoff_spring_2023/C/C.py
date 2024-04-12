def build_directory_tree(paths):
    tree = {}
    for path in paths:
        current = tree
        dirs = path.split('/')
        for directory in dirs:
            if directory not in current:
                current[directory] = {}
            current = current[directory]
    return tree


def print_directory_tree(tree, indent=0):
    for directory, subdirectories in sorted(tree.items()):
        print(' ' * indent + directory)
        print_directory_tree(subdirectories, indent + 2)


n = int(input())
directories = [input() for _ in range(n)]
directory_tree = build_directory_tree(directories)

print_directory_tree(directory_tree, 0)
