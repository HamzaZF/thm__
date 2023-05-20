import os

def list_root_elements():
    root_path = '/'
    elements = os.listdir(root_path)
    for element in elements:
        print(element)

# Call the function to list root directory elements
list_root_elements()
