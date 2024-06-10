import os
import click

import os
import click

@click.command()
@click.argument('path', required=False, default=os.path.dirname(os.path.realpath(__file__)))
def print_directory_structure(path):
    """
    Prints the directory structure starting from the provided path.

    Args:
        path (str, optional): The path to start printing the directory structure from. 
            If not provided, the script's directory will be used instead.

    Returns:
        None

    Usage:
        To print the directory structure starting from the current directory:
        $ python print_directory_structure.py

        To print the directory structure starting from a specific path:
        $ python print_directory_structure.py /path/to/directory
    """
    if not os.path.exists(path):
        print("The provided path does not exist. Using the script's directory instead.")
        path = os.path.dirname(os.path.realpath(__file__))
    prefix = {}
    for root, dirs, files in os.walk(path):
        level = os.path.relpath(root, path).count(os.sep)
        indent = '|   ' * (level - 1) + '|-- ' if level > 0 else ''
        print('{}{}'.format(indent, os.path.basename(root)))
        prefix[level] = '|   ' * level + '|-- '
        for f in files:
            print('{}{}'.format(prefix[level], f))

if __name__ == "__main__":
    print_directory_structure()