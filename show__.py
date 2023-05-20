import os

def display_directory_tree(path, indent=''):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{indent}|- {item}/")
            display_directory_tree(item_path, indent + "  ")
        else:
            print(f"{indent}|- {item}")
            try:
                with open(item_path, 'r') as file:
                    content = file.read()
                    print(content)
            except IOError:
                print("Unable to read the file.")

# Specify the root directory path
root_path = '/root/'

# Display the directory tree and file contents
display_directory_tree(root_path)
